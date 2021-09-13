import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import pandas as pd

"""
Created on Mon Mar  1 03:38:11 2021

@author: Clyde
"""

"""
TODO: Clean up code
TODO: Make more efficient
"""

# FIELD WEATHER


def fieldWeather(path, start, csv):
    print("HERE I AM")
    if csv:
        df = pd.read_csv(path, encoding='unicode_escape')
    else:
        df = pd.read_excel(path)

    renamed = []
    for i in df:
        renamed.append(i.strip())

    df.columns = renamed
    list(df)
    df.shape
    list(df['Date & Time'].values)

    renamed[start:]
    want = renamed[start:]
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

    df3 = pd.DataFrame(columns=['ID', 'Field ID', 'Date/Time', 'Sensor Type', 'Sensor Result', 'Unit'])

    count = 0
    track = 0
    df2_columns = list(df2.columns)
    for index, row in df2.iterrows():
        for j in df2_columns:
            print(track)
            track += 1
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
                new_row = pd.Series(data={'ID': count, 'Field ID': fieldID, 'Date/Time': row['Date & Time'], 'Sensor Type': sensorType, 'Sensor Result':sensorResult, 'Unit':unit})
                df3 = df3.append(new_row, ignore_index=True)
                count += 1

    df3.to_excel(r"C:\Users\Clyde\Desktop\SmartWash\sensors.xlsx")


# RANCH WEATHER BELOW

def ranchWeather(path, end, csv):
    if csv:
        df = pd.read_csv(path, encoding='unicode_escape')
    else:
        df = pd.read_excel(path)

    renamed = []
    for i in df:
        renamed.append(i.strip())

    df.columns = renamed
    renamed[:end]
    want2 = renamed[:end]
    # want.append('Date & Time')
    df2 = pd.DataFrame()

    for i in want2:
        df2[i] = df[i]

    matrix2 = []
    df2.replace(['--'], np.nan, inplace=True)
    for i in df2.columns:
        matrix2.append(i.split())

    df3 = pd.DataFrame(columns=['ID', 'Date/Time', 'Sensor Type', 'Sensor Result', 'Unit'])

    count2 = 0
    tracker = 0
    df4_columns = list(df2.columns)
    for index, row in df2.iterrows():
        for j in df4_columns:
            print(tracker)
            tracker += 1
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
                new_row = pd.Series(data={'ID': count2, 'Date/Time': row['Date & Time'], 'Sensor Type': sensorType, 'Sensor Result':sensorResult, 'Unit':unit})
                df3 = df3.append(new_row, ignore_index=True)
                count2 += 1

    df3.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\ranch_sensors2_new2.xlsx")


# SAMPLES BELOW

def createSamples(path, start):
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
                    offFieldresDF = offFieldresDF.append(new_row, ignore_index = True)
            offCount += 1

        count+=1

    df3.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Jul7_New_ResultsData2.xlsx")
    offFieldDF.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Jul_OffFieldSamp.xlsx")
    offFieldresDF.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Jul_OffFieldRes.xlsx")


# GENERATE FIELD WEATHER LIST

def generateFieldWeatherList():
    df3['Sensor Type'].unique()
    df_weather_sensors = pd.DataFrame();
    df_weather_sensors['FieldWeatherSensor'] = df3['Sensor Type'].unique

    df_weather_sensors.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\field_weather_sensor_list.xlsx")


# GENERATE RANCH WEATHER LIST

def generateRanchWeatherList():
    df5['Sensor Type'].unique()
    df_ranch_sensors = pd.DataFrame();
    df_ranch_sensors['RanchWeatherSensor'] = df5['Sensor Type'].unique()

    df_ranch_sensors.to_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\ranch_weather_sensor_list.xlsx")
