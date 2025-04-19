# MeshCentral Monthly Community Meeting Calendar Generator

This project generates an ICS calendar file for the MeshCentral Monthly Community Meetings. The calendar includes recurring events for the fourth Thursday of each month over a two-year period.

## Prerequisites

1. **Python 3.11+**: Ensure you have Python installed. You can check your version by running:
   ```bash
   python3 --version
   ```
   If not installed, download it from [python.org](https://www.python.org/).

2. **Virtual Environment (Optional but Recommended)**: Use a virtual environment to manage dependencies.

## Setup Instructions

1. **Clone or Download the Project**:
   Navigate to the project directory:
   ```bash
   cd /Users/apple/Documents/Me/MeshCentral-Monthly-Community-Meeting
   ```

2. **Create and Activate a Virtual Environment**:
   - Create the virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   Install the required Python packages:
   ```bash
   pip install ics python-dateutil pytz tzlocal
   ```
   Note: The `hashlib` library is part of Python's standard library and does not require separate installation.

4. **Run the Script**:
   Execute the script to generate the ICS file:
   ```bash
   python main.py
   ```

5. **Output**:
   The script will generate a file named `meshcentral_meetings.ics` in the project directory. You will see a confirmation message:
   ```
   Calendar saved as: meshcentral_meetings.ics
   ```

6. **Open the ICS File**:
   Import the `meshcentral_meetings.ics` file into your preferred calendar application to view the events.

## Deactivate the Virtual Environment (Optional)

When you're done, deactivate the virtual environment by running:
```bash
deactivate
```

## License

This project is licensed under the MIT License.