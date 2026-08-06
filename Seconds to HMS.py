#Seconds to HMS

#Write a program that takes an integer number of seconds ( e.g.. 8645) and converts it into hours, minutes, and seconds, formatted as HH : MM : SS

def format_seconds(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}: {m:02d} :{s:02d}"
