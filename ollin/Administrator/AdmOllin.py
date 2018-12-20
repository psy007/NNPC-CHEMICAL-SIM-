##import sys
##sys.path.append("/Users/jonathanxavier/Developer/sim42")
from ollin.DataBase.DataBase import DataBase
from ollin.Administrator.ThermoCase import ThermoCase
from ollin.Administrator.ThemoObj import ThermoObj
from numpy import array


class AdmOllin:
    """
    Beta term server administrator
    """
    def __init__(self):
        """
        load database
        """
        self.TheCase = {}  # This dictionary is created with a kay as given thermodynamic model(say "PR") and values
        # for that is a ThermoCase() object with given EOS and PV.
        self.TheObj = {}
        self.Model = {}
        self.cur = DataBase()  # cursor obj for given thermodynamic model(say "PR") to load the values for its library
        # values
        print "OllinTS has been loaded\n"

    def Add(self, items, case):
        '''
        :param items: A list of components like:["METHANE", "ETHANE", "PROPANE", ....] to add with thermodynamic model,
        say 'PR' as case.
        :param case: Thermodynamic model, say 'PR'
        :return:
                This function will add items in 'PublicVars' attribute of 'TheCase' in Ollin() obj. For example,
                ["METHANE", "ETHANE", "PROPANE", ....] are appended into Ollin().TheCase['PR'].library list.
        '''
        """
        In Add(), we are adding components in the case. Here items are like:["METHANE", "ETHANE", "PROPANE"] and
        case is given Thermodynamic model, say "PR"
        """
        print("################### STARTING OF Add() WITH ITEMS AND CASE AS ", items, case)
        print ("items::", items)
        print ("case::", case)
        if type(items) == str:
            items = [items,]
        # NOTE: Here, library holds list of components which are trying to add with given
        # Thermodynamic model (case) using Add()
        for item in items:
            if self.TheCase[case].library.count(item) != 0:
                print "The component %s has been add"
                return 0
            temp = self.cur.Dates("IdKey", item)  # temp is ROW no.from data.db for the first occurrence of item. For
            # better understanding see Dates() from DataBase module in ollin

            if temp == (None or []):
                print "Isn,t the compound in databse %s"%(item)
            else:
                print "component %d  %s was add to %s" % (temp[0][0], item, self.TheCase[case].NameEOS)
                self.TheCase[case].library.append(item)  # Adding of an item in library of a case
                self.TheCase[case].Load = 0
        print("Final library for case (%s) as : " %case, self.TheCase[case].library)

    def Remove(self, items, case):
        '''
        :param items: A list of components like:["METHANE", "ETHANE", "PROPANE", ....] to remove from thermodynamic
        model, say 'PR' as example.
        :param case: Thermodynamic model, say 'PR'
        :return: This function will remove items from Ollin().TheCase['PR'].library. Here, library is a list attrb.
        '''

        if type(items) == str:
            items = [items,]
        
        for item in items:
            if self.TheCase[case].library.count(item) != 0:
                self.TheCase[case].library.remove[item]
                print "The component %s has been removed"
                self.TheCase[case].Load = 0

    def AddModel(self, Name, case="SRK", PV="ANTOINE"):
        '''
        :param Name: Thermodynamic model name, say 'PR'
        :param case: Name of the Equation Of State(EOS) for Thermodynamic model
        :param PV: Pressure Vapor(PV) equation for Thermodynamic model
        :return: 1. Provides 'cur' attribute of Ollin() obj.
                 2. Provides 'TheCase' attribute as ThermoCase() obj for Name. For example,
                 Ollin().TheCase['PR']=ThermoCase().
                 3. It returns 'TheCase' as ThermoCase() object.
        '''
        print("Given thermodynamic model Name as : ", Name)
        print("Equation Of State(EOS) for thermodynamic model (%s) as:  %s" %(Name, case))
        print("Pressure Vapor(PV) equation: ", PV)
        ModelKeys={}
        ModelKeys["RKS"] = "RedlichKwongS"
        ModelKeys["RK"] = "RedlichKwong"
        ModelKeys["PR"] = "PengRobinson"
        ModelKeys["SRK"] = "SoaveRK"

        if case not in ModelKeys:
            print "The model %s isnt aviable"%case
            return 0
        print("###### AddModel() for (%s) ######" %Name)
        print("########################### STARTS FINDING OF PUBLIC VARS(Db cols name) FOR PV MODEL (%s) AND EOS MODEL"
              "(%s)################" %(PV, case))
        if Name not in self.TheCase.keys():
            self.TheCase[Name] = ThermoCase(ModelKeys[case], PV)  # ThermoCase() obj contains PresureModel, EOS,
            # EOSModel and NamePresureVap infos for EOS(case) and PV.
            case_i = self.TheObj.keys()
            if case_i != [] and len(self.TheCase.keys())==1:
                self.TheCase[Name].Cases += case_i
                for i in case_i:
                    self.TheObj[i].Model = Name
            print("### ThermoCase dict() for Given thermodynamic model Name (%s) as follows:" %Name)
            print(self.TheCase[Name].__dict__)
            return self.TheCase[Name]
        else:
            print "%s has yet added"%Name
    
    def AddCase (self, Name, Model=None):
        '''
        :param Name: Name of the thermodynamic model say ('PR')
        :param Model:
        :return:
                1. This function initialize 'TheObj' attribute of Ollin() object with ThermoObj() from module
                ThemoObj.py.
                2. This function also adds Name to 'Model' attribute of ThermoObj().
                3. It returns ThermoObj() object
        '''
        if not Name in self.TheObj.keys(): 
            self.TheObj[Name] = ThermoObj()
            case_i = self.TheCase.keys()
            #print("case_i from AddCase()", case_i)
            if len(case_i):
                self.TheCase[case_i[0]].Cases += Name
                #print("IN ADDCASE FROM OLLIN",self.TheCase[case_i[0]].Cases)
                self.TheObj[Name].Model = case_i[0]  # Initialized Model attribute of ThermoObj() with thermodynamic
                # model as name
            return self.TheObj[Name]
        else: # else part is added by prabhat because if is not exceuting for vapor Phasesout
            return self.TheObj[Name]

    def LoadConst(self, case=None):
        '''
        :param case: Name of the thermodynamic model say ('PR')
        :return: Storing the constant value for each PublicVar for a given Thermodynamic model, known as case.
                1. It uses Ollin's 'cur' attribute for accessing the database (data.db).
                2. Using 'cur' it will find constant values for each PublicVars for given Thermodynamic model.
                3. Sample 'Const' attribute from 'TheCase' is as follows:-
                Ollin().TheCase['PR']['Const']= {'PR_B': array([0.02679926, 0.0404462,0.05633893]), '':.....}
                3. Here, const ('PR_B') is an array for 3 PublicVars ["METHANE", "ETHANE", "PROPANE"]
        '''
        """
        In LoadConst, Load information from data base for the Model (case). Here, case is given
        Thermodynamic model, say "PR"
        """
        print("################ In LoadConst, Load information from data base for the Model (case)")
        if not case:
            print("self.TheCase.keys()", self.TheCase.keys())
            for case in self.TheCase.keys():  # Here, it is PR, given Thermodynamic model
                #print('case: ', case)
                #print("self.TheCase[case].library: ", self.TheCase[case].library)
                if self.TheCase[case].Load != 1:
                    comp = self.TheCase[case].library
                    for Var in self.TheCase[case].PublicVars:  # Here, self.TheCase[case].PublicVars, a list of
                        # PublicVars for TheCase['PR']
                        # like: ['MoleWt', 'LIQDEN', 'ANT_A', 'ANT_B', 'ANT_C', 'TC', 'PC', 'VC', 'ZC', 'PR_A', 'PR_B', 'OMEGA',
                        # 'CP_A', 'CP_B', 'CP_C', 'CP_D', 'HV', 'TB', 'DELHF', 'DELGF', 'CP_A', 'CP_B', 'CP_C', 'CP_D', 'HV', 'TB',
                        # 'DELHF', 'DELGF']

                        self.TheCase[case].Const[Var] = array(self.cur.Dates(Var, comp)[0])
                        # Storing the constant value for each PublicVar for given Thermodynamic model, known as case.
                    self.TheCase[case].Load = 1  # For given Thermodynamic model, all PublicVar values are loaded from
                    # Database data.db
        else:
            if self.TheCase[case].Load !=1: 
                comp = self.TheCase[case].library
                for Var in self.TheCase[case].PublicVars:
                    self.TheCase[case].Const[Var] = array(self.cur.Dates(Var, comp)[0])
                self.TheCase[case].Load = 1
        print("TheCase info for case %s as follows:" %case)
        print(self.TheCase[case].__dict__)
        print("################ Completion of LoadConst ###########################")

    def Connect(self, Model, Case):
        '''

        :param Model: A thermodynamic model.
        :param Case: A case which is required to add with Model.
        :return: This method is called when I want to change Model name of a ThermoObj Case.
        '''
        if Case in self.TheObj.keys() and Model in self.TheCase.keys():
            self.TheObj[Case].Model = Model
        else:
            return 0

    def Solve(self, case=None):
        '''
        :param case: None or Thermodynamic model (for example: 'PR")
        :return:
                1. It checks the 'Load' attribute of ThermoCase() and if it is 0 it will call LoadConst() otherwise NOT.
                2. It will call Solve(ThermObj()) from ThermoCase.py module.
                3. The ThermObj() gives an access to Pressure (P) and Temperature (T) for the Thermodynamic model
                (for example: 'PR")
        '''
        print("Inside Solve() of Ollin:")
        print("Ollin obj :", self.__dict__)
        print("Ollin TheObj element val:", self.TheObj)
        print("Ollin TheCase element val:", self.TheCase)
        if self.TheObj !=None and self.TheCase !=None:
            if case!=None:
                print "Solving %s..."%case
                print("Solve->Model",self.TheObj[case].Model)
                model = self.TheObj[case].Model
                if self.TheCase[model].Load == 0:
                    self.LoadConst()
                #print("TheCase[model]",self.TheCase[model])
                self.TheCase[model].Solve(self.TheObj[case])
            else:
                for case in self.TheObj.keys():  # case is coming from 'key' of TheObj dict.
                    print "Solving %s..."%case
                    model = self.TheObj[case].Model
                    
                    if self.TheCase[model].Load == 0:
                        self.LoadConst()
                    
                    self.TheCase[model].Solve(self.TheObj[case])  # It will call Solve(ThermObj()) from ThermoCase.py
                    # module
        else:
            return 0
    
    def Resumen(self,case=None):
        """Print resumen of the case"""
        if case == None:
            for case in self.TheObj.keys():
                self.TheObj[case].CasePrint()
                self.TheObj[case].XPrint()
        else:
                self.TheObj[case].CasePrint()
                self.TheObj[case].XPrint()

Ollin = AdmOllin()
