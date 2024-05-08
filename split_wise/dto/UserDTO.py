from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from LLD.split_wise.model.User import User


class UserDTO:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.balance_sheet: dict[User, float] = defaultdict(float)

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UserDTO):
            return other.name == self.name

        return False
