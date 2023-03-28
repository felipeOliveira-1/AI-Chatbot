import os
import openai

# Set the OpenAI API key from the environment variable
openai.api_key = ""

def prompt_user():
    """
    This function prompts the user for input and defines a list of content categories
    to avoid in the AI-generated responses. It returns the user's input and the avoid_list.

    Returns:
        tuple: (task, objective, answer_format, avoid_list)
    """

    # Collect user input for task, objective, and answer format
    task = input("What should the AI do? ")
    objective = input("What is the specific objective for the output? ")
    answer_format = input("What is the specific format for the answer? ")

    # Define the list of content categories to avoid
    avoid_list = [
        "Profanity or offensive language",
        "Political statements or opinions",
        "Religious statements or opinions",
        "Controversial topics",
        "Medical or health advice",
        "Legal advice",
        "Personal information",
        "Financial advice",
        "Promotion of illegal activities",
        "Discriminatory or derogatory remarks",
        "Self-harm or harm to others"
    ]

    return task, objective, answer_format, avoid_list

def generate_answer(task, objective, answer_format, avoid_list):
    """
    This function uses the OpenAI API to generate an AI-generated answer based on
    the instructions provided by the user. The instructions include the task, objective,
    answer format, and things to avoid.

    Args:
        task (str): The task description provided by the user.
        objective (str): The specific objective for the output.
        answer_format (str): The specific format for the answer.
        avoid_list (list): The list of content categories to avoid.

    Returns:
        str: The AI-generated answer.
    """

    # Construct the instructions using the user input and avoid_list
    instructions = f"{task}\nObjective: {objective}\nAnswer format: {answer_format}\nThings to avoid: {', '.join(avoid_list)}"

    # Define the messages for the OpenAI API call
    messages = [
        {"role": "system", "content": f"Task: {instructions}"},
        {"role": "user", "content": "Please provide the answer."}
    ]

    # Make the API call to OpenAI to generate the answer
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract and return the AI-generated answer
    answer = response.choices[0].message['content'].strip()
    return answer

def main():
    """
    The main function serves as the entry point of the program. It calls the prompt_user
    function to collect user input, and the generate_answer function to obtain an
    AI-generated response based on the user's instructions. Finally, it prints the
    AI-generated answer.
    """

    # Collect user input and the avoid_list
    task, objective, answer_format, avoid_list = prompt_user()

    # Generate the AI answer based on the user input
    answer = generate_answer(task, objective, answer_format, avoid_list)

    # Print the AI-generated answer
    print("\nAI Generated Answer:\n", answer)

if __name__ == "__main__":
    main()
