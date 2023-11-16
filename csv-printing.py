import csv
import pandas as pd
import os, glob
from pathlib import Path
import numpy as np


#NEW METHOD - WORKS!!! This is what I utilised

# our_path = Path("/Users/yujiezhang/Documents/Research/Raw data/screening_colon/")

# for files in our_path.iterdir():
#         print(files)
#         df = pd.read_csv(files)
#         df = df.sort_values(by = ['qulaity'], ascending= True)
#         q15 = df.qulaity.quantile(0.15)
#         upper_q15 = df[df.qulaity > q15]
#         upper_q15 = upper_q15.sort_values(by = ['index_col'], ascending= True)
#         upper_q15 = upper_q15.drop(columns=['canny_ratio','canny_edges','mask_pixels', 
#                                         'All_types_ulcer','type1', 'type2a', 'type2','type3','Normal_normal_likely','Poor_Quality'])
#         upper_q15.to_csv('/Users/yujiezhang/Documents/Research/Processed data/PROCESSED screening_colon/' + 'PROCESSED' + str(files.stem) + '.csv', index= True)

    
#For cleaning screening_ileum
#NO Poor Quality column

# our_path = Path("/Users/yujiezhang/Documents/Research/Raw data/screening_ileum/")

# for files in our_path.iterdir():
#         if files.name != '.DS_Store':
#                 print(files)
#                 df = pd.read_csv(files)
#                 df = df.sort_values(by = ['qulaity'], ascending= True)
#                 q15 = df.qulaity.quantile(0.15)
#                 upper_q15 = df[df.qulaity > q15]
#                 upper_q15 = upper_q15.sort_values(by = ['index_col'], ascending= True)
#                 upper_q15 = upper_q15.drop(columns=['canny_ratio','canny_edges','mask_pixels', 
#                                                 'All_types_ulcer','type1', 'type2a', 'type2','type3','Normal_normal_likely'])
#                 upper_q15.to_csv('/Users/yujiezhang/Documents/Research/Processed data/PROCESSED screening_ileum/' + 'PROCESSED' + str(files.stem) + '.csv', index= True)


# For clearning week52_colon

# our_path = Path("/Users/yujiezhang/Documents/Research/Raw data/week52_colon/")

# for files in our_path.iterdir():
#         if files.name != '.DS_Store':
#                 print(files)
#                 df = pd.read_csv(files)
#                 df = df.sort_values(by = ['qulaity'], ascending= True)
#                 q15 = df.qulaity.quantile(0.15)
#                 upper_q15 = df[df.qulaity > q15]
#                 upper_q15 = upper_q15.sort_values(by = ['index_col'], ascending= True)
#                 upper_q15 = upper_q15.drop(columns=['canny_ratio','canny_edges','mask_pixels', 
#                                                 'All_types_ulcer','type1', 'type2a', 'type2','type3','Normal_normal_likely', 'Poor_Quality'])
#                 upper_q15.to_csv('/Users/yujiezhang/Documents/Research/Processed data/PROCESSED week52_colon/' + 'PROCESSED' + str(files.stem) + '.csv', index= True)


# For cleaning week52_ileum

# our_path = Path("/Users/yujiezhang/Documents/Research/Raw data/week52_ileum/")

# for files in our_path.iterdir():
#         if files.name != '.DS_Store':
#                 print(files)
#                 df = pd.read_csv(files)
#                 df = df.sort_values(by = ['qulaity'], ascending= True)
#                 q15 = df.qulaity.quantile(0.15)
#                 upper_q15 = df[df.qulaity > q15]
#                 upper_q15 = upper_q15.sort_values(by = ['index_col'], ascending= True)
#                 upper_q15 = upper_q15.drop(columns=['canny_ratio','canny_edges','mask_pixels', 
#                                                 'All_types_ulcer','type1', 'type2a', 'type2','type3','Normal_normal_likely'])
#                 upper_q15.to_csv('/Users/yujiezhang/Documents/Research/Processed data/PROCESSED/PROCESSED week52_ileum/' + 'PROCESSED' + str(files.stem) + '.csv', index= True)


############################# October 18   #################################################################################
############################################################################################################################

# Contains each individual coordinate
# upper 75 percentile, all neccessary features
# normalized pixels and features

# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/PROCESSED/PROCESSED screening_ileum")
# for files in our_path.iterdir():
#         if files.name != '.DS_Store':
#                 print(files)
#                 df = pd.read_csv(files, index_col= False)
#                 if 'X' in df.columns:
#                         df = df.drop(columns = ['X', 'Y', 'Z'])
#                         df.sort_values(by=['coord', 'qulaity'], ascending=[False, False], inplace=True)
#                         df = df.groupby('coord').median().reset_index()
#                         if 'ileum_BkgNormal' in df.columns:
# # Calculate the average of 'sum' values for rows meeting the condition using a generator expression
                                
