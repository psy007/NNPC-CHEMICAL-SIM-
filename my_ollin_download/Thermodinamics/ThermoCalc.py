from ollin.pvt.CpCalc import CapG
from Numeric import array

def ThermoCalc(case):
    case.CpGi = CapG(case)
    case.CpG = sum(case.CpGi*case.yf)
    case.Hv = sum(case.Hvi*case.yf)
