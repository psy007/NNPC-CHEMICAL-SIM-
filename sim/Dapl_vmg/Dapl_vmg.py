from ollin.CES.PengRobinson import Model
from ollin.Thermodinamics.PresureVapor import *
from ollin.Administrator.AdmOllin import Ollin



__all__ = ['VMGerror','InitializePkg','AddPkgFromName', 'CompoundStringProperty','CompoundDoubleProperty',
           'SelectedCompoundStringProperty','ExchangeCompound','MoveCompound','RegisterObject',
           'SetObjectDoubleArrayValues','GetSpecialProperty','GetPropertyTable','SetMultipleObjectDoubleValues',
           'GetMultipleObjectDoubleValues','EquilibriumObjectFlash','MultipleBulkObjectDoubleValues',
           'SetFlashSetting','MixTwoObjects','AddCompound','DefineObject','PhaseEnvelope',
           'UnregisterObject','UnregisterObject','SelectedCompoundNames','TerminatePkg','AddAggregatePkgFromName',
           'CustomCommand']


class VMGerror(RuntimeError):
    pass

class VMGwarning(Warning):
    pass

def InitializePkg():
    pass

# Being used in TestSimpleFlash
def AddPkgFromName(pkgName):
    # peng-robinson is being passed to this function

    hnd = Ollin.AddModel(pkgName, case="PR", PV="ANTOINE")
    #hnd = Ollin.AddCase (pkgName, Model=None)
    return hnd

# Being used in TestSimpleFlash
def SelectedCompoundNames(hnd): # needs to be implemented
    return hnd.library

# Being used in TestSimpleFlash
def AddCompound(hnd, cmp): # needs to be implemented
    print('Add compound in VMG ran')
    Ollin.Add(cmp, hnd)


# Being used in TestSimpleFlash
def RegisterObject(hnd, FVL):
    # hnd holding string PR an identifier in dictionary for
    # Thermocase object location in gpkghandles = 1
    # FVL is 'feed' or 'vap' or 'liq'
    val = Ollin.AddCase(hnd, Model=FVL)
    print("ValinRegisterObject",val)
    return val


# Being used in TestSimpleFlash
def SetObjectDoubleArrayValues(hnd, feed, seaComposition, bulkComp):
    feed.SetX(bulkComp)   # setting molfraction for compound
    pass

# Being used in TestSimpleFlash
def SetMultipleObjectDoubleValues(hnd, feed, vmprops, vals):
    feed.P(vals[0])  # setting pressure VMG to OLLIN
    feed.T(vals[1])  # seeting Temp SIM to OLLIN
    pass

# Being used in TestSimpleFlash
def EquilibriumObjectFlash(hnd, initFromInput, flType,
                           liqPhases, withSolid, othersCount,
                           feed, phasesOut, phasesFracs):     # Flash() in ollin TS
    Ollin.Solve(case=hnd)

    xf = feed.Prop["xf"]
    phasesFracs.append(xf)
    yf = feed.Prop["yf"]
    phasesFracs.append(yf)
    FracVap = feed.Prop["FracVap"]
    #FracVap = feed.Prop["x"]
    phasesFracs.append(FracVap)
    return phasesFracs


# Being used in TestSimpleFlash
def MultipleBulkObjectDoubleValues(hnd, liqPhases, withSolid,
                                   othersCount, feed, phasesOut,
                                   phasesFracs, propsNames, seaSeapp):
    bulkprop = []
    for prop in propsNames:
        bulkprop.append(feed.Get(prop))
    return bulkprop


# Being used in TestSimpleFlash
def GetObjectDoubleArrayValues(hnd, feed, prop, unknown):

   # feed is thermobj object
   return feed.Get(prop)

# Being used in TestSimpleFlash
def GetMultipleObjectDoubleValues(hnd, i, propname): # get() from ollin ts
    val = []
    for proname in propname:
        val.append(i.Get(proname))
    return val


def MixTwoObjects(hnd, bulkLiqId, liq1Id, liq2Id, fr1, propsNames):
    pass
def AddAggregatePkgFromName(pkgName):
    pass

def CompoundStringProperty():
    pass



def CompoundDoubleProperty():
    pass
def SelectedCompoundStringProperty():
    pass
def ExchangeCompound():
    pass
def MoveCompound():
    pass


def GetSpecialProperty():
    pass
def GetPropertyTable():
    pass




def SetFlashSetting():
    pass

def DefineObject():
    pass
def PhaseEnvelope():  # can be mapped with plots in ollin TS
    pass
def UnregisterObject():
    pass




def TerminatePkg():
    pass

def AddAggregatePkgFromName():
    pass
def CustomCommand():
    pass
def Oil(a,b,c):
    pass
def SetBinaryPairValues(hnd, ipMatrName, paneIdx, vals):
    pass
def ResetAijChanged(hnd):
    pass
def SetBinaryPairValues(hnd, ipMatrName, paneIdx, kijArray):
    pass
def DeletePkg(a):
    pass
