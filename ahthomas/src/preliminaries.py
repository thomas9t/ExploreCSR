import os
import shutil

if os.path.exists("../temp"):
    shutil.rmtree("../temp")
os.mkdir("../temp")

if os.path.exists("../output"):
    shutil.rmtree("../output")
os.mkdir("../output")

