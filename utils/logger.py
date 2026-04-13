import logging
import sys

def get_logger(name: str = "order_pipeline"):
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
        handler.setFormatter(formatter)

        file_handler = logging.FileHandler("pipeline.log")
        file_handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

    
    return logger