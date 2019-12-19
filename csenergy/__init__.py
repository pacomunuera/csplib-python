#from pvlib.version import __version__
#from pvlib import tools
#from pvlib import atmosphere
#from pvlib import clearsky
## from pvlib import forecast
#from pvlib import irradiance
#from pvlib import location
#from pvlib import solarposition
#from pvlib import iotools
#from pvlib import ivtools
#from pvlib import tracking
#from pvlib import spa
import pandas as pd



PI = 3.141592653589793


#TODO: 1 Preparación dataframe inicial. A partir de CSV como punto de inicio.
#TODO: 2 Preparación de datos del HCE

' Campos del dataframe inicial: '
'    | timestamp | Tamb | Wind | Winddir | DNI | Vector Solar | MassFlow | Tin | Tout |'

#Dic for HTC characteristics 
HCE_type = {"Model ": 'RTC70', "Longitude ": 4, "Din ":0.06, "Dout ":0.12, "e_ext ": 1,
     "h_ext ": 1, "U_rec ": 1, "Sigma ": 1}

HCE_status = {"Hydrogen ": 0, "Vacuum ": 0, "Broken ": False}

HCE_operation = {"Tin ": 293, "Clean ": 1}

class HCE:
    long = 1
    def __init__(self, HCE_type: list, HCE_status: list, HCE_operation: list) -> None:
        self.long = 1
        self.Dro = 1
        self.Dri = 1
        self.massflow = 1
        self.eext = 1
        self.hext = 1
        self.hint = 1
        self.Urec = 1
        self.sigma = 1
        self.tin = 1
        self.tout = 1
        self.SCA = 1
        self.SCAposition = 1
        
        
    def __PRBarbero4grade__() -> float:
        return 0
    
    def __PRBarbero1grade__() -> float:
        return 0
    
    def __PRBarbero0grade__() -> float:
        return 0
   
    def calcTempOut() -> float:
        '''
        HTF output temperature [ºC] Ec. 3.24 Barbero

        Returns
        -------
        float [ºC]
            DESCRIPTION.

        '''
        return 0
    def __len__(self):
        print("coñe")
        
    
    def qabs() -> float:
        '''
        Ec. 3.20 Barbero

        Returns
        -------
        float [W]
            DESCRIPTION.
            Thermal power absorbed by the HCE
        '''
        return 0       
 


SCA_configuration ={"HCE Number ": 12, "Position in Loop": 1,
                    "Temperature probes number": 1,
                    "Temp. probes position": 'Middle', "Defocus Order": 1}

   
class SCA(object):
    #Uso de __slots__ permite ahorrar memoria RAM
    __slots__= ['SCA_configuration']

    
    def __init__(self, SCA_configuration):
        
        self.SCA_type = {    
                'HCEperSCA': 24,
                'Loop': 1,
                'positionInLoop': 1,
                'operationStatus': 0,
                'SCAtemperature': 0
                }
        
        for i in range (1, self.HCEperSCA):
            self.HCElist.append(HCE(HCE_type, HCE_status, HCE_operation))       
        
    def __gettitem__(self, item):
        return self.SCA_type[item]
    
    def setOperationStatus():
        
        if SCAtemperature > SCATempMax():
            operationStatus = 'defocused'
        else:
            soperationStatus = 'tracking'
            
            
class Loop(object):
    def __init__(self, SCAperLOOP = 4):
        self._SCAperLOOP = 4
        
    def tempOut(self, weatherstatus, plantstatus):
        '''
        Calculation of the output temperature Tout of the HTF
        according to the input temperature, mass flow, wheather
        conditions, plant performance

        Returns
        -------
        Output Temperature, Tout

        '''
        pass
    
    def massFlow():
        '''
        Calculation of the current mass flow of HTF in the loop
        by dividing the total mass flow by the number of loops
        in the plant 
        

        Returns
        -------
        current HTF massflow, massFlowLoop

        '''

        pass
    
    def requiredMassFlow():
        '''
        Calculation of the massFlow necessary to obtain the output temperature
        required by the operator

        Returns
        -------
        required HTF mass flow, reqMassFlowLoop

        '''
        pass

class SolarField(object):
    def __init__(self, LoopsPerSolarField):
        pass
    
   
class Plant(object):
    def __init__(self ):
        self._LOOPperPLANT = 120
        
class Site(object):
    def __init__(self, lat=39, long=-3):
        
        self._lat = 39
        self._long = 3
        
class HTF(object):
    
    def __init__(self, *argv):
        self._name = "Therminol VP-1"

class Weather(object):   
    def __init__(self):
        pass
        
    def loadWheatherData(path):
        pass

# format = '%Y-%m-%d %H:%M:%S'
# df['Datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], format=format)
# df = df.set_index(pd.DatetimeIndex(df['Datetime']))
        
    

class Simulation(object):
    ''' 
    Definimos la clase simulacion para representar las diferentes
    pruebas que lancemos, variando el archivo TMY, la configuracion del
    site, la planta, el modo de operacion o el modelo empleado. 
    
    '''
    def __init__(self, weather, site, plant, operation, model):
        self.t_init = 1
        self.t_end = 1
        
    def result():
        pass
        return df
"""
El usuario selecciona:
    
    - Fichero Weather, se crea dataframe con registros a intervalos temporales
    - Configuración de planta (N_campos, N_lazos, N_SCA_lazo, N_HCE_SCA)
    - Modelo de planta:
        - Modelo 1: Parámetros sin dispersión
        - Modelo 2: Parámetros con dispersión
    - Tipo de simulacion:
        - Simulacion 1: Comparación con datos de generacion
        - Simulacion 2: Simulación de planta
    
    - Se genera la planta:
        - Modelo 1: Por ser todos iguales no sería necesario crear N_lazosxN_SCA_lazoxN_HCE_SCA
        sino que se va a recurrir a bucles para generar las salidas de temperatura y guardarlos
        en el dataframe
        
        - Modelo 2: Se crean los N_lazosxN_SCA_lazoxN_HCE_SCA HCE con sus atributos cargados según 
        las funciones de dispersión que toque. 
        
    - Simulación:
        - Simulación 1: para cada registro temporal se toma el caudal y se calcula la temperatura de
        salida. Hay que manejar las temperaturas por encima del setpoint como pérdidas de energía por 
        culpa del desenfoque
        
        - Simulación 2:  para cada registro temporal se calcula el caudal para conseguir la temperatura
        de salida.
        
        datos que debe almacenarse en cada HCE
        - Rendimiento, tin, tout, massflow
        
        datos que debe almacenarse en cada SCA
        - Rendimiento (promedio de sus HCE), tin, tout, t_probe,  massflow, status (desenfoque, etc...)
        
        datos que debe almacenarse en cada LOOP
        - Rendimiento (promedio de sus SCA), tin, tout, massflow
        
        
            


"""        
    
#weather_file = Weather()
#fluid = HTF()
#site = Site()
#plant = Plant()
#
#simulation = Simulation(self, weather_file, plant, operation, model)
#simultation_output = simulation.result()


        

