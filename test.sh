#!/bin/sh

set -x

# Invoke
cd source/invoke/examples
invoke ouverture
cd ../../..

# JSON
cd source/json/examples
python example.py
python stream.py || echo ':-)'
python validation.py
cd ../../..
