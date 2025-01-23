# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal
total_workout_time = 0  # Total workout time for the day in hours
total_calories = 0  # Total calories consumed for the day


def log_workout():
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    workout_type = input('Workout type: ')
    duration = float(input('Duration in minutes: '))
    workouts.append((workout_type, duration))
    print(f"Logged {workout_type} for {duration} minutes.")


def log_calorie_intake():
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    calories_consumed = float(input('Calories_consumed'))
    calories.append(calories_consumed)
    print(f"Logged {calories_consumed} calories consumed.")


def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    global total_workout_time, total_calories
    total_workout_time = sum(duration for _, duration in workouts)
    total_calories = sum(calories)
    print(f'Great job! Total workout time is {total_workout_time} minutes.'
          f'\nTotal calorie intake is {total_calories}. Keep going!')


def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    global  total_workout_time, total_calories
    workouts.clear()
    calories.clear()
    total_workout_time = 0
    total_calories = 0
    print("Progress has been reset.")


def set_daily_goals():
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    global workout_goal, calorie_goal
    workout_goal = float(input('Workout duration goal in minutes: '))
    calorie_goal = float(input('Calorie intake goal: '))


def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    if total_workout_time >= workout_goal:
        print("Congratulations! You've met or exceeded your daily workout goal!")
    else:
        print(f"You can do it! You need {workout_goal - total_workout_time} more minutes to reach your workout goal.")

    if total_calories <= calorie_goal:
        print(f"You're on track! You've consumed {total_calories} calories out of your goal of {calorie_goal}.")
    else:
        print(f"Pay attention! You've exceeded your calorie goal by {total_calories - calorie_goal} calories.")

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
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for workout type and duration
            log_workout()
        elif choice == '2':
            # Prompt for calories consumed
            log_calorie_intake()
        elif choice == '3':
            # Call view_progress function
            view_progress()
            encouragement_system()
        elif choice == '4':
            # Call reset_progress function
            reset_progress()
        elif choice == '5':
            # Prompt for daily goals
            set_daily_goals()
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()