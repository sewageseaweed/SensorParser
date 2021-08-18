# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 03:38:11 2021

@author: Clyde
"""

import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\csumagang\Desktop\SmartWash_2020\frazier.csv", encoding= 'unicode_escape')
df.shape

#FIELD WEATHER
renamed = []
for i in df:
    renamed.append(i.strip())

df.columns = renamed;
list(df)
df.shape
list(df['Date & Time'].values)

renamed[44:]
want = renamed[44:]
want.append('Date & Time')
df2 = pd.DataFrame()

for i in want:
    df2[i] = df[i]
    
print(df2[want[0]][4])
matrix = []
df2.replace(['--'], np.nan, inplace=True)
for i in df2.columns:
    matrix.append(i.split())
    
for i in matrix:
    if i[1].lower() != "port":
        i[0] += i[1]
        del i[1]
    print(i, len(i))

df3 = pd.DataFrame(columns = ['ID', 'Field ID', 'Date/Time', 'Sensor Type', 'Sensor Result', 'Unit']);

count = 0
lol = 0
df2_columns = list(df2.columns)
for index, row in df2.iterrows():
    for j in df2_columns:
        print(lol)
        lol+=1
        if j == 'Date & Time':
            break
        if not pd.isna(row[j]):
            curr = matrix[df2_columns.index(j)]
            if "-" in curr:
                dash = curr.index('-')
            else:
                dash = len(curr)
            sensorType = " ".join(curr[3:dash])
            fieldID = curr[0]
            sensorResult = row[j]
            if dash != len(curr):
                unit = curr[-1]
            elif "State" in curr:
                unit = 'ON/OFF'
                if(row[j] == 'ON'):
                    sensorResult = 1
                else:
                    sensorResult = 0
            else:
                unit = ""
            new_row = pd.Series(data={'ID':count, 'Field ID':fieldID, 'Date/Time': row['Date & Time'], 'Sensor Type': sensorType, 'Sensor Result':sensorResult, 'Unit':unit})
            df3  = df3.append(new_row, ignore_index = True)
            count += 1



df3.to_excel(r"C:\Users\Clyde\Desktop\SmartWash\sensors.xlsx")


#RANCH WEATHER BELOW

renamed[:24]
want2 = renamed[:24]
#want.append('Date & Time')
df4= pd.DataFrame()

for i in want2:
    df4[i] = df[i]
    
matrix2 = []
df4.replace(['--'], np.nan, inplace=True)
for i in df4.columns:
    matrix2.append(i.split())
"""    
for i in matrix2:
    if i[1].lower() != "port":
        i[0] += i[1]
        del i[1]
    print(i, len(i))
