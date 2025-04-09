class InsufficientFundsException(Exception):
    def __init__(self, message="Donation amount is less than the minimum allowed ($10)."):
        super().__init__(message)
