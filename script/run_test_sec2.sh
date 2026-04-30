#!/bin/bash

# Run test script for MP7 Docker container. Should be executed inside the container
# This script tests Spark and Hadoop functionality

set -e

echo "=========================================="
echo "MP7 Section 2 Container Test Script"
echo "=========================================="
echo ""

cd ../section2/python
spark-submit PartA.py
spark-submit PartB.py
spark-submit PartC.py
spark-submit PartD.py
spark-submit PartE.py

cd ../java
./run.sh PartA Output_PartA
./run.sh PartB Output_PartB
./run.sh PartC Output_PartC
./run.sh PartD Output_PartD
./run.sh PartE Output_PartE
