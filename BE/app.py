print( 'Welcome to the BackEnd Code' )

# Code to Read JSON File
with open('Data\companies.json') as jsonFile:
    fileData = jsonFile.read()
    print( 'JSON Data is : \n ')
    print( fileData )
