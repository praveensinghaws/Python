#!/bin/bash

# Activate the virtual environment
source pksenv/bin/activate

# Change directory to Python/wsCubeTech/
cd Python/wsCubeTech/

# Run Jupyter Notebook with IP 0.0.0.0
jupyter-notebook --ip 0.0.0.0
