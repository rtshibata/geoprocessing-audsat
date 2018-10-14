from skimage import img_as_float, img_as_float64  
import numpy as np
import skimage.io as io

def avg_px_val(cut_ndvi_path,cut_ndvi_file):
	img = io.imread(cut_ndvi_path + cut_ndvi_file)
	#print(img.shape)
	img_array = img_as_float64(img).flatten()
	return img_array.mean()
