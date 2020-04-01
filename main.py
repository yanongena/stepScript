from OciPipeline import OciPipeline
import os
from random import randint
import time
import sys

pipeline = OciPipeline()

directory = sys.argv[1]

if directory is None:
    pipeline.error("No input parameters provided.")
    pipeline.finished(pipeline.WITH_ERROR)
    exit(-1)

pipeline.start("Step 1")

count = len(os.listdir(directory))
progress = 0
for filename in os.listdir(directory):
    value = randint(1,10)
    time.sleep(value)
    #print(filename)
    progress += 1
    pipeline.status((progress/count)*100)

pipeline.finished(pipeline.COMPLETED)