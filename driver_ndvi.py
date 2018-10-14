import numpy as np
import skimage.io as io
import generateNDVI
import os
import matplotlib.pyplot as plt
import avgNDVI


path = "./DESAFIO_PYTHON/IMAGENS_PLANET/"
new_dir = path + "ndvi_imgs/"

geodata_path = "./mygeodata/"
geodata_file= "gleba01-polygon.shp"

img_ext= "tif"

all_imgs = []
#clean any old files
for fname in os.listdir(path):
	if fname.endswith("_RED.tif"):
		os.remove(fname)		
		continue
	elif fname.endswith("_NIR.tif"):
		os.remove(fname)
		continue
	elif fname.endswith(".xml"):
		continue
	elif fname.endswith(".tif"): 
		all_imgs.append(fname)
	else:
		continue

i=1
for img_ex in all_imgs:
	img_name = img_ex.replace('.tif', '') 
	print("generating NDVI of the img: ",img_ex,"...")
	inst_genNDVI = generateNDVI.GenerateNDVI(path,img_ex,geodata_path,geodata_file)
	inst_genNDVI.generate_raw_ndvi()
	ndvi_img = inst_genNDVI.get_raw_NDVIimg()

	#plt.figure(0)
	#plt.imshow(ndvi_img, cmap="gray")
	#plt.show()
	print(ndvi_img.shape)
	print("saving NDVI of the img ",img_ex,"...")
	new_name=new_dir + img_name + "_ndvi.tif"
	io.imsave(new_name,ndvi_img)

	#read image testing...
	#img = io.imread(new_dir + img_name + "_ndvi.tif")
	#plt.figure(0)
	#plt.imshow(img, cmap="Greys")
	#plt.show()

	inst_genNDVI.rasterization_clip_from_shp(new_dir,img_name+"_ndvi.tif","GTiff")
	clip_path_file =inst_genNDVI.get_clip_from_shp()
	print(clip_path_file)

	clip_img = io.imread(clip_path_file)
	#plt.figure(0)
	#plt.imshow(clip_img, cmap="Greys")
	#plt.show()

	#using the clip as mask for the ndvi image
	cut_ndvi_img = np.where(clip_img==0,0,ndvi_img)
	io.imsave(new_dir + img_name + "__CLIPPED_ndvi.tif",cut_ndvi_img)
	#plt.figure(0)
	#plt.imshow(cut_ndvi_img, cmap="Greys")
	#plt.show()

	float_val = avgNDVI.avg_px_val(new_dir,img_name + "__CLIPPED_ndvi.tif")
	print("O valor medio do NDVI da imagem {0} é: {1:.{precision}f}".format(img_name,float_val,precision=5))

	#print(i)
	#i+=1



	inst_genNDVI = None




