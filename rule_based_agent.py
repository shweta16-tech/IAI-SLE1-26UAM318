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
        mood = input(
            "Enter your mood (good/tired/stressed): "
        ).strip().lower()

        if mood in ["good", "tired", "stressed"]:
            return mood

        print("Please enter good, tired, or stressed.")


def study_assistant_agent(hours, mood):
    """
    Rule-based decision-making agent.
    It checks predefined rules and gives recommendations.
    """

    recommendations = []

    # Rule 1: Check study hours
    if hours < 2:
        recommendations.append(
            "Increase your study time gradually."
        )
    elif hours < 5:
        recommendations.append(
            "Good study progress. Continue with your plan."
        )
    else:
        recommendations.append(
            "You have studied for sufficient time. Focus on revision."
        )

    # Rule 2: Check mood
    if mood == "good":
        recommendations.append(
            "You can continue studying or revise completed topics."
        )
    elif mood == "tired":
        recommendations.append(
            "Take a short break before continuing your studies."
        )
    else:
        recommendations.append(
            "Relax for some time and study one topic at a time."
        )

    # Final decision
    if hours >= 5 and mood == "good":
        decision = "Excellent study session. Use the remaining time for revision."

    elif hours < 2 and mood in ["tired", "stressed"]:
        decision = "Take a break first and then continue with a shorter study session."

    elif mood in ["tired", "stressed"]:
        decision = "Take a short break and continue studying after you feel better."

    elif hours < 2:
        decision = "Try to increase your study time gradually."

    else:
        decision = "Your study routine is going well. Continue with your plan."

    return decision, recommendations


def main():
    print("=" * 55)
    print("       RULE-BASED STUDENT STUDY ASSISTANT")
    print("=" * 55)

    hours = get_study_hours()
    mood = get_mood()

    decision, recommendations = study_assistant_agent(hours, mood)

    print("\n--- AI AGENT ANALYSIS ---")

    print("\nRecommendations:")
    for number, recommendation in enumerate(recommendations, start=1):
        print(f"{number}. {recommendation}")

    print("\nFinal Decision:")
    print(decision)

    print("-" * 55)


if __name__ == "__main__":
    main()
