import pandas as pd
import glob
import os
import time


date = time.strftime('%Y-%m-%d')

# attendance in (entry)
path = r'D:\FYP FINAL\SEI-Mask-FaceAttendance\attendancein' # path to read save entry
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
df_file = (pd.read_csv(f) for f in all_files)
conc_df1   = pd.concat(df_file, ignore_index=True)
print("Attendance In:\n", conc_df1)

# attendance out (exit)
path = r'D:\FYP FINAL\SEI-Mask-FaceAttendance\attendanceout' # path to read save exit
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
df_file = (pd.read_csv(f) for f in all_files)
conc_df2   = pd.concat(df_file, ignore_index=True)
print("Attendance Out:\n",conc_df2)


result = pd.merge(conc_df1,conc_df2, on=['Name'], how='left')
result.columns = ['Name','DateIn','TimeIn','Mask','DateOut','TimeOut']
decimals = 2
result['Engage-Min'] = (pd.to_datetime(result['TimeOut']) - pd.to_datetime(result['TimeIn'])).astype('>m8[m]').astype(int)
result['Engage-Hrs'] = (result['Engage-Min']/60).round(decimals)
print ("Attendance In & Out:\n", result)    # print result both entry & exit 
result.to_csv("attendanceresult\Attendance_Result_"+date+".csv", index=True, header=True) # path to save print result