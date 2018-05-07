class air():
    def __init__(self,amount):    
        self.CO2=amount*1000
        
        self.O2=amount*1000
        self.solar=True
        print ("air initialised")

class soil():
    # macronutrients should be provided in the order of N, P, K, Ca, S, Mg, C, O, H
    def __init__(self, ph: float, moisture: float, porosity: float, sand: float, silt: float, clay:float, macronutrients: list):
        self.pH = ph
        if moisture < 0 or moisture > 100:
            self.moisture = None
            raise ValueError('Moisture must be a float between 0 and 100')
        else:
            self.moisture = moisture
        if porosity < 0 or porosity > 100:
            self.porosity = None
            raise ValueError('Porosity must be a float between 0 and 100')
        else:
            self.porosity = porosity
        if sand + silt + clay > 100.1 or sand + silt + clay < 99.9:
            self.texture = None
            raise ValueError('Sand, silt, and clay must add up maximally to 100.1 and minimally 99.9')
        else:
            self.texture = {'sand': sand, 'silt': silt, 'clay': clay}
        if len(macronutrients) != 9:
            self.macronutrients = None
            raise ValueError('Macronutrients must be a list containing 9 elements')
        else:
            self.macronutrients = macronutrients
        print("soil initialised")
        
