#coding=utf-8
from bs4 import BeautifulSoup
import requests
from CrawlerLog import *
import  os
from time import sleep
import random
import re
import json

# default parameter
heroDataPath = 'D:/Crawler/FGO/FGO Hero/HeroList.txt'
if(os.path.exists(heroDataPath)):
    nv = 0
    nan = 0
    print('reading file...')
    fo = open(heroDataPath, 'r')

    while True:
        line = fo.readline()
        if not line:
            break
        if('男性' in line):
            nan += 1
        if('女性' in line):
            nv += 1
        print(line)
    fo.close()
    print('nan:' + str(nan) + '  nv:' + str(nv))
