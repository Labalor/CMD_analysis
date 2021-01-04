# Head = ['log(L)', 'log(Teff)', 'dist', 'M(Msun)', 'm(Msun)',
#         'Mbol', 'U', 'B', 'V', 'R', 'I', 'J', 'H', 'K', 'L', 'Li', 'M']


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb # para hacer el mapa de densidad

datos = pd.read_csv("./data/cmd_Nbajo.txt",sep=r"\s+", header = None)
datos = datos.astype(float)

# cmd - sintetico - aproximacion
#x = datos[16]-datos[18]
#y = - datos[18]

# cmd - mock
x = datos[8]-datos[10]
y = - datos[10]

x = np.array(x)
y = np.array(y)

n = 101

x_grid = np.linspace(-0.5, 4.5, n)
y_grid = np.linspace(-4, 9, n)


density = np.zeros((len(x_grid)-1, len(y_grid)-1))

color_ms = 'red'
color_subG = 'green'
color_RGB = 'yellow'
color_AGB = 'blue'
color_otro = 'black'
color_RC = 'magenta'


RC_stars = 0
RGB_stars = 0
subG_stars = 0

MS_stars_old = 0
subG_stars_old = 0
RGB_stars_old = 0
AGB_stars_old = 0

stars_number = 0

# el -1 y el +1 es para que me haga < del elemeno en posicion [1] de x_grid, y no del [0]

