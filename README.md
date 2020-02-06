# EarthquakeDetectorAPI
The purpose of this project was to create a simple API that could be used by an earthquake detector to register any
occurrence. It is developed using Python 3, Flask and uses a local MySQL database. Although it is a pretty simple 
project, the main objective was to keep learning Python and improving my programming skills.

## Getting started 
To get a copy of this repository, you need to install Git and using the command line you can enter the following command:
```
$ git clone https://github.com/Andres710/EarthquakeDetectorAPI.git
```

### Prerequisites
In order to use this project, you need Python and pip. You can download both [here](https://www.python.org/downloads/).
Additionally, this project uses a MySQL database, so you need to install MySQL in your local environment. Another 
option is to use any database of your preference, but you have to adjust the database connection in `app.py`.

### Installation
This project has a `requirements.txt ` file which has the required dependencies for this project. Use it to install the
them, just enter the following command:
```
$ pip install -r requirements.txt
```

### Running 
Go to the root directory and run:
```
$ python app.py
```

## Endpoints
These are the different endpoints exposed by the API

### Get all earthquakes
```html
GET /earthquakes
```
#### Description
Returns a list of all earthquakes. Accepts filters for city and country.

#### Parameters
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `country` | `string` | **Query param - Optional**. Name of the country |
| `city` | `string` | **Query param - Optional**. Name of the city |

#### Return format
A list with earthquake objects in JSON representation.
```javascript
[
  {
    "city": "Bogota",
    "country": "Colombia",
    "date": "29/01/2020",
    "id": 1,
    "magnitude": 4.0,
    "time": "16:04"
  },
  {
    "city": "Guayaquil",
    "country": "Ecuador",
    "date": "30/01/2020",
    "id": 2,
    "magnitude": 5.4,
    "time": "08:48"
  },
  {
    "city": "Rome",
    "country": "Italy",
    "date": "30/01/2020",
    "id": 3,
    "magnitude": 7.5,
    "time": "08:51"
  }
]
```

### Get an earthquake
```html
GET /earthquakes/:identifier
```

#### Description
Gets an specific earthquake given an identifier 

#### Parameters
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `identifier` | `int` | **Path param - Required**. Id of the earthquake |

#### Return format 
The JSON representation of the searched earthquake.
 ```javascript
{
  "city": "Bogota",
  "country": "Colombia",
  "date": "29/01/2020",
  "id": 1,
  "magnitude": 4.0,
  "time": "16:04"
}
```

### Get strongest earthquake
```html
GET /earthquakes/strongest
```

#### Description
Gets the earthquake with the highest magnitude

#### Return format 
The JSON representation of the strongest earthquake.
```javascript
{
  "city": "Rome",
  "country": "Italy",
  "date": "30/01/2020",
  "id": 3,
  "magnitude": 7.5,
  "time": "08:51"
}
```

### Get weakest earthquake
```html
GET /earthquakes/weakest
```

#### Description
Gets the earthquake with the lowest magnitude

#### Return format 
The JSON representation of the weakest earthquake.
```javascript
{
  "city": "Bogota",
  "country": "Colombia",
  "date": "29/01/2020",
  "id": 1,
  "magnitude": 4.0,
  "time": "16:04"
}
```

### Get average magnitude
```html
GET /earthquakes/average
```

#### Description
Gets the average magnitude taking into account all earthquakes

#### Return format
JSON object containing the average magnitude of all the earthquakes and the total number of earthquakes.
```javascript
{
  "average_magnitude": 5.875,
  "number_of_earthquakes": 4
}
```

### Register earthquake
```html
POST /earthquakes
```

#### Description
Registers a new earthquake with the information received.

#### Parameters
There should be an earthquake in JSON format attached to the body of the request:
```javascript
{
  "country": "Country where the earthquake ocurred.",
  "city": "City where the eartquake ocurred.",
  "date": "Date of ocurrence (DD/MM/YYYY)",
  "time": "Time of ocurrence (HH/MM in 24-hour clock.)",
  "magnitude": Magnitude of the earthquake
}
```

#### Return format
JSON representation of the earthquake object that has been created.
```javascript
{
  "city": "Madrid",
  "country": "Spain",
  "date": "07/10/2019",
  "id": 7,
  "magnitude": 7.7,
  "time": "15:25"
}
```

### Remove an earthquake
```html
DELETE /earthquakes/:identifier
```

#### Description 
Removes the earthquake with the given identifier.

#### Parameters
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `identifier` | `int` | **Path param - Required**. Id of the earthquake |
