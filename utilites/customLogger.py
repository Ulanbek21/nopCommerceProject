
#                           -------Geberating logs------- costum logg

import logging

# Creatin class
class LogGen:
    @staticmethod # you can call method directli using class
    def Loggen(): # inside mthod def logfile configuration filename--->format---->datefmt 
        logging.basicConfig(filename=".//Logs//automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p') # After crat object
        logger  = logging.getLogger() # After creating object  next creat set level
        logger.setLevel(logging.INFO) # after seting level return your object
        return logger
        
