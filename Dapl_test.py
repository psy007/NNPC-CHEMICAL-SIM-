import sys
import os
import cPickle
from sim.thermo import ThermoAdmin
from sim.unitop import Flash
from sim.unitop import Stream
from sim.solver import Flowsheet
from sim.unitop import Mixer
from sim.unitop import LiqLiqExt
from sim.unitop import Heater
from sim.unitop import Split
from sim.unitop import Balance
from sim.solver import Ports
from sim.solver.Variables import *
from sim.solver.Error import SimError
from sim.Dapl_vmg.Dapl_vmg import VMGerror



def TestSimpleFlash():

    print """++++++++++++++Init SimpleFlash ++++++++++++++++"""

    package_name = "PR"
    compounds = ("ISOBUTANE", "N-BUTANOL", "2-BUTANOL", "ISOBUTANOL")
    thermo_admin = ThermoAdmin.ThermoAdmin()
    providers = thermo_admin.GetAvThermoProviderNames()
    provider = providers[0]
    thCase = 'myTh'
    thermo = thermo_admin.AddPkgFromName(provider, thCase, package_name)
    for compound in compounds:
        thermo_admin.AddCompound(provider, thCase, compound)


    flash = Flash.SimpleFlash()
    flash.SetThermoAdmin(thermo_admin)
    flash.SetThermo(thermo)
    cmps = flash.GetCompoundNames()
    flash.SetParameterValue(NULIQPH_PAR, 1)  #Should be NULIQPH_PAR
    portsIn = flash.GetPortNames(MAT|IN)
    print 'Names Ports In: ', portsIn
    portsOut = flash.GetPortNames(MAT|OUT)
    print 'Names Ports Out: ', portsOut
    comps = [0.25, 0.25, 0.25, 0.25]
    flash.SetCompositionValues(portsIn[0], comps)
    flash.GetPort(portsIn[0]).SetPropValue(T_VAR, 273.15, FIXED_V)
    flash.GetPort(portsIn[0]).SetPropValue(P_VAR, 101.325, FIXED_V)
    flash.GetPort(portsIn[0]).SetPropValue(MOLEFLOW_VAR, 10.0, FIXED_V)
    print 'Return value from Solve()', flash.Solve()
    print ''

    # Print some info in
    for port_in in portsIn:
        comp = flash.GetCompositionValues(port_in)
        print 'Composition of port in "', port_in, '":'

        for j in range(len(comp)): 
            print 'fraction of ', compounds[j], ': ', comp[j]
        print ''

        print 'Some props of port in "', port_in, '":'
        print T_VAR, ': ', flash.GetPropValue(port_in, T_VAR)
        print H_VAR, ': ', flash.GetPropValue(port_in, H_VAR)
        print MOLEFLOW_VAR, ': ', flash.GetPropValue(port_in, MOLEFLOW_VAR)
        print ''

        port = flash.GetPort(port_in)
        print 'Array properties available: ', port.GetArrPropNames()
        props = port.GetArrPropValue(LNFUG_VAR)
        print 'Array of ', LNFUG_VAR, ' of port in "', port_in, '":'

        if props:
            for j in range(len(props)):
                print 'ln fug of ', compounds[j], ': ', props[j]

        print ''

    # Print some info out
    for i in portsOut:
        comp = flash.GetCompositionValues(i)
        print 'Composition of port out "', i, '":'
        for j in range(len(comp)):
            print('fraction of ', compounds[j], ': ', comp[j])
        print ''

        print 'Some props of port out "', i, '":'
        print T_VAR, ': ', flash.GetPropValue(i, T_VAR)
        print H_VAR, ': ', flash.GetPropValue(i, H_VAR)
        print MOLEFLOW_VAR, ': ', flash.GetPropValue(i, MOLEFLOW_VAR)
        print ''

        port = flash.GetPort(i)
        print 'Array properties available: ', port.GetArrPropNames()
        props = port.GetArrPropValue(LNFUG_VAR)
        #props = port.GetArrPropValue(CMPIDEALG_VAR)
        print 'Array of ', LNFUG_VAR, ' of port out "', i, '":'
        if props:
            for j in range(len(props)): print 'ln fug of ', compounds[j], ': ', props[j]
        print ''

    print """++++++++++Finished SimpleFlash ++++++++++++"""

    # flash.CleanUp()
    # thermo_admin.CleanUp()



