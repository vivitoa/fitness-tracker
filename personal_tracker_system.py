# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration):
    workouts.append((workout_type, duration))
    return f"Logged {workout_type} for {duration:.2f} minutes."


def log_calorie_intake(calories_consumed):
    calories.append(calories_consumed)
    return f"Logged {calories_consumed:.2f} calories consumed."


def view_progress():
    return (f"Great job! Total workout time is {sum(duration for _, duration in workouts):.2f} "
            f"minutes.\nTotal calorie intake is {sum(calories):.2f}. Keep going!")


def reset_progress():
    workouts.clear()
    calories.clear()
    return "Progress has been reset."


def set_daily_goals(workout_minutes, calorie_limit):
    global workout_goal, calorie_goal
    workout_goal = workout_minutes
    calorie_goal = calorie_limit
    return "Daily goals have been updated."


def encouragement_system():
    total_workout = sum(duration for _, duration in workouts)
    total_calories = sum(calories)

    workout_message = (
        "Congratulations! You've met or exceeded your daily workout goal!"
        if total_workout >= workout_goal
        else f"You can do it! You need {workout_goal - total_workout:.2f} more minutes to reach your workout goal."
    )

    calorie_message = (
        f"You're on track! You've consumed {total_calories:.2f} calories out of your goal of {calorie_goal:.2f}."
        if total_calories <= calorie_goal
        else f"Pay attention! You've exceeded your calorie goal by {total_calories - calorie_goal:.2f} calories."
    )

    return f"{workout_message}\n{calorie_message}"


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Feedback")
        print("7. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            input_workout = input('Workout type: ')
            input_duration = float(input('Duration in minutes: '))
            print(log_workout(input_workout, input_duration))

        elif choice == '2':
            input_calories = float(input('Calories consumed: '))
            print(log_calorie_intake(input_calories))

        elif choice == '3':
            print(view_progress())

        elif choice == '4':
            print(reset_progress())

        elif choice == '5':
            workout_ = float(input('Workout duration goal in minutes: '))
            calorie_ = float(input('Calorie intake goal: '))
            print(set_daily_goals(workout_, calorie_))

        elif choice == '6':
            print(encouragement_system())

        elif choice == '7':
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