fig,ax=plt.subplots(figsize=(20,13))
for i in range(len(x)):
	for k in range(len(x_grid)-1): 
		if x[i] < x_grid[k+1]:
			for j in range(len(y_grid)-1): 
				if y[i] < y_grid[j+1]:
					
					# Main sequence
					if k == 24 and j == 0:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
						MS_stars_old += 1
					elif k == 25 and j == 0:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
						MS_stars_old += 1
					elif k == 24 and j == 1:
						ax.plot(x[i], y[i], 'o',  color = color_ms,markersize= 0.6)
						MS_stars_old += 1
					elif k == 25 and j == 1:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
						MS_stars_old += 1
					elif k == 24 and j == 2:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
						MS_stars_old += 1
					elif k == 25 and j == 2:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
						MS_stars_old += 1
					elif k == 25 and j == 3:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
						MS_stars_old += 1

					# Sub-Giant
					elif k == 25 and j == 4:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars_old += 1				
					elif k == 26 and j == 4:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars_old += 1	
					elif k == 26 and j == 5:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars_old += 1	
					elif k == 27 and j == 4:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars_old += 1	
					elif k == 27 and j == 5:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars_old += 1	
					elif k == 28 and j == 5:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars_old += 1	
					elif k == 28 and j == 6:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars_old += 1	
					elif k == 29 and j == 6:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars_old += 1	

					# RGB
					elif k == 29 and j == 7:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1					
					elif k == 29 and j == 8:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 30 and j == 8:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 30 and j == 9:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 30 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 30 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 30 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 30 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1					
					elif k == 30 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)	
						RGB_stars_old += 1				
					elif k == 31 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 31 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 31 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 31 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 31 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 31 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 31 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1					
					elif k == 32 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1					
					elif k == 32 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)	
						RGB_stars_old += 1				
					elif k == 32 and j == 22:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 32 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
					elif k == 32 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars_old += 1
				
					# AGB
					elif k == 33 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)	
						AGB_stars_old += 1				
					elif k == 33 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 33 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 33 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 34 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 34 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 34 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 34 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1					
					elif k == 34 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1					
					elif k == 35 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 35 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 36 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 36 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 36 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 37 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 37 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)	
						AGB_stars_old += 1				
					elif k == 37 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1					
					elif k == 38 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1					
					elif k == 38 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 39 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 39 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 40 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 40 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 41 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 43 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1		
					elif k == 44 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1
					elif k == 48 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
						AGB_stars_old += 1

					# JOVEN --------------------------------------
					# MS 
					elif k == 22 and j == 0:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 23 and j == 0:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 22 and j == 1:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 2:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 22 and j == 2:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 3:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 22 and j == 3:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 4:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 21 and j == 4:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 22 and j == 4:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 5:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 5:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 22 and j == 5:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 6:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 6:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 6:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 22 and j == 6:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 19 and j == 7:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 20 and j == 7:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 7:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 22 and j == 7:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 8:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 8:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 8:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 8:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 22 and j == 8:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 9:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 18 and j == 9:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 9:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 9:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 9:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 22 and j == 9:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 19 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 20 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 22 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 20 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 21 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 16 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 16 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 14 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 15 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 16 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 17 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 18 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 19 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 20 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 21 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 13 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 14 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 15 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 16 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 17 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 18 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 19 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 20 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 21 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)
					elif k == 12 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)		
					elif k == 13 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 16 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 12 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 13 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 20 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 21 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 11 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 18 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 21 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 16 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 17 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 21 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 12 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 13 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 14 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 10 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 17 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 18 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms,markersize= 0.6)					
					elif k == 13 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 14 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 15 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 10 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 13 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 20 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 8 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 15 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 16 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 17 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 20 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 11 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 14 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 17 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 18 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 19 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 9 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 10 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 17 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 18 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 19 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 13 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)	
					elif k == 16 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)				
					elif k == 7 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 14 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 15 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 16 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 13 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 14 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 15 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 13 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 14 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 15 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 7 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 14 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 6 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 13 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 6 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 7 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 9 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 13 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 6 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 9 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 9 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 10 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 9 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 10 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)					
					elif k == 11 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 43:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 44:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 45:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 45:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 45:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 45:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 45:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 45:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 45:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 45:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 46:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 46:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 46:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 46:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)		
					elif k == 9 and j == 46:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 10 and j == 46:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 11 and j == 46:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 12 and j == 46:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 47:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 47:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 47:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 47:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 47:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 48:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 48:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 48:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 48:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 48:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 49:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 49:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 49:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 49:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 49:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 50:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 50:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 50:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 50:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 50:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 51:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 51:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 51:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 51:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 51:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 52:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 52:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 52:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 52:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 52:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 53:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 53:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 53:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 53:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 53:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 54:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 54:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 54:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 54:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 54:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 55:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 55:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 55:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 55:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 55:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 56:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 56:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 56:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 56:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 56:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 57:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 57:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 57:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 57:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 57:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 4 and j == 58:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 5 and j == 58:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 6 and j == 58:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 7 and j == 58:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)
					elif k == 8 and j == 58:
						ax.plot(x[i], y[i], 'o', color = color_ms, markersize= 0.6)

					# Sub-Giant
					elif k == 22 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 22 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 22 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 22 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 22 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 22 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 22 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 22 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 22 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 22 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 22 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 22 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1					
					elif k == 22 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 22 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 22 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 23 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 23 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 23 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 23 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 23 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 23 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 23 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 24 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 24 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 24 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 24 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 24 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 24 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 24 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 24 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 24 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 24 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 24 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 24 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 24 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 24 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 24 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 25 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 25 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 25 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 25 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 25 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 25 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 25 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 25 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 25 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 25 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 25 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 25 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 25 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 25 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 25 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 25 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 26 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 26 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 26 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 26 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 26 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 26 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 26 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 26 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 27 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 27 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 27 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 27 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 27 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 27 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 27 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 27 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 27 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 10:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 28 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 28 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1	
					elif k == 28 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 28 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 28 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)	
						subG_stars += 1
					elif k == 28 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1
					elif k == 28 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_subG, markersize= 0.6)
						subG_stars += 1

					# RGB
					elif k == 29 and j == 11:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1					
					elif k == 29 and j == 12:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 13:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 14:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 15:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 16:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 18:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)	
						RGB_stars += 1				
					elif k == 29 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1					
					elif k == 29 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 22:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 29 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1					
					elif k == 29 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1	
					elif k == 30 and j == 17:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1					
					elif k == 30 and j == 18:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 30 and j == 19:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 30 and j == 20:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 30 and j == 21:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1					
					elif k == 30 and j == 22:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 30 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 30 and j == 24:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 30 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)	
						RGB_stars += 1				
					elif k == 30 and j == 26:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 30 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 30 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 31 and j == 23:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)	
						RGB_stars += 1				
					elif k == 31 and j == 24:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 31 and j == 25:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 31 and j == 26:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 31 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)	
						RGB_stars += 1				
					elif k == 31 and j == 28:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 31 and j == 29:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 31 and j == 30:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 31 and j == 31:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 32 and j == 27:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 32 and j == 28:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)
						RGB_stars += 1					
					elif k == 32 and j == 29:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars += 1
					elif k == 32 and j == 30:
						ax.plot(x[i], y[i], 'o', color = color_RGB, markersize= 0.6)	
						RGB_stars += 1				
					elif k == 32 and j == 31:
						ax.plot(x[i], y[i], 'o',color = color_RGB, markersize= 0.6)
						RGB_stars += 1

					# AGB
					elif k == 32 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 33 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 33 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 33 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 33 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 33 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 34 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 34 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 34 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 34 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 34 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 34 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 35 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 35 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 35 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 35 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 35 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 36 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 36 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 36 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 36 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 36 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)

					elif k == 37 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 37 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 37 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 37 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 38 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 38 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 38 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 38 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)						
					elif k == 39 and j == 39:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 39 and j == 40:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)					
					elif k == 39 and j == 41:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)
					elif k == 39 and j == 42:
						ax.plot(x[i], y[i], 'o', color = color_AGB, markersize= 0.6)						

					# RC
					elif k == 30 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1				
					elif k == 30 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)
						RC_stars += 1
					elif k == 30 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1	
					elif k == 30 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1			
					elif k == 31 and j == 32:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1				
					elif k == 31 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)
						RC_stars += 1
					elif k == 31 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1	
					elif k == 31 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1
					elif k == 31 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1
					elif k == 32 and j == 33:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)
						RC_stars += 1
					elif k == 32 and j == 34:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)
						RC_stars += 1
					elif k == 32 and j == 35:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)
						RC_stars += 1
					elif k == 32 and j == 36:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1	
					elif k == 32 and j == 37:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1
					elif k == 32 and j == 38:
						ax.plot(x[i], y[i], 'o', color = color_RC, markersize= 0.6)	
						RC_stars += 1

					else:
						ax.plot(x[i], y[i], 'ko', markersize= 0.6)	
					
					
					print('x_grid', k)
					print('y_grid', j)
					print(round(x[i], 3), round(y[i], 3))
					

					density[k][j] += 1
					stars_number += 1


					break
			break	
