import subprocess
import os
import pandas as pd


def take_input(ageinput):
    while True:
        try:
            ageinput=int(ageinput)
            return ageinput
        except:
               ageinput = input("Please Enter Age Number Value: ")

output=take_input(input("Please Enter Age Number Value: "))
print(output)

with open('variablpass.txt', 'w') as varPass: # creates the file
    varPass.write(str(output))
varPass.close()

subprocess.Popen([r"C:\\Program Files\\R\\R-4.2.0\\bin\\Rscript", "filereader.R"])

df=pd.read_excel("age_filter.xlsx")

print(df)