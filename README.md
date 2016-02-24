# Play-Hadoop-Python

My implementation of a simple Map/Reduce program in python.

Takes words and Maps each to a a value (1). Then, the reducer aggregates each word, summing its value to return the count of each word.
Plan to make changes to the map/reducing usage, maybe running a learning algorithm on it or something.

This program makes use of "Streaming" within Hadoop. What this does is map the STDin to a mapper and the stdout from the mapper to the reducer.
This allows me to use a python file in order to M/R, rather than traditionally Java.

Some commands to remember: 
cd usr/local/Cellar/Hadoop (brew installation)
First SSH into localhost (by default http://localhost:50070/)

Starting Node for file system:
  $ sbin/start-dfs.sh
Stopping Node for file system:
    $ sbin/stop-dfs.sh


Running jar file with input guten, output dir guten-output2, mapper.py, and reducer.py utilizing STREAM "api"
bin/hadoop jar libexec/share/hadoop/tools/sources/hadoop-streaming-2.7.2.jar \
    -input /user/ahendy/guten/* \   
    -output /user/ahendy/guten-output2 \
    -mapper /Users/ahendy/Documents/hadoopTesting/mapper.py  \
    -reducer /Users/ahendy/Documents/hadoopTesting/reducer.py \
    -file /Users/ahendy/Documents/hadoopTesting/mapper.py \
    -file /Users/ahendy/Documents/hadoopTesting/reducer.py

Note: guten contains txt files, guten-output2 is output directory to be made.
Mapper and reducer are found locally rather than on the HDFS, meaning it needs to be specified as a "file".

Files can be moved from HFDS (hadoop file directory system) to local with:

  hadoop fs -copyToLocal <hfdsfile/> <localdir>
  
Similarily 
  hadoop fs - copyFromLocal <localfile/> <hfdsdir>
  hadoop fs -put
  hadoop fs -mkdir
  hadoop fs -ls


Some tutorials I used to set up hadoop:
  http://zhongyaonan.com/hadoop-tutorial/setting-up-hadoop-2-6-on-mac-osx-yosemite.html
  https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
  https://ambari.apache.org/1.2.5/installing-hadoop-using-ambari/content/ambari-kerb-2-2-2b.html
  http://www.quuxlabs.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
  https://hadoop.apache.org/docs/r1.2.1/streaming.html
  http://hortonworks.com/hadoop-tutorial/using-commandline-manage-files-hdfs/
