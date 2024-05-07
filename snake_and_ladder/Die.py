class Die:
    def __init__(self, faces: int) -> None:
        if faces <= 1:
            raise ValueError("Number of faces of a die must be more than 1")

        self.faces = faces
