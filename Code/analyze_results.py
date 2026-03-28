# Harish Raghav - 727823TUCY016

from datetime import datetime

print("Roll No: 727823TUCY016 | Time:", datetime.now())

try:
    with open("pipeline_wordlist.txt") as f:
        words = f.readlines()

    print("\nAnalysis Results:")
    print("Total passwords generated:", len(words))

    # Extra analysis (good for marks)
    long_words = [w for w in words if len(w.strip()) > 8]
    print("Passwords longer than 8 chars:", len(long_words))

except FileNotFoundError:
    print("Error: pipeline_wordlist.txt not found. Run tool first.")
