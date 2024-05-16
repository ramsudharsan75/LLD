from LLD.parking_lot.dto.CommandDTO import (
    CreateParkingLotCommandDTO,
    DisplayCommandDTO,
    ExitCommandDTO,
    ParkVehicleCommandDTO,
    UnparkVehicleCommandDTO,
)
from LLD.parking_lot.entity.ParkingLot import ParkingLot
from LLD.parking_lot.entity.Vehicle import Vehicle
from LLD.parking_lot.factory.CommandDTOFactory import CommandDTOFactory
from LLD.parking_lot.service.InputReaderService import InputReaderService
from LLD.parking_lot.util.enum import VehicleTypeEnum


class Driver:
    @staticmethod
    def start():
        parking_lot: ParkingLot | None = None

        while True:
            usr_input = InputReaderService.read_input()
            command_dto = CommandDTOFactory.get_command_dto(usr_input)

            if parking_lot is None:
                if not isinstance(command_dto, CreateParkingLotCommandDTO):
                    print("Invalid command")
                else:
                    parking_lot = ParkingLot(
                        command_dto.parking_lot_name,
                        command_dto.no_of_floors,
                        command_dto.no_of_slots_per_floor,
                    )
                    print(
                        f"Created parking lot with {command_dto.no_of_floors} floors and {command_dto.no_of_slots_per_floor} slots per floor"
                    )
            else:
                if isinstance(command_dto, ParkVehicleCommandDTO):
                    vehicle = Vehicle(
                        vehicle_type=VehicleTypeEnum[command_dto.vehicle_type],
                        reg_no=command_dto.reg_no,
                        color=command_dto.color,
                    )
                    parking_lot.park_vehicle(vehicle)
                elif isinstance(command_dto, UnparkVehicleCommandDTO):
                    parking_lot.unpark_vehicle(command_dto.ticket_id)
                elif isinstance(command_dto, DisplayCommandDTO):
                    vehicle_type = VehicleTypeEnum[command_dto.vehicle_type]

                    if command_dto.display_type == "free_count":
                        parking_lot.display_no_of_free_slots_per_floor_per_vehicle_type(
                            vehicle_type
                        )
                    elif command_dto.display_type == "free_slots":
                        parking_lot.display_all_free_slots_per_floor_per_vehicle_type(
                            vehicle_type
                        )
                    elif command_dto.display_type == "occupied_slots":
                        parking_lot.display_all_booked_slots_per_floor_per_vehicle_type(
                            vehicle_type
                        )
                elif isinstance(command_dto, ExitCommandDTO):
                    break
