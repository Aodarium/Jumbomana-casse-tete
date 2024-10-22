"""
Exceptions linked to the api 
"""


class NoMovementError(Exception):
    """Exception raised when no movement is available"""


class FenError(Exception):
    """Exception raised when the fen is not valid"""
