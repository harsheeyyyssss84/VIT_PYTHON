# RE FUNCTIONS ARE:-
# re.search() - finds first match
# re.match() - checks for a match at the beginning
# re.findall() - finds all matching patterns (IMP)
# re.sub - replaces patterns with a string
# re.split() - splits strings using patterns
# always use re.fun(r"pattern") eg. re.findall(r"\d+")

import re

text0 = "There are 4 Dogs, 12 Cats, 20 Parrots."

numbers = re.findall(r"\d+", text0)           # Main Line(REM) Match Only Digits (r"\d+")
print("Numbers Found:", numbers)

# --------------------------------

# import re in each code!!

text1 = ("Todays Date is 28-07-2026, yesterday was 27-07-2026")

dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text1)        # Match Dates(DD-MM-YYYY) Format (r"\b\d{2}-\d{2}-\d{4}\b")
print("Dates Found:", dates)

# --------------------------------

# import re in each code!!

text2 = "Welcome!!! to @Python#World..."

cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", text2)
print("Cleaned Statement Is:", cleaned)