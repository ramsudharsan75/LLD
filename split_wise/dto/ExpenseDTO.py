from LLD.split_wise.model.User import User
from LLD.split_wise.strategy.SplitStrategy import SplitStrategy


class ExpenseDTO:
    def __init__(
        self,
        paid_by: User,
        amount: int,
        no_of_users: int,
        paid_for: list[User],
        split_strategy: SplitStrategy,
        split_values: list[int],
    ) -> None:
        self.paid_by: User = paid_by
        self.amount: int = amount
        self.no_of_users: int = no_of_users
        self.paid_for: list[User] = paid_for
        self.split_strategy: SplitStrategy = split_strategy
        self.split_values: list[int] = split_values
