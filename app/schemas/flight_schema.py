from marshmallow import Schema, fields

class FlightSchema(Schema):
    flight_number = fields.Str(required=True)
    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)
    airport_from = fields.Str(required=True)
    airport_to = fields.Str(required=True)
    duration = fields.Int(required=True)
    capacity = fields.Int(required=True)
