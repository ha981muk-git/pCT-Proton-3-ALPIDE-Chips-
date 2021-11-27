
#Importing different necessary python package at the beginning

from matplotlib import pyplot
import  pandas as pd

#Initializing a new variable for the path
filename = './../../data/raw/pctdata.csv'

#Reading the pctdata.csv file
df = pd.read_csv(filename, low_memory=False)

print("**********************************************************\n")
# first fews dataprint(df.head())
print("\n"*2) #new line

print(type("The Data type of pctdata is " + str(filename))) #data type of the file is in string
print("\n"*2) #new line#

# short description over the pctdata file
print(df.describe().T)
print("\n"*2) #new line

# crossponding rows and columns of pctdata file
print('The pctdata file has the shape of ' + str(df.shape))

df1 = df.copy() # Just coping dataset for other file

#histogram of pctdata

df.hist()
pyplot.show()


# convert all number into integer
def convert_to_float(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        if len(comma_separated_parts[i]) > 6:
            return None
        if i != 0 and len(comma_separated_parts[i]) != 6:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    except ValueError:
        return None


def row_to_list(row):
    row = row.rstrip("\n")
    separated_entries = row.split(",")
    if len(separated_entries) == 5 and "" not in separated_entries:
        return separated_entries
    return None

# process reads raw data cleans.It writes clean data in one file and rows with error in another file.

def preprocess(raw_data_file_path, clean_data_file_path):

 with open(raw_data_file_path, "r") as input_file:
        rows = input_file.readlines()
        with open(clean_data_file_path, "w") as output_file:
          for row in rows:
            row_as_list = row_to_list(row)
            if row_as_list is None:
                continue

            id_plane     = convert_to_float(row_as_list[0])
            id_x         = convert_to_float(row_as_list[1])
            id_y         = convert_to_float(row_as_list[2])
            i_event      = convert_to_float(row_as_list[3])
            i_time_stamp = convert_to_float(row_as_list[4])
            if id_plane is None or id_x is None or id_y is None or i_event is None or i_time_stamp is None :
                continue
            output_file.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(id_plane, id_x, id_y, i_event, i_time_stamp))