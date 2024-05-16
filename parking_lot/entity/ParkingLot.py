from LLD.parking_lot.entity.Floor import Floor
from LLD.parking_lot.entity.Ticket import Ticket
from LLD.parking_lot.entity.Vehicle import Vehicle
from LLD.parking_lot.util.enum import VehicleTypeEnum


class ParkingLot:
    def __init__(
        self, parking_name: str, no_of_floors: int, no_of_slots_per_floor: int
    ) -> None:
        self.parking_lot_name = parking_name
        self.floors: list[Floor] = []
        self.no_of_slots_per_floor = no_of_slots_per_floor
        Floor.initialize_floors(self.floors, no_of_floors, no_of_slots_per_floor)

        self.tickets: dict[str, Ticket] = {}

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            for slot_no in range(self.no_of_slots_per_floor):
                available_slots = floor.booked_slots[vehicle.vehicle_type]
                if slot_no not in available_slots:
                    continue

                slot = available_slots[slot_no]
                floor.book_slot(slot)
                ticket = Ticket(
                    ticket_id=(
                        f"{self.parking_lot_name}_{floor.floor_no}_{slot.slot_no}"
                    ),
                    floor=floor,
                    slot=slot,
                    vehicle=vehicle,
                )
                self.tickets[ticket.ticket_id] = ticket
                print(f"Parked vehicle. Ticket ID: {ticket.ticket_id}")
        print("Parking Lot Full")

    def unpark_vehicle(self, ticked_id: str):
        if ticked_id not in self.tickets:
            print("Invalid Ticket")
            return

        ticket = self.tickets[ticked_id]
        del self.tickets[ticked_id]
        ticket.floor.release_slot(ticket.slot)
        print(
            f"Unparked vehicle with Registration Number: {ticket.vehicle.reg_no} and Color: {ticket.vehicle.color}"
        )

    def display_no_of_free_slots_per_floor_per_vehicle_type(
        self, vehicle_type: VehicleTypeEnum
    ):
        for floor in self.floors:
            print(
                f"No. of free slots for {vehicle_type.value} on Floor {floor.floor_no}: {len(floor.available_slots[vehicle_type])}"
            )

    def display_all_free_slots_per_floor_per_vehicle_type(
        self, vehicle_type: VehicleTypeEnum
    ):
        for floor in self.floors:
            slot_nos = []

            for slot_no in range(self.no_of_slots_per_floor):
                available_slots = floor.available_slots[vehicle_type]

                if slot_no in available_slots.keys():
                    slot_nos.append(str(slot_no))

            print(
                f"Free slots for {vehicle_type.value} on Floor {floor.floor_no}: {",".join(slot_nos)}"
            )

    def display_all_booked_slots_per_floor_per_vehicle_type(
        self, vehicle_type: VehicleTypeEnum
    ):
        for floor in self.floors:
            slot_nos = []

            for slot_no in range(self.no_of_slots_per_floor):
                booked_slots = floor.available_slots[vehicle_type]

                if slot_no in booked_slots.keys():
                    slot_nos.append(str(slot_no))

            print(
                f"Occupied slots for {vehicle_type.value} on Floor {floor.floor_no}: {",".join(slot_nos)}"
            )
