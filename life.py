
from environment import air
from stem import stem

from leaf import leaf   
#import sys  
#
#reload(sys)  
#sys.setdefaultencoding('utf8')

  
leaves={}
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
        print("TOTAL LEAF NUMBER AT RUN {}: {}".format(n,len(leaves)))
        for i,a in leaves.items():
            print("LEAF CODE {}".format(i))
            if a.alive:
                CO2,O2,H2O,sugar=a.life(time_step,steme,env)
                env.CO2+=CO2
                env.O2+=O2
                steme.H2O+=H2O
                steme.sugar+=sugar
            else:
#                I want to remove the leaf from the dictionary, but I need to use another method rather then len to add a ne one
                print ("LEAF NUMBER {} died".format(i))
        print("TOTAL SUGAR IN STEM AT THE END OF RUN {}: {}".format(n,round(steme.sugar,3)))
        n+=time_step