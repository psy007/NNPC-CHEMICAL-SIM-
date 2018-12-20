from ollin.Tools import MixingRules
from math import sqrt
from ollin.Flash.Flash import MyFlash
from ollin.EOS.eos import EOS
from ollin.Thermodinamics.Thermodinamic import Thermo
from numpy import sqrt,array,power,log,exp,absolute
from ollin.Tools.tools import lagrange
from ollin.Thermodinamics.Constans import R


class Model:

    def __init__(self, PV):
        self.TagsOfConst = ["TC","PC","VC","ZC","PR_A","PR_B","OMEGA","CP_A","CP_B","CP_C","CP_D","HV","TB","DELHF","DELGF"]
        self.EOS = EOS(2, -1)  # This will call EOS() constructor from ollin.EOS.eos
        self.PV = PV    # Presure Vapor Equation
        self.Thermo = Thermo()
        self.TagsOfConst += self.Thermo.NeedVars()

    def NeedVars(self):
        return self.TagsOfConst

    # def NeedVars(self):
    #     return self.TagsOfConst

    def FugaP(self,Z,A,B):
        """ Fugacity Coefficient of Pure Substances"""
##        print Z-B
        L = ( 1/( 2*sqrt(2) ) ) * log( ( Z +B*(1+sqrt(2) ) ) / ( Z +B*(1-sqrt(2) ) ) )
        LogFug = Z-1 - log(abs(Z-B)) - A/B*L
        Fug = exp( LogFug )
        return Fug

    def FugaM(self,Z,A_i,B_i,A,B):
        L = ( 1/( 2*sqrt(2) ) ) * log( ( Z +B*(1+sqrt(2) ) ) / ( Z +B*(1-sqrt(2) ) ) )
        LogFug =  B_i/B*(Z-1) - log(Z-B) + A/B * ( B_i/B- 2*A_i/A  ) * L
        Fug = exp ( LogFug )
        return Fug

    def dadT(self,ac,fw,Tr,Tc):
        return ac*fw*( fw*sqrt(Tr)-fw-1 )/( Tc*sqrt(Tr) )

    def d2adT2(self,ac,fw,T,Tr,Tc):

        return fw*( fw+1 )/( 2*Tc*T*sqrt(Tr) )

    '''
    def Solver(self, model, case):
        
        :param model: 'Const' from ThermoCase for given Thermodynamic model.
        :param case:  'Case' as ThermoObj() instance from Ollin() for given Thermodynamic model.
        :return: It will call various methods based on 'P' and 'T' for Prop attribute from case and also
        call following methods as follows:-
        1. For given T and P ---> calls PengRobinson().Isotermic(model, case) and PengRobinson().EOS.Thermal(model,case).
        2. For given T and FracVap ---> calls PengRobinson().FracTemp(model,case) and PengRobinson().EOS.Thermal(model,case).
        3. For given T and H ---> calls PengRobinson().HenTemp(model, case).
        4. For given P and FracVap ---> calls PengRobinson().FracPre(model, case) and PengRobinson().EOS.Thermal(model,case).
        5. For given P and H ---> calls PengRobinson().HenPre(model,case).

        Thermal() method from eos.py module.
        

        print("YEs I have reached in peng Solver", case)
        model["RK_A"] = model["PR_A"]
        model["RK_B"] = model["PR_B"]

        """Case with  defined temperature"""
        if case.Prop["T"] is not None and case.Solve != 1:
            print "Defined Temperature"
            if case.Prop["P"] is not None:
                print "...Defined Presure"
                self.Isotermic(model, case)
                self.EOS.Thermal(model, case)
                case.Solve = 1   # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
                # with T and P
            
            elif case.Prop["FracVap"] is not None:
                print "...Defined FracVap"
                self.FracTemp(model, case)
                self.EOS.Thermal(model, case)
                case.Solve = 1   # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
                # with T and FracVap
                
            elif case.Prop["H"] is not None:
                print "...Defined Hentalpy"
                self.HenTemp(model, case)
                case.Solve = 1   # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
                # with T and H

        """Case with defines Pressure"""
        if case.Prop["P"] is not None and case.Solve != 1:
            print "Defined Presure.........."
            if case.Prop["FracVap"] is not None:
                print "...Defined FracVap"
                self.FracPre(model, case)
                self.EOS.Thermal(model, case)
                case.Solve = 1   # # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
                # with P and FracVap.
                
            elif case.Prop["H"] is not None:
                print "...Defined Hentalpy"
                self.HenPre(model, case)
                case.Solve = 1  # # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
                # with P and H.
    '''

    # This is modified solver to run the script by prabhat original one is above commented
    def Solver(self, model, case):
        '''
        :param model: 'Const' from ThermoCase for given Thermodynamic model.
        :param case:  'Case' as ThermoObj() instance from Ollin() for given Thermodynamic model.
        :return: It will call various methods based on 'P' and 'T' for Prop attribute from case and also
        call following methods as follows:-
        1. For given T and P ---> calls PengRobinson().Isotermic(model, case) and PengRobinson().EOS.Thermal(model,case).
        2. For given T and FracVap ---> calls PengRobinson().FracTemp(model,case) and PengRobinson().EOS.Thermal(model,case).
        3. For given T and H ---> calls PengRobinson().HenTemp(model, case).
        4. For given P and FracVap ---> calls PengRobinson().FracPre(model, case) and PengRobinson().EOS.Thermal(model,case).
        5. For given P and H ---> calls PengRobinson().HenPre(model,case).

        Thermal() method from eos.py module.
        '''

        print("YEs I have reached in peng Solver", case)
        model["RK_A"] = model["PR_A"]
        model["RK_B"] = model["PR_B"]

        """Case with  defined temperature"""
        #if case.Prop["T"] is not None and case.Solve != 1:
        print "Defined Temperature"
            #if case.Prop["P"] is not None:
        print "...Defined Presure"
        self.Isotermic(model, case)
        self.EOS.Thermal(model, case)
        case.Solve = 1  # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
        # with T and P

        #     elif case.Prop["FracVap"] is not None:
        #         print "...Defined FracVap"
        #         self.FracTemp(model, case)
        #         self.EOS.Thermal(model, case)
        #         case.Solve = 1  # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
        #         # with T and FracVap
        #
        #     elif case.Prop["H"] is not None:
        #         print "...Defined Hentalpy"
        #         self.HenTemp(model, case)
        #         case.Solve = 1  # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
        #         # with T and H
        #
        # """Case with defines Pressure"""
        # if case.Prop["P"] is not None and case.Solve != 1:
        #     print "Defined Presure.........."
        #     if case.Prop["FracVap"] is not None:
        #         print "...Defined FracVap"
        #         self.FracPre(model, case)
        #         self.EOS.Thermal(model, case)
        #         case.Solve = 1  # # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
        #         # with P and FracVap.
        #
        #     elif case.Prop["H"] is not None:
        #         print "...Defined Hentalpy"
        #         self.HenPre(model, case)
        #         case.Solve = 1  # # It will set ThermoObj().Solve = 1 and it means Thermodynamic model is solved
        #         # with P and H.

    #################################################################
