import numpy as np
import matplotlib.pyplot as  plt
list1 = np.arange(-3.5,3.5,0.0001)
list2 = np.arange(3.5,-3.5,-0.0001)

t = [*list2,*list1]

def create_x_and_y_lists(data):
	x = np.sin(data + np.cos(100*data))
	y = np.cos(data + np.sin(100*data))
	return x,y

x_list = []
y_list = []

for i in range (0,len(t)):
	x,y = create_x_and_y_lists(t[i])
	x_list.append(x)
	y_list.append(y)

x_list2 = []
y_list2 = []

def create_x_and_y_lists2(data):
	x = 1.5* np.cos(data) - np.cos(30*data)
	y = 1.5* np.sin(data) - np.sin(30*data)
	return x,y

for i in range (0,len(t)):
	x,y = create_x_and_y_lists2(t[i])
	x_list2.append(x)
	y_list2.append(y)

plt.plot(x_list, y_list, '-', linewidth = 0.5)
plt.show()

plt.plot(x_list2, y_list2, '-', linewidth = 0.5)
plt.show()


