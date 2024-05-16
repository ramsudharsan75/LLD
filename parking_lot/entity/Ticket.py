from LLD.parking_lot.entity.Floor import Floor
from LLD.parking_lot.entity.Slot import Slot
from LLD.parking_lot.entity.Vehicle import Vehicle


class Ticket:
    def __init__(
        self, ticket_id: str, vehicle: Vehicle, floor: Floor, slot: Slot
    ) -> None:
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.floor = floor
        self.slot = slot

    def __hash__(self) -> int:
        return hash(self.ticket_id)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Ticket):
            return value.ticket_id == self.ticket_id

        return False
