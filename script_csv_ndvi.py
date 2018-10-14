#!/usr/bin/python
import pandas as pd
import numpy as np
import avgNDVI
import os

'''
Assuming that all NDVI files are already there at the right directory

'''
path_ndvi = "./DESAFIO_PYTHON/IMAGENS_PLANET/ndvi_imgs/"

header_line = ["Valor medio de NDVI","Imagem Clipada"]

all_imgs = []
for fname in os.listdir(path_ndvi):
	if fname.endswith("_RED.tif"):
		os.remove(fname)		
		continue
	elif fname.endswith("_NIR.tif"):
		os.remove(fname)
		continue
	elif fname.endswith(".xml"):
		continue
	elif fname.endswith("__CLIPPED_ndvi.tif"): 
		all_imgs.append(fname)
	else:
		continue

avg_values=np.array([])
img_name=np.array([])

for ndvi in all_imgs: 
	new_avg= avgNDVI.avg_px_val(path_ndvi,ndvi)

	avg_values= np.append(avg_values,new_avg)
	img_name=np.append(img_name,ndvi) 

new_data=np.array(	[avg_values, 
					img_name, 
					]
).transpose()

print(new_data.shape)

data = pd.DataFrame(data=new_data, columns = [
					header_line[0],
					header_line[1],
					])

data.to_csv("ndvi.csv", sep=',')
