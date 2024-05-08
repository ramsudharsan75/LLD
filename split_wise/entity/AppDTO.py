from LLD.split_wise.dao.User import User
from LLD.split_wise.entity.ExpenseDTO import ExpenseDTO


class AppDTO:
    def __init__(self, users: list[User], can_simplify: bool = False) -> None:
        self.users: dict[str, User] = {user.name: user for user in users}
        self.can_simplify: bool = can_simplify
        self.expenses: list[ExpenseDTO] = []
