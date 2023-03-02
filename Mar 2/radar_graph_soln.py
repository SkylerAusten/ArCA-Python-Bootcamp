import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import math

# -m pip install seaborn

# Pre-selected Stats:
categories = ['Attack', 'Hp', 'Sp. Atk', 'Sp. Def','Speed', 'Defense']
bg = [260, 260, 260, 260, 260, 260, 260]

number_of_categories = 7

pi = math.pi
angles = [((n+0.5)/number_of_categories)*(2*pi) for n in range(number_of_categories)]

angles += angles[:1]

#['Attack', 'Hp', 'Sp. Atk', 'Sp. Def', 'Speed', 'Defense','Attack']
val = [92, 45, 65, 45, 36, 55, 92]
text = [i+'\n'+str(int(j)) for i,j in zip(categories, val)]

# set the background and text
fig = plt.figure(figsize=(9, 9))
ax = plt.subplot(111, polar=True)
fig.patch.set_facecolor('#505060')
ax.set_facecolor('#505060')
ax.spines['polar'].set_visible(False)
plt.xticks(angles[:-1], text, color='white', size=23, fontweight='bold')
plt.yticks([269])     
plt.ylim(0,268)
ax.xaxis.set_tick_params(pad=42)

# draw the hexagon shape
mpl.rcParams['hatch.linewidth'] = 0.5
ax.plot(angles, bg, color='#282828', lw=11)
ax.fill(angles, bg, '#e0e0e0', alpha=1, zorder=1, hatch = '+')
ax.vlines(angles, 0, 252, color='#27ac98', lw=6, zorder=2)

# plot data
ax.plot(angles, val, linewidth=0)
ax.fill(angles, val, '#00ff48', alpha=0.9, zorder=3)
plt.tight_layout()
plt.savefig('radar_gen5.png')
plt.show()