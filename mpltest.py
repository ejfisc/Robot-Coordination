import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))
center = (7.5, 7.5)
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
nw = ax.annotate("northwest", xy=(1, 14), xycoords='data',
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))
centerx, centery = 7.5, 7.5
center = ax.annotate("center", xy=(centerx, centery), xycoords='data',
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))
center_robots = ax.annotate("r1, r3, r4", xy=(centerx-0.7, centery-0.6), xycoords='data')

path = ax.annotate("", xy=center.xy, xytext=nw.xy, xycoords='data', arrowprops=dict(arrowstyle="->", shrinkA=15, shrinkB=15))


plt.show()