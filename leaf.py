## -*- coding: utf-8 -*-
#"""
#Created on Mon Nov 13 18:50:54 2017
#
#@author: Andre
#"""
#def getter_setter_gen(name, type_):
#    def getter(self):
#        return getattr(self, "__" + name)
#    def setter(self, value):
#        if not isinstance(value, type_):
#            raise TypeError("%s attribute must be set to an instance of %s" % (name, type_))
#        setattr(self, "__" + name, value)
#    return property(getter, setter)
#
#def auto_attr_check(cls):
#    new_dct = {}
#    for key, value in cls.__dict__.items():
#        if isinstance(value, type):
#            value = getter_setter_gen(key, value)
#        new_dct[key] = value
#    # Creates a new class, using the modified dictionary as the class dict:
#    return type(cls)(cls.__name__, cls.__bases__, new_dct)




#%%
#time_st=2

import numpy as np
class leaf ():
    """the leaf can grow from growth_stage=0.01 to 1 with a basal mantainment consumption of growthstage*3. The growth cost in sugar is inversely proportional to the growthstage: to grow 1%, the consumption is 10*(1-growthstage). """
    def __init__(self):    
        self.growth_stage=0.01
        self.sugar=10
#        self.alive=True
        self.deathcount=0
        self.alive=self.is_alive()
        self.O2_out=0#after interaction returns those
        self.CO2_out=0
        self.H2O_out=0
        self.sugar_out=0
        
        #print ("init:/n sugar %s/n growth stage %s"%(self.sugar,self.growth_stage))
    
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
    def inflow_do(self,what,amount):
        """draws sugar from the stem"""
        if what =="sugar":
            self.sugar_out-=amount
            self.sugar+=amount
#            print(amount,"sugar drawn")
        if what =="H2O":
            self.H2O_out-=amount
       
    def outflow(self,what):
        """if there is excess of sugar in the leaf, returns it to the stem"""
        if what =="sugar":
            if self.sugar>2:
                self.sugar-= self.sugar-2                
                self.sugar_out+= self.sugar-2
     

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
            self.sugar+=self.growth_stage*6
            self.stomataout("O2",6)#returns O2
            if self.verbose==True:
                print ("synth:\n CO2 %s \n H2O %s\n sugar %s\n O2 %s"%(self.air.CO2,self.stem.H2O,self.sugar,self.air.O2))            
        #TODO: dark phase 

    def mantain(self):
        """the leaf cannot live without maintainment"""
        if self.sugar>3*self.growth_stage:
            self.sugar-=3*self.growth_stage
            self.deathcount-=1
#            print("mantained")
        else:
            if self.inflow_test("sugar",3*self.growth_stage):#enough sugar in stem
                self.inflow_do("sugar",3*self.growth_stage)#draw it use at next time step
#                print("for mantainement")
            else:
                if self.stem.sugar>0:#Check if there is sugar at all in stem. I should use a function, rather than a direct test 
                        self.inflow_do("sugar",self.stem.sugar)#draw all sugar available  
#                        print("for mantainment")
            self.deathcount+=1 #no sugar readily available
            
    def grow (self):
        """the leaf can live without growing"""
        print(self.growth_stage,"stage")

        if self.growth_stage<1:#
            print("there is growth only if the leaf is not mature",self.sugar,1-self.growth_stage)
            if self.sugar>=(1-self.growth_stage):#
                self.sugar-=(1-self.growth_stage)
                self.growth_stage+=1-np.exp(-self.growth_stage)#1% of growth for 10sugar*(1-growth stage). The higher the growth stage the cheaper the growth
                if self.growth_stage>1:
                    self.growth_stage=1
#                print("grown!")
            else:#if the sugar is not enough, draw it for the next time step
                if self.inflow_test("sugar",(1-self.growth_stage)):#enough sugar in circulation
                    self.inflow_do("sugar",(1-self.growth_stage))#draw all necessary
#                    print("for growth")
                else:
                    if self.stem.sugar>0:#Check if there is sugar at all in circulation.I should use a function, rather than a direct test 
                        self.inflow_do("sugar",self.stem.sugar)#draw all sugar available
#                        print("for growth")

    def is_alive(self):
        if self.deathcount<4:
            if self.deathcount<0:
                self.deathcount=0
#            print("the leaf is alive")    
            return True
        else:
            print("the leaf died")
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
        return self.CO2_out,self.O2_out,self.H2O_out,self.sugar_out
#                print ("the leaf survived")




#%%
             