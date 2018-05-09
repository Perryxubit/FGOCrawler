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
picturePath = 'D:/Crawler/FGO/picture/'
videoPath = 'D:/Crawler/FGO/video/'
heroPath = 'D:/Crawler/FGO/FGO Hero/'
logDirectory = r'D:/Crawler/FGO/log/'


####### 程序开始 #######
traceOn = True
basedUrl = 'http://fgowiki.com/guide/petdetail/'

if(not os.path.exists(logDirectory)):
    os.makedirs(logDirectory)
    if (traceOn): print("Created - " + logDirectory)
if(not os.path.exists(picturePath)):
    os.makedirs(picturePath)
    if (traceOn): print("Created - " + picturePath)
if(not os.path.exists(videoPath)):
    os.makedirs(videoPath)
    if (traceOn): print("Created - " + videoPath)

if (traceOn): print("PictureCrawler for: " + basedUrl)

# header - 防止防盗链
header = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://fgowiki.com/guide/petdetail/'
}

def getFormattedIndexString(index):
    maxLen = 3
    rev = str(index)
    ilen = len(str(index))
    if(ilen < 1 or ilen > 3):
        return None

    for i in range(0, maxLen-ilen):
        rev = '0' + rev
    return rev

def crawlFGOPicture(heroList, imgType = 'A'):
    # crawling the pictures
    # img.fgowiki.com/fgo/card/servant/002A.jpg
    imgUrl = 'http://img.fgowiki.com/fgo/card/servant/'

    for heroIndex in range(0, len(heroList)):
        cardUrl = imgUrl + getFormattedIndexString(heroIndex+1) + imgType + '.jpg'
        imgHtml = requests.get(cardUrl, headers=header)

        savedFilePath = picturePath + str(heroIndex) + "_" + imgType + ".jpg"
        f = open(savedFilePath, 'wb')
        f.write(imgHtml.content)
        f.close()

        sleep(random.randint(1, 10) * 0.01)
        print("Crawling - " + cardUrl + " done.")

def crawlFGOVideo(heroList):
    # crawling the videos
    # img.fgowiki.com/fgo/card/servant/002A.jpg
    logObject = CrawlerLog(logDirectory + 'video.log')
    videoBasedUrl = 'http://img.fgowiki.com/fgo/mp4/'

    for heroIndex in range(0, len(heroList)):
        videoUrl = videoBasedUrl + 'No.' + getFormattedIndexString(heroIndex+1) + '.mp4'
        if(logObject.checkTargetIn(videoUrl)):
            print("Repeated video - " + videoUrl)
            continue

        imgHtml = requests.get(videoUrl, headers=header)

        savedFilePath = videoPath + str(heroIndex) + ".mp4"
        f = open(savedFilePath, 'wb')
        f.write(imgHtml.content)
        f.close()

        sleep(random.randint(1, 10) * 0.01)
        print("Crawling - " + videoUrl + " done.")
        logObject.addNewEntry(videoUrl)

def crawlFGOHeroData(heroList):
    logObject = CrawlerLog(logDirectory + 'hero.log')
    for heroIndex in range(0, len(heroList)):
        heroPageUrl = basedUrl + str(heroIndex)
        if(logObject.checkTargetIn(heroPageUrl)): # check repeating data
            print("Repeated Hero - No." + str(heroIndex+1) + ' ' + heroList[heroIndex])
            continue

        print("Getting data for New Hero - No." + str(heroIndex+1) + ' ' + heroList[heroIndex])
        pageHtml = requests.get(heroPageUrl, headers=header)
        '''
       Attention: 
       re.match only match the string ONLY from text BEGINNING, 
       re.search match the string from every char
       regular expresss to get JSON data ->  r'\[{\"ID\"(.*?)}\]'
       '''
        jsonData = re.search('\[{\"ID\"(.*?)}\];', pageHtml.text)
        #print(pageHtml.text)
        if(jsonData):
            jsonString = jsonData.group()[:-1]
            if(traceOn): print(jsonString + " Found.")
            heroDict = json.loads(jsonString) # get dictionary of Json
            #for key in heroDict[0]: print(key),
            separator = '###'
            writeText = str(heroIndex+1) + separator + str(heroDict[0]['NAME']) + separator + str(heroDict[0]['CLASS']) + separator + str(heroDict[0]['STAR']) + separator + str(heroDict[0]['Property'])
            if(traceOn): print(writeText)

            heroListFilePath = heroPath + 'HeroList.txt'
            f = open(heroListFilePath, 'a')
            f.write(writeText + '\n')
            f.close()
            print("Hero No." + str(heroIndex+1) + " downloaded.")
            # save in log
            logObject.addNewEntry(heroPageUrl)

def crawlFGO():
    heroList = []
    html = requests.get(basedUrl, headers=header)
    soup = BeautifulSoup(html.text, "html.parser")  # parse this page
    allLabelA = soup.find('select', class_='pet').find_all('option')  # get list of results
    html.encoding = 'utf-8'

    for labelA in allLabelA:
        hero = labelA.get_text()  # 提取 图片主题 的 文本描述
        if (hero == ''):
            continue
        # if(traceOn): print (hero + "/")
        heroList.append(str(hero))

    sleep(random.randint(1, 10) * 0.01)
    print("共有英灵总数 - " + str(len(heroList)))

    #1 crawling data
    crawlFGOHeroData(heroList)

    #2 crawling pictures
    ''' 
    图片索引字母imgType
        A - 1破
        B - 2破
        C - 3破
        D - 4破
        E - 愚人节  
     '''
    crawlFGOPicture(heroList, 'A')

    #3 crawling videos
    crawlFGOVideo(heroList)


if( __name__ == "__main__"):
    # main function
    crawlFGO()

