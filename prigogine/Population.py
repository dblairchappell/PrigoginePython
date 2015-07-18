
from numpy import *

class Population:

    #########################

    def __init__(self, populationSize, parentModel):
        self.populationSize = populationSize
        self.timeStepMem = 2
        self.attributes = {}
        self.stateMasks = {}
        #self.updateCode = []
        #self.startstate = ""
        self.stateData = {}
        self.currentStates = None #zeros((1, populationSize))
        #print "populationSize: "
        #print self.populationSize
        #print "currentStates: "
        #print self.currentStates
        self.model = parentModel

    #########################

    def setGlobalDef(self, attributeName, value):
        self.model.globals[attributeName] = value

    #########################

    def getGlobalDef(self, attributeName):
        return self.model.globals[attributeName]

    #########################

    def getFromDef(self, populationName, attributeName, t):
        readIndex = t
        return self.model.populations[populationName].attributes[attributeName][readIndex]

    #########################

    def getDef(self, attributeName, t):
        readIndex = t
        while readIndex >= self.timeStepMem:
            readIndex -= self.timeStepMem
        return self.attributes[attributeName][readIndex]

    #########################

    def updateDef(self, attributeName, newValue, t):
        writeIndex = t + 1
        while writeIndex >= self.timeStepMem:
            writeIndex -= self.timeStepMem
        #print self.attributes["minWage"][writeIndex]
        self.attributes[attributeName][writeIndex] = newValue

    #########################

    def declareAttribute(self, attributeName):
        self.attributes[attributeName] = None

    #########################

    def addState(self, stateName, stateId):
        self.stateData[stateName] = {}
        self.stateData[stateName]["updateCode"] = []
        self.stateData[stateName]["stateId"] = stateId
        #print self.states

    #########################

    # def addUpdateCode(self, codeString):
    #     self.updateCode.append(codeString)

    def addUpdateCode(self, stateName, codeString):
        self.stateData[stateName]["updateCode"].append(codeString)
        #print self.states[stateName]

    #########################

    def updateAttributes(self, attributes, t):

        setglobal = lambda attributeName, value : self.setGlobalDef(attributeName, value)
        update = lambda attributeName, value : self.updateDef(attributeName, value, t)
        get = lambda attributeName : self.getDef(attributeName, t)
        getglobal = lambda attributeName : self.getGlobalDef(attributeName)
        getfrom = lambda populationName, attributeName : self.getFromDef(populationName, attributeName, t)

        for stateKey, data in self.stateData.items():
            print stateKey
            print data["stateId"]
            for codeblock in data["updateCode"]:
                #print data["stateId"]
                code = compile(codeblock, "<string>", "exec")
                exec code in globals(), locals()

    #########################

    # def initialiseAttributes(self, attributes, t):
    #     startstate = lambda statename : self.startstateDef(statename)
    #     init = lambda attributeName, value : self.initDef(attributeName, value)
    #     for codeblock in self.initialisationCode:
    #         code = compile(codeblock, "<string>", "exec")
    #         exec code in globals(), locals()

    #########################


