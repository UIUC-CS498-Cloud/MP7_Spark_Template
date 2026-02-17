# MP-New: Unified Spark MapReduce and SparkSQL

This directory contains a unified environment for both Spark MapReduce (MP7-style) and SparkSQL (MP8-style) assignments.

## Structure

```
mp-new/
├── Docker/           # Unified Docker image
│   ├── Dockerfile    # Merged Dockerfile
│   └── README.md     # Docker usage instructions
├── PythonTemplate/   # Python Spark MapReduce templates (from MP7)
├── python/           # Python SparkSQL templates (from MP8)
└── java/             # Java SparkSQL templates (from MP8)
```

## Quick Start

1. Build the Docker image:
```bash
cd Docker
docker build -t mp-new .
```

2. Run the container:
```bash
docker run -it --rm mp-new /bin/bash
```

3. Test Spark:
```bash
spark-submit --version
```

4. Test Hadoop:
```bash
hadoop version
```

## Features

- **Single container** for both MapReduce and SparkSQL assignments
- **Updated Spark 3.5.4** (newer than both MP7 and MP8)
- **Full Hadoop 3.3.6** support
- **Maven support** for Java projects
- **Python 3** with numpy and Cython pre-installed
