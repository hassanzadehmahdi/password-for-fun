from infrastructure.chatgpt_api import get_chatgpt_response


def solve_rule(rules: dict, current_password: str):
    false_messages = rules.get('false_messages')
    true_messages = rules.get('true_messages')

    prompt = (
        f"You are given the current password: '{current_password}'. "
        f"The following rules have been satisfied: {true_messages}. "
        f"However, the following rules are not yet satisfied: {false_messages}. "
        f"Your task is to suggest a modification or a new password that satisfies all the rules, "
        f"while retaining as much of the current password's structure as possible."
    )

    return prompt #get_chatgpt_response(prompt)
