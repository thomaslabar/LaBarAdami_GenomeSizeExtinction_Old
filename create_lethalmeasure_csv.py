import copy
import os

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

g=open("data_lethalmeasure.csv","wb")
g.write("Replicate,Extinction,GenomeSize,Complexity,NumLethal,FractionLethal,InformationDensity,ProbLethal\n")

rep_range = range(17885,17905)
        
for replicate in rep_range:
    
    extinct = 0
    genome_size = 0
    complexity = 0
    fraction_lethal = 0
    info_density = 0
    prob_lethal = 0
    
    present_files=os.listdir("data_lethalmeasure/replicate_"+str(replicate)+"/")
    detail_files=[]
    for filename in present_files:
        if filename[:6]=="detail":
            update_num = filename[7:]
            update_num = int(update_num[:len(update_num)-5])
            detail_files.append((update_num,filename))
            
    detail_files.sort(reverse=True)
    detail_files = [i[1] for i in detail_files]
    
    print(detail_files[0])
    
    if detail_files[0] != "detail-250000.spop":
        extinct = 1
    
    lineage_data = GetFileLines("data_lethalmeasure/lineage/replicate_"+str(replicate)+".dat")
    final_line = lineage_data[-1].split(" ")
    line_ct = 0
    
    while True:
        
        if final_line[2] == "0":
            line_ct += 1
            final_line = lineage_data[-1-line_ct].split(" ")
        else:
            break
        
    genome_size = str(final_line[5])
    complexity = str(final_line[7])
    fraction_lethal = str(final_line[11])
    num_lethal = str(25*int(float(genome_size)*float(fraction_lethal)))
    info_density = float(complexity)/float(genome_size)
    prob_lethal = 0.01*float(genome_size)*float(fraction_lethal)
    
    g.write(str(replicate)+","+str(extinct)+","+str(genome_size)+","+str(complexity)+","+str(num_lethal)+","+str(fraction_lethal)+","+str(info_density)+","+str(prob_lethal)+"\n")

g.close()