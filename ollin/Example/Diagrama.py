import sys
#sys.path.append("/Users/jonathanxavier/Developer/sim42")
#sys.path.append("/home/dat-asset-227/code/sim42")
sys.path.append("/Users/DAT-ASSET-236/Desktop/CODE/THESIM42/dapl_sim42")
from ollin.Administrator.AdmOllin import Ollin
from pylab import *

RK = Ollin.AddModel("RK", "PR")
S1 = Ollin.AddCase("PR")
Ollin.Add(["ETHANE","PROPANE","N-BUTANE","N-PENTANE","N-HEXANE"], "RK")
S1.SetX([0.05, 0.15, 0.25, 0.20, 0.35])
S1.P(101.325)

plot_x = range(240, 325, 2)
plot_y0 = []
plot_y1 = []
plot_y2 = []
plot_y3 = []
plot_y4 = []
plot_y5 = []

for T in plot_x:
    S1.T(T)
    Ollin.Solve()
    yf=S1.Get("yf")
    
    plot_y0.append(yf[0])
    plot_y1.append(yf[1])
    plot_y2.append(yf[2])
    plot_y3.append(yf[3])
    plot_y4.append(yf[4])
    plot_y5.append(S1.Get("FracVap"))
##    print adm.TheObj["Str"].Prop["FracVap"],adm.TheObj["Str"].Prop["T"]
 
plot(plot_x, plot_y0)
plot(plot_x, plot_y1)
plot(plot_x, plot_y2)
plot(plot_x, plot_y3)
plot(plot_x, plot_y4)
plot(plot_x, plot_y5)
##axis([244,300,0,1])
grid(True)
titles = RK.library
titles.append("FracVap")
legend(titles)
title("Fraccion Vapor Vs T , Y vs T")
xlabel('T(K)')
ylabel('y,FracVap')
show()
