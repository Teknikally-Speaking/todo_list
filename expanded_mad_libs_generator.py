import random

# List of multiple Mad Libs templates with placeholders
templates = [
    "One day, I was walking through the {place} when I saw a very {adjective} {noun}. I decided to {verb} it, and suddenly I felt really {emotion}! All around me were {plural_noun} jumping up and down.",
    "In the land of {place}, there was a {adjective} {noun} who loved to {verb} all day long. The villagers were {emotion} because of the noisy {plural_noun}.",
    "My best day ever started when I found a {adjective} {noun} at the {place}. I couldn't help but {verb}. It made me feel so {emotion} while {plural_noun} flew overhead!"
]

# Function to get user input
def get_inputs():
    inputs = {}
    print("\n📝 Fill in the blanks to create your Mad Libs story!")
    inputs['adjective'] = input("Enter an adjective: ")
    inputs['noun'] = input("Enter a noun: ")
    inputs['verb'] = input("Enter a verb (present tense): ")
    inputs['place'] = input("Enter a place: ")
    inputs['emotion'] = input("Enter an emotion: ")
    inputs['plural_noun'] = input("Enter a plural noun: ")
    return inputs

# Function to generate story
def generate_story(inputs):
    template = random.choice(templates)
    story = template.format(
        adjective=inputs['adjective'],
        noun=inputs['noun'],
        verb=inputs['verb'],
        place=inputs['place'],
        emotion=inputs['emotion'],
        plural_noun=inputs['plural_noun']
    )
    return story

# Main game loop
def main():
    print("🎉 Welcome to the Expanded Mad Libs Generator!")

    while True:
        user_inputs = get_inputs()
        story = generate_story(user_inputs)

        print("\n📖 Here's your Mad Libs story:\n")
        print(story)

        # Save the story to a text file
        with open("mad_libs_story.txt", "a") as file:
            file.write(story + "\n\n")

        # Ask if the user wants to play again
        play_again = input("\n🔁 Would you like to create another story? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("👋 Thanks for playing Mad Libs! Your story has been saved.")
            break

# Run the program
if __name__ == "__main__":
    main()
