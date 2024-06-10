#%%
for i, x in enumerate(list(range(100001))):
    print(i, end = '\r')
#%%
from tqdm import tqdm 
loop = tqdm(total = 5000, position = 0, leave = False)
for k in range(5000):
    loop.set_description("Cargando...".format(k))
    loop.update(1)

loop.close()

from tqdm.auto import tqdm
for i in tqdm(range(100001)):
    print(" ", end='\r')