import sys

def error_message_detail(error, error_detail: sys):
    """
    Generates a detailed error message including the filename, line number, and error description.

    Parameters:
        error (Exception): The original error.
        error_detail (sys): The sys module for retrieving exception details.

    Returns:
        str: A detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in file [{filename}] at line number [{exc_tb.tb_lineno}] with error [{str(error)}]"
    )
    return error_message

class MyException(Exception):
    """
    Custom exception class to handle detailed error messages.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the custom exception with detailed error information.

        Parameters:
            error_message (str): The error message to display.
            error_detail (sys): The sys module for retrieving exception details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
