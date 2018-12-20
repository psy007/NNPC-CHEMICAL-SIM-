import sys
sys.path.append("/Users/DAT-ASSET-236/Desktop/CODE/THESIM42/dapl_sim42")

from ollin.Administrator.AdmOllin import Ollin
from ollin.Example.UOS import *



PR = Ollin.AddModel ("PR", "PR", "ANTOINE")
Ollin.Add(['PROPANE', 'N-BUTANE', 'ISOBUTANE', 'N-PENTANE' ], "PR")
Ollin.LoadConst()
# S1 = Ollin.AddCase("S1")
S1 = Stream(PR)
S1.X([0.25, 0.25, 0.25, 0.25])
S1.FracVap(0.5)
S1.T(273.15)
S1.P(101.325)
S1.Mol(10.0)
#S1.H(8045.76822554)

S1.Solver()
S1.CasePrint()
S1.Case.XPrint()