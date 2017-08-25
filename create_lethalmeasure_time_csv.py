import copy

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


rep_range = range(17885,17905)

genome_size_data = {}

for replicate in rep_range:
    
            
    dominant_data = GetFileLines("data_lethalmeasure/replicate_"+str(replicate)+"/dominant.dat")
    genome_size_data[replicate] = []
    
    for line in dominant_data:
        
        if len(line) != 0 and not line.startswith("#"):
            
            temp = line.split(" ")
            genome_size = str(temp[5])
            genome_size_data[replicate].extend([genome_size])
            

g=open("data_lethalmeasure_time.csv","wb")

g.write("Replicate,Generation,DominantGenomeSize,Extinct\n")

for replicate in rep_range:
    
    lineage_length = len(genome_size_data[replicate])
    
    if lineage_length != 251:
        extinct = 1
    else:
        extinct = 0
    
    for depth in range(lineage_length):

        gs = genome_size_data[replicate][depth]
        
        g.write(str(replicate)+","+str(int(depth)*1000)+","+str(gs)+","+str(extinct)+"\n")


g.close()
