from LLD.split_wise.dto.UserDTO import UserDTO


class UserFactory:
    @staticmethod
    def create_user_dto(name: str) -> UserDTO:
        return UserDTO(name)
