import csv
import pandas as pd
import os, glob
from pathlib import Path

# # reading the file and sorting the quality by order
# df = pd.read_csv('/Users/yujiezhang/Documents/Research/Raw data/screening_colon/Patient_900002_Screening - 2of2.csv')
# df = df.sort_values(by = ['qulaity'], ascending= True)

# # getting the lower quantile and assigning it to a new dataframe
# q15 = df.qulaity.quantile(0.15)
# print(q15)
# upper_q15 = df[df.qulaity > q15]
# upper_q15 = upper_q15.sort_values(by = ['index_col'], ascending= True)

# # dropping non-relevant values, writing dataf to a newfile
# upper_q15 = upper_q15.drop(columns=['canny_ratio','canny_edges','mask_pixels', 
#                                     'All_types_ulcer','type1', 'type2a', 'type2','type3','Normal_normal_likely','colon_Intrument','Poor_Quality'])
# upper_q15.to_csv('/Users/yujiezhang/Documents/Research/Processed data/screening_colon/Patient_900002_Screening - 2of2.csv', index=True)



#GOOD VERSION below

# counter = 1
# path = '/Users/yujiezhang/Documents/Research/Raw data/screening_colon/'

# # Iterate directory
# for filename in glob.glob(os.path.join(path, '*.csv')):
#         print(os.path.join(os.getcwd(), filename))
#         df = pd.read_csv(os.path.join(os.getcwd(), filename))
#         df = df.sort_values(by = ['qulaity'], ascending= True)
#         q15 = df.qulaity.quantile(0.15)
#         upper_q15 = df[df.qulaity > q15]
#         upper_q15 = upper_q15.sort_values(by = ['index_col'], ascending= True)
#         upper_q15 = upper_q15.drop(columns=['canny_ratio','canny_edges','mask_pixels', 
#                                     'All_types_ulcer','type1', 'type2a', 'type2','type3','Normal_normal_likely','Poor_Quality'])
#         upper_q15.to_csv('/Users/yujiezhang/Documents/Research/Processed data/screening_colon/' + str(path.stem) + '.csv', index= True)
#         counter += 1


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

# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/PROCESSED/PROCESSED screening_colon")
# for files in our_path.iterdir():
#         if files.name != '.DS_Store':
#                 print(files)
#                 df = pd.read_csv(files, index_col= False)
#                 if 'X' in df.columns:
#                         df = df.drop(columns = ['X', 'Y', 'Z'])
#                         df.sort_values(by=['coord', 'qulaity'], ascending=[False, False], inplace=True)
#                         df = df.groupby('coord').median().reset_index()
#                         if 'colon_BkgNormal' in df.columns:
# # Calculate the average of 'sum' values for rows meeting the condition using a generator expression
                                
#                                 avg = df.loc[(df['Erythema'] == 0) & (df['Blood'] == 0) & (df['colon_UlcerMild'] == 0)
#                                 & (df['colon_UlcerModSevere'] == 0) & (df['colon_Erythema'] == 0) & (df['colon_Intrument'] == 0),
#                                         ['colon_BkgNormal', 'colon_Poor_Quality']].sum(axis=1).mean()
#                                 df['colon_BkgNormal'] = (df['colon_BkgNormal'] / avg).round(6)
#                                 df['colon_Poor_Quality'] = (df['colon_Poor_Quality'] / avg).round(6)
#                                 df['Erythema'] = (df['Erythema'] / avg).round(6)
#                                 df['Blood'] = (df['Blood'] / avg).round(6)
#                                 df['colon_UlcerMild'] = (df['colon_UlcerMild'] / avg).round(6)
#                                 df['colon_UlcerModSevere'] = (df['colon_UlcerModSevere'] / avg).round(6)
#                                 df['colon_Erythema'] = (df['colon_Erythema'] / avg).round(6)
#                                 df['colon_Intrument'] = (df['colon_Intrument'] / avg).round(6)

#                                 df = df.drop(columns= ['Unnamed: 0'])
#                 df.to_csv("/Users/yujiezhang/Documents/Research/Processed data/PRO/PRO screening_colon/" + str(files.stem) + '.csv', index = True)

###################################################################################################################################################
###################################################################################################################################################

# Dividing coordinates into 200 points

# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/PRO/PRO screening_colon")

# for file in our_path.iterdir():
#     if file.name != '.DS_Store':
#         print(file)

#     df = pd.read_csv(file, encoding='latin-1')
#     total_rows = len(df)
#     rows_per_iteration = total_rows // 200

#     new_df = pd.DataFrame()
#     for i in range(200):
#         start = i * rows_per_iteration
#         end = (i + 1) * rows_per_iteration
#         temp_df = df.iloc[start:end]
#         temp_median = temp_df.median().to_frame().T
#         new_df = pd.concat([new_df, temp_median], ignore_index=True)

#     new_df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/200/' + str(file.stem) + '.csv', index=True)


# our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/200")

# for file in our_path.iterdir():
#     if (file.name != '.DS_Store'):
#         print(file)
#         df = pd.read_csv(file, index_col= False)
#         if(('colon_Intrument' in df.columns) & ('biopsy' in df.columns) & ('Unnamed: 0' in df.columns) & ('Erythema' in df.columns) & ('index_col' in df.columns) & ('Unnamed: 0' in df.columns) & ('Unnamed: 0.1' in df.columns)):
#                 df = df.drop(columns= ['colon_Intrument', 'biopsy', 'Unnamed: 0', 'Unnamed: 0.1', 'Erythema', 'index_col'])
#                 # df = df.drop(columns= ['Unnamed: 0', 'Unnamed: 0.1'])
#         if 'Unnamed: 0.2' in df.columns:
#                 df = df.drop(columns= ['Unnamed: 0.2'])
        
  
#         df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/200/' + str(file.stem) + '.csv', index= True, index_label= 'index')

###################################################################################################################################################
###################################################################################################################################################


our_path = Path("/Users/yujiezhang/Documents/Research/Processed data/200/")

for file in our_path.iterdir():
    if (file.name != '.DS_Store'):
        print(file)
        # df = pd.read_csv(file, index_col= False)
        df = pd.read_csv(file, encoding='latin-1')
        total_rows = len(df)
        rows_per_iteration = total_rows // 20

        new_df = pd.DataFrame()
        for i in range(20):
                start = i * rows_per_iteration
                end = (i + 1) * rows_per_iteration
                temp_df = df.iloc[start:end]
                temp_median = temp_df.median().to_frame().T
                new_df = pd.concat([new_df, temp_median], ignore_index=True)
        new_df.to_csv('/Users/yujiezhang/Documents/Research/Processed data/20/' + str(file.stem) + '.csv', index=True)