def TestSimpleFlash2LPhase():
    print """ Init SimpleFlash2LPhase ++++++++++++++++++++++++++++++"""
    ##Set Thermo
    pkgName = "Peng-Robinson"
    cmpNames = ("PROPANE", "N-BUTANE", "ISOBUTANE", "N-PENTANE", "WATER")
    thAdmin = ThermoAdmin.ThermoAdmin()
    providers = thAdmin.GetAvThermoProviderNames()
    provider = providers[0] #Should be Virt Mat
    thCase = 'myTh'
    thermo = thAdmin.AddPkgFromName(provider, thCase, pkgName)
    for i in cmpNames:
        thAdmin.AddCompound(provider, thCase, i)

    ##Load vals
    flash = Flash.SimpleFlash()
    flash.SetThermoAdmin(thAdmin)
    flash.SetThermo(thermo)
    flash.SetParameterValue(NULIQPH_PAR, 2) # Should be NULIQPH_PAR
    cmps = flash.GetCompoundNames()
    print 'Cmps: ', cmps
    portsIn = flash.GetPortNames(MAT|IN)
    print 'Names Ports In: ', portsIn
    portsOut = flash.GetPortNames(MAT|OUT)
    print 'Names Ports Out: ', portsOut

    flash.SetCompositionValue(portsIn[0], "PROPANE", 0.20)
    flash.SetCompositionValue(portsIn[0], "N-BUTANE", 0.20)
    flash.SetCompositionValue(portsIn[0], "ISOBUTANE", 0.20)
    flash.SetCompositionValue(portsIn[0], "N-PENTANE", 0.20)
    flash.SetCompositionValue(portsIn[0], "WATER", 0.20)
    flash.GetPort(portsIn[0]).SetPropValue(T_VAR,300.00 , FIXED_V) #273.15
    flash.GetPort(portsIn[0]).SetPropValue(P_VAR, 101.325, FIXED_V)
    flash.GetPort(portsIn[0]).SetPropValue(MOLEFLOW_VAR, 10.0, FIXED_V)
    print 'Return value from Solve()', flash.Solve()
    print ''

    #Print some info in
    for i in portsIn:
        comp = flash.GetCompositionValues(i)
        print 'Composition of port in "', i, '":'
        for j in range(len(comp)): print 'fraction of ', cmpNames[j], ': ', comp[j]
        print ''

        print 'Some props of port in "', i, '":'
        print T_VAR, ': ', flash.GetPropValue(i, T_VAR)
        print H_VAR, ': ', flash.GetPropValue(i, H_VAR)
        print MOLEFLOW_VAR, ': ', flash.GetPropValue(i, MOLEFLOW_VAR)
        print ''

    #Print some info out
    for i in portsOut:
        comp = flash.GetCompositionValues(i)
        print 'Composition of port out "', i, '":'
        for j in range(len(comp)): print 'fraction of ', cmpNames[j], ': ', comp[j]
        print ''

        print 'Some props of port out "', i, '":'
        print T_VAR, ': ', flash.GetPropValue(i, T_VAR)
        print H_VAR, ': ', flash.GetPropValue(i, H_VAR)
        print MOLEFLOW_VAR, ': ', flash.GetPropValue(i, MOLEFLOW_VAR)
        print ''

    print """Finished SimpleFlash2LPhase ++++++++++++++++++++++++++++++
    """

    flash.CleanUp()
    thAdmin.CleanUp()