#Isotermic metode for solve the case
#################################################################

    def Isotermic(self, model, case):

        xm = case.Prop["x"]
        T = case.Prop["T"]
        P = case.Prop["P"]
        Ac = model["PR_A"]
        b_i = model["PR_B"]
        W_i = model["OMEGA"]
        TC_i = model["TC"]
        PC_i = model["PC"]
        VC_i = model["VC"]

        ##        print xm
        TC = sum(xm * TC_i)
        PC = sum(xm * PC_i)
        VC = sum(xm * VC_i)
        ##        print "PC",PC_i
        ##        print "TC",TC_i
        ##        print TC,PC
        case.Prop["ZC"] = PC * VC / (R * TC)
        ##        print case.Prop["ZC"]
        PreVap = self.PV.P(T, model)
        case.Prop["PreVap"] = PreVap

        fwi = []
        for Wii in W_i:
            if Wii < 0.5:
                fwi.append(0.37464 + 1.54226 * Wii - 0.26992 * power(Wii, 2))
            else:
                fwi.append(0.3796 + 1.4850 * Wii - 0.1644 * power(Wii, 2) + 0.01666 * power(Wii, 3))

        fwi = array(fwi)
        case.Prop["fw"] = fwi
        Tr_i = T / TC_i
        case.Prop["Tr"] = Tr_i
        AlphaT = power((1 + fwi * (1 - sqrt(Tr_i))), 2)
        case.Prop["AlphaT"] = AlphaT
        case.Prop["dadT"] = self.dadT(Ac, fwi, Tr_i, TC_i)
        case.Prop["d2adT2"] = self.d2adT2(Ac, fwi, T, Tr_i, TC_i)
        case.Prop["MolWt"] = sum(xm * model["MoleWt"])

        a_i = Ac * AlphaT
        case.Prop["a"] = a_i

        A_i = (a_i * P) / pow(R * T, 2)
        B_i = (b_i * P) / (R * T)
        case.Prop["A"] = A_i
        case.Prop["B"] = B_i

        Zl_i = self.EOS.ZL(A_i, B_i)
        Zv_i = self.EOS.ZG(A_i, B_i)
        case.Prop["Zli"] = Zl_i
        case.Prop["Zvi"] = Zv_i
        case.Prop["Vli"] = Zl_i * R * T / P
        case.Prop["Vvi"] = Zv_i * R * T / P

        CoeFugo_v = self.FugaP(Zv_i, A_i, B_i)
        CoeFugo_l = self.FugaP(Zl_i, A_i, B_i)

        k_i = 1
        RFrac = 2

        FVap, xf, yf = MyFlash(list(xm),list(case.Prop["PreVap"] / P))
        MinFuga = 1e10
        while k_i <= 20:
            A_vi = MixingRules.MolarK2(yf, A_i, k=0)
            A_li = MixingRules.MolarK2(xf, A_i, k=0)
            B_v = MixingRules.Molar(yf, B_i)
            A_v = MixingRules.MolarK(yf, A_i, k=0)
            B_l = MixingRules.Molar(xf, B_i)
            A_l = MixingRules.MolarK(xf, A_i, k=0)

            Z_v = self.EOS.ZG(A_v, B_v)
            Z_l = self.EOS.ZL(A_l, B_l)
            CoeFugM_v = self.FugaM(Z_v, A_vi, B_i, A_v, B_v)
            CoeFugM_l = self.FugaM(Z_l, A_li, B_i, A_l, B_l)
            f_l = P * CoeFugM_l * xf
            f_v = P * CoeFugM_v * yf

            f_l = P * CoeFugM_l * xf
            f_v = P * CoeFugM_v * yf

            dFuga = sum(f_l - f_v)

            if abs(dFuga) < MinFuga:

                MinFuga = abs(dFuga)
                ymin = yf
                xmin = xf

            ki = CoeFugM_l / CoeFugM_v

            FrVap, xf, yf = MyFlash(list(xm), list(ki))

            Z = FrVap * Z_v + (1 - FrVap) * Z_l

            if abs(RFrac - FrVap) <= 1e-10:
                case.Solve = 1
                break

            if abs(dFuga) <= 1e-3:
                case.Solve = 1
                break

            RFrac = FrVap
            k_i += 1
            # End iteration to calculate the Fractio Vapor
        V_l = Z_l * R * T / P
        V_v = Z_v * R * T / P

        case.Prop["Z"] = Z
        case.Prop["Zl"] = Z_l
        case.Prop["Zv"] = Z_v
        case.Prop["Ki"] = ki
        case.Prop["FracVap"] = FrVap
        case.Prop["CoefPureLiq"] = CoeFugo_l
        case.Prop["CoefPureVap"] = CoeFugo_v
        case.Prop["CoefMixVLiq"] = CoeFugM_l
        case.Prop["CoefMixVap"] = CoeFugM_v
        case.Prop["ActivityVap"] = CoeFugM_v / CoeFugo_v
        case.Prop["ActivityLiq"] = CoeFugM_l / CoeFugo_l
        case.Prop["xf"] = xf
        case.Prop["yf"] = yf
        case.Prop["Vl"] = V_l
        case.Prop["Vv"] = V_v
        case.Prop["MolWt_l"] = sum(xf * model["MoleWt"])
        case.Prop["MolWt_v"] = sum(yf * model["MoleWt"])
        case.Prop["LiqDen"] = sum(xf * model["LIQDEN"])
        case.Prop["fl_i"] = f_l
        case.Prop["fv_i"] = f_v



