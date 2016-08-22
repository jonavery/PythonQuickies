day = str(raw_input("Enter 'day' as MMDDYYYY to get its day of the week: "))
m = int(day[0:2])
q = int(day[2:4])
Y = int(day[4:8])
if m < 3:
	m += 12
	Y -= 1
h = (q + ((13* (m+1))/5) + Y + (Y/4) - (Y/100) + (Y/400)) % 7
print("On %s/%s/%s it was the %d day of the week." % (day[0:2], day[2:4], day[4:8], h))
print("0=Saturday, 1=Sunday, 2=Monday, 3=Tuesday...6=Friday")
