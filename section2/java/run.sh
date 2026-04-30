#!/bin/bash

if [ -z "$1" ] 
then 
    echo "Usage: run.sh [MainClassName] e.g. PartA/B/C/D/E/F"
    exit 1
fi 

mvn package

spark-submit --class $1 target/section2_sparksql-1.0.0-SNAPSHOT.jar
