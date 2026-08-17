import math
import os
import time

# Clear terminal once
os.system("cls" if os.name == "nt" else "clear")

A = 0.0
B = 0.0

# Brightness characters (dark -> bright)
chars = ".,-~:;=!*#$@"

while True:
    zbuffer = [0] * 1760
    output = [' '] * 1760

    j = 0
    while j < 6.28:
        i = 0
        while i < 6.28:

            sini = math.sin(i)
            cosi = math.cos(i)
            sinj = math.sin(j)
            cosj = math.cos(j)

            sinA = math.sin(A)
            cosA = math.cos(A)
            sinB = math.sin(B)
            cosB = math.cos(B)

            h = cosj + 2

            D = 1 / (sini * h * sinA + sinj * cosA + 5)

            t = sini * h * cosA - sinj * sinA

            x = int(40 + 30 * D * (cosi * h * cosB - t * sinB))
            y = int(12 + 15 * D * (cosi * h * sinB + t * cosB))

            o = x + 80 * y

            N = int(
                8
                * (
                    (sinj * sinA - sini * cosj * cosA) * cosB
                    - sini * cosj * sinA
                    - sinj * cosA
                    - cosi * cosj * sinB
                )
            )

            if 0 <= y < 22 and 0 <= x < 80:
                if D > zbuffer[o]:
                    zbuffer[o] = D
                    output[o] = chars[max(N, 0)]

            i += 0.02
        j += 0.07

    print("\x1b[H")

    for k in range(1760):
        end = "\n" if k % 80 == 79 else ""
        print(output[k], end=end)

    A += 0.04
    B += 0.02

    time.sleep(0.005)