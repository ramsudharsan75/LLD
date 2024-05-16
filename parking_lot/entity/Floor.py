from collections import defaultdict
from LLD.parking_lot.entity.Slot import Slot
from LLD.parking_lot.util.enum import VehicleTypeEnum


class Floor:
    def __init__(self, floor_no: int) -> None:
        self.floor_no = floor_no
        self.available_slots: dict[VehicleTypeEnum, dict[int, Slot]] = defaultdict(dict)
        self.booked_slots: dict[VehicleTypeEnum, dict[int, Slot]] = defaultdict(dict)

    def __hash__(self) -> int:
        return self.floor_no

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Floor):
            return value.floor_no == self.floor_no

        return False

    def book_slot(self, slot: Slot):
        available_vehicle_type_slots = self.available_slots[slot.vehicle_type]
        del available_vehicle_type_slots[slot.slot_no]
        self.booked_slots[slot.vehicle_type][slot.slot_no] = slot

    def release_slot(self, slot: Slot):
        booked_vehicle_type_slots = self.booked_slots[slot.vehicle_type]
        del booked_vehicle_type_slots[slot.slot_no]
        self.available_slots[slot.vehicle_type][slot.slot_no] = slot

    @staticmethod
    def initialize_floors(
        floors: list["Floor"], no_of_floors: int, no_of_slots_per_floor: int
    ):
        for floor_no in range(no_of_floors):
            floor = Floor(floor_no)
            floors.append(floor)
            Slot.initialize_slots(floor.available_slots, no_of_slots_per_floor)
