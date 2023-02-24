while True:
    try:
        # Prompt user to enter values for the fields and validate the inputs
        manga_title = input("Enter manga title: ")
        if len(manga_title.strip()) == 0:
            raise ValueError("Manga title cannot be empty.")
        volume_number = int(input("Enter volume number: "))
        if volume_number < 1:
            raise ValueError("Volume number must be a positive integer.")
        author_artist = input("Enter author/artist names: ")
        if len(author_artist.strip()) == 0:
            raise ValueError("Author/artist names cannot be empty.")
        genre = input("Enter genre(s) of the manga: ")
        if len(genre.strip()) == 0:
            raise ValueError("Genre(s) cannot be empty.")
        overview = input("Enter a brief overview of the volume: ")
        artwork = input("Comment on the quality of the artwork: ")
        story = input("Comment on the quality of the story in this volume: ")
        themes = input("Comment on any themes or messages that the manga explores: ")
        characters = input("Comment on the development of the main characters in this volume: ")
        anticipated_developments = input("Comment on what you're looking forward to seeing develop in the story or characters in future volumes: ")
        overall_impressions = input("Provide your overall impressions of this volume and whether you would recommend it to others: ")
        pros = input("List the things you liked about this volume: ")
        cons = input("List any areas where this volume fell short or could be improved: ")
        final_thoughts = input("Provide any final thoughts or recommendations for potential readers of this volume: ")
        break
    except ValueError as err:
        print(err)

# Format the fields into the template
review_template = f"""Title: {manga_title}, Volume {volume_number}

Author/Artist: {author_artist}

Genre: {genre}

Overview:
{overview}

Artwork:
{artwork}

Story:
{story}

Themes:
{themes}

Characters:
{characters}

Anticipated Developments:
{anticipated_developments}

Overall:
{overall_impressions}

Pros:
{pros}

Cons:
{cons}

Final Thoughts:
{final_thoughts}
"""

# Print the review
print(review_template)
