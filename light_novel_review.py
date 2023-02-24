import datetime

# Prompt user to enter values for the fields with input validation
while True:
    title = input("Enter the title of the light novel: ")
    if title:
        break
    print("Title cannot be empty. Please try again.")

while True:
    author = input("Enter the author of the light novel: ")
    if author:
        break
    print("Author cannot be empty. Please try again.")

while True:
    try:
        release_date = input("Enter the release date of the light novel (yyyy-mm-dd): ")
        datetime.datetime.strptime(release_date, '%Y-%m-%d')
        break
    except ValueError:
        print("Invalid date format. Please enter a valid date in yyyy-mm-dd format.")

while True:
    publisher = input("Enter the publisher of the light novel: ")
    if publisher:
        break
    print("Publisher cannot be empty. Please try again.")

    # Prompt user to enter values for the fields with input validation
while True:
    plot = input("Enter a brief summary of the plot: ")
    if plot:
        break
    print("Plot summary cannot be empty. Please try again.")

while True:
    characters = input("Discuss the main characters, their development, and impact on the story: ")
    if characters:
        break
    print("Character discussion cannot be empty. Please try again.")

while True:
    worldbuilding = input("Evaluate the worldbuilding and setting of the story: ")
    if worldbuilding:
        break
    print("Worldbuilding evaluation cannot be empty. Please try again.")

while True:
    writing_style = input("Evaluate the quality of the writing, including pacing and dialogue: ")
    if writing_style:
        break
    print("Writing style evaluation cannot be empty. Please try again.")

while True:
    themes = input("Discuss any themes or messages explored in the story: ")
    if themes:
        break
    print("Theme discussion cannot be empty. Please try again.")

while True:
    try:
        overall_rating = int(input("Provide your overall rating for the novel on a scale of 1-10: "))
        if 1 <= overall_rating <= 10:
            break
        print("Rating must be a number between 1 and 10. Please try again.")
    except ValueError:
        print("Rating must be a number between 1 and 10. Please try again.")

final_thoughts = input("Add any concluding thoughts or predictions for future installments, if applicable: ")

# Format the fields into the template
review_template = f"""Title: {title}
Author: {author}
Release Date: {release_date}
Publisher: {publisher}

Plot:
{plot}

Characters:
{characters}

Worldbuilding:
{worldbuilding}

Writing Style:
{writing_style}

Themes:
{themes}

Overall Rating: {overall_rating}

Final Thoughts:
{final_thoughts}
"""

# Print the review
print(review_template)
