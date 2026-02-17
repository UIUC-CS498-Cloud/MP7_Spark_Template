#!/bin/bash

# Run test script for MP-New Docker container
# This script tests Spark and Hadoop functionality

set -e

echo "=========================================="
echo "MP-New Container Test Script"
echo "=========================================="
echo ""

spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ partA
spark-submit TopTitleStatisticsSpark.py partA partB
spark-submit OrphanPagesSpark.py dataset/links/ partC
spark-submit TopPopularLinksSpark.py dataset/links/ partD
spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt partE