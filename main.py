from src.sensor.Expection import MyException
import sys
from src.sensor.logging import logger
def test_exception():
    try:
        logger.info("ki dhdkj sdsd fsd sdsd ")
        a=1/0
        
        
    except Exception as e:
        raise MyException(e,sys)    


if __name__ == "__main__":
    
    try:
      test_exception()
    except Exception as e:
        print(e)