##        print "d"

#################################################################
#Case that Tempererature and Fraction Vapor are defined
#################################################################
    def FracTemp(self, model, case):

        P_i = []
        Fra_i= []
        Fra_r =case.Prop["FracVap"]
        xm = case.Prop["x"]
        case.Prop["P"]= sum(self.PV.P(case.Prop["T"],model)*case.Prop["x"])
        self.Isotermic(model,case)
        P_i.append(case.Prop["P"])
        Fra_i.append( case.Prop["FracVap"] )
        case.Prop["LiqDen"] = sum( xm* model["MoleWt"] )
        if case.Prop["FracVap"] <=0.5:
            case.Prop["P"]= case.Prop["P"]*0.5
            self.Isotermic(model,case)
            while case.Prop["FracVap"] <=0.05:
                case.Prop["P"]= case.Prop["P"]*0.5
                self.Isotermic(model,case)
        else:
            case.Prop["P"]= case.Prop["P"]*1.5
            self.Isotermic(model,case)
            while case.Prop["FracVap"] >=0.95:
                case.Prop["P"]= case.Prop["P"]*1.5
                self.Isotermic(model,case)

##        self.Isotermic( model,case )
        P_i.append( case.Prop["P"] )
        Fra_i.append( case.Prop["FracVap"] )

        case.Prop["P"]= sum(P_i)/2
        self.Isotermic( model,case )
        P_i.append( case.Prop["P"] )
        Fra_i.append( case.Prop["FracVap"] )

        i = 1
        while i<=20:
            case.Prop["P"]=lagrange( Fra_i, P_i, Fra_r )
            self.Isotermic( model, case )
            P_i.append( case.Prop["P"] )
            Fra_i.append( case.Prop["FracVap"] )
            i += 1
            if abs(Fra_r-case.Prop["FracVap"])<=1e-10:
                break


