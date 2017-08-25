import copy
import os
from pandas import *

def GetFileLines(file_str):
    """
    Input: string of file name
    Output: List of lines in file
    """
    
    file_name=str(file_str)
    try:
        f=open(file_name)
    except:
        raise StandardError(file_name+" does not exist")
    lines=f.read().splitlines()
    f.close()
    assert len(lines)!=0,"length of "+str(file_str)+"=0"
    return copy.deepcopy(lines)

rep_range = range(11025,11125)

data_lethalmeasure = pandas.read_csv("data_lethalmeasure.csv")
prob_lethal_data = list(data_lethalmeasure["FractionLethal"])
genomesize_data = list(data_lethalmeasure["GenomeSize"])

treatments = ["genotype7_01","genotype7_02","genotype7_04","genotype7_08","genotype7_10",
              "genotype9_01","genotype9_02","genotype9_04","genotype9_08","genotype9_10",
              "genotype5_0025","genotype5_005","genotype5_01","genotype5_02","genotype5_04",
              "genotype14_0025","genotype14_005","genotype14_01","genotype14_02","genotype14_04",
              "genotype10_01","genotype10_02","genotype10_04","genotype10_08","genotype10_10",]

g=open("data_lethalmeasure_varmut.csv","wb")
g.write("GenotypeNum,GenomeSize,PointMutationRate,GenomicMutationRate,LethalMutationRate,NumExtinctions\n")
for genotype_num in [7,9,5,14,10]:
    
    if genotype_num in [7,9,10]:
        
        point_mutation_rates = [0.01,0.02,0.04,0.08,0.1]
        point_mutation_rate_strings = ["01","02","04","08","10"]
        
    elif genotype_num in [5,14]:
        point_mutation_rates = [0.0025,0.005,0.01,0.02,0.04]
        point_mutation_rate_strings = ["0025","005","01","02","04"]
        
    else:
        raise StandardError("Unknown Genotype Number")
    
    for i,pmrs in enumerate(point_mutation_rate_strings):
        
        pmr = point_mutation_rates[i]
        gmr = float(pmr)*float(genomesize_data[genotype_num])
        lmr = float(gmr)*float(prob_lethal_data[genotype_num])
        
        treatment = "genotype"+str(genotype_num)+"_"+str(pmrs)
        
        total_extinctions = 0
        
        for replicate in rep_range:
        
            files = os.listdir("data_lethalmeasure_varmut/"+str(treatment)+"/replicate_"+str(replicate))
            
            extinction = 1
            
            for f in files:
                
                if "detail" in f:
                    extinction = 0
                    break
                
            if len(files) == 0:
                print("No files",t,replicate)
                
            if extinction == 1:
                total_extinctions += 1
                
        g.write(str(genotype_num)+","+str(genomesize_data[genotype_num])+","+str(pmr)+","+str(gmr)+","+str(lmr)+","+str(total_extinctions)+"\n")

g.close()