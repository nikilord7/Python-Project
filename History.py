import json
import os


class HistoryManager:

    def __init__(self):
        self.Filename = "History.json"

    def SaveCalculation(self, Calculation):
        History = self.LoadHistory()
        History.append(Calculation)
        with open(self.Filename, "w") as File:
            json.dump(History, File, indent=4)

    def LoadHistory(self):
        if not os.path.exists(self.Filename):
            return []

        with open(self.Filename, "r") as File:
            return json.load(File)

    def ClearHistory(self):
        with open(self.Filename, "w") as File:
            json.dump([], File)