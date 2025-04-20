# Airline Ticketing API

This project is an airline ticketing system developed using Python (Flask). It provides core functionalities such as flight management, user authentication, ticket purchasing, check-in, and flight querying with JWT-based authentication. The API is hosted on Render.com and uses PostgreSQL for the database.

---

## Technologies Used

| Technology        | Description                                     |
|-------------------|-------------------------------------------------|
| Python            | Main development language                       |
| Flask             | Web framework                                   |
| Flask-JWT-Extended | JWT-based authentication                       |
| Flask-Migrate     | Database migrations                             |
| PostgreSQL        | Cloud database (hosted on Render)               |
| SQLAlchemy        | ORM (Object-Relational Mapper)                  |
| DTO & Service     | Layered architecture (data transfer & service)  |
| Swagger (Flasgger)| API documentation                               |
| Render.com        | Hosting service for the API and database        |

---

## 🗂️ Project Structure

```
airline-api/
│
├── app/
│   ├── models/               # SQLAlchemy models
│   ├── services/             # Application logic (business layer)
│   ├── dtos/                 # Data Transfer Objects
│   ├── controllers/          # Blueprint API endpoints
│   ├── routes/               # Additional route definitions
│   ├── extensions.py         # db, jwt, and other extensions
│   └── __init__.py           # Application creator
│
├── config.py                 # Application configuration
├── run.py                    # Application launcher
├── .env                      # Environment variables
├── requirements.txt          # Required dependencies
├── Procfile                  # Render deployment file
└── README.md                 # This file
```

---

## 🛢️ Database (Render PostgreSQL)

- PostgreSQL hosted on Render is used.
- The `DATABASE_URL` is stored in the `.env` file.

### 📋 ER Model (Entity Relationship)

```text
User
- id (PK)
- username
- password

Flight
- id (PK)
- departure
- arrival
- date
- quota

Ticket
- id (PK)
- user_id (FK)
- flight_id (FK)
- seat_number


Checkin
- id (PK)
- ticket_id (FK)
- checkin_time
```

---

## 🧪 Swagger API Documentation

You can explore the API documentation via:

[Swagger API Documentation](https://airline-api-lx1v.onrender.com/swagger/)

---

## 🛡️ Auth (JWT)

- Users obtain a JWT token after logging in.
- Bearer token is required for all secure endpoints.

---

## 🧾 DTO & Service Structure

- **DTO (Data Transfer Object)**: Templates for request and response data, used for transferring data between controller and service.
- **Service**: Contains the business logic, independent of the controller.

**Example DTO:**
```python
class AddFlightDTO:
    def __init__(self, departure, arrival, date, quota):
        self.departure = departure
        self.arrival = arrival
        self.date = date
        self.quota = quota
```

**Example Service:**
```python
class FlightService:
    def add_flight(dto: AddFlightDTO):
        ...
```

---

## ✈️ API Features

- `POST /api/v1/auth/login` → User login
- `POST /api/v1/flight/add` → Add flight (JWT required)
- `POST /api/v1/ticket/buy` → Buy a ticket
- `POST /api/v1/checkin/{ticket_id}` → Check-in process
- `GET /api/v1/flights/query` → Flight search
- `GET /api/v1/flights/passengers/{flight_id}` → Flight passengers list

---

## 📌 Notes

- The free Render plan may cause a delay of up to 50 seconds when starting the API due to inactivity.
- All operations are isolated in service layers.
- API versioning is set to `v1`.

---
