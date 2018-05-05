
from environment import air
from stem import stem
from logger import create_logfile
from leaf import leaf   
#import sys  
#
#reload(sys)  
#sys.setdefaultencoding('utf8')

  
leaves={}
log=[]
def add_leaf():
    if steme.sugar>=6:
        leaves[len(leaves)+1]=leaf()    


if __name__ == '__main__':

    env=air(5000)    
    steme=stem(6)
    time_step=1
    n=0
    while n<= 50:
        add_leaf()
        log.append("TOTAL LEAF NUMBER AT RUN {}: {}\n".format(n,len(leaves)))
        for i,a in leaves.items():
            log.append("LEAF CODE {}\n".format(i))
            if a.alive:
                CO2,O2,H2O,sugar,logword=a.life(time_step,steme,env)
                env.CO2+=CO2
                env.O2+=O2
                steme.H2O+=H2O
                steme.sugar+=sugar
                for f in logword:
                    log.append(f)
                
            else:
#                I want to remove the leaf from the dictionary, but I need to use another method rather then len to add a ne one
                log.append("LEAF NUMBER {} died\n".format(i))
        log.append("TOTAL SUGAR IN STEM AT THE END OF RUN {}: {}\n".format(n,round(steme.sugar,3)))
        n+=time_step
    create_logfile(log)