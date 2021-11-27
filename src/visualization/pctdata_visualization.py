from matplotlib import pyplot as plt

from project_Mukhiya_inf3692_SS21.src.data.data_reader import df

#Each id_x and id_y on a single Graph or combination of all three planes in one graph excluding the losed protons.

plt.figure(figsize=(8, 6))
plt.title("Graph of each Points in all three plane", fontsize=16)
plt.scatter(df['id_x'], df['id_y'])
plt.grid()
plt.xlabel("Points of ID_X", fontsize=14)
plt.ylabel("Points of ID_Y", fontsize=14)
plt.show()

#Assigning different variablbe for diffent  belonging plane

plane_0 = df[df['id_plane'] == 0] #Photon hitting in first Plane
plane_1 = df[df['id_plane'] == 1] #Photon hitting second plane after moving through first plane
plane_2 = df[df['id_plane'] == 2] #Photon which reach the third plane

#Picture of all photons hitting in first plane
plt.figure(figsize=(13, 10))
plt.title("Plane_0", fontsize=16)
plt.scatter(plane_0['id_x'], plane_0['id_y'], color='indigo', alpha=0.2)
plt.grid()
plt.xlabel("Coordinate of ID_X in First Plane", fontsize=14)
plt.ylabel("Coordinate of ID_Y in First Plane", fontsize=14)
plt.show()

#Picture of all photons hitting in second plane
plt.figure(figsize=(13, 10))
plt.title("Plane_1", fontsize=16)
plt.scatter(plane_1['id_x'], plane_1['id_y'], color='lime', alpha=0.2)
plt.grid()
plt.xlabel("Coordinate of ID_X in Second Plane", fontsize=14)
plt.ylabel("Coordinate of ID_Y in Second Plane", fontsize=14)
plt.show()

#Picture of all photons hitting in third plane
plt.figure(figsize=(13, 10))
plt.title("Plane_2", fontsize=16)
plt.scatter(plane_2['id_x'], plane_2['id_y'], color='teal', alpha=0.2)
plt.grid()
plt.xlabel("Coordinate of ID_X in Third Plane", fontsize=14)
plt.ylabel("Coordinate of ID_Y in Third Plane", fontsize=14)
plt.show()
