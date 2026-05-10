# Fetch ubuntu 22.04 LTS docker image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive 
ENV PYSPARK_PYTHON=python3

# Update apt repository mirror for faster downloads
RUN sed -i 's|http://security.ubuntu.com|http://archive.ubuntu.com|g' /etc/apt/sources.list

# Install all dependencies needed for both sections
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        vim \
        wget \
        expect \
        git \
        zip \
        unzip \
        ca-certificates-java \
        openjdk-21-jdk \
        maven \
        sudo \
        python3 \
        python3-pip \
    && apt-get clean

################################################################################
####################   Hadoop stuff (from mp7)   ###############################
################################################################################

# downloads.apache.org is the fast CDN; archive.apache.org is the fallback in case the release is removed from CDN
RUN (curl --fail --progress-bar "https://downloads.apache.org/hadoop/core/hadoop-3.3.6/hadoop-3.3.6.tar.gz" \
    || curl --progress-bar "https://archive.apache.org/dist/hadoop/core/hadoop-3.3.6/hadoop-3.3.6.tar.gz") \
    | tar -xz --checkpoint=.1000 -C /usr/local/ \
    && ln -s /usr/local/hadoop-3.3.6 /usr/local/hadoop \
    && chmod a+rwx -R /usr/local/hadoop/

ENV HADOOP_PREFIX=/usr/local/hadoop
ENV HADOOP_COMMON_HOME=/usr/local/hadoop
ENV HADOOP_HDFS_HOME=/usr/local/hadoop
ENV HADOOP_MAPRED_HOME=/usr/local/hadoop
ENV HADOOP_YARN_HOME=/usr/local/hadoop
ENV HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop
ENV YARN_CONF_DIR=$HADOOP_PREFIX/etc/hadoop
ENV PATH="/usr/local/hadoop/bin:${PATH}"

################################################################################
####################   Spark stuff (newer version)   ################
################################################################################

# downloads.apache.org is the fast CDN; archive.apache.org is the fallback in case the release is removed from CDN
RUN (curl --fail --progress-bar "https://downloads.apache.org/spark/spark-3.5.8/spark-3.5.8-bin-hadoop3.tgz" \
    || curl --progress-bar "https://archive.apache.org/dist/spark/spark-3.5.8/spark-3.5.8-bin-hadoop3.tgz") \
    | tar -xz --checkpoint=.1000 -C /usr/local/ && \
    ln -s /usr/local/spark-3.5.8-bin-hadoop3 /usr/local/spark && \
    rm -rf /usr/local/spark/external && \
    chmod a+rwx -R /usr/local/spark/

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install Cython
RUN pip3 install numpy

# Ensure spark log output is redirected to stderr
RUN cp /usr/local/spark/conf/log4j2.properties.template /usr/local/spark/conf/log4j2.properties

# Set relevant environment variables to simplify usage of spark
ENV SPARK_HOME=/usr/local/spark
ENV PATH="/usr/local/spark/bin:${PATH}"
RUN chmod a+rwx -R /usr/local/spark/

################################################################################
####################   Java Configuration (merged)   ###########################
################################################################################

# Test the arch and set JAVA_HOME accordingly
RUN if [ "$(uname -m)" = "x86_64" ]; then \
        export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64; \
    else \
        export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-arm64; \
    fi && \
    export HADOOP_CLASSPATH=$JAVA_HOME/lib/tools.jar && \
    sed -i "/^export JAVA_HOME/ s:.*:export HADOOP_PREFIX=/usr/local/hadoop HADOOP_HOME=/usr/local/hadoop\n:" $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \
    sed -i "/^export HADOOP_CONF_DIR/ s:.*:export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:" $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \
    echo "export JAVA_HOME=$JAVA_HOME" >> $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \
    echo "export JAVA_HOME=$JAVA_HOME" >> /root/.bashrc

# Use update-alternatives to set the default java executable
RUN if [ "$(uname -m)" = "x86_64" ]; then \
        update-alternatives --set java /usr/lib/jvm/java-21-openjdk-amd64/bin/java; \
    else \
        update-alternatives --set java /usr/lib/jvm/java-21-openjdk-arm64/bin/java; \
    fi

################################################################################
####################   Additional Configuration   ##############################
################################################################################

# Make vim nice
RUN echo "set background=dark" >> ~/.vimrc

# Add spark-submit alias
RUN echo "alias spark-submit='/usr/local/spark/bin/spark-submit'" >> ~/.bashrc