#                                 avg = df.loc[(df['Erythema'] == 0) & (df['Blood'] == 0) & (df['ileum_UlcerMild'] == 0)
#                                 & (df['ileum_UlcerModSevere'] == 0) & (df['ileum_Erythema'] == 0) & (df['ileum_Intrument'] == 0),
#                                         ['ileum_BkgNormal', 'ileum_Poor_Quality']].sum(axis=1).mean()
#                                 df['ileum_BkgNormal'] = (df['ileum_BkgNormal'] / avg).round(6)
#                                 df['ileum_Poor_Quality'] = (df['ileum_Poor_Quality'] / avg).round(6)
#                                 df['Erythema'] = (df['Erythema'] / avg).round(6)
#                                 df['Blood'] = (df['Blood'] / avg).round(6)
#                                 df['ileum_UlcerMild'] = (df['ileum_UlcerMild'] / avg).round(6)
#                                 df['ileum_UlcerModSevere'] = (df['ileum_UlcerModSevere'] / avg).round(6)
#                                 df['ileum_Erythema'] = (df['ileum_Erythema'] / avg).round(6)
#                                 df['ileum_Intrument'] = (df['ileum_Intrument'] / avg).round(6)

#                                 df = df.drop(columns= ['Unnamed: 0'])
#                 df.to_csv("/Users/yujiezhang/Documents/Research/Processed data/PRO/PRO screening_ileum/" + str(files.stem) + '.csv', index = True)

###################################################################################################################################################
###################################################################################################################################################

# Dividing coordinates into 200 or 50 points

# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/PRO/PRO screening_ileum/")

# for file in our_path.iterdir():
#     if file.name != '.DS_Store':
#         print(file)

    
#     df = pd.read_csv(file, encoding='latin-1')
#     total_rows = len(df)
#     rows_per_iteration = total_rows // 50

#     new_df = pd.DataFrame()
#     for i in range(50):
#         start = i * rows_per_iteration
#         end = (i + 1) * rows_per_iteration
#         temp_df = df.iloc[start:end]
#         temp_median = temp_df.median().to_frame().T
#         new_df = pd.concat([new_df, temp_median], ignore_index=True)

#     if(('ileum_Intrument' in df.columns) & ('biopsy' in df.columns) & ('Unnamed: 0' in df.columns) & ('Erythema' in df.columns) & ('index_col' in df.columns) & ('Unnamed: 0' in df.columns) & ('Unnamed: 0.1' in df.columns)):
#         new_df = new_df.drop(columns= ['ileum_Intrument', 'biopsy', 'Unnamed: 0', 'Unnamed: 0.1', 'Erythema', 'index_col'])

#     if 'Unnamed: 0.2' in df.columns:
#         new_df = new_df.drop(columns= ['Unnamed: 0.2'])

#     new_df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/200/200_ileum/' + str(file.stem) + '.csv', index= True, index_label= 'index')

###################################################################################################################################################
###################################################################################################################################################

# Divide into 20 or 5 coordinates

# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/200/200_ileum/")

# dataframes = []
# for file in our_path.iterdir():
#     if (file.name != '.DS_Store'):
#         print(file)
#         # df = pd.read_csv(file, index_col= False)
#         df = pd.read_csv(file, encoding='latin-1')
#         total_rows = len(df)
#         rows_per_iteration = total_rows // 5

#         new_df = pd.DataFrame()
#         for i in range(5):
#                 start = i * rows_per_iteration
#                 end = (i + 1) * rows_per_iteration
#                 temp_df = df.iloc[start:end]
#                 temp_median = temp_df.median().to_frame().T
#                 new_df = pd.concat([new_df, temp_median], ignore_index=True)
        
#         dataframes.append(new_df)


#         new_df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/20/20_ileum/' + str(file.stem) + '.csv', index=True)

###################################################################################################################################################
###################################################################################################################################################

# reshape range 55

# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/20/20_ileum/")

# for file in our_path.iterdir():
#     if (file.name != '.DS_Store.csv' ):
#         print(file)
#         df = pd.read_csv(file, index_col= False)
#         if(('ileum_Intrument' in df.columns) & ('biopsy' in df.columns) & ('Unnamed: 0' in df.columns) & ('Erythema' in df.columns) & ('index_col' in df.columns)):
#             df = df.drop(columns= ['Unnamed: 0', 'index_col', 'biopsy', 'ileum_Intrument', 'Erythema', 'index_col'])

