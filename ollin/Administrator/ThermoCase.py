#thermo case
#from numpy.oldnumeric import array,Float0
import ollin.Thermodinamics.PresureVapor as PresureVapor
import ollin.CES
import sys, imp, re


class ThermoCase:
    """
    Trying to create ThermoCase object for on given given Thermodynamic model with given PV and EOS values.
    Here, default PV as Anotine and EOS as RedlichKwong.
    """
    def __init__(self, EOS="RedlichKwong", PV="Antoine"):
        '''
        :param EOS: Accepts EOS from Ollin admin for a thermodynamic model
        :param PV: Accepts PV from Ollin admin for a thermodynamic model
        '''
        self.library = []               # hold list of components or mixture which are being added from Add() on given.
        # Thermodynamic model
        self.NamePresureVap = PV        # Name of Pressure Vapor Equation from argument.
        self.NameEOS = EOS              # Equation of state.
        self.PresureVap = None          # Instance of PV function. Say, Antoine() or Harlacher().
        self.EOS = None                 # Instance of EOS function. Say, PengRobinson().
        self.PublicVars = ["MoleWt", "LIQDEN"]  # This variable is updated with needed variables for PV and EOS class.
        self.LoadPresureModel(PV)       # Find exact PV class obj either Antoine() or Harlacher().
        self.LoadEOSModel(ollin.CES, EOS)  # Find exact EOS class obj like: PengRobinson() or SoaveRK() or SRK() or
        # as default RedlichKwong().
        self.Const = {}  # Hold the constant values for each library element from given Thermodynamic model.
        self.Cases = []
        self.Load = 0       # Var to determinate if is necessary to load from database. Better to say whether
        # LoadConst() from AdmOllin.py is called on given Thermodynamic model or not.

    def Comp(self):
        """ print current componets in case"""
        print "<<Numero>> <<Clave>> <<Nombre>>"
        print "_______________________________"
        for x in self.library.keys():
            print "%-10d>> %-8d >> %-10s"%(x,self.library[x][1],self.library[x][0])
        del x

    def LoadPresureModel(self, model):
        """
        load the class of Presure Vapor Model
        """
        print("############################ STARTS exec of LoadPresureModel(PV=%s" % model),
        print(")###########################")
        print('load equation for pressure model: ', model)
        print("PresureVapor.Equation.keys()", PresureVapor.Equation.keys())
        if model in PresureVapor.Equation.keys():
            self.PresureVap = PresureVapor.Equation[model]()  # This will call either Antoine() or Harlacher()
            # constructor/equation based on PV model
            print("I will call ", self.PresureVap.Name, "()")
            self.PublicVars += self.PresureVap.NeedVars()  # Needed variables for PV model
            print("Needed variables for PV model:", self.PresureVap.Name, "() as follows:", self.PublicVars)
        else:
            print "The model is no aviable!"
        print("############################ ENDS exec of LoadPresureModel(PV=%s" % model),
        print(")###########################")

    def LoadEOSModel(self, module, model):
        """
        load the class of Equation of state Model
        """
        print("############################ STARTS exec of LoadEOSModel(model=%s" % model),
        print(")###########################")
        print("LoadEOSModel module::", module)
        print("LoadEOSModel model::", model)
        modpath = module.__path__
        print("LoadEOSModel module path::", modpath)
        fullName = module.__name__ + '.' + model
        print("LoadEOSModel module fullName::", fullName)
        #print("sys.modules", sys.modules)
        if fullName in sys.modules:
            lang = sys.modules[fullName]
            print(fullName, "found in ", lang)
            print("lang in detail::", lang.__dict__)
        else:
                file, path, description = imp.find_module(model, modpath)
                #print("file, path, description from python imp.find_module", file, path, description)
                try:
                    lang = imp.load_module(model, file, path, description)
                    #print("lang from imp.load_module", file, path, description)

                finally:
                    file.close()
        print("Calling of EOS model from lang as :", lang.__dict__['Model'])
        print("Needed public variables from LoadPresureModel() are as::", self.PublicVars)  #self.PresureVap.NeedVars())
        self.EOS = lang.Model(self.PresureVap)  # This will call Model(PV=self.PresureVap) based on 'Model'
        # attribute of lang and self or ThermoCase().EOS is initialized with Model() obj from corresponding
        # EOS parameter of ThermoCase().
        ########################## NOTE:###########################
        #  Here, lang is the path of PengRobinson module and we call Model() func using lang.Model(PV=self.PresureVap)
        print("ThermoCase class EOS attribute::", self.EOS.__dict__)
        self.PublicVars += self.EOS.NeedVars()  # This will call NeedVars() from Model() obj from corresponding
        # EOS parameter of ThermoCase()
        print("Needed public variables after LoadPresureModel() and LoadEOSModel() are as::", self.PublicVars)
        # Important Note: This PublicVars are cols of SQLite3 Db (data.db)
##        else:
##            print "The model is no aviable!"
        print("############################ ENDS exec of LoadEOSModel(model=%s" % model),
        print(")###########################")

    def Get(self, Var):
        '''
        :param Var: Thermodynamic model variable. For example, 'PR'.
        :return: Const dict() for the Var
        '''
        if Var in self.Const.keys():
            return self.Const[Var]
        else:
            return 0
    
    def Solve(self, case):
        '''
        :param case: ThermoObj()
        :return: It will call Solver() from EOS class. Here, it is PengRobinson.
        '''
        print("############### Calling of Solve() from ThermoCase.py")
        case.library = self.library  # Store the ThermoCase().library to ThermObj.library
        print("self.EOS",self.EOS)
        self.EOS.Solver(self.Const, case)  # It will call Solver() from EOS class. Here, it is PengRobinson

