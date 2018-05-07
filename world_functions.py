"""
IO_trasf 
IO"""

def __tra_L_photosynthesis():
    """tests availability of resources and produces new sugar consuming other resources"""
        
    if self.inflow_test("H2O",6) and self.stomatain_test("CO2",6) and self.air.solar==True:#light phase
        self.inflow_do("H2O",6)#draws water            
        self.stomatain_do("CO2",6)#draws CO2   
        self.logword.append("the sugar changes due to photosynthesis from {} to {} due to a 6 x {}(growthstage)= {}\n".format(round(self.sugar,2),round(self.sugar+self.growth_stage*6,2),round(self.growth_stage,2),round(self.growth_stage*6,2)))
        self.sugar+=self.growth_stage*6
            
        self.stomataout("O2",6)#returns O2
def __tra_D_photosynthesis():
    pass
def __tra_growth():
    pass
def __tra_respiration():
    pass
def __IO_internal_draw():
    pass
def __IO_external_draw():
    pass
