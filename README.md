![python](https://img.shields.io/badge/version-1.0-green)

# getPaid

This tool calculates total earnings in a given pay period using Google Calendar APIs

## Getting Started

### Installing

This project is rough around the edges and can only be run through the command line.

Download getPaid-master to a directory of your choice:

```
~/Users/USERNAME/Desktop/carpool-for-gh
```

### Dependencies
`google-api-python-client`

`google-auth`

`google-auth-httplib2`

`google-auth-oauthlib`

`google-calendar-api-client-python`

`pyrfc3339`

Install these using pip or however your IDE handles libraries.

### Setup
Follow instructions [https://developers.google.com/calendar/quickstart/python](here) to authenticate the Google Calendar API

## Usage
Enter the pay rate as the third argument in the function call in line 50

Enter the calendar event title in line 34

Run getPaid.py

Enter the pay period start date in mm/dd/yyyy format

Enter the pay period end date in mm/dd/yyyy format

## Built With

* [Java](https://java.com/en/download/)
* [Google APIs](https://developers.google.com/products/) - Map data analysis

## Authors

* **Cole McCorkle** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
