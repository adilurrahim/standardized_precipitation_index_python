import spi_function 
import pandas as pd

'data_type is weekly with no null value'
data_for= 30   # the number of week for which spi will be calculated
time_scale= 11 # = cumulative weeks
path= 'D:/'   # path to save the result

df= pd.read_csv('Barishal.csv')
spi= spi_function.spi_submonthly(df,data_for,time_scale,path)
spi.columns=['SPI']
spi.to_csv('spi.csv',index=False)