def name_constructor(coding_change):
    type = coding_change.split("	")[9]
    amino = coding_change.split("	")[17]
    #handle the case where there is no amino acid change
    if amino != "-":
        before_amino = amino.split("/")[0]  
        after_amino = amino.split("/")[1]
        amino_position = coding_change.split("	")[16]
        return "p."+before_amino+amino_position+after_amino
    return type

def class_constructor(coding_change):
    variant = coding_change.split("	")[3]
    if "frameshift_variant" in variant or "stop_gained" in variant or "splice" in variant:
        return "LGN"
    if variant == "missense_variant":
        return "M"
    else :
        return "Unknown"

# Read the data from the txt file
with open('Mane_select.txt', 'r') as file:
    lines = file.readlines()

with open('graph.txt', 'w') as file:
        file.write('')

# Loop through each line in the file convert date to graph format
for line in lines:
    name = name_constructor(line)
    position = "chr"+line.split("	")[1].split("-")[0]
    #TODO: handle the different types of mutations
    classname = class_constructor(line)
    result = name+";"+ position + ";" + classname
    #clear previous data
    with open('graph.txt', 'a') as file:
        file.write(result+"\n")


