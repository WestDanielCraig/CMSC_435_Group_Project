from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd
import re

lengths = []
weights = []

countA = []
countC = []
countD = []
countE = []
countF = []
countG = []
countH = []
countI = []
countK = []
countL = []
countM = []
countN = []
countP = []
countQ = []
countR = []
countS = []
countT = []
countV = []
countW = []
countY = []

aromaticity = []

instability_index = []
isoelectric_point = []

countA = []
countC = []
countD = []
countE = []
countF = []
countG = []
countH = []
countI = []
countK = []
countL = []
countM = []
countN = []
countP = []
countQ = []
countR = []
countS = []
countT = []
countV = []
countW = []
countY = []

aromaticity = []

instability_index = []
isoelectric_point = []

gravy_list = []

helix = []
turn = []
sheet = []

cysteines_reduced = []
cystines_residues = []

training_data = pd.read_csv('../datasets/original_training.csv')

for protein in training_data.itertuples():
    print(protein[1])
    protein_length = len(str(protein[1]))  # length of sequence
    lengths.append(protein_length)
    analyzed_protein = ProteinAnalysis(str(protein[1]))
    ambigious_match = re.findall("X+|Z+|U+", protein[1])
    if ambigious_match:
        molecular_weight = "?"
    else:
        molecular_weight = analyzed_protein.molecular_weight()
    weights.append(molecular_weight)

    amino_acid_count = analyzed_protein.count_amino_acids()
    print(amino_acid_count)

    amino_acid_countA = (analyzed_protein.count_amino_acids()['A'])
    countA.append(amino_acid_countA)
    amino_acid_countC = (analyzed_protein.count_amino_acids()['C'])
    countC.append(amino_acid_countC)
    amino_acid_countD = (analyzed_protein.count_amino_acids()['D'])
    countD.append(amino_acid_countD)
    amino_acid_countE = (analyzed_protein.count_amino_acids()['E'])
    countE.append(amino_acid_countE)
    amino_acid_countF = (analyzed_protein.count_amino_acids()['F'])
    countF.append(amino_acid_countF)
    amino_acid_countG = (analyzed_protein.count_amino_acids()['G'])
    countG.append(amino_acid_countG)
    amino_acid_countH = (analyzed_protein.count_amino_acids()['H'])
    countH.append(amino_acid_countH)
    amino_acid_countI = (analyzed_protein.count_amino_acids()['I'])
    countI.append(amino_acid_countI)
    amino_acid_countK = (analyzed_protein.count_amino_acids()['K'])
    countK.append(amino_acid_countK)
    amino_acid_countL = (analyzed_protein.count_amino_acids()['L'])
    countL.append(amino_acid_countL)
    amino_acid_countM = (analyzed_protein.count_amino_acids()['M'])
    countM.append(amino_acid_countM)
    amino_acid_countN = (analyzed_protein.count_amino_acids()['N'])
    countN.append(amino_acid_countN)
    amino_acid_countP = (analyzed_protein.count_amino_acids()['P'])
    countP.append(amino_acid_countP)
    amino_acid_countQ = (analyzed_protein.count_amino_acids()['Q'])
    countQ.append(amino_acid_countQ)
    amino_acid_countR = (analyzed_protein.count_amino_acids()['R'])
    countR.append(amino_acid_countR)
    amino_acid_countS = (analyzed_protein.count_amino_acids()['S'])
    countS.append(amino_acid_countS)
    amino_acid_countT = (analyzed_protein.count_amino_acids()['T'])
    countT.append(amino_acid_countT)
    amino_acid_countV = (analyzed_protein.count_amino_acids()['V'])
    countV.append(amino_acid_countV)
    amino_acid_countW = (analyzed_protein.count_amino_acids()['W'])
    countW.append(amino_acid_countW)
    amino_acid_countY = (analyzed_protein.count_amino_acids()['Y'])
    countY.append(amino_acid_countY)

    aromaticity_count = analyzed_protein.aromaticity()
    aromaticity.append(aromaticity_count)

    ambigious_instability = re.findall("X+|Z+|U+", protein[1])
    if ambigious_instability:
        instability = "?"
    else:
        instability = analyzed_protein.instability_index()

    instability_index.append(instability)

    isoelectic = analyzed_protein.isoelectric_point()
    isoelectric_point.append(isoelectic)

    # print("Index: %s" % protein[0])
    # print("Protein Length: " + str(protein_length))
    # print("Molecular Weight: %s" % molecular_weight)
    # print(" ")
    # print(amino_acid_count)

    # df=pd.DataFrame(amino_acid_count)
    # print(df)
    # df.to_csv("amino.csv")
    training_data.columns = ["PROTEIN SEQUENCE", "CLASS"]
    training_data["LENGTH"] = lengths
    training_data["MOLECULAR WEIGHT"] = weights
    training_data["Aromaticity"] = aromaticity
    training_data["Instability Index"] = instability_index
    training_data["Isoelectric Point"] = isoelectric_point

    training_data["COUNT-A"] = countA
    training_data["COUNT-C"] = countC
    training_data["COUNT-D"] = countD
    training_data["COUNT-E"] = countE
    training_data["COUNT-F"] = countF
    training_data["COUNT-G"] = countG
    training_data["COUNT-H"] = countH
    training_data["COUNT-I"] = countI
    training_data["COUNT-K"] = countK
    training_data["COUNT-L"] = countL
    training_data["COUNT-M"] = countM
    training_data["COUNT-N"] = countN
    training_data["COUNT-P"] = countP
    training_data["COUNT-Q"] = countQ
    training_data["COUNT-R"] = countR
    training_data["COUNT-S"] = countS
    training_data["COUNT-T"] = countT
    training_data["COUNT-V"] = countV
    training_data["COUNT-W"] = countW
    training_data["COUNT-Y"] = countY

    ambigious_gravy = re.findall("X+|Z+|U+", protein[1])
    if ambigious_gravy:
        gravy = "?"
    else:
        gravy = analyzed_protein.gravy()

    gravy_list.append(gravy)

    secondary_structure = analyzed_protein.secondary_structure_fraction()
    helix.append(secondary_structure[0])
    turn.append(secondary_structure[1])
    sheet.append(secondary_structure[2])

    molar_extinction = analyzed_protein.molar_extinction_coefficient()
    cysteines_reduced.append(molar_extinction[0])
    cystines_residues.append(molar_extinction[1])

