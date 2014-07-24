# Topogram Data

Download, extract and index the the Weiboscope dataset collected from **Sina Weibo** by JMSC HKU - [link](http://147.8.142.179/datazip/).

Requirements are  :

    * 30+ GB free space
    * ElasticSearch
    * ElasticSearch SmartCN Analyzer plugin
    * MongoDB
    * Python 2.7

## How to use it

    ./setup.sh


## Install

You will need mongoDB and Elastic Search with the [Smart Chinese Analyzer](https://github.com/elasticsearch/elasticsearch-analysis-smartcn)

    bin/plugin -install elasticsearch/elasticsearch-analysis-smartcn/2.1.0


## Data : the Weiboscope  corpus 

The dataset contains sample data from 52 weeks of 2012 from more than 350,000 Chinese microbloggers who have more than 1,000 followers [(Fu, Chan &Chau, 2013)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2265271).

Note : this data has been anonymized

**Data Set Statistics:**

    * Number of weibo messages: 226841122
    * Number of deleted messages: 10865955
    * Number of censored ('Permission Denied') messages: 86083
    * Number of unique weibo users: 14387628
    * 57 files, 18G

