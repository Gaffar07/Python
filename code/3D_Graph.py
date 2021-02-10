import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig=plt.figure()
ax=plt.axes(projection="3d")
x=[1,2,3,4,5,6,7,8,9]
y=[2,3,4,5,6,7,8,9,1]
#z=[5,6,2,4,8,6,5,6,1]

ax.scatter(x,y,color='b')
ax.set_xlabel('x Axes')
ax.set_ylabel('y Axes')
#ax.set_zlabel('z Axes');

# ax = plt.axes(projection='3d')
# ax.plot_surface(x, y, z, rstride=1, cstride=1,
#                 cmap='viridis', edgecolor='none')
# ax.set_title('surface');


plt.show()