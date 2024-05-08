from LLD.split_wise.dto.AppDTO import AppDTO
from LLD.split_wise.dto.CommandDTO import ExpenseCommandDTO
from LLD.split_wise.factory.CommandFactory import CommandFactory
from LLD.split_wise.factory.UserFactory import UserFactory
from LLD.split_wise.model.App import App
from LLD.split_wise.model.User import User
from LLD.split_wise.service.InputReaderService import InputReaderService


class Driver:
    @staticmethod
    def start():
        u1_dto = UserFactory.create_user_dto("u1")
        u2_dto = UserFactory.create_user_dto("u2")
        u3_dto = UserFactory.create_user_dto("u3")
        u4_dto = UserFactory.create_user_dto("u4")

        u1 = User(u1_dto)
        u2 = User(u2_dto)
        u3 = User(u3_dto)
        u4 = User(u4_dto)

        app_dto = AppDTO([u1, u2, u3, u4])
        app = App(app_dto)

        while True:
            input_str = InputReaderService.read_input()
            inputs = input_str.split(" ")
            command_dto = CommandFactory.create_command_dto(inputs)

            if isinstance(command_dto, ExpenseCommandDTO):
                InputReaderService.validate_input(
                    command_dto.split_strategy_name,
                    command_dto.amount,
                    command_dto.split_values,
                )

            app.process_command_dto(command_dto)
