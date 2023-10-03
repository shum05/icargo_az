import sys
from src.logger import logging

# set a custom exception
def generate_error_message(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):  #  inherits from the built-in Exception class.
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=generate_error_message(error_message,error_detail=error_detail)
    
    # print the erro message
    # __str__ method is overridden to return the custom error message when the exception is converted to a string.
    def __str__(self):
        return self.error_message
    
# Research
# run 'python src/exception.py' from terminal
# import math
# if __name__=="__main__":
#     try:
#         res = math.sqrt(-4)
#     except Exception as e:
#         logging.info("NaN- sqrt of a negative number")
#         raise CustomException(e,sys)
     
    
#     # Note that 'Logs' folder created, formatted log recoreded