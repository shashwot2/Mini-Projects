def make_readable(seconds):
    temp_sec = seconds
    minutes = int((seconds / 60) % 60)
    hours = int(seconds / 3600)
    seconds = int(temp_sec % 3600)
    if seconds >= 60:
        seconds = seconds % 60
    return str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)

print(make_readable(60))
