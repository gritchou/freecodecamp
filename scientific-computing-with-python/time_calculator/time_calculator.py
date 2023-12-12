def add_time(start, duration, day_of_week=None):
  # Dictionary to convert day of the week to an integer and vice versa
  days_of_week = {
      "Sunday": 0,
      "Monday": 1,
      "Tuesday": 2,
      "Wednesday": 3,
      "Thursday": 4,
      "Friday": 5,
      "Saturday": 6,
      0: "Sunday",
      1: "Monday",
      2: "Tuesday",
      3: "Wednesday",
      4: "Thursday",
      5: "Friday",
      6: "Saturday"
  }

  # Parsing the start time and duration
  start_hours, start_minutes = map(int, start[:-3].split(':'))
  am_pm = start[-2:]
  duration_hours, duration_minutes = map(int, duration.split(':'))

  # Convert start time to 24-hour format
  if am_pm == "PM":
    start_hours += 12

  # Adding duration to start time
  total_hours = start_hours + duration_hours
  total_minutes = start_minutes + duration_minutes

  # Adjust for extra hours from minutes
  total_hours += total_minutes // 60
  total_minutes %= 60

  # Calculate days passed and adjust hours to 24-hour format
  days_passed = total_hours // 24
  total_hours %= 24

  # Convert back to 12-hour format and determine AM or PM
  new_am_pm = "AM" if total_hours < 12 else "PM"
  total_hours = 12 if total_hours == 0 or total_hours == 12 else total_hours % 12

  # Format the new time
  new_time = f"{total_hours}:{total_minutes:02d} {new_am_pm}"

  # Add day of the week if provided
  if day_of_week:
    day_index = (days_of_week[day_of_week.capitalize()] + days_passed) % 7
    new_day = days_of_week[day_index]
    new_time += f", {new_day}"

  # Add information about the number of days passed
  if days_passed == 1:
    new_time += " (next day)"
  elif days_passed > 1:
    new_time += f" ({days_passed} days later)"

  return new_time
