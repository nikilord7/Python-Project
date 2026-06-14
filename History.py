#Import necessary libraries
import json
import os

#Historymanager class to manage calculation history
class HistoryManager:

    def __init__(self):
        self.FileName = "History.json"

    #Save calculation to history
    def SaveCalculation(self, Calculation):
        History = self.LoadHistory()
        History.append(Calculation)
        
        with open(self.FileName, "w") as File:
            json.dump(History, File, indent=4)

    #Load history from file
    def LoadHistory(self):
        if not os.path.exists(self.FileName):
            return []

        try:
            with open(self.FileName, "r") as File:
                return json.load(File)
        except json.JSONDecodeError:
            return []

    #Clear your calculation history
    def ClearHistory(self):
        with open(self.FileName, "w") as File:
            json.dump([], File)