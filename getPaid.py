from __future__ import print_function
from pyrfc3339 import generate, parse
import pytz
from datetime import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)


def revenue(periodStart, periodEnd, payRate):  # Strings in form MM/DD/YY
    service = build('calendar', 'v3', credentials=creds)

    periodStartDateTime = datetime.strptime(periodStart, "%m/%d/%Y")
    periodEndDateTime = datetime.strptime(periodEnd, "%m/%d/%Y")

    rfcStart = generate(periodStartDateTime, accept_naive=True)
    rfcEnd = generate(periodEndDateTime, accept_naive=True)

    events_result = service.events().list(calendarId='primary', timeMin=rfcStart,
                                          timeMax=rfcEnd,
                                          maxResults=50, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    total = 0

    for event in events:
        if (event['summary'] == "Event Title"):
            startTime = event['start']['dateTime']
            endTime = event['end']['dateTime']

            startDateTime = parse(startTime)
            endDateTime = parse(endTime)

            dateTimeDifference = endDateTime - startDateTime
            dateTimeDifferenceInHours = dateTimeDifference.total_seconds() / 3600

            total += dateTimeDifferenceInHours
    return(total*payRate)

pStart = input("Enter pay period start (mm/dd/yyyy): ")
pEnd = input("Enter pay period end (mm/dd/yyyy): ")

print("You should earn $"+str(revenue(pStart, pEnd, payRate)))
