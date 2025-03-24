
from ics import Calendar, Event
from datetime import datetime, timedelta
from dateutil.rrule import rrule, MONTHLY

# Define event details
event_name = "MeshCentral Monthly Community Meeting"
event_description = (
    "Monthly community meeting for the MeshCentral community.\n\n"
    "Meeting link will be provided before the meeting\n\n"
    "More details: https://github.com/Ylianst/MeshCentral/wiki/Community-Monthly-Meetings"
)
event_location = "Online"
event_start_time = datetime(2025, 2, 27, 14, 0)  # Start on Feb 27, 2025, at 14:00 UTC
event_duration = timedelta(hours=1)  # 1-hour event

# Create an ICS calendar
calendar = Calendar()
calendar.creator = "MeshCentral Community"
calendar.method = "PUBLISH"

# Create a single recurring event
event = Event()
event.uid = "meshcentral-monthly-meeting"
event.name = event_name
event.begin = event_start_time
# Add RRULE for fourth Thursday of each month for 2 years
event.extra.append(
    Event.Extra(name="RRULE", value="FREQ=MONTHLY;COUNT=24;BYDAY=4TH;BYDAY=TH")
)
event.duration = event_duration
event.location = event_location
event.description = event_description
event.created = datetime.now()
event.status = "CONFIRMED"
event.transparent = True  # Does not block time in calendar
event.url = "https://github.com/Ylianst/MeshCentral/wiki/Community-Monthly-Meetings"

# Add image attachment
with open("meshagent-circle.png", "rb") as image_file:
    event.attach(image_file.read(), "meshagent-circle.png")

calendar.events.add(event)

# Save the ICS file
ics_file_path = "meshcentral_meetings.ics"
with open(ics_file_path, "w") as f:
    f.writelines(calendar)

print(f"Calendar saved as: {ics_file_path}")
