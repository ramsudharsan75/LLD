from LLD.parking_lot.util.enum import VehicleTypeEnum


class Vehicle:
    def __init__(self, reg_no: str, vehicle_type: VehicleTypeEnum, color: str) -> None:
        self.reg_no = reg_no
        self.vehicle_type = vehicle_type
        self.color = color
