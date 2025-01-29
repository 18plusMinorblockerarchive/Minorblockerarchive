import matplotlib.pyplot as plt
import pandas as pd

class Instagram_Grapher:
    def __init__(self):
        self.Ploter()
        
    def CreatePlot(self):
        self.CheckCSV()
        if self.CheckCSV() == True:
            self.df.plot()
            plt.show()
        else:
            print('No CSV SCRIPT FILE FOUND')
        
    def Ploter(self):
        self.CheckUp2Date_CSV()
            
    def CheckCSV(self):
        self.df = pd.read_csv('SRC\18+MBArchiver\CSV\twitter\Twitter.csv')
        if self.df == None:
            return False
        else:
            return True

    def CheckUp2Date_CSV(self):
        try:    
            if self.CheckCSV() == True:
                self.Ploter()
                return True
            else:
                self.DeleteOld()
                return False
        except:
            print("FATAL: CSV SCRIPT NOT FOUND")
        
    def DeleteOld(self):
        if self.CheckUp2Date_CSV() == True:
            self.df.to_csv('SRC\18+MBArchiver\CSV\instagram\Instagram.csv', index=False)
            self.df = pd.read_csv('SRC\18+MBArchiver\CSV\instagram\Instagram.csv')
            print('OLD CSV SCRIPT FILE DELETED')
        else:
            print('No CSV SCRIPT FILE FOUND')