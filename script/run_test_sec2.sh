#!/bin/bash

# Run test script for MP-New Docker container
# This script tests Spark and Hadoop functionality

set -e

echo "=========================================="
echo "MP-New Container Test Script"
echo "=========================================="
echo ""

cd section2/python
spark-submit MP8_PartA.py
spark-submit MP8_PartB.py
spark-submit MP8_PartC.py
spark-submit MP8_PartD.py
spark-submit MP8_PartE.py

cd ../java
./run.sh MP8_PartA Output_PartA
./run.sh MP8_PartB Output_PartB
./run.sh MP8_PartC Output_PartC
./run.sh MP8_PartD Output_PartD
./run.sh MP8_PartE Output_PartE