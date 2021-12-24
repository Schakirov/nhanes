import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

dirname = '/media/ai/74b9925e-0644-4a7c-a23d-1639723b5793/nhanes/'
years = ['1999', '2001', '2003', '2005', '2007', '2009', '2011', '2013', '2015', '2017']
glucose_filenames = ['LAB10AM', 'L10AM_B', 'L10AM_C', 'GLU_D', 'GLU_E', 'GLU_F', 'GLU_G', 'GLU_H', 'GLU_I', 'GLU_J']
glucose_varnames = ['LBXGLUSI'] * 2 + ['LBDGLUSI'] * 8
demo_filenames = ['DEMO', 'DEMO_B', 'DEMO_C', 'DEMO_D', 'DEMO_E', 'DEMO_F', 'DEMO_G', 'DEMO_H', 'DEMO_I', 'DEMO_J', 'P_DEMO']

def add_to_data(data, arr, year, nameOf2ndColumn):
    #adds 2D array to data[year]
    #1st column of 2D array always should be SEQN
    #2nd column of 2D array might be f.e. glucose (of those SEQNs)
    for i in range(len(arr)):
        seqn = int(arr[i][0])
        added_variable = arr[i][1]
        if seqn not in data[year].keys():
            data[year][seqn] = {}
        data[year][seqn][nameOf2ndColumn] = added_variable
    return data

data = {year:{} for year in years + ['nhanesIII']}
glucose_data = {}
glucose_rawdata = {}
age_data = {}
demo_rawdata = {}
for i in range(len(years)):
    year = years[i]
    fname = dirname + 'data/' + year + '/Laboratory/' + glucose_filenames[i]
    glucose_rawdata[year] = pd.read_sas(fname, format='xport')
    glucose_data[year] = glucose_rawdata[year][['SEQN', glucose_varnames[i]]].to_numpy()
    data = add_to_data(data, glucose_data[year], year, 'glucose')
    #now demography (age):
    fname = dirname + 'data/' + year + '/Demographics/' + demo_filenames[i]
    demo_rawdata[year] = pd.read_sas(fname, format='xport')
    age_data[year] = demo_rawdata[year][['SEQN', 'RIDAGEYR']].to_numpy() #in years
    data = add_to_data(data, age_data[year], year, 'age')

with open(dirname + 'data/nhanesIII/lab.dat', 'r') as f:
    lab = f.readlines()

glucose_data['nhanesIII'] = []
age_data['nhanesIII'] = []
for i in range(len(lab)):
    seqn = int(lab[i][0:5])
    glucose = lab[i][1870:1876]
    if glucose == '      ':
        glucose = 0
    age = int(int(lab[i][18:22])/12) #in years
    glucose_data['nhanesIII'].append([seqn, glucose])
    age_data['nhanesIII'].append([seqn, age])

glucose_data['nhanesIII'] = np.array(glucose_data['nhanesIII'], 'float')
age_data['nhanesIII'] = np.array(age_data['nhanesIII'], 'int')
data = add_to_data(data, glucose_data['nhanesIII'], 'nhanesIII', 'glucose')
data = add_to_data(data, age_data['nhanesIII'], 'nhanesIII', 'age')

maxage = 125;
glucoseStatAge = [[] for i in range(maxage)] #glucoseStatAge[24] would have all glucose values happened when year was 24
glucoseByAge = [] #all pairs [age, glucose]  to show on plot
for year in data.keys():
    for seqn in data[year].keys():
        if 'glucose' in data[year][seqn].keys() and 'age' in data[year][seqn].keys():
            age = data[year][seqn]['age']
            glucose = data[year][seqn]['glucose']
            if 0.1 < glucose < 100 and 0 <= age < maxage:
                glucoseStatAge[int(age)].append(glucose)
                glucoseByAge.append([age, glucose])

glucoseByAge = np.array(glucoseByAge)
plt.plot(glucoseByAge[:,0], glucoseByAge[:,1], '.', markersize=1); plt.show()

for percentile in range(10, 100, 2):
    percentile_line = []
    for year in range(len(glucoseStatAge)):
        if len(glucoseStatAge[year]) > 0:
            percentile_line.append(np.percentile(glucoseStatAge[year], percentile))
        else:
            percentile_line.append(0)
    plt.plot(percentile_line)

plt.show()

