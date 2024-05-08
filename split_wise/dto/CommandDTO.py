class CommandDTO:
    pass


class ExpenseCommandDTO(CommandDTO):
    def __init__(
        self,
        paid_by_user_name: str,
        amount: int,
        no_of_users: int,
        paid_for_user_names: list[str],
        split_strategy_name: str,
        split_values: list[int],
    ) -> None:
        super().__init__()
        self.paid_by_user_name: str = paid_by_user_name
        self.amount: int = amount
        self.no_of_users: int = no_of_users
        self.paid_for_user_names: list[str] = paid_for_user_names
        self.split_strategy_name: str = split_strategy_name
        self.split_values: list[int] = split_values


class ShowCommandDTO(CommandDTO):
    def __init__(self, user_name: str = "") -> None:
        super().__init__()
        self.user_name = user_name
