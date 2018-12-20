# -*- coding: latin-1 -*-
# Contributed by J.-Henrique Pinto  2003-Nov-18
# Contribution de J.-Henrique Pinto  2003-Nov-18

def Messages():
    """create dictionary of French messages :: messages en franais"""
    m = {}
    m['AddCompoundError']          = "Le fournisseur de donnes thermodynamiques signale lerreur suivante lors de lajout du composant:\n%s"
    m['AdjustingFromOlderVersion'] = "Rcupration dun cas cre avec une version prcdente. Mise  jour  partir de: VersionDiagProc = %d; version = %s. : VersionDiagProc %d; version %s"
    m['AfterPortDisconnect']       = "%s dconnect de %s"
    m['BalanceInvalidPort']        = "Port incorrect pour le bilan : pas de matire ou dnergie"
    m['BeforePortDisconnect']      = "Dconnexion de %s de %s"
    m['BubbleTCouldNotCalc']       = "Impossible de calculer la temprature du point de bulle dans %s  P = %skPa et composition = %s"
    m['CantAddObject']             = "Impossible dajouter %s  %s"
    m['CantAddToStage']            = "Impossible dajouter %s  l'tage %d de %s"
    m['CantAddToStageObject']      = "Impossible dajouter %s  %s sur l'tage %d de %s"
    m['CantChangeName']            = "Impossible de changer le nom de %s"
    m['CantCreateSpec']            = "Impossible de crer spcif. %s. Probablement elle nest pas prise en charge"
    m['CantDeleteFromStage']       = "Impossible de supprimer %s de ltage %d de %s"
    m['CantDeleteObject']          = "Impossible de supprimer lobjet %s. Les calculs de lopration unitaire ne peut pas tre effectus sans cet objet"
    m['CantMoveToStage']           = "Impossible de dplacer %s  l'tage %d de %s. Assurez quil ny ait pas de conflits dans les noms."
    m['CantOverwriteThermo']       = "Impossible de remplacer un cas thermo. Supprimez dabord le vieux cas thermo avant den dfinir un nouveau. Op. unit: %s; cas thermo actuel: %s"
    m['CantSetIP']                 = "Impossible de dfinir un paramtre interactif de valeur %f pour les composs %s et %s"
    m['CantSetLiqPhPar']           = "Impossible de dfinir le nombre de phases liquides comme %s"
    m['CantSetParameter']          = "Impossible dattribuer la valeur %s au paramtre %s"
    m['ChangedEffMatrix']          = "Il y a eu un changement dans la matrice defficacits en raison dun changement de la configuration dans %s"
    m['CompNotNormalized']         = "La somme des fractions molaires de %s est gale  %f, pas 1"
    m['ConnectErrorNoPort']        = "Impossible de connecter %s.%s  %s.%s car un port est manquant"
    m['ConnectErrorNoUop']         = "Impossible de connecter %s.%s  %s.%s car une opration unitaire est manquante"
    m['ConnectSameTypePorts']      = "Tentative de connexion de ports de types diffrents dans %s"
    m['ConnectSigToNonSig']        = "Tentative de connexion dun signal dun port %s  un signal incompatible"
    m['ContDerivCalc']             = "Calcul des drivs %d par le calculateur du contrleur %s"
    m['ControllerConvergeFail']    = "Pas de convergence du calculateur du contrleur pour %s"
    m['ControllerTotalError']      = "Calculateur du contrleur pour %s erreur - %f"
    m['CouldNotConverge']          = "Convergence impossible de %s aprs  %d itrations"
    m['CouldNotConvergeInner']     = "Convergence impossible de la boucle interne %s aprs  %d itrations"
    m['CouldNotConvergeOuter']     = "Convergence impossible de la boucle externe %s aprs  %d itrations"
    m['CouldNotConvergeUA']        = "Impossible de rsoudre UA = %f dans %s"
    m['CouldNotInitialize']        = "Initialisation impossible de l'ensemble d'quations lors de la solution de %s"
    m['CouldNotInvertJacobian']    = "Impossible dinverser le Jacobien dans %s"
    m['CouldNotLoadLanguage']      = "Impossible de charger la langue %s"
    m['CouldNotLoadProvider']      = "Impossible de charger le fournisseur de donnes thermodynamiques %s"
    m['CouldNotSolve']             = "Impossible de calculer %s"
    m['CouldNotSolveNonSuppFlash'] = "Impossible de resoudre le flash non pris en charge avec les variables %s = %s, %s = %s dans %s"
    m['CreatePortTypeError']       = "Le type du port %s nest pas correct dans %s"
    m['CrossConnMoleLoss']         = "Une perte importante du dbit molaire de %f a t dtecte dans le connecteur crois %s. Une raison probable est la non-correspondance des composs dont les dbits sont importants"
    m['DeletePortError']           = "Impossible de supprimer le port %s de %s"
    m['DewTCouldNotCalc']          = "Impossible de calculer la temprature du point de rose dans %s  P = %skPa et composition = %s"
    m['DiffThCaseInConn']          = "Un cas thermo diffrent a t retrouv  travers la connexion de ports %s -> %s. Les valeurs nont pas pu tre transfres"
    m['DuplicateName']             = "chec de la commande en raison dune duplication du nom %s dans %s"
    m['ErrInCleanUp']              = "Erreur lors de la maintenance de %s"
    m['ErrNotifyChangeCmp']        = "Erreur lors de lavertissement  %s dun changement dans la liste des composs"
    m['ErrNotifyLiqChange']        = "Erreur lors de lavertissement  %s dun changement dans le nombre de phases liquides. PhasesLiquides = %s"
    m['ErrNotifyParChange']        = "Erreur lors de lavertissement  %s dun changement dans la valeur dun paramtre. %s = %s"
    m['ErrNotifySolChange']        = "Erreur lors de lavertissement  %s dun changement dans le nombre de phases solides. PhasesLiquides = %s"
    m['ErrNotifyThChange']         = "Erreur lors de lavertissement  %s dun changement de cas thermo. CasThermo = %s"
    m['ERRSettingThermo']          = "Erreur lors de lessai de dfinition de thermo dans une op. unit.: %s; cas thermo essay: %s"
    m['ErrorSolvingDesign']        = "Erreur de calcul de lobjet %s"
    m['ERRTowerArithmetic']        = "chec de la convergence de la tour %s en raison dune erreur arithmtique"
    m['EqnCalcError']              = "Erreur de calcul dans %s"
    m['EqnDuplicateSigName']       = "Le nom du signal %s est employ plus dune fois dans lquation %s"
    m['EqnNumbMismatch']           = "Erreur lors du comptage dquations dans %s"
    m['EqnParenMismatch']          = "Erreur dans le comptage du nombre de parenthses en %s de lquation %s"
    m['EqnSyntax']                 = "Erreur de syntaxe dans %s de lquation %s"
    m['EqnUnknownToken']           = "Impossible de traiter %s dans lquation %s de %s"
    m['EqnBasedUOpError']          = "%s itration %d erreur max %f"
    m['HotTLowerThanColdT']        = "La temprature de lentre chaude %f est infrieure  celle de lentre froide %f in %s"
    m['HydrateCouldNotCalc']       = "chec dans %s lors du calcul de la temprature de l'hydrate  P = %skPa et composition = %s"
    m['HydrateLowP']               = "Impossible de former l'hydrate sous la condition de basse pression P = %s kPa dans %s"
    m['InvalidCalcStatusInSet']    = "calcStatus non valide dans SetValue"
    m['InvalidComposition']        = "La composition %s = %f dans %s.  Elle a t remise  zro."
    m['InvalidDrawPhase']          = "Phase incorrecte pour le prlvement  ltage %d de %s"
    m['InvalidTowerSpecPhase']     = "Phase incorrecte dans la spcification  ltage %d de %s"
    m['LumpLiqs']                  = "Un second liquide de composition %f a t dtect dans un flash LV  deux phases."
    m['MaxSolverIterExceeded']     = "Le nombre max ditrations %d a t dpass lors de lexcution du procd %s"
    m['MissigZInCommonProps']      = "Le facteur Z doit tre toujours dans les proprits communes. Essai de dfinition: %s"
    m['NonHydrateFormerFound']     = "Formation de non hydrate trouve en venant vers %s"
    m['NoPortDirection']           = "Le port %s ncessite un sens ( entrant ou sortant ) dans %s"
    m['NoSupportForReqArrProps']   = "Le fournisseur de donnes thermodynamiques %s ne prend pas en charge les proprits requises suivantes %s"
    m['NoSupportForReqProps']      = "Le fournisseur de donnes thermodynamiques %s ne prend pas en charge les proprits requises suivantes %s"
    m['NoVersionUpdate']           = "Aucune mise  jour de %d (%s)  %d (%s)"
    m['PortNotFlashedDesignObj']   = "Le flash des ports de lop. unit. na pas t effectu. Le calcul de lobjet %s nest donc pas effectu"
    m['RawOutput']                 = "%s"
    m['RecycleErrorDetail']        = "%s %s %g contre %g"
    m['RecycleConsistency']        = "Erreur de cohrence %s %s %g contre %g"
    m['RecycleIter']               = "Itration %d -> erreur max %f"
    m['RenamePortError']           = "Impossible dattribuer le nom %s au port %s"
    m['RenamePortNameExists']      = "Impossible dattribuer le nom %s au port %s parce que ce nom est dj utilis"
    m['RevertingFromNewerVersion'] = "Rcupration dun cas cre avec une version plus rcente. Mise  jour  partir de: version du diagramme de proc. %d, version %s. : version du diagramme de proc. %d version %s"
    m['SetValueUnknownNotNone']    = "SetValue avec un indicateur UNKNOWN_V doit avoir la valeur = None"
    m['SetVarTypeMismatch']        = "Le type de variable du port %s nest pas %s dans %s"
    m['SigConnectTypeMismatch']    = "Conflit de type de variable (%s c. %s) lors de la connexion de %s  %s"
    m['SigShareMismatch']          = "Conflit de type de variable (%s c. %s) lors de la cration du partage de %s avec %s"
    m['SolvingDesign']             = "Calcul de lobjet %s en cours"
    m['SolvingOp']                 = "Rsolution de lopration %s en cours"
    m['TemperatureCross']          = "Tempratures croises (%f %f) dans %s"
    m['NoPkgSelected']             = "Aucun ensemble thermo na t slectionn lors de lessai de cration de %s"
    m['TooManySolidPhases']        = "Trop de phases solides ont excut une requte(%d) lors de lessai dexcution dun flash de %s"
    m['TooManyTowerSpecs']         = "%d spcifications trouves, seulement %d requises dans %s"
    m['TowerCalcJacobian']         = "Calcul du Jacobien pour %s en cours"
    m['TowerCmpMatrixError']       = "%s erreur lors du calcul du bilan matire pour le composant %d"
    m['TowerDeletePort']           = "Impossible de supprimer directement le port %s de %s. Slectionnez et supprimez le prlvement ou spcif. correspondants"
    m['TowerFailedToConverge']     = "Pas de convergence de %s aprs %d itrations - erreur = %f"
    m['TowerInnerError']           = "%s Erreur interne %f"
    m['TowerNoPressure']           = "Aucune pression de sortie pour la colonne %s"
    m['TowerOuterError']           = "%s Itration %d erreur externe %f"
    m['TowerQSpecError']           = "Impossible dattribuer un courant dnergie  ltage %d"
    m['TowerRemoveLastStage']      = "Impossible de supprimer %d tages au-dessous de ltage %d"
    m['TowerPARemovalError']       = "Impossible de supprimer un stage avec une alimentation procure par une recirculation localise sauf si celle-ci est aussi supprim. Lali,mentation est  ltage %I et la recirculation de ltage %i"
    m['TowerSSRemoveError']        = "Impossible de supprimer la tte ou le fond de la colonne sans la suppression de toute la section"
    m['TowerUpdateEffErr']         = "Erreur lors de lessai de mise  jour de la matrice defficacits dans %s. Terminez la mise  jour manuellement"
    m['UpdateInvalidPort']         = "Port %s inexistant dans %s - mise  jour impossible"
    m['WrongDiamEjector']          = "Spcification incorrecte du diamtre dans %s. Le diamtre de l'ajutage doit tre plus petit que celui de la gorge. Diam. ajutage = %f; D gorge = %f"
    m['WrongNumberTowerSpecs']     = "Erreur dans le nombre de spcifications de la colonne - %d contre %d requises dans %s"
    m['WrongParentDesignObj']      = "Lobjet %s contenu dans un type incorrect dopration unitaire"
    m['DoneSolving']               = "Procd %s calcul"
    m['NoMessage']                 = ""
    m['MissingValue']              = "%s na pas de valeur attribue"
    m['ErrorValue']                = "Erreur = %s"
    m['OK']                        = "OK"

    #Following messages not in alphabetical order to keep all the properties together
    m['T']                         = "Temprature"
    m['P']                         = "Pression"
    m['H']                         = "Enthalpie"
    m['VapFrac']                   = "Fraction_vapeur"
    m['MoleFlow']                  = "Dbit_molaire"
    m['MassFlow']                  = "Dbit_massique"
    m['VolumeFlow']                = "Dbit_volumtrique"
    m['Energy']                    = "nergie"
    m['MolecularWeight']           = "Masse_molaire"
    m['ZFactor']                   = "FacteurZ"
    return m