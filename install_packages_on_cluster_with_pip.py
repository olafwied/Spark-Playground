#INSTALL PYTHON PACKAGES ON WORKER NODES USING PIP INSTALL

import os
L = sc.parallelize([1,2,3])

def install_package(x):
    os.system('sudo /usr/local/bin/pip install pandas')
    print 'installed'
    return 

L.map(lambda x: install_package(x)).collect()


import pandas as pd
L.map(lambda x: pd.DataFrame({'test':[x]})).collect()