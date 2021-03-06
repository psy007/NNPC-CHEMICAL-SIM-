def Messages():
    """create dictionary of English messages"""
    m = {}
    m['AddCompoundError']       = "Thermo provider reports the following error when adding compound:\n%s"
    m['AdjustingFromOlderVersion'] = "Recalling case created in an older version. Updating from: FlowsheetVersion = %d; ReleaseVersion = %s. To: FlowsheetVersion %d; ReleaseVersion %s"
    m['AfterPortDisconnect']    = "%s disconnected from %s"
    m['BalanceInvalidPort']     = "Invalid port for balance (not material or energy)"
    m['BeforePortDisconnect']   = "Disconnecting %s from %s"
    m['BubbleTCouldNotCalc']    = "Bubble Point temperature could not be calculated in %s at P = %s kPa and composition = %s"
    m['CalcDisturbance']        = "Calculating disturbance %i of %i in jacobian of %s"
    m['CalculatingProfile']     = "Calculating profile in %s. Segment %i. Properties %s"
    m['CalculatingStep']        = "Calculating step %i in %s. Currently in %g. Going from %g to %g"
    m['CantAddObject']          = "Can't add %s to %s"
    m['CantAddToStage']         = "Can't add %s to stage %d of %s"
    m['CantAddToStageObject']   = "Can't add %s to %s on stage %d of %s"
    m['CantChangeName']         = "Can't change name of %s"
    m['CantCloneFlowsheet']     = "Can't clone flowsheet %s if stacks are not empty (solve, forget, unconverged recycles, consistency errors)"
    m['CantCreateSpec']         = "Can't create spec %s. It is probably not supported"
    m['CantDeleteFromStage']    = "Can't delete %s from stage %d of %s"
    m['CantDeleteObject']       = "Can't delete object %s. Unit op can not solve with out it"
    m['CantDelPortDirectly']    = "Can't delete port %s from %s. Delete associated object instead"
    m['CantEstimate']           = "Could not estimate missing %s while initializing %s"
    m['CantFindPhCh']           = "Can't find phase changes in %s for more than two sides or when solving in rating mode (UA values specified)"
    m['CantMoveToStage']        = "Can't move %s to stage %d of %s. Make sure there are no conflicting names"
    m['CantOverwriteThermo']    = "Can't overwrite a thermo case. The correct procedure is to first delete old thermo and then set a new thermo. Unit op: %s; Current thermo: %s"
    m['CantSetIP']              = "Can't set interaction parameter with value %f for compounds %s and %s"
    m['CantSetLiqPhPar']        = "Can't set number of liquid phases to %s"
    m['CantSetSingleFrac']      = "Can't set the mass or volume fraction of one single compound %s in a material port %s."
    m['CantSetParameter']       = "Can't set parameter %s to value %s"
    m['CantUseSpecInZeroFlow']  = "Can't use specs in a zero flow draw %s."
    m['ChangedEffMatrix']       = "The efficiencies matrix changed as a result of a change in configuration in %s"
    m['ChangedPortState']       = "Changed state of port %s to %d (0=Normal port; 1=Recycle port)"
    m['CompNotNormalized']      = "Mole fractions of %s sums to %f, not 1"
    m['ConnectErrorNoPort']     = "Can't connect %s.%s to %s.%s as a port is missing"
    m['ConnectErrorNoUop']      = "Can't connect %s.%s to %s.%s as a unit op is missing"
    m['ConnectSameTypePorts']   = "Attempt to connect ports of differing types in %s"
    m['ConnectSigToNonSig']     = "Attempt to connect signal port %s to a non signal port"
    m['ContDerivCalc']          = "Controller solver for %s calculating derivative %d"
    m['ControllerConvergeFail'] = "Controller solver for %s failed to converge"
    m['ControllerTotalError']   = "Controller solver for %s error - %f"
    m['Converged']              = "Converged %s in %i iterations"
    m['ConvergedOp']            = "Converged %s"
    m['CouldNotConverge']       = "Could not converge %s after %d iterations"
    m['CouldNotConvergeInner']  = "Could not converge Inner loop %s after %d iterations"
    m['CouldNotConvergeOuter']  = "Could not converge Outer loop %s after %d iterations"
    m['CouldNotConvergeUA']     = "Could not solve for UA = %f in %s"
    m['CouldNotInitialize']     = "Could not initialize set of equations when solving %s"
    m['CouldNotInvertJacobian'] = "Could not invert Jacobian in %s"
    m['CouldNotLoadLanguage']   = "Could not load language %s"
    m['CouldNotLoadProvider']   = "Could not load thermo provider %s"
    m['CouldNotRestorePlugIn']  = "Could not restore plug in object %s when recalling case. The default object will be used instead"
    m['CouldNotSolve']          = "Could not solve %s"
    m['CouldNotSolveNonSuppFlash'] = "Could not solve non supported flash with variables %s = %s, %s = %s in %s"
    m['CreatePortTypeError']    = "Port %s does not have a valid type in %s"
    m['CrossConnMoleLoss']      = "A significant loss of mole flow of %f was detected in the cross connector %s. A common reason is the mismatch of compounds that contain significant flows"
    m['DeletePortError']        = "Cannot delete port %s from %s"
    m['DewTCouldNotCalc']       = "Dew Point temperature could not be calculated in %s at P = %s kPa and composition = %s"
    m['DiffThCaseInConn']       = "Different thermo case found across port connection %s -> %s. The values could not be passed"
    m['DoneProfile']            = "Done calculating profile in %s"
    m['DuplicateName']          = "Command failed due to a duplication of the name %s in %s"
    m['ErrInCleanUp']           = "Error while cleaning up %s"
    m['ErrNotifyChangeCmp']     = "Error while notifying %s of a change in the compounds list"
    m['ErrNotifyLiqChange']     = "Error while notifying %s of a change of the number of liquid phases. LiquidPhases = %s"
    m['ErrNotifyParChange']     = "Error while notifying %s of a change of the value of a parameter. %s = %s"
    m['ErrNotifySolChange']     = "Error while notifying %s of a change of the number of solid phases. LiquidPhases = %s"
    m['ErrNotifyThChange']      = "Error while notifying %s of a change of thermodynamic case. ThermoCase = %s"
    m['ERRSettingThermo']       = "Error attempting to set thermo into unit op: %s; Thermo attempted: %s"
    m['ErrSpecialProp']         = "Error calculating special property in %s. Message form thermo provider: %s"
    m['ErrorSolvingDesign']     = "Error solving design object %s"
    m['ERRTowerArithmetic']     = "Tower %s failed to converge due to an arithmetic error"
    m['EqnCalcError']           = "Calculation error in %s"
    m['EqnDuplicateSigName']    = "Signal name %s is used more than once in equation %s"
    m['EqnNumbMismatch']        = "Error in equation counting in %s"
    m['EqnParenMismatch']       = "Mismatched parenthesis in %s of Equation %s"
    m['EqnSyntax']              = "Syntax error in %s in Equation %s"
    m['EqnUnknownToken']        = "Don't know how to deal with %s in equation %s of %s"
    m['EqnBasedUOpError']       = "%s Iteration %d Max Error %f"
    m['FlashFailure']           = "Flash failed in %s. Message from Thermo Provider: %s"
    m['HotTLowerThanColdT']     = "The temperature of the hot inlet %f is  lower than the temperature of the cold inlet %f in %s"
    m['HydrateCouldNotCalc']    = "Hydrate temperature could not be calculated in %s at P = %s kPa and composition = %s"
    m['HydrateLowP']            = "Hydrate can not be formed at low pressure condition of P = %s kPa in %s"
    m['InnerErrorDetail']       = "%s Inner Details. Error: %13.6g ; MaxErrorValue: %13.6g ; MaxErrorEqnName: %s "
    m['InnerLoopSummary']       = """%s Inner Loop Summary:
        MaxErrorEqnName:......... %s
        MaxErrorValue:........... %.6g
        
        MaxDeltaTStage(0 at top): %i
        MaxDeltaTValue(New-Old):. %.4g
        
        Converged:............... %i
        Iterations:.............. %i"""
    m['InvalidCalcStatusInSet'] = "Invalid calcStatus in SetValue"
    m['InvalidComposition']     = "The %s composition = %f in %s.  It has been reset to zero."
    m['InvalidDrawPhase']       = "Invalid phase for draw on stage %d of %s"
    m['InvalidTowerSpecPhase']  = "Invalid phase in spec on stage %d of %s"
    m['LumpLiqs']               = "A second liquid with fraction %f is detected in a two phase VL flash."
    m['MaxSolverIterExceeded']  = "Maximum %d iterations exceeded in solving flowsheet %s"
    m['MissingSpecs']           = "Missing %d specifications"
    m['MissingVariable']        = "Missing %s in %s"
    m['MissigZInCommonProps']   = "Z Factor should always be in the common properties. Attempted to set: %s"
    m['NonHydrateFormerFound']  = "Non hydrate former was found coming into %s"
    m['NoPortDirection']        = "Port %s requires direction (in or out) in %s"
    m['NoSupportForReqArrProps']= "The thermo provider %s doesn't support the following required array properties %s"
    m['NoSupportForReqProps']   = "The thermo provider %s doesn't support the following required properties %s"
    m['NotConverging']          = "%s does not seem to be converging and calculations were stopped. Change the parameter MonitorConvergence to 0 if you wish to deactivate this feature"
    m['NoVersionUpdate']        = "No update for %d (%s) to %d (%s)"
    m['ODEMaxSteps']            = "Maximum integration steps reached (%i) in %s. Increase ODEMaxSteps if integration was proceeding correctly"
    m['OuterErrorDetail']       = "%s Iteration %d Outer Error %13.6g. MaxErrorStage(0 at top) %i WaterDrawError %13.6g"
    m['OverspecFlash']          = "Could not perform flash calculation in %s because it is overspecified. Only 2 variables needed and %i were given (%s)"
    m['PortNotFlashedDesignObj']= "Ports from unit op are not flashed therefore design object %s not ready to be solved"
    m['RawOutput']              = "%s"
    m['RecycleErrorDetail']     = "%s %s %g vs %g"
    m['RecycleConsistency']     = "Consistency Error %s %s %g vs %g"
    m['RecycleIter']            = "Iteration %d -> max Error %f in %s"
    m['RenamePort']             = "Rename port %s.%s to %s.  It is connected to %s"
    m['RenamePortError']        = "Cannot rename port %s to %s"
    m['RenamePortNameExists']   = "Cannot rename port %s to %s as that name is already used"
    m['RevertingFromNewerVersion'] = "Recalling case created in a newer version. Updating from: flowsheet version %d, release version %s. To: flowsheet version %d release version %s"
    m['SetValueUnknownNotNone'] = "SetValue with UNKNOWN_V flag must have value = None"
    m['SetVarTypeMismatch']     = "Port variable type %s is not %s in %s"
    m['SigConnectTypeMismatch'] = "Variable type conflict (%s vs %s) when connecting %s to %s"
    m['SigShareMismatch']       = "Variable type conflict (%s vs %s) when sharing %s with %s"
    m['SolvingDesign']          = "Solving design object %s"
    m['SolvingOp']              = "Solving operation %s"
    m['SpecConflict']           = "Specification conflict between %s and %s in %s"
    m['Status']                 = "%s"
    m['StepSizeTooSmall']       = "Step size underflow in %s. Step size = %g"
    m['TemperatureCross']       = "Temperature cross (%f %f) in %s"
    m['InternalTCross']         = "Internal temperature cross in %s. See profiles for details"
    m['NoPkgSelected']          = "No thermo package was selected when attempted to create %s"
    m['ThermoProviderMsg']      = "Msg from thermo provider when solving %s:\n%s"
    m['TooManySolidPhases']     = "Too many solid phases requested(%d) when attempting flash from %s"
    m['TooManyTowerSpecs']      = "%d specs found, only %d needed in %s"
    m['TowerCalcJacobian']      = "Calculating Jacobian for %s"
    m['TowerCmpMatrixError']    = "%s had an error in solving the material balances for component %d"
    m['TowerDeletePort']        = "Cannot directly delete port %s from %s. Select and delete the associated draw or spec"
    m['TowerEffSetToOne']       = "Tower efficiency in the top stage was set to 1.0 because the vapour draw is 0"
    m['TowerFailedToConverge']  = "%s failed to converge in %d iterations - error = %f"
    m['TowerInnerError']        = "%s Inner Error %f"
    m['TowerNoPressure']        = "No outlet pressures available for tower %s"
    m['TowerOuterError']        = "%s Iteration %d Outer Error %f"
    m['TowerQSpecError']        = "Can't assign energy flow to stage %d"
    m['TowerRemoveLastStage']   = "Cannot remove %d stages from below stage %d"
    m['TowerPARemovalError']    = "Cannot remove a stage with a feed from a pump around unless the pump around is removed too. Feed is in stage %i, pump around from stage %i"
    m['TowerSSRemoveError']     = "Top or bottom tower stages cannot be removed unless the whole section is removed"
    m['TowerUpdateEffErr']      = "An error occurred while attempting to update the efficiencies matrix in %s. Please update manually"
    m['TowerMissingFeedInfo']   = "Feed %s is not fully specified"
    m['TwrNoFeed']              = "No feeds were found in %s"
    m['TwrSpecErr']             = "Error while calculating the spec %s"
    m['TwrSpecErrConfig']       = "The spec %s was installed into an invalid object %s. For example, a pump around spec installed into something different from a pump around"
    m['TwrSubCooledVapDraw']    = "Tower failed to converge due to a sub cooled solution at the top where there is a vapour draw. Degrees of subcooling = %f"
    m['UnresolvedConsistencyErrors'] = "The following consistency errors in flowsheet %s have not been resolved (only lists one per unit operation):\n%s"
    m['UnresolvedRecycles']     = "The following recycle ports in flowsheet %s have not been converged (only lists one per unit operation):\n%s"
    m['UpdateInvalidPort']      = "Port %s does not exist in %s - can't update"
    m['WrongDiamEjector']       = "Wrong diameter specification in %s. Nozzle diameter must be smaller than throat diameter. Nozzle D = %f; Throat D = %f"
    m['WrongNumberTowerSpecs']  = "Mismatch in number of tower specs - %d vs %d needed in %s"
    m['WrongParentDesignObj']   = "Design object %s contained in the wrong type of unit operation"
    m['WrongSetting']           = "Invalid value %s for setting %s in object %s"
    m['DoneSolving']            = "Flowsheet %s solved"
    m['NoMessage']              = ""
    m['MissingValue']           = "%s has no value"
    m['ErrorValue']             = "Error = %s"
    m['OK']                     = "OK"

    #Following messages not in alphabetical order to keep all the properties together
    m['T']                      = "Temperature"
    m['P']                      = "Pressure"
    m['H']                      = "Enthalpy"
    m['VapFrac']                = "VapFrac"
    m['MoleFlow']               = "MoleFlow"
    m['MassFlow']               = "MassFlow"    
    m['VolumeFlow']             = "VolumeFlow"  
    m['Energy']                 = "Energy"
    m['MolecularWeight']        = "MolecularWeight"  
    m['ZFactor']                = "ZFactor"     
    return m