training_data.columns = ["PROTEIN SEQUENCE", "CLASS"]
training_data["Length"] = lengths
training_data["Molecular Weight"] = weights
training_data["Aromaticity"] = aromaticity
training_data["Instability Index"] = instability_index
training_data["Isoelectric Point"] = isoelectric_point
training_data["Gravy"] = gravy_list
training_data["Helix"] = helix
training_data["Turn"] = turn
training_data["Sheet"] = sheet
training_data["Cysteines Reduced"] = cysteines_reduced
training_data["Cystines Residues"] = cystines_residues

training_data["COUNT-A"] = countA
training_data["COUNT-C"] = countC
training_data["COUNT-D"] = countD
training_data["COUNT-E"] = countE
training_data["COUNT-F"] = countF
training_data["COUNT-G"] = countG
training_data["COUNT-H"] = countH
training_data["COUNT-I"] = countI
training_data["COUNT-K"] = countK
training_data["COUNT-L"] = countL
training_data["COUNT-M"] = countM
training_data["COUNT-N"] = countN
training_data["COUNT-P"] = countP
training_data["COUNT-Q"] = countQ
training_data["COUNT-R"] = countR
training_data["COUNT-S"] = countS
training_data["COUNT-T"] = countT
training_data["COUNT-V"] = countV
training_data["COUNT-W"] = countW
training_data["COUNT-Y"] = countY

training_data.to_csv('../datasets/training_data.csv')
