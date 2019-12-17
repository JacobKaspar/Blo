import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat
import scipy.signal as signal 

data = loadmat('MO1_117_03.mat')

x=data['x']

x=x[0,:]

plt.plot(x)
plt.show()




b=signal.firwin(81,cutoff=[16-5,16+5],pass_zero='bandpass',fs=500)
a=np.zeros(len(b))
a[0]=1


y1=signal.lfilter(b, a, x)


plt.plot(y1)
plt.show()


y2=y1**2


plt.plot(y2)
plt.show()



b=np.ones(51)/51
a=np.zeros(len(b))
a[0]=1


y3=signal.lfilter(b, a, y2)


plt.plot(y3)
plt.show()



from scipy.signal import find_peaks



pos,props=find_peaks(y3,distance=20,height=50000)




pos=pos-(40+25)




plt.plot(x)
plt.plot(pos,x[pos],'r*')

plt.show()
