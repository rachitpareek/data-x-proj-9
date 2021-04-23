#!/usr/bin/env bash

# Error script on individual command error
set -e

# In order to use this script, type ".deploy.sh ARGUMENT", where ARGUMENT is one of the following:
#   "setup", "server", or "jupyter". See sections below to see what each does.

# "setup" will activate install necessary dependencies, 
#   activate the conda environment, and will finally download the trained model file.
if [[ $1 == "setup" ]]
then
    ENVS=$(conda env list)
    if [[ $ENVS = *"datax"* ]]
    then
        echo "datax environment already exists!"
    else 
        echo "Creating datax environment from environment file..."
        conda env create -f environment.yml
    fi
    echo "Downloading pretrained model file from Google Drive (438 MB)..."
    gdown https://drive.google.com/uc?id=1qc2Gp4bIahQHIbrDnpmq0v5SBDkScEAj
fi

# "server" will run the local Flask server.
if [[ $1 == "server" ]]
then
    python3 server/app.py
fi

# "jupyter" will run the local Jupyter Notebook server.
if [[ $1 == "jupyter" ]]
then
    jupyter notebook
fi

echo "Script execution complete for command \"$1\"!"
