# Dojo PEP and Good Practices

This exercise focuses on improving Python coding standards by adhering to PEP8 style guide. You'll be working on a simple Codebreaker game where you have to guess a hidden sequence of numbers. 

## Installation

1. **Fork the Project:** First, create your own copy of this project 
   repository by "forking" it on GitHub. If you're not familiar with forking,
   you can learn more about it [here](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).


2. Clone the **repository**
    ```
    git clone https://github.com/jpcadena/dojo_pep8.git
    ```
3. Change the directory to **root project**
    ```
    cd dojo_pep8
    ```
4. Create a **virtual environment** *venv*
    ```
    python3 -m venv venv
    ```
5. Activate **environment** in Windows
    ```
    .\venv\Scripts\activate
    ```
6. Or with Unix/Mac OS X
    ```
    source venv/bin/activate
    ```
7. Install requirements with PIP
    ```
    pip install -r requirements.txt
    ```

## Exercise

For this exercise, you need to correct the errors in this Python project by following the PEP8 style guide:

1. **Correct the Code:** The main task is to correct the code's logic to 
   ensure the game functions correctly and revise the code style to make it adhere to the PEP8 style guide. If you're not familiar with PEP8, you can learn more about it [here](https://www.python.org/dev/peps/pep-0008/).

2. **Add Comments:** Make sure your code is understandable. Add comments and 
   documentation wherever necessary.

3. **Include a Linter:** Add a linter to the project. A linter is a tool 
   that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs. If you're not familiar with linters, you can learn more about Python Linters [here](https://realpython.com/python-code-quality/).

4. **Include a Formatter:** Add a formatter to the project. A formatter is a 
   tool that transforms source code into a new code that adheres to a particular style guide. If you're not familiar with formatters, you can learn more about Python Formatters [here](https://realpython.com/python-formatter/).

5. **(Optional) Include a Pre-commit Hook:** As an optional task, try adding 
   a pre-commit hook to the project. This ensures that every commit meets your project's requirements before it's committed. You can learn more about Pre-commit Hooks [here](https://pre-commit.com/).

After making these changes, generate a Pull Request with your updates. This is your solution submission. If you're not familiar with Pull Requests, you can learn more about it [here](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).

## How to Play Codebreaker?

1. The objective of the game is to guess a hidden 4-digit numeric sequence, put together by your opponent, in as few attempts as possible.

2. The numeric sequence can consist of numbers from 0 to 9, and numbers within the sequence do not repeat.

3. Each time you make an attempt, you'll receive feedback in the form of "X" and "_".

4. An "X" means you've correctly guessed a number in the right position within the sequence.

5. A "_" means you've correctly guessed a number, but it's in the wrong position within the sequence.

6. Using this feedback, you should deduce the correct sequence. For example, if your attempt is "1234" and you receive feedback of "XX__", it means that you've guessed two numbers correctly in their right positions, and two numbers are in the wrong positions.

7. Based on the feedback received, make new attempts adjusting your guesses until you manage to guess the correct sequence.

8. Continue making attempts and receiving feedback until you manage to decipher the complete sequence.

Remember, the challenge is to find the correct sequence in as few attempts as possible. Good luck and enjoy playing Codebreaker
