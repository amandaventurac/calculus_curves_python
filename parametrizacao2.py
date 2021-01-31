import numpy as np
import matplotlib.pyplot as  plt

def create_x_and_y_lists(data): 
    x = np.sin(data + np.cos(100 * data))
    y = np.cos(data + np.sin(100 * data))
    return x, y

def create_x_and_y_lists2(data):
    x = 1.5 * np.cos(data) - np.cos(30 * data)
    y = 1.5 * np.sin(data) - np.sin(30 * data)
    return x,y

list1 = np.linspace(-3.5, 3.5, 10000)
list2 = np.linspace(3.5, -3.5, 10000)

t = np.concatenate([list2, list1])

x_list, y_list = create_x_and_y_lists(t)
x_list2, y_list2 = create_x_and_y_lists2(t)

plt.plot(x_list, y_list, '-', linewidth = 0.5)
plt.show()

plt.plot(x_list2, y_list2, '-', linewidth = 0.5)
plt.show()
