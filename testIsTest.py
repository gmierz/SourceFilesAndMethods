#isTest() tester:
#Finds all test files and source file url's in a given directory

import SourcesAndMethods
import json
import os
import re

#Holds a directory of JSON files
class JSONFileDirectory:
    directory = ''            #Direcctory containing JSON's
    jsonFiles = []            #list of JSON files
    touchedFiles = []         #list of JSONFile objects containing information on each
    
    def __init__(self, directory):
         self.directory = directory
    
    def getJSONFiles(self):
        for file in os.listdir('./' + self.directory):                 #For each file in the given directory
            self.jsonFiles.append(file)                                #Keep the file name
            self.touchedFiles.append(JSONFile(file, self.directory))   #Create a new JSONFile for the given JSON
            

            
#Holds a JSON file with information about the file that were tested
class JSONFile:
    directory = ''           #Directory containing JSON file
    jsonFile = ""            #JSON file name
    files = []               #Entire list of contained touched files
    sourceFiles = []         #List of source files
    testFiles = []           #List of ignored test files
    
    def __init__(self, jsonFile, directory):
        self.jsonFile = jsonFile 
        self.directory = directory
        self.files = SourcesAndMethods.getSourceFiles(self.directory, self.jsonFile)     #Get the files touched into a list
        self.fillFileTypes()                                                #Seperate the files based on whether or not
                                                                            #it's a test
    
    def fillFileTypes(self):
        for resourceFile in self.files:                                     #For each file touched
            if SourcesAndMethods.isTest(resourceFile):                                   #If it is a test
                self.testFiles.append(resourceFile)                         #Reject it and place into testFiles
            else:
                self.sourceFiles.append(resourceFile)                       #Otherwise, accept it and place into sourceFiles

                
                
'''
Will be used in the future
'''

class SourceFile:
    uri = ""          #Name of file       
    jsonFile = []     #Occurs in these files
    lineCov = []      #Lines covered in this file
    methods = []      #methods covered in this file
    
    def __init__(self, uri, jsonFile):
        self.uri = uri
        self.jsonFile.append(jsonFile)
        self.lineCov.append(SourcesAndMethods.lineCov(uri, jsonFile))
        
  
#########################################################################    

#Pass directory containing only JSON files
jsFD = JSONFileDirectory('JSON/')

#Load jsFD with all information on each JSON file
jsFD.getJSONFiles()

#Print source files that were touched
for jsFile in jsFD.touchedFiles:
    for file in jsFile.sourceFiles:
        print file + '\n'
