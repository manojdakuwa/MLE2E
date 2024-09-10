import sys #sys library automatically have information if there is any change in file for exception

from src.logger import logging

def err_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error accurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = err_message_detail(error_message, error_details)
    
    def __str__(self):
        return self.error_message
    
# if __name__=="__main__":
#     try:
#         a = 1/0
#     except Exception as e:
        
#         logging.info("Divide by Zero error")
#         raise CustomException(e, sys)