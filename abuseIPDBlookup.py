#!/usr/bin/python
import requests
import json
import os, sys
import sys, json
from urllib2 import Request, urlopen
import yaml
import numpy as np
from urllib2 import Request, urlopen
import os, sys
import sys, json

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

IP = raw_input("What IP would you like to check? ")
response = []

arr = []

API_KEY="YOUR_API_KEY_HERE"

r = requests.post("https://www.abuseipdb.com/check/" + str(IP) + "/json?key=" + str(API_KEY))
response =  json.loads(r.text)

abScores = [li['abuseConfidenceScore'] for li in response]
arr2 = []

# ========================================================
# this space will be for the countries
# ========================================================
country = [li['country'] for li in response]
arr3 = []
x = []
for i in country:
    arr3.append(i)
for i in arr3:
    if i not in x:
        x.append(i)



# ========================================================
# This space will be where i gather the abuse scores and average them
# ========================================================

def aveScoreCalc(scores):
    absScores = scores
    for i in absScores:
        arr2.append(i)
    aveScore = np.mean(arr2)
    if (aveScore >= 50.0):
        return "Poor"
    elif ( 49.0 >= aveScore >=10.0):
        return "Neutral"
    elif (aveScore <= 9.0):
        return "Low Risk"


if response:
    print "\n\n" + "Source: " + IP + "\n"
    print "This IP has been reported " + str(len(country)) + " times to AbuseIPDB."
    print "Country:",
    for i in x:
        print i
    print "Reputation: " + aveScoreCalc(abScores) 
    print "https://www.abuseipdb.com/check/" + str(IP)
    print '\n' + "This IP has been reported in the past for the following reasons: " + '\n'
else:
    print '\n' + "This IP is NOT in the DataBase" + '\n'
# ========================================================
# this space will be for the yaml file to pull descriptions
# ========================================================
cats = [li['category'] for li in response]
arr = []
s=[]
for i in cats:
    for k in i:
        arr.append(k)
for i in arr:
    if i not in s:
        s.append(i)
f = open('abuseIPDB.yaml', 'r')
c = yaml.safe_load(f)

for i in s:
    print "- " + c["ID"][i]
f.close()
     
print '\n'
