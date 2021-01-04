# Head = ['log(L)', 'log(Teff)', 'dist', 'M(Msun)', 'm(Msun)',
#         'Mbol', 'U', 'B', 'V', 'R', 'I', 'J', 'H', 'K', 'L', 'Li', 'M']


import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("./data/cmd_14550.txt",sep=r"\s+", header = None)

datos = datos.astype(float)

x = datos[16]-datos[18]
y = - datos[18]


fig,ax=plt.subplots(figsize=(20,13))
    
ax.plot(x,y, 'o', markersize= 0.6)
ax.set_xlabel('V - I', fontsize= 20)
ax.set_ylabel("-I",  fontsize= 20)
ax.set_facecolor("whitesmoke")
ax.grid(linestyle="--", color="black",linewidth = 0.3)

plt.savefig('./graphs/cmd_Nbajo.png')
