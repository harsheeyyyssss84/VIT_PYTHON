"""NeuroMind: laptop-side brain for an emotion-aware ESP32 robot.

Run this file on a laptop. It reads text typed by the user, estimates emotion,
remembers key facts, creates an empathetic reply, and sends commands over USB
serial to an ESP32.
"""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

try:
    import serial
    from serial.tools import list_ports
except ImportError:
    print("Missing pyserial. Run: pip install -r requirements.txt")
    raise SystemExit(1)

MEMORY_FILE = Path("neuromind_memory.json")
BAUD_RATE = 115200

# Change this to your actual port if automatic selection does not work.
# Windows examples: "COM3", "COM4". Leave as None for automatic detection.
SERIAL_PORT = None

EMOTION_WORDS = {
    "JOY": ["happy", "great", "awesome", "excited", "wonderful", "thank", "good"],
    "SADNESS": ["sad", "lonely", "cry", "upset", "depressed", "hurt", "bad"],
    "ANGER": ["angry", "hate", "annoyed", "furious", "irritated", "mad"],
    "FEAR": ["scared", "afraid", "worried", "anxious", "nervous", "stress", "exam"],
}


def load_memory() -> dict:
    if MEMORY_FILE.exists():
        try:
            return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {"facts": [], "history": []}


def save_memory(memory: dict) -> None:
    MEMORY_FILE.write_text(json.dumps(memory, indent=2), encoding="utf-8")


def extract_fact(text: str) -> str | None:
    """Save simple personal facts that make later replies feel contextual."""
    patterns = [
        r"\bmy name is ([a-zA-Z ]{2,30})",
        r"\bi am ([a-zA-Z ]{2,30})",
        r"\bi have (an? [a-zA-Z ]{2,40})",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(0).strip(" .!?")
    return None


def detect_emotion(text: str) -> str:
    lower_text = text.lower()
    scores = {emotion: 0 for emotion in EMOTION_WORDS}
    for emotion, words in EMOTION_WORDS.items():
        scores[emotion] = sum(1 for word in words if word in lower_text)
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "CALM"


def update_state(state: dict[str, float], detected: str) -> dict[str, float]:
    """Emotion decays with time, then the detected emotion gets stronger."""
    for emotion in state:
        state[emotion] *= 0.82
    state[detected] += 0.45
    for emotion in state:
        state[emotion] = round(max(0.0, min(1.0, state[emotion])), 2)
    return state


def dominant_emotion(state: dict[str, float]) -> str:
    return max(state, key=state.get)


def make_reply(text: str, emotion: str, memory: dict) -> str:
    recent = " ".join(item["text"].lower() for item in memory["history"][-4:])
    context = " You mentioned an exam earlier." if "exam" in recent and "exam" not in text.lower() else ""

    replies = {
        "JOY": "That sounds wonderful. I am glad to hear it!",
        "SADNESS": "I am sorry that you are feeling this way. I am here to listen.",
        "ANGER": "I can see that this is frustrating. Let us slow down and work through it calmly.",
        "FEAR": "It is understandable to feel worried. We can take one small step at a time.",
        "CALM": "I understand. Please tell me more so I can support you.",
    }
    return replies[emotion] + context


def choose_port() -> str | None:
    ports = list(list_ports.comports())
    if not ports:
        return None
    likely = [p for p in ports if "USB" in p.description.upper() or "CP210" in p.description.upper() or "CH340" in p.description.upper()]
    return (likely[0] if likely else ports[0]).device


def send_command(device: serial.Serial, command: str) -> None:
    device.write((command + "\n").encode("utf-8"))
    device.flush()
    print(f"  [Robot command] {command}")


def main() -> None:
    port = SERIAL_PORT or choose_port()
    if not port:
        print("No ESP32/Arduino serial port found. Connect it, then set SERIAL_PORT in robot_brain.py.")
        raise SystemExit(1)

    try:
        device = serial.Serial(port, BAUD_RATE, timeout=1)
        time.sleep(2)  # ESP32 resets after opening its serial port.
    except serial.SerialException as error:
        print(f"Cannot open {port}: {error}")
        raise SystemExit(1)

    memory = load_memory()
    state = {"JOY": 0.1, "SADNESS": 0.0, "ANGER": 0.0, "FEAR": 0.0, "CALM": 0.8}
    print(f"NeuroMind connected to {port}. Type exit to close.\n")
    send_command(device, "EMOTION:CALM")

    while True:
        text = input("You: ").strip()
        if not text:
            continue
        if text.lower() in {"exit", "quit"}:
            send_command(device, "EMOTION:CALM")
            print("NeuroMind: Goodbye.")
            break

        detected = detect_emotion(text)
        state = update_state(state, detected)
        robot_emotion = dominant_emotion(state)
        fact = extract_fact(text)
        if fact and fact not in memory["facts"]:
            memory["facts"].append(fact)

        reply = make_reply(text, robot_emotion, memory)
        memory["history"].append({"text": text, "detected": detected, "time": time.time()})
        memory["history"] = memory["history"][-30:]
        save_memory(memory)

        send_command(device, f"EMOTION:{robot_emotion}")
        print(f"NeuroMind [{robot_emotion}]: {reply}")
        print(f"State: {state}\n")

    device.close()


if __name__ == "__main__":
    main()