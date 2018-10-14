import numpy as np
import skimage.io as io
from skimage import data, img_as_float, img_as_float64   
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import ogr
import gdal

class GenerateNDVI:
	def __init__(self,path,img_ex,shp_path,shp_file):
		self.path = path
		self.img_ex = img_ex
		self.shp_path = shp_path
		self.shp_file = shp_file
		self.ndvi_img = []
		self.clip_file = []
		
	def get_raw_NDVIimg(self):
		print ("ndvi img: {}".format(self.img_ex))
		return self.ndvi_img
	
	def get_clip_from_shp(self):
		return self.clip_file

	def generate_raw_ndvi(self):
		img = io.imread(self.path + self.img_ex)


		dimx, dimy = img[:,:,2].shape
		fraction = 0.01
		noise = fraction * np.ones((dimx,dimy),dtype=float)

		red = img_as_float64(img[:,:,2]) + noise
		nir = img_as_float64(img[:,:,3]) + noise
		#ndvi_out = np.where(((nir-red)==0)&((nir+red)==0),0,(nir-red)/(nir+red))

		#print red
		#print nir
		#plt.figure(0)
		#plt.imshow(nir,cmap="gray")
		#plt.title("nir")
		#plt.show()

		self.ndvi_img=(nir-red)/(nir+red)
		#self.ndvi_img =  rgb2gray(ndvi_out)

		new_dir = self.path + "ndvi_imgs/"		
		#io.imsave(new_dir + self.img_ex.replace('.tif', '') + "_RED.tif",red)
		#io.imsave(new_dir + self.img_ex.replace('.tif', '') + "_NIR.tif",nir)

	def getParametersFromSrcImg(self):
		raster_ds = gdal.Open(self.path+self.img_ex,gdal.GA_ReadOnly)
		return raster_ds.RasterXSize, raster_ds.RasterYSize, raster_ds.GetGeoTransform(),raster_ds.GetProjectionRef()

	### assuming that the shapefile has only 1 layer ###
	def rasterization_clip_from_shp(self,ndvi_path,ndvi_file,fileformat):
		shapefile = ogr.Open(self.shp_path + self.shp_file)

		layer = shapefile.GetLayer()
		raster_source = gdal.Open(ndvi_path+ndvi_file,gdal.GA_ReadOnly)

		n_col,n_row,ext,proj = self.getParametersFromSrcImg()
		#print(ext)
		#print(proj)
		#print(n_row,n_col)	

		driver = gdal.GetDriverByName(fileformat)
		out_raster_name = ndvi_path+"__CLIP__"+ndvi_file
		out_raster = driver.Create(out_raster_name,n_col,n_row,1,gdal.GDT_Int32)

		out_raster.SetProjection(proj)
		out_raster.SetGeoTransform(ext)

		b = out_raster.GetRasterBand(1)
		b.Fill(0) 	
		print("Rasterizing image {}".format(ndvi_file))
		gdal.RasterizeLayer(out_raster,  
				                     [1], 
				                     layer, 
				                     None, None,  
				                    [1],
									['ALL_TOUCHED=TRUE'], 
				                     )
	
		out_raster = None
		raster_source = None
		self.clip_file = out_raster_name


