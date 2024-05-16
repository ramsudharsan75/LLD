from LLD.parking_lot.util.enum import VehicleTypeEnum


class Slot:
    def __init__(self, slot_no: int, vehicle_type: VehicleTypeEnum) -> None:
        self.slot_no = slot_no
        self.vehicle_type = vehicle_type

    def __hash__(self) -> int:
        return self.slot_no

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Slot):
            return self.slot_no == value.slot_no

        return False

    @staticmethod
    def initialize_slots(
        slots: dict[VehicleTypeEnum, dict[int, "Slot"]], no_of_slots: int
    ):
        for slot_no in range(no_of_slots):
            if slot_no == 0:
                vehicle_type = VehicleTypeEnum.TRUCK
            elif slot_no <= 2:
                vehicle_type = VehicleTypeEnum.BIKE
            else:
                vehicle_type = VehicleTypeEnum.CAR

            slot = Slot(slot_no, vehicle_type)
            slots[vehicle_type][slot.slot_no] = slot
