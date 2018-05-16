# FGOCrawler
---
I'm a big Fan of Fate Grand Order (FGO) mobile game, <br/>
recently I made a FGO Draw Card simulator in my github, but it only shows the text.<br/>
<br/>
So I'm thinking if we can get a 'real' card draw? -> then we have this crawler program to crawl the pitctures/videos from FGO wiki page.
<br/>
Main resource crawled from website:<br/>
1. crawl Hero Data (name, type, gender, rarity, etc)<br/>
crawlFGOHeroData(heroList)
2. crawl Hero Pictures (most hero has 4 pictures, i.e. 001A/001B/001C/001D)<br/>
crawlFGOPicture(heroList, 'A')
3. crawl videos for hero super unique skill! (宝具)<br/>
crawlFGOVideo(heroList)
(actually some videos for new heros are not uploaded yet and missed from website...)<br/>
4. crawl the mystic code card picture (魔术礼装, some mystic code has multiple pictures, e.g. 001A/001B)<br/>
mycodeMaxNo = crawlFGOMyCode('A')
(return value is the total amount of available mystic code so far)<br/>
5. crawl Mystic code data (name, rarity, skills, etc)<br/>
crawlFGOMyCodeData(int(mycodeMaxNo))<br/>
<br>
<br>
PS: Main page of FGO wiki: (with Chinese language)<br/>
http://fgowiki.com/guide/petdetail

