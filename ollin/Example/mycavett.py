# from ollin.Administrator.AdmOllin import Ollin      # Loading Data Base data.db \ ..........
# from ollin.Example.UOS import Stream, Valve, Heater, Flash
# PR = Ollin.AddModel("PR", "PR", 'ANTOINE')        # Create a thermodynamic models and naming
# print(PR.__dict__)
# Ollin.Add(["METHANE","ETHANE","PROPANE","ISOBUTANE","N-BUTANE","N-PENTANE","N-HEXANE","N-HEPTANE","N-OCTANE","N-NONANE","N-DECANE","N-UNDECENE"],"PR")
# # Add the compounds of the mixture
# #Ollin.Add(["ETHANE" "PROPANE", "N-BUTANE", "N-PENTANE", "N-HEXANE"], "PR")
# Ollin.LoadConst()
# print(PR.__dict__)
#
# print("############## Calling of AddCase() of Ollin")
# thermo_obj_PR = Ollin.AddCase('PR')
# print("############## Calling SetX() from ThemoObj.py using ThermoObj()")
# thermo_obj_PR.SetX([2995.5,2395.5,2291,2991,1539.9,790.4,1129.9,1764.7,1844.5,1699,831.7,1214.5])
#
# #thermo_obj_PR.SetX([0.05,0.15,0.25,0.20,0.35])
#
# print("############## Calling T() from ThemoObj.py using ThermoObj()")
# thermo_obj_PR.T(322)
#
# print("############## Calling FracVap() from ThemoObj.py using ThermoObj()")
# thermo_obj_PR.FracVap(0.6)
#
# print("############## Calling P() from ThemoObj.py using ThermoObj()")
# thermo_obj_PR.P(1861)
#
# print("------------- ThermoObj for PR -----------", )
# print(thermo_obj_PR.__dict__)
#
# print("#################### Calling Ollin().Solve()")
# Ollin.Solve()
# print("#################### Calling Ollin().Resumen()")
# Ollin.Resumen()


# print("############# calling of Stream() from myTestExp.py ####################")
# S1 = Stream(PR)
# print("Stream() obj dict: ")
# print(S1.__dict__)
# print("ThermoCase Model attribute from Stream() obj: ")
# print(S1.Model.__dict__)
# print("Thermodynamic Case attribute from Stream() obj: ")
# print(S1.Case.__dict__)
# print("Set Thermodynamic x property: ")
# S1.X([2995.5,2395.5,2291,2991,1539.9,790.4,1129.9,1764.7,1844.5,1699,831.7,1214.5])
# # Set MassFraction for Stream() obj and mole fraction of the Thermodynamic obj as ThemoObj()
# print("MassFraction for Stream() obj and mole fraction of the Thermodynamic Case obj as ThemoObj() are created")
# print("Mass Fraction: ", S1.MassFraction)
# print("Mole Fraction: ", S1.Case.Prop["x"])
# print("Set Temperature of Thermodynamic Case obj as ThemoObj()")
# S1.T(322)
# print("Temperature: ", S1.Case.Prop["T"])
# print("Set Pressure of Thermodynamic Case obj as ThemoObj()")
# S1.P(1861)
# print("Pressure: ", S1.Case.Prop["P"])
# print("Set MoleFlow of Stream() obj")
# S1.Mol(455)
# print("MoleFlow: ", S1.MoleFlow)

# V1 = Valve(PR)
# V1.DP = 50
#
# H1 = Heater(PR)
# H1.DP = 1
# H1.DT = 1
#
#
# print("############## Calling of AddCase() of Ollin")
# Ollin.AddCase('PR')
# print("#####################################################")
# Ollin.Solve()
# Ollin.Resumen()
#########################################################################################################
from ollin.Administrator.AdmOllin import Ollin
PR = Ollin.AddModel("PR", "PR")
print(PR.__dict__)
Ollin.Add(["METHANE","ETHANE","PROPANE","ISOBUTANE","N-BUTANE","N-PENTANE","N-HEXANE","N-HEPTANE","N-OCTANE","N-NONANE"
              ,"N-DECANE","N-UNDECENE"],"PR")
Ollin.LoadConst()
print("####################### Calling of AddCase() #####################################")
thermo_obj_PR = Ollin.AddCase('PR')
thermo_obj_PR.SetX([2995.5,2395.5,2291,2991,1539.9,790.4,1129.9,1764.7,1844.5,1699,831.7,1214.5])
thermo_obj_PR.T(322)
thermo_obj_PR.P(1861)
print("################### Ollin PresureVap obj")
print(PR.PresureVap)
print("#################### Calling Ollin().Solve()")
Ollin.Solve()
print("#################### Calling Ollin().Resumen()")
Ollin.Resumen()
