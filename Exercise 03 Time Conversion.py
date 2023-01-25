secs = eval(input("Enter the number of seconds:\n"))

secs = secs % (24 * 3600)
h = secs // 3600
secs %= 3600
mins = secs // 60
secs %= 60

print(f'{h:d}:{mins:02d}:{secs:02d}')