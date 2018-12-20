from numpy import power,array
from ollin.Tools.tools import lagrange
from scipy.optimize import fsolve, newton, brenth

def Flash(k,z,fr=None):
    """Flash"""
##    if x!=None:
##        return Fraction(k,x,y)
    if len(z) == 1:
        x = array([1])
        y = array([1])
        if k ==1:
            Frac = 1
        else:
            Frac = FracVap(k,z,fr)
            #Frac = MyFracVap(k, z, fr)
        return (Frac,x,y)
    
#     if k.any()==1.0:
#         Frac = 1.0
#         y = z
#         x = z
#         return(Frac,x,y)
#     else:
    Frac = FracVap(k,z,fr)
    #Frac = MyFracVap(k, z, fr)
    
    if Frac<= 0.000001:
        Frac= 1e-12
        x = z
        y = k*z / (0.000001*(k-1)+1)
        if abs(sum(y)-1.000) >= 1e-5:
            y = Normal(y)
        return(Frac,x,y)
    
    if Frac >=0.99999:
        Frac =1-1e-12
        y = z
        x = z / (0.99999*(k-1)+1)
        if abs(sum(x)-1.000) >= 1e-5:
            x = Normal(x)
        return (Frac,x,y)
    x = z / ( Frac*(k-1)+1)
    y = k*x
    return(Frac,x,y)

def MyFlash(zs, Ks):
    '''
     This function is defined by prabhat singh yadav reference activity.py
     this is an alternate of above Flash
    :param zs: array of mole fraction of compound
    :param Ks: constant
    :return: Vapour fraction as V_over_F
    '''
    Kmin = min(Ks)
    Kmax = max(Ks)
    z_of_Kmax = zs[Ks.index(Kmax)]

    V_over_F_min = ((Kmax - Kmin) * z_of_Kmax - (1. - Kmin)) / ((1. - Kmin) * (Kmax - 1.))
    V_over_F_max = 1. / (1. - Kmin)

    V_over_F_min2 = max(0., V_over_F_min)
    V_over_F_max2 = min(1., V_over_F_max)

    x0 = (V_over_F_min2 + V_over_F_max2) * 0.5
    try:
        # Newton's method is marginally faster than brenth
        V_over_F = newton(Rachford_Rice_flash_error, x0=x0, args=(zs, Ks))
        #V_over_F = brenth(Rachford_Rice_flash_error, V_over_F_max - 1E-7, V_over_F_min + 1E-7, args=(zs, Ks))
        # newton skips out of its specified range in some cases, finding another solution
        # Check for that with asserts, and use brenth if it did
        assert V_over_F >= V_over_F_min2
        assert V_over_F <= V_over_F_max2
    except:
        V_over_F = brenth(Rachford_Rice_flash_error, V_over_F_max - 1E-7, V_over_F_min + 1E-7, args=(zs, Ks))
    # Cases not covered by the above solvers: When all components have K > 1, or all have K < 1
    # Should get a solution for all other cases.
    xs = [zi / (1. + V_over_F * (Ki - 1.)) for zi, Ki in zip(zs, Ks)]
    ys = [Ki * xi for xi, Ki in zip(xs, Ks)]
    return V_over_F, array(xs), array(ys)

def Rachford_Rice_flash_error(V_over_F, zs, Ks):

    return sum([zi * (Ki - 1.) / (1. + V_over_F * (Ki - 1.)) for Ki, zi in zip(Ks, zs)])


def FracVap(k,z,Frac):
    """
    Flash Calc ki, x, Oi=0.5
    """
    if Frac ==None:
        Frac= 0.5
    fk1 = k-1
    fk2 = fk1*z
##    print fk1
    fk3 = power(fk1,2)
    #print k
    j = 1

    while j<=30:

        fk4 = fk1*Frac+1

        Fkz = sum(fk2 / fk4)
        dFkz = sum(-fk3*z / power(fk4,2))
##        print j, Frac, Fkz , dFkz
        if abs(Fkz)<=1e-8:
            break
        Frac = Frac - Fkz / dFkz
        j+=1

##    if Frac > 1:
##        Frac = 1
####        print "Vapor Saturado"
##    if Frac < 0:
##        Frac = 0
##        print "Liquido comprido"
    return Frac
    
    
def Normal(x):
    if type(x) == list:
        x = array(x,typecode = Float0)
    Px = sum(x)
    
    if Px == 1.000:
        return x
    else:
        xi= x/Px
    for i in range(len(x) ):
        if xi[i]<1e-8:
            xi[i]= 1e-8
    return xi
##def Fraction(k,x,y):
##    """
##    calc fracction
##    """
##    F_i = []
##    SF_i= []
##    fk1 = k-1
####    fk2 = fk1*z
##    fk3 = power(fk1,2)
##    Frac=0.1
##    fk4 = fk1*Frac+1
##    zi = (1-Frac)*x+Frac*y
##    Fk = sum( fk1*zi / fk4)
####    Fk = sum( Frac*x*k-Frac*x+x )
##    Fy = sum( y*(Frac*(k-1)+1)/k)
##    print FracVap(k,zi)
##    F_i.append(0.1)
##    SF_i.append(Fk)
##    print Fk
##    Frac=0.5
##    fk4 = fk1*Frac+1
##    zi = (1-Frac)*x+Frac*y
##    Fk = sum( fk1*zi / fk4)
##    Fy = sum(y*(Frac*(k-1)+1)/k)
##    F_i.append(0.5)
##    SF_i.append(Fk)
##    print Fk
##    Frac=0.9
##    fk4 = fk1*Frac+1
##    zi = (1-Frac)*x+Frac*y
##    Fk = sum( fk1*zi / fk4)
##    Fy = sum(y*(Frac*(k-1)+1)/k)
##    F_i.append(0.9)
##    SF_i.append(Fk)
##    i = 1
##    print Fk
####    while i<=20:
####        Frac=lagrange(SF_i,F_i,1)
####        Fk = sum( Frac*x*k-Frac*x+x )
####        F_i.append(Frac)
####        SF_i.append(Fk)
####        i += 1
####        print Fk,Frac
####        if abs(Fk-1)<=1e-6:
####            break 
####    print Fk
##       # print j, Frac, Fkz , dFkz
####        if abs(Fk)<=1e-12:
####            break
####        Frac = Frac - Fk / dFk
####    print Frac
####    if Frac > 1:
####        Frac = 1
######        print "Vapor Saturado"
####    if Frac < 0:
####        Frac = 0
##    z = ( Frac*(k-1)+1)*x
##    return (Frac,z)
