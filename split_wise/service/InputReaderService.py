class InputReaderService:
    @staticmethod
    def read_input():
        print()
        return input("Enter input")

    @staticmethod
    def validate_input(split_strategy_name: str, amount: int, split_values: list[int]):
        if (split_strategy_name == "EXACT" and amount != sum(split_values)) or (
            split_strategy_name == "PERCENT" and sum(split_values) != 100
        ):
            raise ValueError("Entered values dont sum up")