#################################################################
#Case that Tempererature and Hentalpy are defined
#################################################################
    def HenTemp(self,model,case):
        P_i = []
        H_i= []
        H_r =case.Prop["H"]
        case.Prop["P"]= sum(self.PV.P(case.Prop["T"],model)*case.Prop["x"])
        self.Isotermic(model,case)
        self.EOS.Thermal(model,case)

        P_i.append(case.Prop["P"])
        H_i.append( case.Prop["H"] )

        if case.Prop["H"] <=0.5*H_r:
            case.Prop["P"]= case.Prop["P"]*0.5
        else:
            case.Prop["P"]= case.Prop["P"]*1.5

        self.Isotermic(model,case)
        self.EOS.Thermal(model,case)
        P_i.append(case.Prop["P"])
        H_i.append( case.Prop["H"] )

        case.Prop["P"]= sum(P_i)/2
        self.Isotermic(model,case)
        self.EOS.Thermal(model,case)
        P_i.append(case.Prop["P"])
        H_i.append( case.Prop["H"] )

        i = 1

        while i<=20:
            case.Prop["P"]=lagrange(H_i,P_i,H_r)
            self.Isotermic(model,case)
            self.EOS.Thermal(model,case)
            P_i.append(case.Prop["P"])
            H_i.append( case.Prop["H"] )
            i += 1

            if abs(H_r-case.Prop["H"])<=1e-10:
                break

