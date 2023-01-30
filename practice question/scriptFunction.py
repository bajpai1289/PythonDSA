from datetime import datetime
def calculateRNTOT(string_start,string_end)->tuple[float,float]: #return Value would be of the format (Regular OT hour,night time OT hour)
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
    if start_time>datetime.strptime("22:00:00","%H:%M:%S") and end_time<datetime.strptime("23:59:59","%H:%M:%S"):
        delta3 =  end_time -start_time
        sec3 = delta3.total_seconds()
        hours3 = sec3 / (60 * 60)
        x=round(hours3,2)
        
    if temp>0:
        end_time_same_day = datetime.strptime("22:00:00","%H:%M:%S")
        delta_rune=end_time_same_day-start_time
        sec_rune=delta_rune.total_seconds()
        hour_rune=sec_rune/(60*60)
        temp_rune=round(hour_rune,2)
        if temp_rune<0:
            return (0.0,temp_rune+temp-temp_rune)
        elif (temp-temp_rune)<0:
            return (temp_rune+temp-temp_rune,0.0)
        else: return (temp_rune,temp-temp_rune)
    else:
        temp+=24
        # return('Total OT in hours:', temp)
    if start_time<datetime.strptime("22:00:00","%H:%M:%S"):
        start_time2 = datetime.strptime(string_start, "%H:%M:%S")
        end_time2 = datetime.strptime("22:00:00", "%H:%M:%S")
        delta2 =  end_time2 -start_time2
        sec2 = delta2.total_seconds()
        hours2 = sec2 / (60 * 60)
        x=round(hours2,2)
        # return (x)
        #night OT hour is: temp-x 
        #regular OT hour is x
        # return('The regular OT hour is: ', x)
        return (x,temp-x)
    else:
        return (0.0 ,temp)
    
print(calculateRNTOT('14:00:00','17:30:00'))