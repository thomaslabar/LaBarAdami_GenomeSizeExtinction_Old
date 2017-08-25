import copy
import numpy as np
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

g=open("data.csv","wb")
g.write("Treatment,Replicate,Extinction,FinalGenomeSize\n")

for t in ["repeat","lowmut","fixedmut","notraits","fixedlength"]:
    
    if t == "repeat":
        rep_range = range(11631,11731)
    elif t == "fixedmut":
        rep_range = range(18411,18511)
    elif t == "lowmut":
        rep_range = range(15458,15558)
    elif t == "notraits":
        rep_range = range(19565,19665)
    elif t == "fixedlength":
        rep_range = range(13476,13576)
        
    for replicate in rep_range:
        
        try:
            dom_data = GetFileLines("data_"+str(t)+"/replicate_"+str(replicate)+"/dominant.dat")
        except:
            print("Dominant File Missing",t,replicate)
            continue
                    
        final_dom_line = dom_data[-1].split(" ")
        final_genome_size = str(final_dom_line[5])
        
        extinction = 1
        rep_files = os.listdir("data_"+str(t)+"/replicate_"+str(replicate))
        for f in rep_files:
            if "detail" in f:
                extinction = 0        
        
        g.write(t+","+str(replicate)+","+str(extinction)+","+str(final_genome_size)+"\n")
    
    print(t)

g.close()