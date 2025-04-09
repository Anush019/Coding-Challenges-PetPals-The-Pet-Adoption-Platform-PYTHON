class FileHandlingException(Exception):
    def __init__(self, message="Error while handling the file."):
        super().__init__(message)
