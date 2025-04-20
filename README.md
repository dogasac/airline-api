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

Here’s how you can format the section for the README to clearly represent the entities and their attributes, as well as the relationships between them:

---

## **Database Entities**

### **User**
- **id** (Primary Key): Unique identifier for each user.
- **username** (Unique, Not Null): The user's username, which must be unique.
- **password** (Not Null): The user's password.

### **Flight**
- **flight_number** (Primary Key): Unique identifier for each flight.
- **airport_from** (String, 50 characters): The departure airport.
- **airport_to** (String, 50 characters): The arrival airport.
- **date_from** (Date): The departure date.
- **date_to** (Date): The arrival date.
- **duration** (Integer): The flight duration in minutes.
- **capacity** (Integer): The total number of seats available on the flight.

### **Ticket**
- **id** (Primary Key, Auto Increment): Unique identifier for each ticket.
- **user_id** (Foreign Key referencing **User.id**): The user who purchased the ticket.
- **flight_number** (Foreign Key referencing **Flight.flight_number**): The flight that the ticket is for.
- **seat_number** (Integer, Not Null): The seat number assigned to the passenger.

### **Checkin**
- **id** (Primary Key): Unique identifier for each check-in record.
- **ticket_id** (Foreign Key referencing **Ticket.id**): The ticket associated with the check-in.
- **checkin_time** (Date, Not Null): The date when the passenger checked in.
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
