#logging in python
#use to track events occurs in software when it runs
#used in development,debugging,testing
#it is useful to track the error or exception or information
#logging module can be used with flask and jango


#waht if there is no logging
#RCA- root cause analysis
#it may take long time to find routr cause.


#what problem soteware can face.
#exception,network issue,file not found.server down.access deined

#how logging work in python
#import module-- import logging or from logging import *

#level- DEBUG,INFO,WARNING,ERROR,CRITICAL
#application store shop

import logging
logging.basicConfig(filename="app.log",
                    level=logging.DEBUG,
                    filemode='w',
                    format="{message}:{asctime}:{lineno}:{process}:{levelname}:{name}" ,
                    datefmt='%d-%b-%y %M:%H:%S',
                    style="{")



#logging.debug('demo msg') #10
#logging.info('modulr2 got completed and module3 started') #20
#logging.warning('warning msg is displaying') #30
#logging.error('error messgae')#40
#logging.critical('critical msg is displaying')#50

#run code
#debug and info will not run, beacuse warning is by default set level and will print messages from warning onward

#to set level
#logging.basicConfig(level=logging.DEBUG)

#WARNING:root:warning msg is displaying
#level:name:msg

#to create log file and collect meassages

#logging.basicConfig(filename="app.log",level=DEBUG) on top of code

#app.log #a=append mode defalut all messages will append.

#if filemode='w' #all data will overwrite

#logging.basicConfig(filename="app.log",level=DEBUG,filemode='w')

#formatting log in python

#logging.basicConfig(filename="app.log",
               #      level=logging.DEBUG,
                #     filemode='w',
                 #    format="%(name)s:%(levelname)s:%(message)s")

#log process id:logging.basicConfig(filename="app.log",
               #      level=logging.DEBUG,
                #     filemode='w',
                 #    format="%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s")

#we will get process id along with line number,process id is useful for debugging

#to get date and time just add in format

#logging.basicConfig(filename="app.log",
               #      level=logging.DEBUG,
                #     filemode='w',
                 #    format=%(asctime):"%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s
                #     datefmt='%d-%b-%y %M:%H:%S",
                #       style="{")
#now we can change out format line
#format="{message}:{asctime}:{lineno}:{process}:{levelname}:{name}"


#create logger object and perform logging

#logger=logging.getLogger("kush")
#logger object

#logger.setLevel(10)
#logger.info("here is the info")
#logger.error("error message here")

#to change root name logger=logging.getLogger('kush')


#example 
#ag=int(input("enter your age:")) #if we put hello then error appear so we use exception handling
#try:
 #   ag=int(input("enter your age:"))
#except Exception as obj:
#    logging.error(obj)


 #output======invalid literal for int() with base 10: 'hello':04-Feb-24 25:12:59:100:3232:ERROR:root
   #now we can use exc_info=True
#try:
 #   ag=int(input("enter your age:"))
#except Exception as obj:
 #   logging.error("meassge",exc_info=True)  

class Accessdenied(Exception):
    pass

try:
    ag=int(input("enter age"))
    if ag<18:
        raise Accessdenied("access denied")
    logging.info(f'{ag}has logged in')
except Exception as obj:
    logging.exception("obj")