# bloomfilter-api
A bloom filter which base web.py

RUN
===
python bloomfilter.py 8080

+++ Bloom filter test
curl 127.0.0.1:8080/find?id=XXXXX

if the segement is not process bloomfilter yet,it return a string names "FALSE".
otherwise,processing a duplicate data,it would return a string "TURE"

+++ Save the bloom filter for continue   
curl 127.0.0.1:8080/save


+++ Delete the saved file
curl 127.0.0.1:8080/init


