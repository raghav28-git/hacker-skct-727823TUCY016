# Harish Raghav - 727823TUCY016

from datetime import datetime
from tool_main import generate_wordlist

print("Roll No: 727823TUCY016 | Time:", datetime.now())

# Predefined test input (important for pipeline)
name = "raghav"
dob = "28012006"
pet = "jim"
fav = "gun"

result = generate_wordlist(name, dob, pet, fav)

print("\nGenerated Wordlist:\n")
for word in result:
    print(word)

# Save output
filename = "pipeline_wordlist.txt"

with open(filename, "w") as f:
    for word in result:
        f.write(word + "\n")

print(f"\nWordlist saved to {filename}")
