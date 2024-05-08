from typing import Self

from LLD.split_wise.dto.UserDTO import UserDTO


class User:
    def __init__(self, user_dto: UserDTO) -> None:
        self.user_dto = user_dto

    @property
    def name(self):
        return self.user_dto.name

    def update_balance(self, owed_to: Self, amount: float):
        self.user_dto.balance_sheet[owed_to] += amount

    def print_user_balances(self):
        if self.user_dto.balance_sheet:
            for owed_to, amount in self.user_dto.balance_sheet.items():
                if amount:
                    print(f"{self.name} owes {owed_to.name}: {amount}")
        else:
            print(f"{self.name} has no balances")

    def no_of_balance(self):
        return len(self.user_dto.balance_sheet)
