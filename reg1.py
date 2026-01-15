import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'

from urllib.request import urlretrieve
urlretrieve(medical_charges_url, 'medical.csv')

medical_df = pd.read_csv('medical.csv')
print(medical_df.head())

non_smokers_df=medical_df[medical_df.smoker=='no']
plt.title('Age vs. charges')
sns.scatterplot(data=non_smokers_df,x='age',y='charges',alpha=0.7,s=15)
plt.show()