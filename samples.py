import numpy as np
import pandas as pd

df = pd.read_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Database_Raw_RR_ResultsUploadTest.xlsx")
df2 = df = pd.read_excel(r"C:\Users\csumagang\Desktop\SmartWash_2020\Database_Raw_RR_ResultsUploadTest.xlsx")
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
