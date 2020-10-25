import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from plots.df import make_df
import numpy as np

df = make_df()

col_width = 3.2
fig, ax = plt.subplots(figsize=(col_width, col_width * 1.7875))  # (shape1: col, shape2: row)
size = fig.get_size_inches()  # fig.dpi

c = ax.pcolormesh(df, cmap='cividis')

# ax.set_title('Co-citation Matrix', fontsize=col_width * 0.5, pad=col_width * 0.5) # caption will  replace it

# Articles
# plt.yticks(np.arange(0.5, len(df.index), 143)) #, df.index) #, fontsize=col_width * 0.1)

# df_columns_wo_parenthesis = [col.split(':') for col in df.columns.values]
# df_columns_wo_parenthesis = [col[0] + ':' + '\n' + col[1] if len(col) == 2 else col[0] + '\n' + '' for col in df_columns_wo_parenthesis]

# DS Numbers
# plt.xticks(np.arange(0.5, len(df.columns), 1), df_columns_wo_parenthesis) #, fontsize=8)
# ax.xaxis.tick_top()
# ax.set_ylim((0, len(df.index)))

# Legend
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("bottom", size="0.5%", pad=0.1)
# cb = fig.colorbar(c, orientation="horizontal", cax=cax)
# cb.ax.tick_params(labelsize=25)

# plt.show()

plt.axis('off')

import tikzplotlib
tikzplotlib.save('../pred.tex')
print(size)

if __name__ == "__main_":
    pass



