import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'

from urllib.request import urlretrieve
urlretrieve(medical_charges_url, 'medical.csv')
medical_df = pd.read_csv('medical.csv')
def estimate_charges(age,w,b):
    return w*age +b
w=50
b=100

result = estimate_charges(30,w,b)

non_smokers_df=medical_df[medical_df.smoker=='no']
ages=non_smokers_df.age

estimated_charges= estimate_charges(ages,w,b)

smoker_df = medical_df[medical_df.smoker=='yes']
targets = smoker_df.charges
print(targets)

prediction = estimated_charges
print(prediction)

def rmse(targests, prediction):
    return np.sqrt(np.mean(np.square(targets-prediction)))

w=50
b=1000

targets=smoker_df['charges']
prediction=estimate_charges(smoker_df['age'],w,b)
print(rmse(targets,prediction))

# def try_parameters(w,b):
#     ages=smoker_df.age
#     target=smoker_df.charges
#     plt.plot(ages,estimated_charges,'r-',alpha=0.9)
#     plt.scatter(ages,target,s=9,alpha=0.8)
#     plt.xlabel('Age');
#     plt.ylabel('Charges');
#     plt.title('Estimated Charges vs Age');
#     plt.legend(['Estimated Charges','Actual Charges'])
# try_parameters(w,b)
# plt.show()

def try_parameters(w,b):
    ages=smoker_df.age 
    targets=smoker_df.charges
    prediction=estimate_charges(ages,w,b)
    plt.plot(ages,prediction,'r-',alpha=0.9)
    plt.scatter(ages,targets,s=9,alpha=0.8)
    plt.xlabel('Age');
    plt.ylabel('Charges');
    plt.legend(['Prediction','Actual']);
    loss=rmse(targets,prediction)
    print("RMSE loss:",loss)

# try_parameters(45,250000)
# plt.show()

try_parameters(400,5000)
plt.show()