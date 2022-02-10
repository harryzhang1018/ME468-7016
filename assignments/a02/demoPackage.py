#!/user/bin/python3


import numpy as np
import pandas as pd

dates = pd.date_range("20220209",periods=5)

dateWithData = pd.DataFrame(np.random.randint(5,12,size=(5,1)),index=dates,columns=['Studying hour'])




print(dateWithData)

