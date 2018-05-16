# FGOCrawler
---
I'm a big Fan of Fate Grand Order (FGO) mobile game, <br>
recently I made a FGO Draw Card simulator in my github, but it only shows the text.<br>
<br>
So I'm thinking if we can get a 'real' card draw? -> then we have this crawler program to crawl the pitctures/videos from FGO wiki page. <br>
<br>
Main resource crawled from website: <br>
1. get Hero list data structure - **heroList** (including hero id, hero name, etc) <br>
2. crawl Hero Data (name, type, gender, rarity, etc) <br>
**crawlFGOHeroData(heroList)** <br>
3. crawl Hero Pictures (most hero has 4 pictures, i.e. 001A/001B/001C/001D) <br>
**crawlFGOPicture(heroList, 'A')** <br>
4. crawl videos for hero super unique skill! (宝具) <br>
**crawlFGOVideo(heroList)** <br>
(actually some videos for new heros are not uploaded yet and missed from website...) <br>
5. crawl the mystic code card picture (魔术礼装, some mystic code has multiple pictures, e.g. 001A/001B) <br>
**mycodeMaxNo = crawlFGOMyCode('A')** <br>
(return value is the total amount of available mystic code so far) <br>
6. crawl Mystic code data (name, rarity, skills, etc) <br>
**crawlFGOMyCodeData(int(mycodeMaxNo))** <br>
<br>
PS1: Main entrance function: **Crawler_FGO.py** <br>
PS2: All output data will be saved in your local disk, so you need to set following file path parameters to run this program: <br>
For example: <br>
  &emsp;picturePath = 'D:/Crawler/FGO/picture_hero/' <br>
  &emsp;videoPath = 'D:/Crawler/FGO/video/' <br>
  &emsp;mycodePath = 'D:/Crawler/FGO/picture_mycode/' <br>
  &emsp;heroPath = 'D:/Crawler/FGO/FGO Hero/' <br>
  &emsp;mycodeDataPath = 'D:/Crawler/FGO/FGO Mystic Code/' <br>
  &emsp;logDirectory = r'D:/Crawler/FGO/log/' <br>
PS3: Main page of FGO wiki: (with Chinese language)<br>
http://fgowiki.com/guide/petdetail <br>
<br>
Result examples: <br>
![image](https://github.com/Perryxubit/FGOCrawler/blob/master/pictures/MysticCodeCards.jpg)

Mystic cards 魔术礼装卡 (1 card per mystic code) <br>
![image](https://github.com/Perryxubit/FGOCrawler/blob/master/pictures/MysticCodeCards.jpg)

Hero skill videos 宝具动画 (1 mp4 video per hero) <br>
![image](https://github.com/Perryxubit/FGOCrawler/blob/master/pictures/HeroVideos.jpg)
