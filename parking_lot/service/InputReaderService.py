class InputReaderService:
    @staticmethod
    def read_input(prompt: str = ""):
        return input((prompt + ": " if prompt else prompt))
