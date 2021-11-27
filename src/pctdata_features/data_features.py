
from matplotlib import pyplot as plt
from project_Mukhiya_inf3692_SS21.src.data.data_reader import df1

# Comparing distinct features with i_time_stamp

for c in df1.columns[:-1]:
    plt.figure(figsize=(8, 5))
    plt.title("{} vs. \ni_time_stamp".format(c), fontsize=16)
    plt.scatter(x=df1[c], y=df1['i_time_stamp'], color='blue', edgecolor='k')
    plt.grid(True)
    plt.xlabel(c, fontsize=14)
    plt.ylabel('i_time_stamp\n', fontsize=14)
    plt.show()

