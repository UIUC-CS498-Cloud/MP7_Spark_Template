# MP7_Spark_Template: Unified Spark MapReduce and SparkSQL

This directory contains a unified environment for both Spark MapReduce and SparkSQL assignments.

## Structure

```
MP7_Spark_Template/
├── README.md
├── Docker/                # Unified Docker image and Docker-related assets
│   ├── Dockerfile
│   └── README.md
├── script/                # helper scripts (package & test helpers)
│   ├── package_submission.sh
│   ├── check_submission_zip.py
│   ├── run_test_sec1.sh   # run in container
│   └── run_test_sec2.sh   # run in container
├── section1/              # Spark MapReduce templates
│   ├── OrphanPagesSpark.py
│   ├── PopularityLeagueSpark.py
│   ├── TitleCountSpark.py
│   ├── TopPopularLinksSpark.py
│   ├── TopTitleStatisticsSpark.py
│   ├── delimiters.txt
│   ├── stopwords.txt
│   └── dataset/
└── section2/              # SparkSQL templates
    ├── java/
    │   ├── pom.xml
    │   ├── run.sh
    │   └── src/main/java/
    └── python/
        ├── PartA.py
        ├── PartB.py
        ├── PartC.py
        ├── PartD.py
        ├── PartE.py
        └── PartF.py
```

## Quick Start

1. Build the Docker image:
```bash
cd Docker
docker build -t mp7 .
```

2. Run the container:
```bash
docker run -v <PATH_TO_LOCAL_REPO>:/MP7_Spark_Template --name mp7-cntr -it mp7
```

3. Test Spark:
```bash
spark-submit --version
```

4. Test Hadoop:
```bash
hadoop version
```

## Package Submission Script
The `script/package_submission.sh` helper packages student work into `submission.zip` for grader submission. It supports two modes: Python submissions (default) and Java submissions.

- Python mode (default for section2): collects `.py` files from `section1/` and `section2/` and creates `submission.zip`.
- Java mode: expects `section2/java/pom.xml` and `section2/java/src/` to exist; it packages `pom.xml` and `src/` into `submission.zip`.

Usage examples:
```bash
# Package Python submission (section2 Python files)
./script/package_submission.sh --python

# Package Java submission (section2/java project)
./script/package_submission.sh --java
```

The script performs basic validation for Java mode and exits with an error if required files are missing. The produced archive is `submission.zip` in the repository root.

## Check Submission Zip
Use `script/check_submission_zip.py` as a quick check for submission zip file format before submitting to grader. For more info, run
```bash
python3 script/check_submission_zip.py -h
```

## Features

- **Single container** for both MapReduce and SparkSQL assignments
- **Updated Spark 3.5.4**
- **Full Hadoop 3.3.6** support
- **Maven support** for Java projects
- **Python 3** with numpy and Cython pre-installed


## Log

Created 4/6/2026 by Jiyu Hu (jiyuhu2@illinois.edu)
