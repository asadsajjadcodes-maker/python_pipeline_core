import logging
import sys 
# setup logging 
def setup_pipeline_logger(log_path = "pipeline.log"):

    logging.basicConfig(
        level=logging.INFO, # setting to level info
        format= "%(asctime)s [%(levelname)s] [%(name)s] %(message)s", # format 
        datefmt="%Y-%m-%d %H:%M:%S", # time format 
        handlers=[
            logging.FileHandler(log_path, mode="a", encoding="utf-8"), # save in log file 
            logging.StreamHandler(sys.stdout) # display on terminal
        ]
    )
    # return a logger object with the name "PipelineLogger"
    return logging.getLogger("PipelineLogger")
#========================================================