"""

df5 = pd.DataFrame(columns = ['ID','Date/Time', 'Sensor Type', 'Sensor Result', 'Unit']);

count2 = 0
lol2 = 0
df4_columns = list(df4.columns)
for index, row in df4.iterrows():
    for j in df4_columns:
        print(lol2)
        lol2+=1
        if j == 'Date & Time':
            continue
        if not pd.isna(row[j]):
            curr = matrix2[df4_columns.index(j)]
            if "-" in curr:
                dash = curr.index('-')
            else:
                dash = len(curr)
            sensorType = " ".join(curr[0:dash])
            print(sensorType)
            sensorResult = row[j]
            if dash != len(curr):
                unit = curr[-1]
            elif "State" in curr:
                unit = 'ON/OFF'
                if(row[j] == 'ON'):
                    sensorResult = 1
                else:
                    sensorResult = 0
            else:
                unit = ""
            new_row = pd.Series(data={'ID':count2, 'Date/Time': row['Date & Time'], 'Sensor Type': sensorType, 'Sensor Result':sensorResult, 'Unit':unit})
            df5  = df5.append(new_row, ignore_index = True)
            count2 += 1

df5.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\ranch_sensors2_new2.xlsx")


##SAMPLES BELOW


import numpy as np
import pandas as pd

df = pd.read_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Database_Raw_RR_ResultsUploadTest.xlsx")
df.shape
df.columns
df2 = pd.read_excel(r"C:\Users\csumagang\Desktop\tblFieldSample.xlsx")

df.rename(columns={"Sample Type": "SampleType", "Sample Subtype": "SampleSubType", "Sample Barcode": "Barcode", "Picture": "Media"}, inplace=True)

df3 = pd.DataFrame(columns = ['Lab', 'Method', 'Date', 'Time', 'SamplesID', 'Result'])
offFieldDF = pd.DataFrame(columns = ['SampleType', 'SampleSubType', 'RawDate', 'SpecificSampler', 'GPS', 'Barcode', 'Media', 'Notes', 'ExperimentsID'])
offFieldresDF = pd.DataFrame(columns = ['Lab', 'Method', 'Date', 'Time', 'SamplesID', 'Result'])

methods = df.columns[17:]
count = 0
offCount = 1

for index, row in df.iterrows():
    print(count)
    checker = False
    for inner_index, inner_row in df2.iterrows():
        if str(row['SampleType']) == str(inner_row['SampleType']) and str(row['SampleSubType']) == str(inner_row['SampleSubType']) and str(row['GPS']) == str(inner_row['GPS']) and str(row['Barcode']) == str(inner_row['Barcode']) and str(row['Media']) == str(inner_row['Media']) and str(row['Notes']) == str(inner_row['Notes']):
            checker = True
            for i in methods:
                if pd.isnull(row[i]):
                    continue
                else:
                    new_row = pd.Series(data={'Lab': row['Lab'], 'Method': i, 'Date': row['Date'], 'Time': row['Time'], 'SamplesID': inner_row['SamplesID'], 'Result': row[i]})
                    df3  = df3.append(new_row, ignore_index = True)
    if checker == False:
        new_row = pd.Series(data={'SampleType': row['SampleType'], 'SampleSubType': row['SampleSubType'], 'RawDate': row['Date'], 'SpecificSampler': 'Sullivan, Genevieve', 'GPS': row['GPS'], 'Barcode': row['Barcode'], 'Media': row['Media'], 'Notes': row['Notes']})
        offFieldDF = offFieldDF.append(new_row, ignore_index = True)
        for i in methods:
            if pd.isnull(row[i]):
                continue
            else:
                new_row = pd.Series(data={'Lab': row['Lab'], 'Method': i, 'Date': row['Date'], 'Time': row['Time'], 'SamplesID': offCount, 'Result': row[i]})
                offFieldresDF  = offFieldresDF.append(new_row, ignore_index = True)
        offCount += 1
            
    count+=1
                
df3.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Jul7_New_ResultsData2.xlsx")
offFieldDF.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Jul_OffFieldSamp.xlsx")
offFieldresDF.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Jul_OffFieldRes.xlsx")
"""
for index, row in df.iterrows():
    for inner_index, inner_row in df2.iterrows():
        if row['SampleType'] != inner_row['SampleType']:
            print("SAMPLE TYPE: ")
            print(row['SampleType'], inner_row['SampleType'])
        if row['SampleSubType'] != inner_row['SampleSubType']:
            print("SAMPLE SUB TYPE: ")
            print(row['SampleSubType'], inner_row['SampleSubType'])
        if row['GPS'] != inner_row['GPS']:
            print("GPS: ")
            print(row['GPS'], inner_row['GPS'])
            print(type(str(row['GPS'])), type(str(inner_row['GPS'])))
        if row['Barcode'] != inner_row['Barcode']:
            print("BARCODE: ")
            print(row['Barcode'], inner_row['Barcode'])
            print(type(row['Barcode']), type(inner_row['Barcode']))
        if row['Media'] != inner_row['Media']:
            print("MEDIA: ")
            print(row['Media'], inner_row['Media'])
        if row['Notes'] != inner_row['Notes']:
            print("NOTES: ")
            print(row['Notes'], inner_row['Notes'])
        break
    break
"""
"""
list(df)
df.shape

want = df.columns[:17]
print(want)
df2 = pd.DataFrame()

for i in want:
    df2[i] = df[i]
    
df2.replace(np.nan, "", inplace=True)
    
df2.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\SampleData.xlsx")


#RESULTS BELOW

want = df.columns[17:]

df3 = pd.DataFrame()

for i in want:
    df3[i] = df[i]

df3['Date'] = df['Date']
df3['Time'] = df['Time']
df3['Lab'] = df['Lab']

df4 = pd.DataFrame(columns = ['Lab', 'Method', 'Date', 'Time', 'SamplesID', 'Result']);

count = 1
lol = 0
df2_columns = list(df3.columns)[:13]
print(df2_columns)

for index, row in df3.iterrows():
    for j in df2_columns:
        print(lol)
        lol+=1
        if pd.isna(row[j]):
            continue
        new_row = pd.Series(data={'Lab': row['Lab'], 'Method': j, 'Date': row['Date'], 'Time': row['Time'], 'SamplesID': count, 'Result': row[j]})
        df4  = df4.append(new_row, ignore_index = True)
    count += 1
    
df4.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\ResultsData_New.xlsx")
"""
#GENERATE FIELD WEATHER LIST
df3['Sensor Type'].unique()
df_weather_sensors = pd.DataFrame();
df_weather_sensors['FieldWeatherSensor'] = df3['Sensor Type'].unique

df_weather_sensors.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\field_weather_sensor_list.xlsx")

#GENERATE RANCH WEATHER LIST
df5['Sensor Type'].unique()
df_ranch_sensors = pd.DataFrame();
df_ranch_sensors['RanchWeatherSensor'] = df5['Sensor Type'].unique()

df_ranch_sensors.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\ranch_weather_sensor_list.xlsx")