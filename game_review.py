# Prompting the user to enter in game information with input validation and error handling

while True:
    game_title = input("Please enter the game title: ")
    if game_title:
        break
    else:
        print("Invalid input. Please enter a game title.")

while True:
    developer_name = input("Please enter the developer's name: ")
    if developer_name:
        break
    else:
        print("Invalid input. Please enter a developer name.")

while True:
    platforms = input("Please enter the platforms available: ")
    if platforms:
        break
    else:
        print("Invalid input. Please enter at least one platform.")

while True:
    price = input("Please enter the price, if applicable (enter 0 if it's free): ")
    try:
        price = float(price)
        if price < 0:
            print("Invalid input. Please enter a non-negative number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    overview = input("Please provide a brief overview of the game, including its genre and setting: ")
    if overview:
        break
    else:
        print("Invalid input. Please enter an overview.")

while True:
    gameplay = input("Please describe the gameplay mechanics, controls, and any unique features of the game: ")
    if gameplay:
        break
    else:
        print("Invalid input. Please enter the gameplay description.")

while True:
    graphics = input("Please comment on the quality of the game's graphics and art style: ")
    if graphics:
        break
    else:
        print("Invalid input. Please comment on the graphics.")

while True:
    sound = input("Please comment on the quality of the game's sound effects and music: ")
    if sound:
        break
    else:
        print("Invalid input. Please comment on the sound.")

while True:
    story = input("Please comment on the quality and depth of the game's story and characters, if applicable (enter N/A if not applicable): ")
    if story or story.lower() == "n/a":
        break
    else:
        print("Invalid input. Please comment on the story or enter N/A if not applicable.")

while True:
    replayability = input("Please comment on the game's replay value and whether it encourages multiple playthroughs: ")
    if replayability:
        break
    else:
        print("Invalid input. Please comment on the replayability.")

while True:
    overall_impressions = input("Please provide your overall impressions of the game and whether you would recommend it to others: ")
    if overall_impressions:
        break
    else:
        print("Invalid input. Please enter your overall impressions.")

while True:
    pros = input("Please list the things you liked about the game, such as mechanics, graphics, story, etc. (enter N/A if not applicable): ")
    if pros or pros.lower() == "n/a":
        break
    else:
        print("Invalid input. Please enter the pros or enter N/A if not applicable.")

while True:
    cons = input("Please list any areas where the game fell short or could be improved, such as bugs, repetitive gameplay, or lack of content (enter N/A if not applicable): ")
    if cons or cons.lower() == "n/a":
        break
    else:
        print("Invalid input. Please enter the cons or enter N/A if not applicable.")

while True:
    final_thoughts = input("Please provide any final thoughts or recommendations for potential players: ")
    if final_thoughts
