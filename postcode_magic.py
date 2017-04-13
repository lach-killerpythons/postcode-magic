#(snakepit) env= python3.5
#CONVERTS ANY AUSTRALIAN POSTCODE INTO SUBBURB AND GEOLOCATION
import pandas as pd #FOR CSV IMPORT

#REFERENCE FILES
australia_postcodes = pd.DataFrame(pd.read_csv('NSW_pcs.csv')) #change file to aus_pcs.csv for all australia
pc_lib = australia_postcodes['postcode']
sub_lib=australia_postcodes[' suburb']
lat_lib=australia_postcodes['latitude']
long_lib=australia_postcodes['longitude']
combined_lib=[]

#INPUT LIST FILES - this can be any csv or list
demographics= pd.DataFrame(pd.read_csv('imput_postcodes.csv')) #CHANGE THIS TO FILE NAME
input_listA = demographics['postcode'] #AND THIS TO COLUMN NAME WITH POSTCODES (as int)
input_listA=list(input_listA)
example_list=[2000,2020,4022] #not used

#JOINER AND CLEANER FUNCTIONS
n=0
for i in sub_lib:
    combine=",".join([str(i).strip(" ''"),str(lat_lib[n]), str(long_lib[n])])
    combined_lib.append(combine)
    n+=1
"""
def fix_cols(input_list):
    new_list = []
    for word in input_list:
        splited = list([c for c in word])
        del splited[0],splited[0], splited[len(splited)-1] #delete first character twice then last
        output = "".join(splited)
        new_list.append(output)
    return new_list
"""

def fix_numbs(input_list):
    new_list = []
    for word in input_list:
        splited = list([c for c in word])
        del splited[0], splited[len(splited)-1] #delete first character twice then last
        output = int("".join(splited))
        new_list.append(output)
    return new_list


#sub_fix = fix_cols(sub_lib)
pc_fix = fix_numbs(pc_lib)
postcode_dict = dict(zip(pc_fix,combined_lib))
output_list = []

def new_sub_list(N):
    n_list = list(N) #create destructable list
    nn=1
    while len(n_list) > 0:
        try:
            name = postcode_dict[n_list[0]]
            output_list.append(name)
        except:
            #print("Unknown")
            output_list.append("Unknown,,")
        print(str(nn) + "/" + str(len(N)))
        del n_list[0]
        nn+=1



new_sub_list(input_listA)  #POPULATE DETAILS CAN CHANGE TO ANY OTHER LIST OF POSTCODES

#now save the output
output_file = open("postcode_output_file.csv", "w") #name for output file
output_file.write("suburb, latitude, longitude,\n")
for i in output_list:
    output_file.write(str(i)+",\n")
output_file.close() #MUST close the file!


