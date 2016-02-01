#Helper file for testIsTEst

import json
import os
import re
from pprint import pprint
#############################################################################

#Returns a list of the source files that were tested
def getSourceFiles(directory, jsonFile):
    with open(directory + '/' + jsonFile) as json_data:
        d = json.load(json_data)
        json_data.close()
        c = []
        for number, val in enumerate(d):
            c.append(d[number]['sourceFile'])
        return c

#Gets the lines covered of a particular source file from a JSON
def getLCOV(jsonFile, jsFile):
    lineCov = []

    with open("JSON/" + jsonFile) as json_data:
        d = json.load(json_data)
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

    with open("JSON/" + jsFile, "r") as d:
        searchLines = d.readlines();
        json_data.close();
        i = 1
        for line in searchLines:
            if "function" in line and lineExists(lineCov, i):
                print i, line
	        i = i + 1	

#Search through a JSON file to find out if a source file, jsFile, exists there
def searchJSON(jsonFile, jsFile):	
    with open("JSON/" + jsonFile) as json_data:		
        d = json.load(json_data)
        json_data.close()
        for number, val in enumerate(d):
            if jsFile in d[number]['sourceFile']: #Changing the return to appending to a list will find multiple files
                return jsonFile
	return "default"			  #Remove this if that is the case

#Gets the name of the JSON which holds information of the tested file
def getJSON(jsFile):
    for file in os.listdir('./JSON'):
	    if searchJSON(file, jsFile) != "default" : #Search through json
		    return file    

def isTest(filename):
    testPattern = re.compile(r"browser_.+\.js")
    testPattern1 = re.compile(r"'.'test-.+\.js")
    testPattern2 = re.compile(r".+\.xpi")
    testPattern3 = re.compile(r"(browser|test)_.+\.(xul|html|js|xhtml)")
    testPattern4 = re.compile(r"webapprt_")
    testPattern5 = re.compile(r"browser")
    testPattern6 = re.compile(r"\.test.js")
    testPattern7 = re.compile(r"[tT]est")
    testPattern8 = re.compile(r"[hH]arness")
    #pathPieces = filename.split("/")

    if testPattern.search(filename):
        return 1;
    elif testPattern1.search(filename):
        return 1;
    elif testPattern2.search(filename):
        return 1;
    elif testPattern3.search(filename):
        return 1;
    elif testPattern4.search(filename):
        return 1;
    elif testPattern5.search(filename):
        return 1;
    elif testPattern6.search(filename):
        return 1;
    elif testPattern7.search(filename):
        return 1;
    elif testPattern8.search(filename):
        return 1
    
    return 0;
#############################################################################
