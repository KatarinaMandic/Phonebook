class InvalidTelephoneError (Exception):

    def __init__(self) -> None:
        super().__init__('Invalid telephone.')