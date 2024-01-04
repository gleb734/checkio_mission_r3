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
        },
        {
            "input": ['s1', 's1', 's1', 's2', 's2', 's2', 's3', 's3', 's3', 's4', 's4', 's4', 's5', 'oh, no...'],
            "answer": None,
            "explanation": "Oh, no!"
        },
        {
            "input": ['s1', 's1', 's1', 's2', 's2', 's2', 's3', 's3', 's3', 's4', 's4', 's4', 's5', 's0'],
            "answer": None,
            "explanation": "Alas, there is no tile s0 in mahjong..."
        },
        {
            "input": ['s1', 's1', 's1', 's1', 's1', 's2', 's2', 's2', 's3', 's3', 's3', 's4', 's4', 's4'],
            "answer": None,
            "explanation": "There can't be FIVE same tiles..."
        },
        {
            "input": ['s2', 's2', 's2', 's3', 's3', 's3', 's4', 's4', 's4', 's5', 's5', 's6', 's6', 's6'],
            "answer": 0,
            "explanation": "Yes, this hand is ALREADY winning. And it cost very, very much..."
        },
        {
            "input": ['s1, 's1', 's2', 's2', 's3', 's3', 's4', 's4', 's5', 's5', 's6', 's6', 's7', 'dg'],
            "answer": 1,
            "explanation": "Chitoy. In tempay. What? You didn't think about it? ¯\_(ツ)_/¯"
        },
        {
            "input": ['s1', 's9', 'p1', 'p9', 'm1', 'm9', 'dg', 'dw', 'dr', 'ww', 'we', 'ws', 'wn', 'p5'],
            "answer": 1,
            "explanation": "Kokushi muso. Also in tempay. I'm sorry that you forgot about it."
        },
        {
            "input": ['s1', 's9', 'p1', 'p9', 'm1', 'm9', 'dg', 'dw', 'dr', 'ww', 'we', 'ws', 'wn', 'ha'],
            "answer": 1,
            "explanation": "This is NOT kokushi. This is not a right hand at all. Don't relax you mind."
        },
        {
            "input": ['m1', 'm2', 'm3', 'p2', 'p3', 'p7', 'p8', 's4', 's5', 's6', 's7', 's8', 's9', 'dw'],
            "answer": 2,
            "explanation": "Ishanten. What did you say? I already checked it?"
        }
    ]
}
