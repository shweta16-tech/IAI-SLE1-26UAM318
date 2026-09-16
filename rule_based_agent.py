# Rule-Based Student Study Assistant Agent
# Course: 02AML204 - Introduction to Artificial Intelligence
# SLE-1

def get_study_hours():
    """Get valid study hours from the user."""
    while True:
        try:
            hours = float(input("Enter study hours today: "))

            if hours < 0:
                print("Study hours cannot be negative. Try again.")
            elif hours > 24:
                print("Please enter a value between 0 and 24.")
            else:
                return hours

        except ValueError:
            print("Please enter a valid number.")


def get_mood():
    """Get a valid mood from the user."""
    while True:
        mood = input("Enter your mood (good/tired/stressed): ").strip().lower()

        if mood in ["good", "tired", "stressed"]:
            return mood

        print("Please enter good, tired, or stressed.")


def study_assistant_agent(hours, mood):
    """
    Rule-based decision-making agent.
    The agent checks predefined rules and gives a recommendation.
    """

    if hours < 2 and mood == "good":
        decision = "You have studied for a short time. Continue studying for some more time."

    elif hours < 2 and mood in ["tired", "stressed"]:
        decision = "You have studied for a short time and you are not feeling well. Take a short break and then study."

    elif 2 <= hours < 5 and mood == "good":
        decision = "Good progress. Continue studying or start revising the topics you completed."

    elif 2 <= hours < 5 and mood == "tired":
        decision = "You have studied for a reasonable time. Take a short break before continuing."

    elif 2 <= hours < 5 and mood == "stressed":
        decision = "Take a break, relax for some time, and then continue with one topic at a time."

    elif hours >= 5 and mood == "good":
        decision = "You have studied for sufficient time. Use the remaining time for revision."

    elif hours >= 5 and mood in ["tired", "stressed"]:
        decision = "You have studied for a long time. Take proper rest before studying again."

    else:
        decision = "Maintain a balanced study routine and take care of your health."


    return decision


def main():
    print("=" * 50)
    print("  RULE-BASED STUDENT STUDY ASSISTANT AGENT")
    print("=" * 50)

    hours = get_study_hours()
    mood = get_mood()

    decision = study_assistant_agent(hours, mood)

    print("\n--- AI AGENT DECISION ---")
    print(decision)
    print("--------------------------")


if __name__ == "__main__":
    main()
