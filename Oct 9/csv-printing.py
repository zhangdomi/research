import csv
import pandas as pd
import os, glob


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


counter = 1
path = '/Users/yujiezhang/Documents/Research/Raw data/screening_colon/'
# Iterate directory
for filename in glob.glob(os.path.join(path, '*.csv')):
        print(os.path.join(os.getcwd(), filename))
        df = pd.read_csv(os.path.join(os.getcwd(), filename))
        df = df.sort_values(by = ['qulaity'], ascending= True)
        q15 = df.qulaity.quantile(0.15)
        upper_q15 = df[df.qulaity > q15]
        upper_q15 = upper_q15.sort_values(by = ['index_col'], ascending= True)
        upper_q15 = upper_q15.drop(columns=['canny_ratio','canny_edges','mask_pixels', 
                                    'All_types_ulcer','type1', 'type2a', 'type2','type3','Normal_normal_likely','Poor_Quality'])
        upper_q15.to_csv('/Users/yujiezhang/Documents/Research/Processed data/screening_colon/Patient_' + str(counter) + '.csv', index= True)
        counter += 1


    