#################################################################
#Case that Presure and Fraction Vapor are defined
#################################################################
    def FracPre(self,model,case):

        T_i = []
        Fra_i= []
        Fra_r =case.Prop["FracVap"]
        print(case.Prop)
        print("############ self.PV", self.PV.__dict__)
        print("############# self.PV.T(case.Prop[P], model)", self.PV.T(case.Prop["P"], model))
        print("case.Prop[x]", case.Prop["x"])
        temp_abhi = self.PV.T(case.Prop["P"], model)*case.Prop["x"]
        print("temp_abhi", temp_abhi)
        case.Prop["T"] = sum(self.PV.T(case.Prop["P"], model)*case.Prop["x"])
        #print(sum(self.PV.T(case.Prop["P"], model)*case.Prop["x"]))
        self.Isotermic(model, case)

        T_i.append(case.Prop["T"])
        Fra_i.append( case.Prop["FracVap"] )
##        print case.Prop["FracVap"],case.Prop["T"]

        if case.Prop["FracVap"] <=0.5:
            case.Prop["T"]= case.Prop["T"]*1.05
            self.Isotermic(model,case)
            while case.Prop["FracVap"] <=0.05:
                case.Prop["T"]= case.Prop["T"]*1.05
                self.Isotermic(model,case)
        else:
            case.Prop["T"]= case.Prop["T"]*0.95
            self.Isotermic(model,case)
            while case.Prop["FracVap"] >=0.95:
                case.Prop["T"]= case.Prop["T"]*0.95
                self.Isotermic(model,case)

        self.Isotermic(model,case)
        T_i.append(case.Prop["T"])
        Fra_i.append( case.Prop["FracVap"] )

        case.Prop["T"]= sum(T_i)/2
        self.Isotermic( model,case )
        T_i.append( case.Prop["T"] )
        Fra_i.append( case.Prop["FracVap"] )

##        print case.Prop["FracVap"],case.Prop["T"]

        i = 1
        while i<=20:
            case.Prop["T"]=lagrange(Fra_i,T_i,Fra_r)
##            print case.Prop["FracVap"],case.Prop["T"]
            self.Isotermic(model,case)
            T_i.append(case.Prop["T"])
            Fra_i.append( case.Prop["FracVap"] )
            i += 1
            if abs(Fra_r-case.Prop["FracVap"])<=1e-10:
                break

#################################################################
#Case that Presure and Hentalpy are defined
#################################################################
    def HenPre(self,model,case):
        print("########### Now you are now HenPre() for defined H and P ............")
        T_i = []
        H_i= []
        H_r =case.Prop["H"]
        case.Prop["T"]= sum(self.PV.T(case.Prop["P"],model)*case.Prop["x"])
        print("case.Prop[T] from ")
        self.Isotermic(model,case)
        self.EOS.Thermal(model,case)
        T_i.append(case.Prop["T"])
        H_i.append( case.Prop["H"] )
##        print case.Prop["T"],case.Prop["FracVap"]
        if case.Prop["FracVap"] <=0.5:
            case.Prop["T"]= case.Prop["T"]*1.1
##            print case.Prop["T"]
            self.Isotermic(model,case)
            while case.Prop["FracVap"] <=0.05:
                case.Prop["T"]= case.Prop["T"]*1.1
                self.Isotermic(model,case)
        else:
            case.Prop["T"]= case.Prop["T"]*0.9
            self.Isotermic(model,case)
            while case.Prop["FracVap"] >=0.95:
                case.Prop["T"]= case.Prop["T"]*0.9
                self.Isotermic(model,case)

        self.Isotermic(model,case)
        self.EOS.Thermal(model,case)
        T_i.append(case.Prop["T"])
        H_i.append( case.Prop["H"] )
        i = 1
        while i<=20:
            case.Prop["T"]=lagrange(H_i,T_i,H_r)
            self.Isotermic(model,case)
            self.EOS.Thermal(model,case)
            T_i.append(case.Prop["T"])
            H_i.append( case.Prop["H"] )
            i += 1
            if abs(H_r-case.Prop["H"])<=1e-10:
                break

