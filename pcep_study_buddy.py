# A 30 minut PCEP practice project: ClI quiz + scoring

PASS_PERCENT = 70


def build_questions():
    """
    Returns a list of dicts.
    Each dict is one question wwith choices and the correct answer letter.
    """
    return [
        {
            "q": "What is the type of the value: 3.0 ?",
            "choices": {"A": "int", "B": "float", "C": "str", "D": "bool"},
            "answer": "B",
        },
        {
            "q": "What does this evaluate to? 5 // 2",
            "choices": {"A": "2", "B": "2.5", "C": "3", "D": "Error"},
            "answer": "A",
        },
        {
            "q": "Which keyword ends a loop early?",
            "choices": {"A": "stop", "B": "exit", "C": "break", "D": "end"},
            "answer": "C",
        },
        {
            "q": "What is the output?\n"
            "x = 10\n"
            "if x > 5:\n"
            "    print('Yes')\n"
            "else:\n"
            "    print('No')",
            "choices": {"A": "Yes", "B": "No", "C": "10", "D": "Error"},
            "answer": "A",
        },
        {
            "q": "What is the result of:  'py' + 'thon' ?",
            "choices": {
                "A": "'py thon'",
                "B": "'python'",
                "C": "Error",
                "D": "'python'",
            },
            "answer": "D",
        },
        {
            "q": "What is the output?\n" "print(len([1, 2, 3]))",
            "choices": {"A": "2", "B": "3", "C": "1", "D": "Error"},
            "answer": "B",
        },
        {
            "q": "What does bool('') return?",
            "choices": {"A": "True", "B": "False", "C": "''", "D": "None"},
            "answer": "B",
        },
        {
            "q": "Which line correctly creates a function?",
            "choices": {
                "A": "function hi():",
                "B": "def hi():",
                "C": "fun hi():",
                "D": "define hi():",
            },
            "answer": "B",
        },
        {
            "q": "What is the output?\n"
            "nums = [1, 2]\n"
            "nums.append(3)\n"
            "print(nums)",
            "choices": {
                "A": "[1, 2]",
                "B": "[1, 2, 3]",
                "C": "(1, 2, 3)",
                "D": "Error",
            },
            "answer": "B",
        },
        {
            "q": "What is the output?\n" "a = 2\n" "b = 3\n" "print(a ** b)",
            "choices": {"A": "6", "B": "8", "C": "9", "D": "Error"},
            "answer": "B",
        },
    ]
