import math
from abc import ABC, abstractmethod

from LLD.split_wise.model.User import User


class SplitStrategy(ABC):
    @staticmethod
    @abstractmethod
    def split_expense(
        amount: int,
        no_of_users: int,
        paid_by: User,
        paid_for: list[User],
        split_values: list[int],
    ):
        pass


class EqualSplitStrategy(SplitStrategy):
    @staticmethod
    def split_expense(
        amount: int,
        no_of_users: int,
        paid_by: User,
        paid_for: list[User],
        split_values: list[int],
    ):
        first_user_split_amount = math.ceil(amount * 100 / no_of_users) / 100
        other_user_split_amount = math.floor(amount * 100 / no_of_users) / 100

        for i, ower in enumerate(paid_for):
            if ower == paid_by:
                continue

            if i == 0:
                ower.update_balance(paid_by, first_user_split_amount)
            else:
                ower.update_balance(paid_by, other_user_split_amount)


class ExactSplitStrategy(SplitStrategy):
    @staticmethod
    def split_expense(
        amount: int,
        no_of_users: int,
        paid_by: User,
        paid_for: list[User],
        split_values: list[int],
    ):
        for i, ower in enumerate(paid_for):
            if ower == paid_by:
                continue

            ower.update_balance(paid_by, split_values[i])


class PercentSplitStrategy(SplitStrategy):
    @staticmethod
    def split_expense(
        amount: int,
        no_of_users: int,
        paid_by: User,
        paid_for: list[User],
        split_values: list[int],
    ):
        for i, ower in enumerate(paid_for):
            if ower == paid_by:
                continue

            value = split_values[i] * amount / 100
            ower.update_balance(paid_by, value)
