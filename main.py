from ics import Calendar, Event
from datetime import datetime, timedelta
from dateutil.rrule import rrule, MONTHLY, TH
from tzlocal import get_localzone
import pytz
import hashlib

# Define event details
event_name = "MeshCentral Monthly Community Meeting"
event_description = (
    "Monthly community meeting for the MeshCentral community.\n\n"
    "Join the meeting: https://meet.evoludata.com/rooms/zm9-wx7-t07-xbu/join\n\n"
    "More details: https://github.com/Ylianst/MeshCentral/wiki/Community-Monthly-Meetings"
)
event_location = "Online (https://meet.evoludata.com/rooms/zm9-wx7-t07-xbu/join)"
event_duration = timedelta(hours=1)

# UTC start time
utc = pytz.utc
event_start_utc = utc.localize(datetime(2025, 2, 27, 14, 0))  # Feb 27, 2025, 14:00 UTC

# Get local timezone
local_tz = get_localzone()

# Generate recurring dates (fourth Thursday of each month for 2 years)
recurrence_rule = rrule(MONTHLY, dtstart=event_start_utc, count=24, byweekday=TH(4))

# Create an ICS calendar
calendar = Calendar()
calendar.creator = "MeshCentral Community"
calendar.method = "PUBLISH"

# Add events
for utc_dt in recurrence_rule:
    local_dt = utc_dt.astimezone(local_tz)
    event = Event()
    event.name = event_name
    event.begin = local_dt.isoformat()
    event.duration = event_duration
    event.location = event_location
    event.description = event_description
    event.created = datetime.now(local_tz)
    event.status = "CONFIRMED"
    event.transparent = True
    event.url = "https://github.com/Ylianst/MeshCentral/wiki/Community-Monthly-Meetings"

    # Generate a consistent UID based on event details
    uid_data = f"{event_name}-{local_dt.isoformat()}-{event_location}"
    event.uid = hashlib.md5(uid_data.encode()).hexdigest() + "@meshcentral.org"

    calendar.events.add(event)

# Save the ICS file
ics_file_path = "meshcentral_meetings.ics"
with open(ics_file_path, "w") as f:
    f.writelines(calendar)

print(f"Calendar saved as: {ics_file_path}")
