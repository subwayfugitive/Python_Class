# Thomas Powell Horan
import matplotlib.pyplot as plt

# make some empty lists to append the calcualted values into
y_line = []
y_square = []
y_cube = []
 
# this will calucate all the values that we need and append them into the lists 
for i in range(51):
    y_line.append(i*0.25)
    y_square.append((i*0.25)**2)
    y_cube.append((i*0.25)**3)

print(y_line)

# # title for plot
# plt.title("LINE, CUBE, SQUARE")

# # plotting changing color and marker type (Method 1)
# plt.plot(y_line,y_line, 'g:o')#green "O"
# plt.plot(y_line, y_square,'b:*')#blue "*"
# plt.plot(y_line, y_cube, 'r:H')#red hexagon

# #legend(Method 2)
# plt.legend(['line','square','cube'])

# #grid on(Method 3)
# plt.grid()

# #label axis(Method 4)
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")

# plt.show()
