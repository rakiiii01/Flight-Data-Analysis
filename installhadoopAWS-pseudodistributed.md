### Install Hadoop pseudo distributed mode in an AWS-EC2 instance
```https://tokluo.wordpress.com/2016/01/18/setup-hadoop-in-single-node/```


### More notes
ubuntu 16.04 or 18.04 has an issue
ERROR org.apache.hadoop.security.token.delegation.AbstractDelegationTokenSecretManager: ExpiredTokenRemover received java.lang.InterruptedException: sleep interrupted

downgrade to 14.04


14.04 ubuntu: 1 vCPUs, 2 GiB

* ssh ubuntu@public DNS (to login into master machine)

* wget https://archive.apache.org/dist/hadoop/core/hadoop-2.6.5/hadoop-2.6.5.tar.gz

* install java 7
sudo apt install openjdk-7-jre-headless 
which java # to find java home

* install jps
sudo apt install openjdk-7-jdk-headless 

* edit .bashrc

export HADOOP_HOME="/home/ubuntu/bigdata/hadoop-2.6.5"
export PATH="$PATH:$HADOOP_HOME/bin"
export PATH="$PATH:$HADOOP_HOME/sbin"
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR="$HADOOP_HOME/etc/hadoop"
export HADOOP_COMMON_LIB_NATIVE_DIR="$HADOOP_HOME/lib/native"

export JAVA_HOME="/usr"
export PATH=$JAVA_HOME/bin:$PATH



* in etc/hadoop/hadoop-env.sh 
export JAVA_HOME="/usr"
export HADOOP_PREFIX=/home/ubuntu/bigdata/hadoop-2.6.5

export HADOOP_CONF_DIR=/home/ubuntu/bigdata/hadoop-2.6.5/etc/hadoop
export HADOOP_HOME=/home/ubuntu/bigdata/hadoop-2.6.5

for file in $HADOOP_HOME/share/hadoop/*/*.jar
do
  export CLASSPATH=$CLASSPATH:$file
done

for file in $HADOOP_HOME/share/hadoop/*/lib/*.jar
do
  export CLASSPATH=$CLASSPATH:$file
done









