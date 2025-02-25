from ics import Calendar, Event
from datetime import datetime, timedelta
from dateutil.rrule import rrule, MONTHLY

# Define event details
event_name = "MeshCentral Monthly Community Meeting"
event_description = (
    "Monthly community meeting for MeshCentral users and contributors.\n\n"
    "More details: https://github.com/Ylianst/MeshCentral/wiki/Community-Monthly-Meetings"
)
event_location = "Online"
event_start_time = datetime(2025, 2, 27, 14, 0)  # Start on Feb 27, 2025, at 14:00 UTC
event_duration = timedelta(hours=1)  # 1-hour event

# Generate recurring dates (fourth Thursday of each month for 2 years)
recurrence_rule = rrule(MONTHLY, dtstart=event_start_time, count=24, byweekday=3, bysetpos=4)

# Create an ICS calendar
calendar = Calendar()
calendar.creator = "MeshCentral Community"
calendar.method = "PUBLISH"

# Add events to the calendar
for event_date in recurrence_rule:
    event = Event()
    event.name = event_name
    event.begin = event_date.isoformat()
    event.duration = event_duration
    event.location = event_location
    event.description = event_description
    event.created = datetime.now()
    event.status = "CONFIRMED"
    event.transparent = True  # Does not block time in calendar
    event.url = "https://github.com/Ylianst/MeshCentral/wiki/Community-Monthly-Meetings"
    calendar.events.add(event)

# Save the ICS file
ics_file_path = "meshcentral_meetings.ics"
with open(ics_file_path, "w") as f:
    f.writelines(calendar)

print(f"Calendar saved as: {ics_file_path}")
