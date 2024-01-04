"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [['p4', 'p5', 'p6', 'm1', 'm1', 'm1', 's2', 's3', 's4', 's9', 'we', 'we', 'dw', 'dw']],
            "answer": 1,
            "explanation": "tempay"
        },
        {
            "input": [['p4', 'p5', 'p6', 'm1', 'm1', 'm1', 's2', 's3', 's4', 's9', 'we', 'ws', 'dw', 'dw']],
            "answer": 2,
            "explanation": "ishanten"
        },
        {
            "input": [['p4', 'p5', 'p7', 'm1', 'm1', 'm1', 's2', 's3', 's4', 's9', 'we', 'ws', 'dw', 'dw']],
            "answer": 3,
            "explanation": "ryanshanten"
        },
        {
            "input": [['p4', 'p5', 'p7', 'm1', 'm1', 's2', 's3', 's4', 's9', 'we', 'ws', 'wn', 'dw', 'dw']],
            "answer": 4,
            "explanation": "sanshanten"
        },
    ],
    "Extra": [
        {
            "input": [],
            "answer": None,
            "explanation": "I speaked you about thoroughly check. And?"
        },
        {
            "input": ['incorrect string'],
            "answer": None,
            "explanation": "Sorry, your solution is incomplete yet."
        },
        {
            "input": [6, 66, 666],
            "answer": None,
            "explanation": "This is absolutely wrong input data. You should prevent errors."
        }
    ]
}
