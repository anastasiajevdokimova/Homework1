import numpy as np
import matplotlib

fail=open("dannie.txt","r")
text=[]
numb=[]
for line in fail:
    n=line.find(",")
    text.append(line[0:n].strip())
    numb.append(int(line[n+1:len(line)].strip()))
fail.close()

title="Данные по ИТ безопасности"
plt.grid(True)
