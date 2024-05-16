from LLD.parking_lot.dto.CommandDTO import (
    CreateParkingLotCommandDTO,
    DisplayCommandDTO,
    ExitCommandDTO,
    ParkVehicleCommandDTO,
    UnparkVehicleCommandDTO,
)


class CommandDTOFactory:
    @staticmethod
    def get_command_dto(input: str):
        inputs = input.split(" ")
        command_type = inputs[0]

        if command_type == "create_parking_lot":
            return CommandDTOFactory.get_create_parking_lot_command_dto(inputs)
        elif command_type == "park_vehicle":
            return CommandDTOFactory.get_park_vehicle_command_dto(inputs)
        elif command_type == "unpark_vehicle":
            return CommandDTOFactory.get_unpark_vehicle_command_dto(inputs)
        elif command_type == "display":
            return CommandDTOFactory.get_display_command_dto(inputs)
        else:
            return ExitCommandDTO()

    @staticmethod
    def get_create_parking_lot_command_dto(inputs: list[str]):
        return CreateParkingLotCommandDTO(
            parking_lot_name=inputs[1],
            no_of_floors=int(inputs[2]),
            no_of_slots_per_floor=int(inputs[3]),
        )

    @staticmethod
    def get_display_command_dto(inputs: list[str]):
        return DisplayCommandDTO(display_type=inputs[1], vehicle_type=inputs[2])

    @staticmethod
    def get_park_vehicle_command_dto(inputs: list[str]):
        return ParkVehicleCommandDTO(
            vehicle_type=inputs[1], reg_no=inputs[2], color=inputs[3]
        )

    @staticmethod
    def get_unpark_vehicle_command_dto(inputs: list[str]):
        return UnparkVehicleCommandDTO(ticket_id=inputs[1])
