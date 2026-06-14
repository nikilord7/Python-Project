#Import necessary libraries
import json
import os

#Historymanager class to manage calculation history
class HistoryManager:

    def __init__(self):
        self.Filename = "History.json"

    #Save calculation to history
    def SaveCalculation(self, Calculation):
        History = self.LoadHistory()
        History.append(Calculation)
        
        with open(self.Filename, "w") as File:
            json.dump(History, File, indent=4)

    #Load history from file
    def LoadHistory(self):
        if not os.path.exists(self.Filename):
            return []

        with open(self.Filename, "r") as File:
            return json.load(File)

    #Clear your calculation history
    def ClearHistory(self):
        with open(self.Filename, "w") as File:
            json.dump([], File)