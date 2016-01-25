import json
import os
import re
from pprint import pprint

#############################################################################

#Prints the source files that were tested, returns the test's that were run
def getSourceFiles(jsonFile):
    with open(jsonFile) as json_data:
        d = json.load(json_data)
        json_data.close()
        json_data.close()
        c = d[1]['testUrl'] 
        e = 0
        for number, val in enumerate(d):
            print d[number]['sourceFile']
            print '\n'
	    if d[number]['testUrl'] != d[1]['testUrl']:
	        e = e + 1
        return c

#Gets the lines covered of a particular source file from a JSON
def getLCOV(jsonFile, jsFile):
    lineCov = []

    with open(jsonFile) as json_data:
	d = json.load(json_data)
	json_data.close()
	json_data.close()
	for number, val in enumerate(d):
	    if jsFile in d[number]['sourceFile']:
		lineCov.append(d[number]['covered'])

    return lineCov

#Determines if a line number was covered or not
def lineExists(lineCov, lineNumber):
    for file in lineCov:
	for line in file:
	    if lineNumber == line:
		return 1
    return 0

#Gets the methods that were covered
def getMethods(jsFile, lineCov):
    methods = []
    lineOffset = []

    with open(jsFile, "r") as d:
	searchLines = d.readlines();
	i = 1
        for line in searchLines:
	    if "function" in line and lineExists(lineCov, i):
	        print i, line
	    i = i + 1	

#Search through a JSON file to find out if a source file, jsFile, exists there
def searchJSON(jsonFile, jsFile):	
    with open(jsonFile) as json_data:		
	d = json.load(json_data)
	json_data.close()
	json_data.close()
	for number, val in enumerate(d):
	    if jsFile in d[number]['sourceFile']: #Changing the return to appending to a list will find multiple files
		return jsonFile
	return "default"			  #Remove this if that is the case

#Gets the name of the JSON which holds information of the tested file
def getJSON(jsFile):
    for file in os.listdir('.'): 				#The directory containing SourcesAndMethods.py
	if file != 'SourcesAndMethods.py' and file != 'SimpleTest.js' :
	    if searchJSON(file, jsFile) != "default" :
		return file
    return 'DoesNotExistInAnyJson'	    

#############################################################################

L = []

#Go through the JSONs and print the source files that were touched and get the test names
for file in os.listdir('.'):					#The directory containing SourcesAndMethods.py
    if file != 'SourcesAndMethods.py' and file != 'SimpleTest.js' :
        L.append(getSourceFiles(file))

#Print the test names
print 'Test Names: BEGINS HERE---------------------------------------------\n'
for strings in L:
    print strings
    print '\n'

jsTestedFile = 'SimpleTest.js'					#The js file to search for methods

#Get the JSON for jsTestedFile
jsonFile = getJSON(jsTestedFile)

#Get the lines covered from the JSON for jsTestedFile
lineCov = getLCOV(jsonFile, jsTestedFile)

#Print the lines covered
print "%s" % (lineCov)

#Print the methods that were covered
getMethods('SimpleTest.js', lineCov)
