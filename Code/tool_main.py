# student_name: Harish Raghav
# roll_number: 727823TUCY016
# project_name: CustomWordlistGenerator
# date: 2026-03-28

import itertools
from datetime import datetime


def generate_wordlist(name, dob, pet, fav):
    words = [name, pet, fav]
    numbers = [dob, dob[-2:], "123", "2024"]
    symbols = ["@", "#", "!", "_"]

    wordlist = []

    # Word + Number combinations
    for w in words:
        for n in numbers:
            wordlist.append(w + n)
            wordlist.append(w.capitalize() + n)

    # Word + Symbol combinations
    for w in words:
        for s in symbols:
            wordlist.append(w + s)

    # Word permutations (combine words)
    combinations = itertools.permutations(words, 2)
    for combo in combinations:
        wordlist.append("".join(combo))
        wordlist.append("_".join(combo))

    return list(set(wordlist))


if __name__ == "__main__":
    print("Roll No: 727823TUCY016 | Time:", datetime.now())

    # User inputs
    name = input("Enter name: ")
    dob = input("Enter DOB (YYYY or DDMMYYYY): ")
    pet = input("Enter pet name: ")
    fav = input("Enter favorite word: ")

    # Generate wordlist
    result = generate_wordlist(name, dob, pet, fav)

    print("\nGenerated Wordlist:\n")
    for word in result:
        print(word)

    # Save with unique filename (IMPORTANT FEATURE 🔥)
    filename = f"wordlist_{name}_{datetime.now().strftime('%H%M%S')}.txt"

    with open(filename, "w") as f:
        for word in result:
            f.write(word + "\n")

    print(f"\nWordlist saved to {filename}")
