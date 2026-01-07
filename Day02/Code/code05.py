# Ask user for their name
name = input("What's your name?").strip().title()

# Split user's name into first and last names
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")