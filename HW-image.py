#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#1
img_a=mpimg.imread('a.jpg')
img_b=mpimg.imread('b.jpg')

img_c = img_a.copy()[:, :, :]

img_c[250:650, 100: 500, :]=img_b

#imgplot = plt.imshow(img_c)

plt.imshow(img_c)
mpimg.imsave('c.jpg', img_c)




#2
img_g=mpimg.imread('g.jpg')
img_h=mpimg.imread('h.jpg')
diffs = img_g.astype("float")  - img_h.astype("float") 
diffs=np.absolute(diffs)

diffs.astype(np.uint8)
plt.imshow(diffs.astype(np.uint8))
diffs=diffs.astype(np.uint8)
mpimg.imsave('i.jpg', diffs)

#3

img_e=mpimg.imread('e.jpg')
img_f=img_e.copy()[:, :, :]
red = img_f[:,:,0]
green = img_f[:,:,1]
blue = img_f[:,:,2]

img_d=mpimg.imread('d.jpg')
img_d=img_d.copy()[:, :, :]

#plt.imshow(img_d)
rows,cols,channels = img_f.shape
roi = img_d[580:rows+580, 300:cols+300, : ]
#plt.imshow(roi)
mask_nongreen=np.logical_not(np.logical_and(green > 180, red<50, blue<50))

roi[mask_nongreen]=img_f[mask_nongreen]

img_d[580:rows+580, 300:cols+300, : ]=roi
plt.imshow(img_d)
mpimg.imsave('f.jpg', img_d)