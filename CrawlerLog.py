#coding=utf-8
import  os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class CrawlerLog:

    traceOn = False
    __logFileLocation = ""
    __uniqueSet = set()

    def __init__(self, defaultLocation):
        self.__logFileLocation = defaultLocation

        # initilize and load log file
        if(not os.path.exists(self.__logFileLocation)):
            if (self.traceOn): print('Creating log file...')
            parentDirectory = os.path.dirname(self.__logFileLocation)
            if(not os.path.exists(parentDirectory)):
                if (self.traceOn):print('Creating file path...')
                os.makedirs(parentDirectory)

            fo = None
            try: # create log file
                fo = open(self.__logFileLocation, 'w')
            except IOError:
                print('Unexpected IO Error happened when writing file.')
            else:
                if (self.traceOn):
                    print('Log file created.')
            finally:
                if 'fo' in locals():  # only close if file exist
                    fo.close()
 
        else: # load file
            fo = None
            try:  # read file
                fo = open(self.__logFileLocation, 'r')
                while(True):
                    line = fo.readline().strip('\n') # get rid of \n
                    # save record into set
                    self.__updateUniqueSet(line)
                    if(not line): # end file
                        break
            except IOError:
                print('Unexpected IO Error happened when reading file.')
            else:
                if (self.traceOn):print('Log file loaded.')
            finally:
                if 'fo' in locals():  # only close if file exist
                    fo.close()

    def __updateUniqueSet(self, content):
        self.__uniqueSet.add(content)
        return

    def addNewEntry(self, info):
        if(not info in self.__uniqueSet):
            self.__uniqueSet.add(info)
            fo = None
            try:  # append file
                fo = open(self.__logFileLocation, 'a')
                fo.write(str(info) + '\n')
            except IOError:
                print('Unexpected IO Error happened when reading file.')
            else:
                if (self.traceOn): print('Append log with: ' + info)
            finally:
                if 'fo' in locals():  # only close if file exist
                    fo.close()
        else:
            print("Repeated information from Set")
        return

    def checkTargetIn(self, info):
        uInfo = "u'" + info + "'"
        if(info in self.__uniqueSet or uInfo in self.__uniqueSet):
            return True
        else:
            return False

    def resetCrawlerLog(self):
        fo = None
        try:  # create log file
            fo = open(self.__logFileLocation, 'w')
        except IOError:
            print('Unexpected IO Error happened when writing file.')
        else:
            if (self.traceOn): print('Log file reset.')
        finally:
            if 'fo' in locals():  # only close if file exist
                fo.close()
