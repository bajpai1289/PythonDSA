from datetime import datetime
import pandas as pd
import colorama
from colorama import Fore, init
init(convert=True)
from sys import stdout
import glob
def calculateRNTOT(string_start,string_end): #result= Value would be of the format (Regular OT hour,night time OT hour)
    start_time = datetime.strptime(string_start, "%H:%M:%S")
    end_time = datetime.strptime(string_end, "%H:%M:%S")
    if start_time==datetime.strptime("00:00:00","%H:%M:%S") and end_time==datetime.strptime("00:00:00","%H:%M:%S"):
        return (0.0,0.0)
    EOD=datetime.strptime("12:00:00","%H:%M:%S")
    delta = end_time - start_time
    sec = delta.total_seconds()
    min = sec / 60
    hours = sec / (60 * 60)    
    temp=round(hours,2)

    #if the person works 2 days
    if temp<0:
        deltaday1day=datetime.strptime("22:00:00","%H:%M:%S")-start_time
        day1daysec=deltaday1day.total_seconds()
        day1day=day1daysec/(60*60)
        day1day=round(day1day,2)
        day1night=2.0
        if day1day<0:
            day1day=0
            deltaday1night=datetime.strptime("23:59:59","%H:%M:%S")-start_time
            day1nightsec=deltaday1night.total_seconds()
            day1night=day1nightsec/(60*60)
            day1night=round(day1night,2)
        #day 2
        if end_time<=datetime.strptime("05:00:00","%H:%M:%S"):
            day2day=0.0
            deltaday2night=end_time-datetime.strptime("00:00:10","%H:%M:%S")
            day2nightsec=deltaday2night.total_seconds()
            day2night=day2nightsec/(60*60)
            day2night=round(day2night,2)
        else:
            day2night=5.0
            deltaday2day=end_time-datetime.strptime("05:00:00","%H:%M:%S")
            day2daysec=deltaday2day.total_seconds()
            day2day=day2daysec/(60*60)
            day2day=round(day2day,2)
        return (day1day+day2day, day1night+day2night)
    #if person works at the same day
    else:
        if start_time>=datetime.strptime("05:00:00","%H:%M:%S") and end_time<=datetime.strptime("22:00:00","%H:%M:%S"):
            #correct
            return round(temp,2),0.0
        elif start_time<=datetime.strptime("05:00:00","%H:%M:%S") and end_time<=datetime.strptime("22:00:00","%H:%M:%S") and end_time>=datetime.strptime("05:00:00","%H:%M:%S") :
            day0nightdelta=datetime.strptime("05:00:00","%H:%M:%S")-start_time
            day0nightsec=day0nightdelta.total_seconds()
            day0night=day0nightsec/(60*60)
            day0night=round(day0night,2)
            day0daydelta=end_time-datetime.strptime("05:00:00","%H:%M:%S")
            day0daysec=day0daydelta.total_seconds()
            day0day=day0daysec/(60*60)
            day0day=round(day0day,2)
            return (day0day,day0night)
        # elif start_time>=datetime.strptime("22:00:00","%H:%M:%S") and end_time<=datetime.strptime("23:59:59","%H:%M:%S") :
        #     day0nightdelta=datetime.strptime("23:59:59","%H:%M:%S")-start_time
        #     day0nightsec=day0nightdelta.total_seconds()
        #     day0night=day0nightsec/(60*60)
        #     day0night=round(day0night,2)
        #     day0daydelta=end_time-datetime.strptime("05:00:00","%H:%M:%S")
        #     day0daysec=day0daydelta.total_seconds()
        #     day0day=day0daysec/(60*60)
        #     day0day=round(day0day,2)
        #     return (day0day,day0night)
            
        elif end_time<=datetime.strptime("23:59:59","%H:%M:%S") and start_time>=datetime.strptime("22:00:00","%H:%M:%S"):
            day0day=0.0
            # day0night=temp
            # print("hello")
            day0night=round(temp,2)
            return day0day, day0night
            
        elif end_time<=datetime.strptime("23:59:59","%H:%M:%S") and start_time>=datetime.strptime("05:00:00","%H:%M:%S"):

            day0nightdelta=end_time - datetime.strptime("22:00:00","%H:%M:%S")
            day0nightsec=day0nightdelta.total_seconds() 
            day0night=day0nightsec/(60*60)
            day0night=round(day0night,2)
            day0day=temp-day0night
            # print('reached here')
            return day0day,day0night
        elif start_time<=datetime.strptime("05:00:00","%H:%M:%S") and end_time<=datetime.strptime("05:00:00","%H:%M:%S"):
          #this is correct
            day0day=0.0
            day0night=round(temp,2)
            return day0day, day0night
        
path="./"
file_list = glob.glob(path + "//*.xlsx")
print(file_list)

