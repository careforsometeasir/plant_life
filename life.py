
from environment import air
from stem import stem

from leaf import leaf   
#import sys  
#
#reload(sys)  
#sys.setdefaultencoding('utf8')

  
leaves={}
def add_leaf():
    if steme.sugar>=9:
        leaves[len(leaves)+1]=leaf()    


if __name__ == '__main__':

    env=air(5000)    
    steme=stem(9)
    time_step=1
    n=0
    while n<= 3:
        add_leaf()
        print("leaves:",len(leaves))
        for a in leaves.values():
            if a.alive:
                CO2,O2,H2O,sugar=a.life(time_step,steme,env)
                print(sugar)
                
                env.CO2+=CO2
                env.O2+=O2
                steme.H2O+=H2O
                steme.sugar+=sugar
            else:
#                I want to remove the leaf from the dictionary, but I need to use another method rather then len to add a ne one
                print ("a died")
        print steme.sugar
        n+=time_step