#         reshaped_df = pd.DataFrame(df.values.reshape(1, -1))

#         reshaped_df.columns = range(55)
#         reshaped_df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/4/4_ileum/' + str(file.stem) + '.csv', index=True)


###################################################################################################################################################
###################################################################################################################################################


# Four sections five segments

# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/4/4_ileum/")

# # list = ['Left','Transverse', 'Right', 'Rectum']

# for file in our_path.iterdir():
#     if not file.name.startswith('.'):
#         print(file)
#         df = pd.read_csv(file, encoding='latin-1')
#         df = df.drop(columns= ['0','1','2','11','12', '13','22','23', '24', '33','34','35','44', '45', '46'])
#         df.rename(columns={'3':'quality', '4' : 'severity_class', '5': 'Blood', '6': 'ileum_UlcerMild', '7': 'ileum_UlcerModSevere', '8': 'ileum_Erythma',
#                             '9':'ileum_BkgNormal', '10': 'ileum_Poor_Quality', '14': 'quality2', '15':'severity_class2', '16': 'Blood2', '17':'ileum_UlcerMild2',
#                             '18':'ileum_UlcerModSevere2', '19': 'ileum_Erythma2', '20':'ileum_BkgNormal2', '21':'ileum_Poor_Quality2'
#                            , '25': 'quality3', '26': 'severity_class3', '27': 'Blood3', '28': 'ileum_UlcerMild3', '29': 'ileum_UlcerModSevere3', '30': 'ileum_Erythma3', '31': 'ileum_BkgNormal3', '32': 'ileum_Poor_Quality3', 
#                            '36': 'quality4', '37': 'severity_class4', '38': 'Blood4', '39': 'ileum_UlcerMild4', '40': 'ileum_UlcerModSevere4', '41': 'ileum_Erythma4', '42': 'ileum_BkgNormal4', '43': 'ileum_Poor_Quality4',
#                             '47': 'quality5', '48':'severity_class5', '49': 'Blood5', '50': 'ileum_UlcerMild5', '51': 'ileum_UlcerModSevere5', '52': 'ileum_Erythma5', '53': 'ileum_BkgNormal5', '54': 'ileum_Poor_Quality5'},inplace= True)
#         new_col = str(file.stem)
#         df.insert(loc=0, column='Patient', value= new_col)
#         # df.insert(loc=1, column= 'Parts', value=list)

#     df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/4f/4f_ileum/' + str(file.stem) + '.csv', index=False)

###################################################################################################################################################
###################################################################################################################################################

# Putting all df into one file

# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/4f/4f_ileum/")

# combined_df = None
# for file in our_path.iterdir():
#     if not file.name.startswith('.'):
#         print(file)
#         df = pd.read_csv(file, encoding='latin-1')
#         if combined_df is None:
#             combined_df = df
#         else:
#             combined_df = pd.concat([combined_df, df], ignore_index=True)

# combined_df = combined_df.sort_values(by = ['Patient'], ascending= True)

# df = combined_df
# df.dropna(inplace=True)
# df = df.drop(columns= 'Unnamed: 0')
# df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/final/ileum/' + str(file.stem) + '.csv', index=False)

##################################################################################################################################################
##################################################################################################################################################

# Total and ulcersize and erythema size columns for colon/ileum

df = pd.read_csv('/Users/yujiezhang/Documents/Research/Processed data/final/colon/colonfinaldf.csv', encoding='latin-1')


df['ulcersize1'] = df['colon_UlcerMild'] + df['colon_UlcerModSevere']
df['ulcersize2'] = df['colon_UlcerMild2'] + df['colon_UlcerModSevere2']
df['ulcersize3'] = df['colon_UlcerMild3'] + df['colon_UlcerModSevere3']
df['ulcersize4'] = df['colon_UlcerMild4'] + df['colon_UlcerModSevere4']
df['ulcersize5'] = df['colon_UlcerMild5'] + df['colon_UlcerModSevere5']

df['erythma1'] = df['colon_Erythma'] 
df['erythma2'] = df['colon_Erythma2']
df['erythma3'] = df['colon_Erythma3']
df['erythma4'] = df['colon_Erythma4'] 
df['erythma5'] = df['colon_Erythma5']