#<================    ==================>#
if __name__=="__main__":
    res=[]
    for file in file_list:
        org=pd.read_excel(file)
        OTdf=org[~org['Over Time- In (IST)'].isna()]
        OTdf=org[org['Approved/Not Approved']=='Approved']
        OTdf=OTdf[~OTdf['Over Time- In (IST)'].isna()]
        OTdf=OTdf[OTdf['Over Time- In (IST)']!='00:00:00']
        df_calculate_total_OT = OTdf[OTdf['Sub-Status']=='Present']
        df_calculate_weekdayOT=df_calculate_total_OT[df_calculate_total_OT['Status']=='Weekday']
        df=org.iloc[0:1,0:6]
        del df['Date']
        try:
            df_calculate_weekdayOT['Weekday Regular Ot'] = df_calculate_weekdayOT.apply(lambda x: calculateRNTOT(str(x['Over Time- In (IST)']), str(x['Over Time-Out(IST)']))[0], axis=1)
        except:
            stdout.write(Fore.YELLOW + '\n NaN values Encountered in Weekday regular OT, setting it to zero\n')
            df_calculate_weekdayOT['Weekday Regular Ot']=0.0
        try:
            df_calculate_weekdayOT['Weekday Night Ot'] = df_calculate_weekdayOT.apply(lambda x: calculateRNTOT(str(x['Over Time- In (IST)']), str(x['Over Time-Out(IST)']))[1], axis=1)
        except:
            stdout.write(Fore.YELLOW + '\nSome NaN values Encountered in Weekday Night OT, setting it to zero\n')
            df_calculate_weekdayOT['Weekday Night Ot']=0.0
        df_calculate_holidayOT=df_calculate_total_OT[df_calculate_total_OT['Status']=='Holiday']
        try:
            df_calculate_holidayOT['Holiday Regular Ot'] = df_calculate_holidayOT.apply(lambda x: calculateRNTOT(str(x['Over Time- In (IST)']), str(x['Over Time-Out(IST)']))[0], axis=1)
        except:
            stdout.write(Fore.YELLOW + '\nSome NaN values Encountered in Holiday regular OT, setting it to zero\n')
            df_calculate_holidayOT['Holiday Regular Ot']=0.0
        try:
            df_calculate_holidayOT['Holiday Night Ot'] = df_calculate_holidayOT.apply(lambda x: calculateRNTOT(str(x['Over Time- In (IST)']), str(x['Over Time-Out(IST)']))[1], axis=1)
        except:
            stdout.write(Fore.YELLOW + '\nSome NaN values Encountered in Holiday Night OT, setting it to zero\n')
            df_calculate_holidayOT['Holiday Night Ot']=0.0
        sum_of_holiday_day_ot=df_calculate_holidayOT['Holiday Regular Ot'].sum()
        sum_of_holiday_night_ot=df_calculate_holidayOT['Holiday Night Ot'].sum()
        df_calculate_weekendOT=df_calculate_total_OT[df_calculate_total_OT['Status']=='Weekend']
        try:
            df_calculate_weekendOT['weekend Regular Ot'] = df_calculate_weekendOT.apply(lambda x: calculateRNTOT(str(x['Over Time- In (IST)']), str(x['Over Time-Out(IST)']))[0], axis=1)
        except:
            stdout.write(Fore.YELLOW + '\nSome NaN values Encountered in Weekend regular OT, setting it to zero\n')
            df_calculate_weekendOT['weekend Regular Ot']=0.0
        try:    
            df_calculate_weekendOT['weekend Night Ot'] = df_calculate_weekendOT.apply(lambda x: calculateRNTOT(str(x['Over Time- In (IST)']), str(x['Over Time-Out(IST)']))[1], axis=1)
        except:
            stdout.write(Fore.YELLOW + '\nSome NaN values Encountered in Weekend night OT, setting it to zero\n')
            df_calculate_weekendOT['weekend Night Ot']=0.0
        df_sum_of_weekend_Regular_ot=df_calculate_weekendOT['weekend Regular Ot'].sum()
        df['Weekend regular OT']=df_sum_of_weekend_Regular_ot
        df_sum_of_weekend_night_ot=df_calculate_weekendOT['weekend Night Ot'].sum()
        df['Weekend night OT']=df_sum_of_weekend_night_ot
        df_sum_of_weekday_regular_ot=df_calculate_weekdayOT['Weekday Regular Ot'].sum()
        df_sum_of_weekday_night_ot=df_calculate_weekdayOT['Weekday Night Ot'].sum()
        df['Weekday regular OT']=df_sum_of_weekday_regular_ot
        df['Weekday night OT']=df_sum_of_weekday_night_ot
        sum_of_holiday_day_ot=df_calculate_holidayOT['Holiday Regular Ot'].sum()
        sum_of_holiday_night_ot=df_calculate_holidayOT['Holiday Night Ot'].sum()
        df['Holiday day OT']=sum_of_holiday_day_ot
        df['Holiday Night OT']=sum_of_holiday_night_ot
        df['Total OT']=df['Holiday day OT']+df['Holiday Night OT']+df['Weekday night OT']+df['Weekday regular OT']+df['Weekend night OT']+df['Weekend regular OT']
        res.append(df)

    excl_merged = pd.DataFrame()
    for excl_file in res:
        excl_merged = excl_merged.append(
        excl_file, ignore_index=True)
    # del excl_merged['Status']

    result_path="./"
    excl_merged.to_excel(result_path+"testRes.xlsx")


    stdout.write(Fore.GREEN + '\nFinished compiling the result.\nPress any key to exit...')
    ex=input()