# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T):
    minute = 60
    hour = minute*60
    day = hour*24


    seconds = T%60
    remaining_time = T-seconds

    minutes_as_seconds = remaining_time%hour
    minutes = minutes_as_seconds/minute
    
    hours_as_seconds=remaining_time-minutes_as_seconds
    hours = hours_as_seconds / hour

    formatted_time = f"{int(hours)}h{int(minutes)}m{int(seconds)}s"

    return formatted_time
