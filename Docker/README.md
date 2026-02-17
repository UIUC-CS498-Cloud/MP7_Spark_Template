# Unified Docker for MP7 (Spark MapReduce) and MP8 (SparkSQL)

This Docker image combines the capabilities of both MP7 and MP8 into a single container.

## What's Included

- **Ubuntu 22.04 LTS** base image
- **Hadoop 3.3.6** (from MP7)
- **Spark 3.5.4** (updated from MP8 - newer than MP7's 3.5.1)
- **OpenJDK 21**
- **Maven** (for Java builds from MP8)
- **Python 3** with pip, numpy, and Cython

## Environment Variables

- `HADOOP_PREFIX`, `HADOOP_HOME` - Hadoop installation
- `SPARK_HOME` - Spark installation
- `PYSPARK_PYTHON=python3`
- `JAVA_HOME` - Java installation (auto-detected for x86_64 or ARM64)

## Build Instructions

```bash
cd mp-new/Docker
docker build -t mp-new .
```

## Usage

### Run interactively
```bash
docker run -it --rm mp-new /bin/bash
```

### Mount your code
```bash
docker run -it --rm --mount type=bind,source=$PATH_TO_CODE,target=/cs498/ mp-new /bin/bash
```

## Directory Structure

This unified container supports:
- Python Spark MapReduce (MP7 style)
- Python SparkSQL (MP8 style)
- Java SparkSQL (MP8 style with Maven)

## Log

Created February 2025 - Merged from MP7 and MP8 Docker configurations
