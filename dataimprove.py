import pandas as pd

dataset = pd.read_csv('/home/akshay.kumar/machine_learning/Data_Preprocessing/loan_small.csv')

subset = dataset.iloc[0:3, 1:3]

subsetN = dataset[['Gender', 'ApplicantIncome']][0:3]

# Read Data from tsv.

datasetT = pd.read_csv('/home/akshay.kumar/machine_learning/Data_Preprocessing/loan_small_tsv.txt', sep='\t')

#Head for selecting first few records - returns deafult 10 rows
dataset.head(10)

# Shape of the dataset
dataset.shape

#Get column names of the dataset
dataset.columns

#Get missing values in a dataset
#isnull and sum
dataset.isnull().sum()

#Replace missing values in the dataset

#Drop the rows if there are very few rows missing values
cleandata = dataset.dropna()

# drop the specific columns basis only
cleandata = dataset.dropna(subset=['Loan_Status'])

#Replace nan values with other values
#Mode for categorical
dt = dataset.copy() #making a copy of dataset

cols = ['Gender', 'Area', 'Loan_Status']
dt[cols] = dt[cols].fillna(dt.mode().iloc[0])
dt.isnull().sum()

#mean for numerical
cols2 = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
dt[cols2] = dt[cols2].fillna(dt.mean())
dt.isnull().sum()


##Categorical Variables - we need to convert them to numeric via label encoding
dt.dtypes
dt[cols] = dt[cols].astype('category')
dt.dtypes


for col in cols:
    dt[col] = dt[col].astype('category')

for columns in cols:
    dt[columns] = dt[columns].cat.codes

dt.dtypes

# Hot Encoding for Categorical Data
df2 = dataset.drop(['Loan_ID'], axis=1)
df2 = pd.get_dummies(df2)

#####Normalization#####
#ZScore
import pandas as pd
from sklearn.preprocessing import StandardScaler
dataset = pd.read_csv('/home/akshay.kumar/machine_learning/Data_Preprocessing/loan_small.csv')
cleandata = dataset.dropna()

data_to_scale = cleandata.iloc[: , 2:5]

scaler_ = StandardScaler()
ss_scaler = scaler_.fit_transform(data_to_scale)


#MinMax to minimise
from sklearn.preprocessing import minmax_scale
mm_scaler = minmax_scale(data_to_scale)


#####Train and Test Data
import pandas as pd
dataset = pd.read_csv('/home/akshay.kumar/machine_learning/Data_Preprocessing/loan_small.csv')
cleandata = dataset.dropna(subset=['Loan_Status'])
df = cleandata.copy()
cols = ['Gender', 'Area', 'Loan_Status']
df[cols] = df[cols].fillna(df.mode().iloc[0])

cols2 = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
df[cols2] = df[cols2].fillna(df.mean())
df = df.drop(['Loan_ID'], axis = 1)
df = pd.get_dummies(df)

df = df.drop(['Loan_Status_N'], axis=1)

# Split into X (independent) and y (predicted)

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

#Split for rows
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=1234)


















































