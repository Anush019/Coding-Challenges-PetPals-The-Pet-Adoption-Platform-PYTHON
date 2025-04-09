class AdoptionException(Exception):
    def __init__(self, message="Adoption operation failed."):
        super().__init__(message)

