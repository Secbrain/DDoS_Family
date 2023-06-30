# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib
import numpy as np
import math
import os
from collections import Counter
import math
import leidenalg as la
import igraph as ig

import os
import math
import pandas as pd
import numpy as np
import leidenalg as la
import igraph as ig

f=open('...','wb')
f.close()

quan=np.zeros((10,89,770,1000))
for i0 in range(10):
  w1=lu+str(i0)+'/'
  for i1 in range(89):
    quan[i0,i1,:,:]=np.load(w1+'n-'+str(i1)+'.npy')

lu='...'

lieind=[68, 194, 320, 446, 572, 698]
cheng=[56, 182, 308, 434, 560, 686]

lieind=[24]

heng=np.arange(0,1,0.001)

for i0 in range(10):
  w1=lu+str(i0)+'/'
  data=np.zeros((89,770,1000))
  linjie=np.zeros((89,89))
  for i1 in range(89):
    data[i1,:,:]=np.load(w1+'n-'+str(i1)+'.npy')
  mian=heng*data
  ...
  for i1 in range(len(g.es)):
    wei0=g.es[i1].tuple[0]
    wei1=g.es[i1].tuple[1]
    g.es[i1]['wei']=dui[wei0,wei1]
  part=la.find_partition(g, la.ModularityVertexPartition,weights='wei',n_iterations=-10,seed=42)#,max_comm_size=10
  for i in part:
    print(i)
  print('='*6)

partition=la.CPMVertexPartition(g,resolution_parameter = 0.5)
optimiser=la.Optimiser()
diff=optimiser.optimise_partition(partition)
