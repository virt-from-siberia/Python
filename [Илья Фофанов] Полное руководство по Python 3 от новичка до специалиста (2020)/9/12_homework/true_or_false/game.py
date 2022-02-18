from typing import Callable, List

from game_status import GameStatus
from question import Question
from game_result import GameResult


class Game:
    def __init__(self, file_path: str, allowed_mistakes: int, end_of_game_event: Callable):
        self.__file_path = file_path
        self.__allowed_mistakes: allowed_mistakes
        self.__end_of_game = end_of_game_event
        self.__mistakes = 0
        self.__questions: List[Question] = []
        self.__counter = 0
        self._game_status = GameStatus.IN_PROGRESS

        self.__fill_in_questions(file_path, self.__questions)

    def get_next_question(self) -> Question:
        return self.__questions[self.__counter]

    def give_answer(self, answer: bool):
        def is_last_question() -> bool:
            return self.__counter == len(self.__questions) - 1

        def exidded_allowed_mistakes() -> bool:
            return self.__mistakes > self.__allowed_mistakes

        if self.__questions[self.__counter].is_true != answer:
            self.__mistakes += 1

        if is_last_question() or exidded_allowed_mistakes():
            self._game_status = GameStatus.GAME_IS_OVER

            result = GameResult(self.__counter, self.__mistakes, self.__mistakes <= self.__allowed_mistakes)
            self.__end_of_game(result)

        self.__counter += 1

    @property
    def game_status(self):
        return self._game_status

    def __fill_in_questions(self, file_path, questions):
        with open(file_path, encoding="utf8") as file:
            for line in file:
                q = self.__parse_line(line)
                questions.append(q)

    def __parse_line(self, line: str) -> Question:
        parts = line.split(';')
        text = parts[0]
        is_correct = parts[1] == 'Yes'
        explanation = parts[2]

        return Question(text, is_correct, explanation)
