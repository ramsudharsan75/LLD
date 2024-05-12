from LLD.chess_validator.entity.Chess import Chess
from LLD.chess_validator.service.InputReaderService import InputReaderService


class Driver:
    @staticmethod
    def start():
        chess = Chess()

        while True:
            user_input = InputReaderService.read_input()

            if user_input == "exit":
                break

            user_inputs = user_input.strip().split(" ")
            from_pos, to_pos = user_inputs[0], user_inputs[1]

            if chess.board.is_move_valid(chess.players[0], from_pos, to_pos):
                chess.players.append(chess.players.popleft())
                chess.board.update_pos(from_pos, to_pos)
            else:
                print("Invalid Input")
