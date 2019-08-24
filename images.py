import rawpy
import imageio

for i in range(33):
    raw = rawpy.imread('HG/'+str(i)+'.CR2')
    rgb = raw.postprocess()
    imageio.imsave('HG/'+str(i)+'.tiff', rgb)