df['total_colon'] = (df['colon_UlcerMild'] + df['colon_UlcerModSevere'] + df['colon_UlcerMild2'] + df['colon_UlcerModSevere2'] + df['colon_UlcerMild3'] + df['colon_UlcerModSevere3'] + df['colon_UlcerMild4'] + df['colon_UlcerModSevere4'] + df['colon_UlcerMild5'] + df['colon_UlcerModSevere5'])/5
df['total_ulcer'] = (df['colon_Erythma'] + df['colon_Erythma2'] + df['colon_Erythma3'] + df['colon_Erythma4'] + df['colon_Erythma5']) / 5

quartile = df[['ulcersize1', 'ulcersize2', 'ulcersize3', 'ulcersize4', 'ulcersize5']].values.flatten()

quartile_erythma = df[['erythma1', 'erythma2', 'erythma3', 'erythma4', 'erythma5']].values.flatten()

df['total_colon'] = df[['total_colon']].values.flatten()
df['total_ulcer'] = df[['total_ulcer']].values.flatten()


df_25 = np.quantile(quartile, 0.25)
df_50 = np.quantile(quartile, 0.5)
df_75 = np.quantile(quartile, 0.75)
df_100 = np.quantile(quartile, 1)

df_e_25 = np.quantile(quartile_erythma, 0.25)
df_e_50 = np.quantile(quartile_erythma, 0.5)
df_e_75 = np.quantile(quartile_erythma, 0.75)
df_e_100 = np.quantile(quartile_erythma, 1)

df_tc_25 = np.quantile(df['total_colon'], 0.25)
df_tc_50 = np.quantile(df['total_colon'], 0.5)
df_tc_75 = np.quantile(df['total_colon'], 0.75)
df_tc_100 = np.quantile(df['total_colon'], 1)

print(df_tc_25)
print(df_tc_50)
print(df_tc_75)


df_tu_25 = np.quantile(df['total_ulcer'], 0.25)
df_tu_50 = np.quantile(df['total_ulcer'], 0.5)
df_tu_75 = np.quantile(df['total_ulcer'], 0.75)
df_tu_100 = np.quantile(df['total_ulcer'], 1)

print(df_tu_25)
print(df_tu_50)
print(df_tu_75)

def categorize_value(value, q25, q50, q75):
    if value <= q25:
        return 0
    elif q25 <= value < q50:
        return 1
    elif q50 <= value < q75:
        return 2
    else:
        return 3

columns_to_categorize = ['ulcersize1', 'ulcersize2', 'ulcersize3', 'ulcersize4', 'ulcersize5']
columns_to_categorize_erythma = ['erythma1', 'erythma2', 'erythma3', 'erythma4', 'erythma5', 'total_colon', 'total_ulcer']


for column in columns_to_categorize:
    df[column] = df[column].apply(categorize_value, args=(df_25, df_50, df_75))

for column in columns_to_categorize_erythma:
    df[column] = df[column].apply(categorize_value, args=(df_e_25, df_e_50, df_e_75))


quartile_total_colon = df['total_colon'].apply(categorize_value, args=(df_tc_25, df_tc_50, df_tc_75))

quartile_total_ulcer = df['total_ulcer'].apply(categorize_value, args=(df_tu_25, df_tu_50, df_tu_75))



selected_columns = [
    'Patient', 'Parts', 'total_colon', 'total_ulcer','quality', 'severity_class', 'Blood',
    'colon_UlcerMild', 'colon_UlcerModSevere', 'ulcersize1',
    'colon_Erythma', 'erythma1', 'colon_BkgNormal', 'colon_Poor_Quality',
    'quality2', 'severity_class2', 'Blood2',
    'colon_UlcerMild2', 'colon_UlcerModSevere2', 'ulcersize2',
    'colon_Erythma2', 'erythma2', 'colon_BkgNormal2', 'colon_Poor_Quality2',
    'quality3', 'severity_class3', 'Blood3',
    'colon_UlcerMild3', 'colon_UlcerModSevere3', 'ulcersize3', 
    'colon_Erythma3', 'erythma3', 'colon_BkgNormal3', 'colon_Poor_Quality3',
    'quality4', 'severity_class4', 'Blood4',
    'colon_UlcerMild4', 'colon_UlcerModSevere4', 'ulcersize4',
    'colon_Erythma4', 'erythma4', 'colon_BkgNormal4', 'colon_Poor_Quality4',
    'quality5', 'severity_class5', 'Blood5',
    'colon_UlcerMild5', 'colon_UlcerModSevere5', 'ulcersize5', 
    'colon_Erythma5', 'erythma5', 'colon_BkgNormal5', 'colon_Poor_Quality5'
]

# Select the specified columns in the final DataFrame
df = df[selected_columns]

df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/final/colon_week52/colon_week52.csv', index=False)


# ###################################################################################################################################################
# ###################################################################################################################################################


