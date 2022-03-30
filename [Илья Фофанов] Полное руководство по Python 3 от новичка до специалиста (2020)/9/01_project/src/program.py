import random
from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Character:
    def __init__(self, armor: int, power: int):
        self.power = power
        self.armor = armor
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(30, 20)

amount: int

price: Optional[int]
price = 10

attack: Any
attack = 1

length: Union[int, float]
length = 1
length = 1.2

quotes: list
quotes: List[int]

player: Tuple[str, int] = ('Aleksey', 276)

changes_in_rating: Tuple[int, ...]
changes_in_rating = (3, 4, 5, 4, 456, 3, 4, 4, 54)

chess_player: Dict[str, int] = {"Alex": 3334}


def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)
