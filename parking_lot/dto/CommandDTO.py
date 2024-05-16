from dataclasses import dataclass


class CommandDTO:
    ...


@dataclass
class CreateParkingLotCommandDTO(CommandDTO):
    parking_lot_name: str
    no_of_floors: int
    no_of_slots_per_floor: int


@dataclass
class ParkVehicleCommandDTO(CommandDTO):
    vehicle_type: str
    reg_no: str
    color: str


@dataclass
class UnparkVehicleCommandDTO(CommandDTO):
    ticket_id: str


@dataclass
class DisplayCommandDTO(CommandDTO):
    display_type: str
    vehicle_type: str


@dataclass
class ExitCommandDTO(CommandDTO):
    pass
