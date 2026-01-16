import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from urllib.request import urlretrieve

medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
urlretrieve(medical_charges_url, 'medical.csv')

medical_df = pd.read_csv('medical.csv')
def estimate_charges(age,w,b):
    return w*age +b
    
w=50
b=100

result = estimate_charges(30,w,b)
print(result)

# the result is much more inaccurate 

non_smokers_df=medical_df[medical_df.smoker=='no']
ages=non_smokers_df.age
print(ages)

estimated_charges= estimate_charges(ages,w,b)
print(estimated_charges)

print(non_smokers_df.charges)


# plt.plot(ages,estimated_charges,'r-');
# plt.xlabel('Age');
# plt.ylabel('Estimated_charges');
# plt.title('Estimated_charges vs Age');
# plt.show()

target=non_smokers_df.charges
plt.plot(ages,estimated_charges,'r-',alpha=0.9)
plt.scatter(ages,target,s=9,alpha=0.8)
plt.xlabel('Age');
plt.ylabel('Charges');
plt.title('Estimated Charges vs Age');
plt.legend(['Estimated Charges','Actual Charges'])
plt.show()
