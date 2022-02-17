from dataclasses import dataclass


class Question:
    def __init__(self, test, is_true, explanation):
        self.test = test
        self.is_true = is_true
        self.explanation = explanation


@dataclass
class Question:
    text: str
    is_true: bool
    explanation: str


q = Question('test', True, 'lol')
print(q.text)


@dataclass(frozen=True)
class Question:
    text: str
    is_true: bool
    explanation: str


q = Question('test', True, 'lol')
print(q.text)
