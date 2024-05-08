from LLD.split_wise.dto.AppDTO import AppDTO
from LLD.split_wise.dto.CommandDTO import CommandDTO, ExpenseCommandDTO, ShowCommandDTO
from LLD.split_wise.dto.ExpenseDTO import ExpenseDTO
from LLD.split_wise.strategy.SplitStrategy import (
    EqualSplitStrategy,
    ExactSplitStrategy,
    PercentSplitStrategy,
)


class App:
    def __init__(self, app_dto: AppDTO) -> None:
        self.app_dto = app_dto

    def process_command_dto(self, command_dto: CommandDTO):
        if isinstance(command_dto, ExpenseCommandDTO):
            paid_by = self.app_dto.users[command_dto.paid_by_user_name]
            paid_for = [
                self.app_dto.users[user_names]
                for user_names in command_dto.paid_for_user_names
            ]

            if command_dto.split_strategy_name == "EQUAL":
                split_strategy = EqualSplitStrategy()
            elif command_dto.split_strategy_name == "EXACT":
                split_strategy = ExactSplitStrategy()
            else:
                split_strategy = PercentSplitStrategy()

            split_values = command_dto.split_values
            expense_dto = ExpenseDTO(
                paid_by=paid_by,
                amount=command_dto.amount,
                no_of_users=command_dto.no_of_users,
                paid_for=paid_for,
                split_strategy=split_strategy,
                split_values=split_values,
            )
            self.app_dto.expenses.append(expense_dto)
            split_strategy.split_expense(
                amount=expense_dto.amount,
                no_of_users=expense_dto.no_of_users,
                paid_by=expense_dto.paid_by,
                paid_for=expense_dto.paid_for,
                split_values=expense_dto.split_values,
            )
        elif isinstance(command_dto, ShowCommandDTO):
            if command_dto.user_name:
                user = self.app_dto.users[command_dto.user_name]
                user.print_user_balances()
            else:
                for user in self.app_dto.users.values():
                    user.print_user_balances()
