from django.db import models
import datetime

class Schedule(models.Model):
	def __init__(self, day, *args):
		self.day = day
		self.classes = args

class Event(models.Model):
	def __init__(self, event, name, start, end):
		self.event = event
		self.name = name
		self.end = end
		self.start = start

monday = Schedule("Monday", 
	Event("All School", "Check-In", datetime.time(hour=8, minute=30), datetime.time(hour=9, minute=0)),
	Event("All School", "Mentor Mt.", datetime.time(hour=9, minute=0), datetime.time(hour=9, minute=30)),
	Event("Humanities", "1 and 2", datetime.time(hour=9, minute=30), datetime.time(hour=10, minute=30)),
	Event("Math", "1B", datetime.time(hour=9, minute=30), datetime.time(hour=10, minute=30)),
	Event("Humanities", "3 and 4", datetime.time(hour=10, minute=30), datetime.time(hour=11, minute=45)),
	Event("Math", "2B and 3A", datetime.time(hour=10, minute=30), datetime.time(hour=11, minute=45)),
	Event("All School", "Lunch", datetime.time(hour=11, minute=45), datetime.time(hour=12, minute=30)),
	Event("Math", "1A and 3B", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("Spanish", "7", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("Math", "2A", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45)),
	Event("Spanish", "6", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45)),
	Event("WSH", "WSH", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45))
	)

tuesday = Schedule("Tuesday", 
	Event("Science", "1", datetime.time(hour=8, minute=30), datetime.time(hour=9, minute=30)),
	Event("WW", "1", datetime.time(hour=8, minute=30), datetime.time(hour=9, minute=30)),
	Event("All School", "Acad. Studio", datetime.time(hour=9, minute=30), datetime.time(hour=10, minute=30)),
	Event("Science", "2", datetime.time(hour=10, minute=30), datetime.time(hour=11, minute=45)),
	Event("WW", "2", datetime.time(hour=10, minute=30), datetime.time(hour=11, minute=45)),
	Event("All School", "Lunch", datetime.time(hour=11, minute=45), datetime.time(hour=12, minute=30)),
	Event("WW", "3 and 4", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("Science", "4", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45)),
	Event("WW", "5", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45))
	)

wednesday = Schedule("Wednesday", 
	Event("All School", "Com. Mt.", datetime.time(hour=8, minute=30), datetime.time(hour=9, minute=0)),
	Event("Book Discussion", "Discussion", datetime.time(hour=9, minute=0), datetime.time(hour=10, minute=00)),
	Event("Book Discussion", "Reading", datetime.time(hour=10, minute=00), datetime.time(hour=10, minute=30)),
	Event("Math", "2A", datetime.time(hour=10, minute=30), datetime.time(hour=11, minute=30)),
	Event("All School", "Lunch", datetime.time(hour=11, minute=30), datetime.time(hour=12, minute=30)),
	Event("Math", "2B", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("Spanish", "8", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("Spanish", "6", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45)),
	Event("PE", "A", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45))
	)

thursday = Schedule("Thursday", 
	Event("Humanities", "1 and 2", datetime.time(hour=8, minute=30), datetime.time(hour=9, minute=45)),
	Event("Math", "1B and 3B", datetime.time(hour=8, minute=30), datetime.time(hour=9, minute=45)),
	Event("All School", "Seminar", datetime.time(hour=9, minute=45), datetime.time(hour=10, minute=45)),
	Event("Humanities", "3 and 4", datetime.time(hour=10, minute=45), datetime.time(hour=11, minute=45)),
	Event("All School", "Lunch", datetime.time(hour=11, minute=45), datetime.time(hour=12, minute=30)),
	Event("Math", "1A", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("Spanish", "8", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("PE", "B", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("Math", "3A", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45)),
	Event("Spanish", "7", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45)),
	Event("PE", "C", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45))
	)

friday = Schedule("Friday", 
	Event("WW", "3 and 4", datetime.time(hour=8, minute=30), datetime.time(hour=9, minute=45)),
	Event("Science", "4", datetime.time(hour=9, minute=45), datetime.time(hour=11, minute=00)),
	Event("WW", "5", datetime.time(hour=9, minute=45), datetime.time(hour=11, minute=00)),
	Event("All School", "Acad. Studio", datetime.time(hour=11, minute=00), datetime.time(hour=11, minute=45)),
	Event("All School", "Lunch", datetime.time(hour=11, minute=45), datetime.time(hour=12, minute=30)),
	Event("Science", "1", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("WW", "1", datetime.time(hour=12, minute=30), datetime.time(hour=13, minute=40)),
	Event("Science", "2", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45)),
	Event("WW", "2", datetime.time(hour=13, minute=40), datetime.time(hour=14, minute=45))
	)