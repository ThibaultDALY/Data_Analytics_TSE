# Python work friday 24/02/2017



import pandas
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt

# data_sectors = pandas.read_pickle('C:\\Users\\xavierdaly\\Desktop\\LAST YEAR OF SCHOOL\\SEMESTRE 10\\Dara Analytics\\Data_Analytics_TSE\\Sectors.pkl')
# data_SPX = pandas.read_pickle('C:\\Users\\xavierdaly\\Desktop\\LAST YEAR OF SCHOOL\\SEMESTRE 10\\Dara Analytics\\Data_Analytics_TSE\\Returns.pkl\\SPX.pkl')
# data_strategy = pandas.read_pickle('C:\\Users\\xavierdaly\\Desktop\\LAST YEAR OF SCHOOL\\SEMESTRE 10\\Dara Analytics\\Data_Analytics_TSE\\Returns.pkl\\Strategy.pkl')
#data_returns = pandas.read_pickle('C:\\Users\\xavierdaly\\Desktop\\LAST YEAR OF SCHOOL\\SEMESTRE 10\\Dara Analytics\\Data_Analytics_TSE\\Returns.pkl')


RET = pandas.read_pickle('Returns.pkl')
data_sectors = pandas.read_pickle('Sectors.pkl')
SPX = pandas.read_pickle('SPX.pkl')
data_strategy = pandas.read_pickle('Strategy.pkl')



#seabor, package plot
RET2 = pandas.concat([RET.copy(), SPX], axis = 1).dropna()
eqtcodes = list(RET2.columns)
betas = []
for s in eqtcodes:
    covmat = np.cov(RET2[s], RET2['SPX'])
    betas.append(covmat[0, 1]/covmat[1, 1])
print(betas)

plt.plot(betas)
plt.grid(True)
plt.show()



