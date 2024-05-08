from LLD.split_wise.dto.ExpenseDTO import ExpenseDTO
from LLD.split_wise.model.User import User


class AppDTO:
    def __init__(self, users: list[User], can_simplify: bool = False) -> None:
        self.users: dict[str, User] = {user.name: user for user in users}
        self.can_simplify: bool = can_simplify
        self.expenses: list[ExpenseDTO] = []
