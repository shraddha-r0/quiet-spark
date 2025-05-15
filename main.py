from agents.affirmation_agent import get_affirmation
from agents.companion_agent import get_companion_response
import yaml

def main():
    print("🟣 QuietSpark")
    agent_choice = input("Which agent would you like to talk to? (affirmation / companion): ").strip().lower()

    if agent_choice not in ["affirmation", "companion"]:
        print("Invalid agent. Please restart and choose either 'affirmation' or 'companion'.")
        return

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        if agent_choice == "affirmation":
            response = get_affirmation(user_input)
        elif agent_choice == "companion":
            response = get_companion_response(user_input)

        print(f"\n{agent_choice.capitalize()} Agent:\n{response}\n")

def load_user_profile():
    with open("config/shraddha_profile.yaml", "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    main()
