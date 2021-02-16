# HUUM sauna controller

GET - api.huum.eu/action/home/status - returns your current sauna status
POST - api.huum.eu/action/home/start?tartetTemperature=80 - wants targetTemperature as a parameter, which must be a number between 40 and 110, turns on the sauna for 3h
POST - api.huum.eu/action/home/stop - turns off the sauna
Basic authentication should be used and all requests must be over a https connection. The username and password are the same as in the app and the user must be connected to a sauna.
All requests return the current state of the sauna in JSON: ({"statusCode": 232, "door": true, "temperature": "23", "targetTemperature": "50", "startDate": 1507184846, "endDate": 1507184846, "duration": 0, "config": 2, "steamerError": 0, "paymentEndDate" : SOMEDATE})
statusCode:
  230 - sauna offline
  231 - online and heating
  232 sauna online but not heating
  233 sauna is beeing used by another user and is locked
  400 sauna is put to emergency stop
door: 
  true - the door is closed
  false - the door is open and sauna can't be started
temperature: The current temperature of the sauna
targetTemperature: The temperature the sauna is trying to reach
startDate: heating start time in UNIX
endDate: heating end time
duration: time of the remaining heating period
config: 
  2 shows that the controller is configured to use a light system
  1 shows that the controller is configured to use a steamer system
  3 shows that the controller is configured to use both the light and steamer system .
steamerError: if 1 then the steamer is empty of water and needs to be refilled also no steamer start is allowed
paymentEndDate: shows the date when the payment period is ending. Only relevant for GSM controllers with our SIM card.
