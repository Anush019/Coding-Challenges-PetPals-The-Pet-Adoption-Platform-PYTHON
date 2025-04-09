class NullReferenceException(Exception):
    def __init__(self,message="Null reference encountered in pet details."):
        super().__init__(message)