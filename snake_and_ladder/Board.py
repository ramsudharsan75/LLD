from typing import Self

from .Player import Player


class Snake:
    def __init__(self, head: int, tail: int) -> None:
        self.head = head
        self.tail = tail

    def __hash__(self) -> int:
        return self.head

    def __eq__(self, other: Self) -> bool:
        return self.head == other.head


class Ladder:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __hash__(self) -> int:
        return self.start

    def __eq__(self, other: Self) -> bool:
        return self.start == other.start


class Board:
    def __init__(self, snakes: set[Snake], ladders: set[Ladder]) -> None:
        self.snakes = snakes
        self.ladders = ladders

    def update_player_position(self, player: Player, face: int):
        prev_position = player.position
        player.position = self._get_new_position(prev_position + face)
        print(
            f"{player} rolled a {face} and moved from {prev_position} to {player.position}"
        )

    def _get_new_position(self, position) -> int:
        for ladder in self.ladders:
            if ladder.start == position:
                return self._get_new_position(ladder.end)
        for snake in self.snakes:
            if snake.head == position:
                return self._get_new_position(snake.tail)

        return position

    def add_snake(self, snake: Snake):
        if snake.head <= snake.tail:
            raise ValueError("Invalid snake values")
        if self._does_snake_form_infinite_loop(snake):
            raise ValueError("Snake forms infinite loop")
        if self._does_snake_clash_with_ladder(snake):
            raise ValueError("Snake clashes with ladder")
        if snake in self.snakes:
            raise ValueError("Snake already present")

        self.snakes.add(snake)

    def _does_snake_clash_with_ladder(self, snake: Snake):
        return snake in self.ladders

    def _does_snake_form_infinite_loop(self, snake: Snake):
        for ladder in self.ladders:
            if ladder.start == snake.tail:
                if snake.head == ladder.end:
                    return True

                break

        return False

    def add_ladder(self, ladder: Ladder):
        if ladder.start >= ladder.end:
            raise ValueError("Invalid ladder values")
        if self._does_ladder_form_infinit_loop(ladder):
            raise ValueError("Ladder forms infintie loop")
        if self._does_ladder_clash_with_snake(ladder):
            raise ValueError("Ladder clashes with snake")
        if ladder in self.ladders:
            raise ValueError("Ladder already present")

        self.ladders.add(ladder)

    def _does_ladder_clash_with_snake(self, ladder: Ladder):
        return ladder in self.snakes

    def _does_ladder_form_infinit_loop(self, ladder: Ladder):
        for snake in self.snakes:
            if ladder.end == snake.head:
                if ladder.start == snake.tail:
                    return True
                break
        return False
