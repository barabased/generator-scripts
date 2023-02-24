import datetime

def generate_schedule():
    while True:
        duration = input("Would you like to generate a workout schedule for a week or a month? ")
        if duration.lower() == "week":
            num_days = 7
            break
        elif duration.lower() == "month":
            num_days = 30
            break
        else:
            print("Invalid input. Please enter either 'week' or 'month'.")

    start_date = input("Enter the start date for the schedule (format: MM/DD/YYYY): ")
    try:
        start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y')
    except ValueError:
        print("Invalid date format. Please enter the date in MM/DD/YYYY format.")
        return

    schedule = {}

    for i in range(num_days):
        current_date = start_date + datetime.timedelta(days=i)
        schedule[current_date.strftime("%m/%d/%Y")] = []

        while True:
            exercise = input(f"Enter an exercise for {current_date.strftime('%m/%d/%Y')}: ")
            if not exercise:
                break

            sets = input("Enter the number of sets: ")
            try:
                sets = int(sets)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            reps = input("Enter the number of reps: ")
            try:
                reps = int(reps)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            weight = input("Enter the weight (in lbs): ")
            try:
                weight = float(weight)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            schedule[current_date.strftime("%m/%d/%Y")].append((exercise, sets, reps, weight))

    print("Here's your workout schedule:\n")
    for date, exercises in schedule.items():
        print(f"{date}:")
        if not exercises:
            print("  Rest day")
        else:
            for exercise in exercises:
                print(f"  {exercise[0]} - {exercise[1]} sets of {exercise[2]} reps at {exercise[3]} lbs")

if __name__ == "__main__":
    generate_schedule()
