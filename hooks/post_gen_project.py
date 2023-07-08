#!/bin/python

import os

COMMANDS_TO_RUN = [
    "pip install -r requirements.txt",
    "pre-commit install"
]

for command in COMMANDS_TO_RUN:
    os.system(command)