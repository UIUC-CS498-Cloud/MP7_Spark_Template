#!/bin/bash

# Run test script for MP7 Docker container. Should be executed inside the container
# This script tests Spark and Hadoop functionality

set -e

echo "=========================================="
echo "MP7 Section 1 Container Test Script"
echo "=========================================="
echo ""

cd ../section1

spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ partA
spark-submit TopTitleStatisticsSpark.py partA partB
spark-submit OrphanPagesSpark.py dataset/links/ partC
spark-submit TopPopularLinksSpark.py dataset/links/ partD
spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt partE