print('brote joven')
print('RC_stars', RC_stars)
print('RGB_stars', RGB_stars)
print('subG_stars', subG_stars)

print('brote antiguo')
print('MS_stars_old', MS_stars_old)
print('subG_stars_old', subG_stars_old)
print('RGB_stars_old', RGB_stars_old)
print('AGB_stars_old', AGB_stars_old)

total_start_old = MS_stars_old + subG_stars_old + RGB_stars_old + AGB_stars_old
print('total_start_old', total_start_old)
print('MS_stars_old porcentaje', MS_stars_old * 100 / total_start_old)
print('subG_stars_old porcentaje', subG_stars_old * 100 / total_start_old)
print('RGB_stars_old porcentaje', RGB_stars_old * 100 / total_start_old)
print('AGB_stars_old porcentaje', AGB_stars_old * 100 / total_start_old)


print('stars', stars_number)
print('total_start_old porcentaje', total_start_old * 100 / stars_number)
print('total_start_young porcentaje', 100 - total_start_old * 100 / stars_number)
print('len(x)', len(x))




ax.set_xlabel('V - I', fontsize= 20)
ax.set_ylabel("- I", fontsize= 20)
ax.set_title('CMD - Nbajo - Brote jóven', fontsize= 20)
ax.set_facecolor("whitesmoke")
ax.grid(linestyle="--", color="black",linewidth = 0.3)
plt.savefig('./graphs/partes_joven.png')

fig,ax=plt.subplots(figsize=(20,13))
manzanas = [MS_stars_old, subG_stars_old, RGB_stars_old, AGB_stars_old]
nombres = ["MS","subG","RGB","AGB"]
colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%", colors=colores)
plt.axis("equal")
plt.savefig('./graphs/pie_old.png')


#print('x_grid', x_grid)
#print('y_grid', y_grid)

'''
fig,ax=plt.subplots(figsize=(20,13))
heat_map = sb.heatmap(density, annot = True, cmap="YlGnBu", cbar_kws={'label': 'Número de estrellas', 'orientation': 'horizontal'})
# annot = True, para poner el número de estrellas en el diagrama de densidad
ax.set_xlabel('V - I', fontsize= 20)
ax.set_ylabel("- I", fontsize= 20)
ax.set_title('Mapa de densidad de estrellas del CMD', fontsize= 20)
plt.savefig('./graphs/density_01.png')
'''

fig,ax=plt.subplots(figsize=(20,13))
ax.plot(x, y, 'o', markersize= 0.6)

for i in range(len(x_grid)):
	ax.hlines(y_grid[i], -0.5, 4.5, colors = 'k', linestyle = 'solid')
	ax.vlines(x_grid[i], -4, 9, colors = 'k', linestyle = 'solid')

ax.set_ylabel('V - I', fontsize= 20)
ax.set_xlabel("-I", fontsize= 20)
ax.set_title('CMD con malla ', fontsize= 20)
ax.set_facecolor("whitesmoke")
ax.grid(linestyle="--", color="black",linewidth = 0.3)

plt.savefig('./graphs/data_and_grid_01.png')
# plt.show()

#plt.savefig('./graphs/regions_diagram_Nbajo.png')


