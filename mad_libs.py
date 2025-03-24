# --------------------------------------------
# 🎮 Mad Libs Generator
# Author: [Your Name]
# Bootcamp: Week 4 Project
# Description: A fun text-based game where users fill in blanks to generate a silly story!
# --------------------------------------------

# Print a welcome message
print("🎉 Welcome to the Mad Libs Generator!")
print("Let's create a silly story together. You'll be asked to enter some words.\n")

# 📥 Step 1: Get user input (parts of speech)
# These inputs are stored in variables
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (present tense): ")
place = input("Enter a place: ")
emotion = input("Enter an emotion: ")
plural_noun = input("Enter a plural noun: ")

# ✍️ Step 2: Create the Mad Libs story using f-strings
story = f"""
🌟 Here's your story! 🌟

One day, I was walking through the {place} when I saw a very {adjective} {noun}.
I decided to {verb} it, and suddenly I felt really {emotion}!
All around me were {plural_noun} jumping up and down.
It was the strangest day ever!

🎉 Thanks for playing Mad Libs!
"""

# 📤 Step 3: Display the final story
print(story)