def TestMixAndFlash():
    print """ Init MixAndFlash ++++++++++++++++++++++++++++++"""
    ##Set Thermo
    pkgName = "Peng-Robinson"
    cmpNames = ("PROPANE", "N-BUTANE", "ISOBUTANE", "N-PENTANE")
    thAdmin = ThermoAdmin.ThermoAdmin()
    providers = thAdmin.GetAvThermoProviderNames()
    provider = providers[0]  # Should be Virt Mat
    thCase = 'myTh'
    thermo = thAdmin.AddPkgFromName(provider, thCase, pkgName)
    for i in cmpNames: thAdmin.AddCompound(provider, thCase, i)

    flowsheet = Flowsheet.Flowsheet()
    flowsheet.SetThermoAdmin(thAdmin)
    flowsheet.SetThermo(thermo)

    ##Load vals
    flash = Flash.MixAndFlash()
    flowsheet.AddUnitOperation(flash, 'Flash')
    cmps = flash.GetCompoundNames()
    print 'Cmps: ', cmps
    portsIn = flash.GetPortNames(MAT | IN)
    print 'Names Ports In: ', portsIn
    portsOut = flash.GetPortNames(MAT | OUT)
    print 'Names Ports Out: ', portsOut
    flash.SetParameterValue(NULIQPH_PAR, 1)
    flash.SetParameterValue(NUSTIN_PAR, 2)
    flash.SetCompositionValue(portsIn[0], "PROPANE", 0.5)
    flash.SetCompositionValue(portsIn[0], "N-BUTANE", 0.5)
    flash.SetCompositionValue(portsIn[0], "ISOBUTANE", 0.0)
    flash.SetCompositionValue(portsIn[0], "N-PENTANE", 0.0)
    flash.GetPort(portsIn[0]).SetPropValue(T_VAR, 460.15, FIXED_V)
    flash.GetPort(portsIn[0]).SetPropValue(P_VAR, 700.325, FIXED_V)
    flash.GetPort(portsIn[0]).SetPropValue(MOLEFLOW_VAR, 10.0, FIXED_V)

    flash.SetCompositionValue(portsIn[1], "PROPANE", 0.0)
    flash.SetCompositionValue(portsIn[1], "N-BUTANE", 0.0)
    flash.SetCompositionValue(portsIn[1], "ISOBUTANE", 0.5)
    flash.SetCompositionValue(portsIn[1], "N-PENTANE", 0.5)
    flash.GetPort(portsIn[1]).SetPropValue(T_VAR, 200.15, FIXED_V)
    flash.GetPort(portsIn[1]).SetPropValue(P_VAR, 700.325, FIXED_V)
    flash.GetPort(portsIn[1]).SetPropValue(MOLEFLOW_VAR, 10.0, FIXED_V)

    print 'Return value from Solve()', flowsheet.Solve()
    print ''

    # Print some info in
    for i in portsIn:
        comp = flash.GetCompositionValues(i)
        print 'Composition of port in "', i, '":'
        for j in range(len(comp)): print 'fraction of ', cmpNames[j], ': ', comp[j]
        print ''

        print 'Some props of port in "', i, '":'
        print T_VAR, ': ', flash.GetPropValue(i, T_VAR)
        print H_VAR, ': ', flash.GetPropValue(i, H_VAR)
        print MOLEFLOW_VAR, ': ', flash.GetPropValue(i, MOLEFLOW_VAR)
        print ''

        # Print some info out
    for i in portsOut:
        comp = flash.GetCompositionValues(i)
        print 'Composition of port out "', i, '":'
        for j in range(len(comp)): print 'fraction of ', cmpNames[j], ': ', comp[j]
        print ''

        print 'Some props of port out "', i, '":'
        print T_VAR, ': ', flash.GetPropValue(i, T_VAR)
        print H_VAR, ': ', flash.GetPropValue(i, H_VAR)
        print MOLEFLOW_VAR, ': ', flash.GetPropValue(i, MOLEFLOW_VAR)
        print ''

    print """Finished MixAndFlash ++++++++++++++++++++++++++++++
   """

    flash.CleanUp()
    thAdmin.CleanUp()


if __name__ == '__main__':

    TestSimpleFlash()
    #TestSimpleFlash2LPhase()
    #TestMixAndFlash()





