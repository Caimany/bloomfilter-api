# bloomfilter-api
A simply bloom filter  which base web.py

REQUIREMENT
===========
pip install web.py

pip insatll pybloom

pip install json

RUN
===
python bloomfilter.py 8080

HOW TO USE
==========
+++ Change the capacity of bloom filter

 modify the value of the bloomfilter.py 
 
 default exact is 1000000 , it located about 500M memory .

+++ Bloom filter test
 curl 127.0.0.1:8080/bloom?id=XXXXX

if the segement is not process bloomfilter yet,it return  "FALSE".
 otherwise,processing a duplicate data,it would return  "TURE"

+++ Save the bloom filter for continue   
 curl 127.0.0.1:8080/save


+++ Delete the saved file 
 curl 127.0.0.1:8080/init



