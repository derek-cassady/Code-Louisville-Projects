#import libraries
import pandas as pd
pd.set_option('display.max_columns', None)

#read .txt file from path specified and creates new .csv file to specified path. 
#'r' used to change to raw string to avoid syntax error
read_file = pd.read_csv(r'C:\Users\Derek\Desktop\Code_Louisville\Project\CEU0800000003.txt', sep="|")
read_file.to_csv(r'C:\Users\Derek\Desktop\Code_Louisville\Project\CEU0800000003.csv', index=0)

read_file = pd.read_csv(r'C:\Users\Derek\Desktop\Code_Louisville\Project\CEU0800000008.txt', sep="|")
read_file.to_csv(r'C:\Users\Derek\Desktop\Code_Louisville\Project\CEU0800000008.csv', index=0)

#read the .csv file created above into a dataframe accessible by Pandas
df_all = pd.read_csv('CEU0800000003.csv')
df_non = pd.read_csv('CEU0800000008.csv')


