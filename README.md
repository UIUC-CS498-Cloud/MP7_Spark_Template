# MP7_Spark_Template: Unified Spark MapReduce and SparkSQL

This directory contains a unified environment for both Spark MapReduce and SparkSQL assignments.

## Structure

```
MP7_Spark_Template/
├── README.md
├── Docker/                # Unified Docker image
│   ├── Dockerfile
│   └── README.md
├── script/                # section separate test script (run in docker)
│   ├── run_test_sec1.sh
│   └── run_test_sec2.sh
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
