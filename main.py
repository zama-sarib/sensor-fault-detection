from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.logger import logging

import os,sys

try:
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
except Exception as e:
    print(e)
    logging.exception(e)