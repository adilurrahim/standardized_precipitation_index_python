import numpy as np
import pandas as pd
import os
import scipy.stats as stats
from scipy.stats import norm

def spi_submonthly(df,data_for,time_scale=4,path='D:/'):
    columns = df.columns.tolist()        
    df1=pd.DataFrame()
    for j in range(time_scale+1):
        df_sample= df[df[columns[0]]==(data_for-j)].copy()
        df_sample.reset_index(drop=True, inplace=True)
        df1.loc[:,j]= df_sample.loc[:,columns[2]].copy()
        df1.reset_index(drop=True, inplace=True)
    lists= [i for i in df1.sum(axis=1)]
    z= len(lists)
    lists1= [i for i in lists if i!=0]
    n=len(lists1)
    ln_lists= [round(np.log(i),6) for i in lists1]
    avg = round(np.mean(lists1),6)
    sums = round(np.sum(ln_lists),6)
    A= round(np.log(avg)-(sums/n),6)
    alpha= round((1/(4*A))*(1+np.sqrt(1+(4*A/3))),6)
    beta= round(avg/alpha,6)
    q= (z-n)/z
    listess=[]
    for k in lists:
        g1 = stats.gamma.cdf(k,a=alpha, scale=beta)
        g2=round(q+(1-q)*g1, 4)
        spi= round(norm.ppf(g2),2)
        listess.append(spi)        
    return pd.DataFrame(listess)