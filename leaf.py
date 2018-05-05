## -*- coding: utf-8 -*-
#"""
#Created on Mon Nov 13 18:50:54 2017
#
#@author: Andre
#"""
import numpy as np

class leaf ():
    """the leaf can grow from growth_stage=0.01 to 1 with a basal mantainment consumption of growthstage*3. The growth cost in sugar is inversely proportional to the growthstage: to grow 1%, the consumption is (1-growthstage). """
    def __init__(self):   

        self.growth_stage=0.01
        self.sugar=0
#        self.alive=True
        self.deathcount=0
        self.alive=self.is_alive()
        self.O2_out=0#after interaction returns those
        self.CO2_out=0
        self.H2O_out=0
        self.sugar_out=0
        self.logword=[]
        self.lognum=[]

    def inflow_test(self,what,amount):
        """tests if there is sugar available from the stem"""        
        if what =="sugar":
            if self.stem.sugar>=amount:
                
                return True
            else:
                return False
        if what =="H2O":
            if self.stem.H2O>=amount:
                
                return True
            else:
                return False
#    @logger               
    def inflow_do(self,what,amount):
        """draws sugar from the stem"""
        if what =="sugar":
            self.sugar_out-=amount
            self.sugar+=amount
            self.logword.append("{} of sugar was drawn from the stem; \n Now the internal sugar is {}\n".format(round(amount,2),round(self.sugar,2)))
            
        if what =="H2O":
            self.H2O_out-=amount
#    @logger   
    def outflow(self,what):
        """if there is excess of sugar in the leaf, returns it to the stem"""
        if what =="sugar":
            if self.sugar>2:
                self.logword.append("the sugar is in excess ({})\n".format(round(self.sugar,2)))
                delta = self.sugar-2
                self.sugar-= delta    
                self.logword.append("note, this is the sugar out: {} \n".format(round(self.sugar_out,2)))
                self.sugar_out += delta
                self.logword.append("now the internal amount of sugar is {}, while the outgoing is going to be {}\n".format(round(self.sugar,2),self.sugar_out))
     

    def stomatain_test(self,what,amount):
        """activates respiration if there is enough CO2 in the air"""        
        if what =="CO2":
            if self.air.CO2>=amount:
                return True
            else:
                return False
        #TODO: dark phase                 
        
    def stomatain_do(self,what,amount):
        """draws CO2 from the environment"""
        if what =="CO2":
            self.CO2_out-=amount
        #TODO: dark phase 
    def stomataout(self,what,amount):
        """returns O2 to the environment"""        
        if what =="O2":
            self.O2_out+=amount
        #TODO: dark phase 
    def photosynthesys(self):
        """tests availability of resources and produces new sugar consuming other resources"""
        
        if self.inflow_test("H2O",6) and self.stomatain_test("CO2",6) and self.air.solar==True:#light phase
            self.inflow_do("H2O",6)#draws water            
            self.stomatain_do("CO2",6)#draws CO2   
            self.logword.append("the sugar changes due to photosynthesis from {} to {} due to a 6 x {}(growthstage)= {}\n".format(round(self.sugar,2),round(self.sugar+self.growth_stage*6,2),round(self.growth_stage,2),round(self.growth_stage*6,2)))
            self.sugar+=self.growth_stage*6
            
            self.stomataout("O2",6)#returns O2
          
        #TODO: dark phase 
#    @logger    
    def mantain(self):
        """the leaf cannot live without maintainment"""
        if self.sugar>3*self.growth_stage:
            self.logword.append("{} is being used for mantainment\n".format(round(3*self.growth_stage,2)))
            self.sugar-=3*self.growth_stage
            self.logword.append("now the in sugar is {}\n".format(round(self.sugar,3)))
            self.deathcount-=1
        else:
            if self.inflow_test("sugar",3*self.growth_stage):#enough sugar in stem
                self.logword.append("warning, not enough sugar for mantainment\n")
                self.inflow_do("sugar",3*self.growth_stage)#draw it use at next time step
            else:
                if self.stem.sugar>0:#Check if there is sugar at all in stem. I should use a function, rather than a direct test 
                        self.inflow_do("sugar",self.stem.sugar)#draw all sugar available  
                        self.logword.append("warning, not enough sugar for mantainment II\n")
            self.deathcount+=1 #no sugar readily available
#    @logger        
    def grow (self):
        """the leaf can live without growing. There is growth only until the leaf is mature"""
        self.logword.append("growt stage: {}\n".format(round(self.growth_stage,2)))

        if self.growth_stage<1:#
            if self.sugar>=(1-self.growth_stage):#
                self.sugar-=(1-self.growth_stage)
                self.growth_stage+=1-np.exp(-0.5*self.growth_stage)#1% of growth for 10sugar*(1-growth stage). The higher the growth stage the cheaper the growth
                self.logword.append("just grown\n")
                if self.growth_stage>1:
                    self.growth_stage=1
#                print("grown!")
            else:#if the sugar is not enough, draw it for the next time step
                if self.inflow_test("sugar",(1-self.growth_stage)):#enough sugar in circulation
                    self.logword.append("drawing for growth in next stage\n")
                    self.inflow_do("sugar",(1-self.growth_stage))#draw all necessary
#                    print("for growth")
                else:
                    if self.stem.sugar>0:#Check if there is sugar at all in circulation.I should use a function, rather than a direct test 
                        self.logword.append("something else\n")
                        self.inflow_do("sugar",self.stem.sugar)#draw all sugar available
#                        print("for growth")
#    @logger
    def is_alive(self):
        if self.deathcount<4:
            if self.deathcount<0:
                self.deathcount=0
#            print("the leaf is alive")    
            return True
        else:
            self.logword.append("the leaf died\n")
            return False
        
        
    def life (self,duration,stem,air,verbose=False):
        self.stem=stem #take for logic tests
        self.air=air
        self.verbose=verbose
        for i in range (duration):
            
            if self.alive:#♣this reeats but better to kee it in
                self.photosynthesys()                
                self.mantain()
                self.grow()   
                self.outflow("sugar")
                self.alive=self.is_alive()
                CO2_out=self.CO2_out
                O2_out=self.O2_out
                H2O_out=self.H2O_out
                sugar_out=self.sugar_out
                logword=self.logword
                self.logword=[]
                self.CO2_out=0
                self.O2_out=0
                self.H2O_out=0
                self.sugar_out=0
                
        return CO2_out,O2_out,H2O_out,sugar_out,logword
#                print ("the leaf survived")




#%%
             