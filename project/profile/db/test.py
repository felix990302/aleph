from Connector import Connection
from main import guessLocation

conn = Connection("18.216.32.253", "root", "password", "test")

rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]

conn.insert("Login", rows, values)

print(conn.query("Login", "*", conditions=["username <> 'SIU'"] ,order=["username", "ASC"]))


conn.update("Login", ["username='Poo'", "hashedpw='PLOP'"], ["username='David'"])

print(conn.query("Login", "*"))


conn.delete("Login", ['''username="Poo"'''])

print(conn.query("Login", "*"))

print(guessLocation(100113))


print(conn.query("Frequency", ["frequency"], ["userID=100113", "location='MC'"]))