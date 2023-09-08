#!/bin/bash
set -e # stop when encountering error
cd ..
source venv/bin/activate
cd src
uvicorn main:app --reload --host 0.0.0.0 --port 8000

