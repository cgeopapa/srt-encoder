import sys, os, re

# Convert total seconds into hours, min, sec and milli sec
def sec_to_time(sec):
    hours = int(sec / 3600)
    minutes =  int((sec % 3600) / 60)
    seconds = int(sec % 3600 % 60)
    milli = int(1000*round(sec - int(sec),3))
    if sec<0:
        return None,None,None,None
    return hours,minutes,seconds,milli

# Convert hours, min, sec and milli sec to total sec
def time_to_sec(h,m,s,ms):
    return float(h*3600+m*60+s+ms/60.0)

# Function to convert frame number to corresponding minutes and seconds
def frame_to_time(frame, frame_rate, span=0):
    sec = int(frame)/float(frame_rate)
    if span!=0:
        temp = span
        try:
            neg = temp.split("-")[1]
        except:
            neg = None
        h = int(span.split(":")[0])
        m = int(span.split(":")[1])
        s = int(span.split(":")[2])
        ms = int(span.split(":")[3])
        span = time_to_sec(abs(h),m,s,ms)
        if neg!=None:
            span = -span
    hours,minutes,seconds,milli = sec_to_time(sec+span)
    if hours != None:
        return "%02d:%02d:%02d,%s" % (hours,minutes,seconds,milli)
    else:
        return None

# Function to convert sub format to srt
def sub_to_srt(sub,srt,frame_rate,span=0):
    line_count = 0
    out_file = open(srt, "w")
    # Read sub file line by line
    for line in open(sub):
        line_count +=1
        try:
            start_frame, end_frame, text = re.findall(r"\{(\d+)\}\{(\d+)\}(.*)$", line)[0]
        except:
            continue
        start_time = frame_to_time(start_frame, frame_rate,span)
        end_time = frame_to_time(end_frame, frame_rate,span)
        # Write to file
        if start_time != None or end_time != None:
            out_file.write("%d\n%s --> %s\n%s\n\n" %(line_count,start_time,end_time,text.strip().replace("|", "\n")))
    out_file.close()
