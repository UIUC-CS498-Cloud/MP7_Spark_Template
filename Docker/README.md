# Unified Docker for Spark MapReduce and SparkSQL

This Docker image combines the capabilities of both Spark MapReduce and SparkSQL into a single container.

## What's Included

- **Ubuntu 22.04 LTS** base image
- **Hadoop 3.3.6**
- **Spark 3.5.4**
- **OpenJDK 21**
- **Maven** (for Java builds of SparkSQL)
- **Python 3** with pip, numpy, and Cython

## Environment Variables

- `HADOOP_PREFIX`, `HADOOP_HOME` - Hadoop installation
- `SPARK_HOME` - Spark installation
- `PYSPARK_PYTHON=python3`
- `JAVA_HOME` - Java installation (auto-detected for x86_64 or ARM64)

## Build Instructions
It might take some time to fetch and build all layers
```bash
cd MP7_Spark_Template/Docker
docker build -t mp7 .
```

## Usage

### run with the code directory mounted
```bash
docker run -v <PATH_TO_LOCAL_REPO>:/MP7_Spark_Template --name mp7-cntr -it mp7
```

## Directory Structure

This unified container supports:
- Python Spark MapReduce
- Python SparkSQL
- Java SparkSQL

## Log

Created March 2026 - Merged from earlier MP Spark Docker configurations (Jiyu Hu: jiyuhu2@illinois.edu)
