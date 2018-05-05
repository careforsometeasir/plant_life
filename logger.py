import os
import datetime as dt
#import io
#import sys            

def create_logfile(logs):
        if os.path.isdir("logs")==False:
            os.makedirs("logs")
#        csv=os.path.join("logs","data_logged{}.csv".format(str(dt.datetime.now())))
        log=os.path.join("logs","log{}.txt".format(str(dt.datetime.now())))
        
        with open(log, "a") as txt: 
            for s in logs:
                txt.write(s)
#def logger(function):
#    
#    def wrapper(*a):
#        sveit=sys.stdout
#        sys.stdout = io.StringIO()
#        try:
#            function(*a)
#        finally:
#            v= sys.stdout.getvalue()
#            sys.stdout=sveit
#        with open(log, "a") as txt: 
#    #        line=[f for f in args]
#            txt.write(v)
#    return wrapper


    