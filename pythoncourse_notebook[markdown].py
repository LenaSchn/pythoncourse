# %% [markdown]
# #my Notebook for python course

# %%
import numpy as np
import panda as pd


# %%
x= np.linspace (0, 50, 1000)
x*= np.cos(x)
pd.dataframe ({"x":x}).plot()




