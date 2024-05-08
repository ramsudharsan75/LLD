from LLD.split_wise.dto.CommandDTO import ExpenseCommandDTO, ShowCommandDTO


class CommandFactory:
    @staticmethod
    def create_command_dto(inputs: list[str]):
        if inputs[0] == "EXPENSE":
            return CommandFactory._create_expense_command_dto(inputs=inputs[1:])
        else:
            return CommandFactory._create_show_command(inputs=inputs[1:])

    @staticmethod
    def _create_expense_command_dto(inputs: list[str]) -> ExpenseCommandDTO:
        no_of_users = int(inputs[2])
        return ExpenseCommandDTO(
            paid_by_user_name=inputs[0],
            amount=int(inputs[1]),
            no_of_users=no_of_users,
            paid_for_user_names=inputs[3 : 3 + no_of_users],
            split_strategy_name=inputs[3 + no_of_users],
            split_values=[int(val) for val in inputs[no_of_users + 4 :]],
        )

    @staticmethod
    def _create_show_command(inputs: list[str]):
        if inputs:
            return ShowCommandDTO(user_name=inputs[0])
        return ShowCommandDTO()
