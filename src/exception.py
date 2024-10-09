import sys 

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message  ="Error occured in python script name [{0}] line number [{1}] erro message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    #when ever my error rase is i am going to call this function
    return error_message
    


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message