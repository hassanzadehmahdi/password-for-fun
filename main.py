from infrastructure.selenium_handler import SeleniumHandler
from domain.password import Password
from domain.rules import solve_rule
from infrastructure.config import GAME_URL


def main():
    # Initialize components
    selenium_handler = SeleniumHandler(GAME_URL)

    try:
        # Handle consent dialog if it appears
        selenium_handler.handle_consent_dialog()

        # Start the game by entering an initial character
        selenium_handler.start_game(initial_character="a")

        while True:
            # Fetch the current password
            current_password = selenium_handler.get_current_password()
            if not current_password:
                print("Failed to retrieve the current password!")
                break

            # Fetch all rules
            rules = selenium_handler.get_all_rules()
            if not rules:
                print("No more rules or game completed!")
                break

            print(f"Current Password: {current_password}")
            print(f"Current Rules: {rules}")

            # Solve the rule using ChatGPT
            prompt = solve_rule(rules, current_password)
            print(f'prompt: {prompt}')
            new_password = input("Enter the solution: ")

            # Update the password with ChatGPT's solution
            selenium_handler.update_password(new_password)

    except KeyboardInterrupt:
        print("Process interrupted by user.")
    finally:
        selenium_handler.close()


if __name__ == "__main__":
    main()
    # TODO capcha url: https://neal.fun/password-game/captchas/33p4e.png
    # sponsors: shell , starbucks, pepsi
