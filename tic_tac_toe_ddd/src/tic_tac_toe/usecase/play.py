from src.tic_tac_toe.domain.entity.game import Game


class PlayTicTacToeUseCase:
    def __init__(self) -> None:
        self.game = Game()

    def play(self):
        while not self.game.has_ended:
            self.game.current_player.play(self.game)

        if self.game.winner:
            print(f"Player {self.game.winner.symbol.value} won!")
        else:
            print("It's a tie!")
