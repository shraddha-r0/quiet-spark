from agents.affirmation_agent import get_affirmation

def main():
    print("🟣 QuietSpark | Affirmation Agent")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        response = get_affirmation(user_input)
        print(f"\nAffirmation Agent:\n{response}\n")

if __name__ == "__main__":
    main()