'''
fig,ax=plt.subplots(figsize=(20,13))


for item in range(len(x)):
	if x[item] < x_grid[1]:
		k = 1
		for i in range(len(y_grid)):
			if y[item] < y_grid[k]:
				ax.plot(x[item], y[item], 'ro', markersize= 0.6)
				break
			else:
				k += 1

		if y[item] < -1:
			ax.plot(x[item], y[item], 'ro', markersize= 0.6)
		elif y[item] > -1:
			ax.plot(x[item], y[item], 'bo', markersize= 0.6)	 
	elif x[item] < x_grid[2]:
		if y[item] < -1:
			ax.plot(x[item], y[item], 'bo', markersize= 0.6)
		elif y[item] > -1:
			ax.plot(x[item], y[item], 'ro', markersize= 0.6)
	elif x[item] < x_grid[3]:
		if y[item] < -1:
			ax.plot(x[item], y[item], 'ro', markersize= 0.6)
		elif y[item] > -1:
			ax.plot(x[item], y[item], 'bo', markersize= 0.6)
	elif x[item] < x_grid[4]:
		if y[item] < -1:
			ax.plot(x[item], y[item], 'bo', markersize= 0.6)
		elif y[item] > -1:
			ax.plot(x[item], y[item], 'ro', markersize= 0.6)
	elif x[item] < x_grid[5]:
		if y[item] < -1:
			ax.plot(x[item], y[item], 'ro', markersize= 0.6)
		elif y[item] > -1:
			ax.plot(x[item], y[item], 'bo', markersize= 0.6)
	elif x[item] < x_grid[6]:
		if y[item] < -1:
			ax.plot(x[item], y[item], 'bo', markersize= 0.6)
		elif y[item] > -1:
			ax.plot(x[item], y[item], 'ro', markersize= 0.6)
	elif x[item] < x_grid[7]:
		if y[item] < -1:
			ax.plot(x[item], y[item], 'ro', markersize= 0.6)
		elif y[item] > -1:
			ax.plot(x[item], y[item], 'bo', markersize= 0.6)
	elif x[item] < x_grid[8]:
		if y[item] < -1:
			ax.plot(x[item], y[item], 'bo', markersize= 0.6)
		elif y[item] > -1:
			ax.plot(x[item], y[item], 'ro', markersize= 0.6)


    
ax.set_xlabel('V - I', fontsize= 20)
ax.set_ylabel("-I")
ax.set_facecolor("whitesmoke")
ax.grid(linestyle="--", color="black",linewidth = 0.3)

plt.savefig('./graphs/regions_diagram_Nbajo.png')
'''

'''
x = [1, 2.3, 3, 4.2, 5.1, 1.3, 2.3, 3, 4.4, 5.5, 0.5, 3.1, 5.2]
y = [0.15, 2.47, 1.75, 3.22, 5.01, 1.4, 2.10, 1.95, 3.02, 5.52, 1.7, 3.8, 4.2]
malla_x = [0, 2, 4, 6]
malla_y = [0, 2, 4, 6]

density = np.zeros((len(malla_x)-1, len(malla_x)-1))

for i in range(len(x)):
	for k in range(len(malla_x)-1):
		if x[i] < malla_x[k+1]:
			for j in range(len(malla_y)-1):
				if y[i] < malla_y[j+1]:
					print('x_grid', k)
					print('y_grid', j)
					print(round(x[i], 3), round(y[i], 3))	
					density[k][j] += 1


								
					break
			break	


heat_map = sb.heatmap(density, cmap="YlGnBu", annot = True, cbar_kws={'label': 'My Colorbar', 'orientation': 'horizontal'})

plt.savefig('./graphs/01.png')

fig,ax=plt.subplots(figsize=(20,13))
ax.plot(x, y, 'yo', markersize= 14.6)


for i in range(len(malla_x)):
	ax.hlines(malla_x[i], 0, 6, colors = 'k', linestyle = 'solid')
	ax.vlines(malla_y[i], 0, 6, colors = 'k', linestyle = 'solid')

ax.set_xlabel('V - I', fontsize= 20)
ax.set_ylabel("-I")
ax.set_facecolor("whitesmoke")
ax.grid(linestyle="--", color="black",linewidth = 0.3)

plt.savefig('./graphs/02.png')

'''

'''
	if x[i] < 2:
		for j in range(len(malla_y)):
			if y[i] < malla_y[j]:
				print(j)

				print(x[i], y[i])
				break


	elif x[i] < 4:
		for j in range(len(malla_y)):
			if y[i] < malla_y[j]:
				print(j)

				print(x[i], y[i])
				break	

	elif x[i] <= 5:
		for j in range(len(malla_y)):
			if y[i] < malla_y[j]:
				print(j)

				print(x[i], y[i])
				break	
'''

