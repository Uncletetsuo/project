import csv 

def read_csv(path): #Declaring the function with the path as a parameter 
    with open(path, 'r') as csvfile: #opening the file and granting this code the permission to read the file (also the file will close 
        # at the end of the block) and saving this in a var called csvfile 
        reader = csv.reader(csvfile, delimiter=',') # we imported the CSV module and we are using the method reader to read our csvfile 
        # and giving it structure with our delimiter, all inside the reader variable
        header = next(reader) # we are storing the first line of the Csvfile in header
        data = [] # we create an empty list
        for row in reader: #now for every line in the csvfile 
            iterable = zip(header, row) # we are going to pair each individual title with their respective data for every row in the Csvfile
            country_dict= { key: value for key, value in iterable} # we are going to give it a dictionary structure 
            data.append(country_dict) # and each dictionary is going to be appended to the data list
        return data   # with the return statement I have to do this ---------------------
#   This is due to the fact that i'm not printing anything in the  Function             |
#    And I have to save the returned value                                              |
if __name__ == '__main__':                             #                                |
    data = read_csv('/home/fercs/Documents/python_lambda/app/data.csv')   #<------------
    print(data[12]) # the only way to put the data on the terminal is giving it a list index, because it's a lot easier
    # to navigate between a sea of data with the list methods, so there's a lot of advantage with using a dictionary within a list    