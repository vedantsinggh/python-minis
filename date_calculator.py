def add_time(start, duration, day=None):
	start_hour = int(start[:start.index(":")]) 
	start_minute = int(start[start.index(":") + 1:start.index(":") + 3])

	days = [
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday',
		'Sunday'
	]
	dayIndex = 0
	if day:
		for d in days:
			if d.lower() == day.lower():
				break
			dayIndex += 1
	isAM = True if start[-2:] == "AM" else False

	duration_hour = int(duration[:duration.index(":")]) 
	duration_minute = int(duration[duration.index(":") + 1:])
	end_hour = ((start_hour + duration_hour) + int((start_minute + duration_minute) / 60)) % 12
	rem_hour = int(((start_hour + duration_hour) + int((start_minute + duration_minute) / 60)) / 12)
	end_minute = (start_minute + duration_minute) % 60

	day_count = 0

	if rem_hour == 1 and not isAM:
		day_count = 1
	elif rem_hour > 1:
		day_count = 1 + int(rem_hour/2)
	if not (rem_hour % 2 == 0):
		isAM = not isAM

	req_day = days[((dayIndex + day_count) % 7)]

	time = ""

	time += "12" if end_hour == 0 else str(end_hour)
	time += ":"
	time += "0" + str(end_minute) if end_minute < 10 else str(end_minute) 
	time += " AM" if isAM else " PM"

	if not day == None:
		time += ", " + req_day
	if day_count == 1:
		time += " (next day)"
	if day_count > 1:
		time += f" ({day_count} days later)"

	return time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
