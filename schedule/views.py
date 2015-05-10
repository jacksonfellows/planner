from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
import datetime, calendar
from schedule.models import Event


def planner(request, y, m, d):
	template = loader.get_template('schedule/index.html')

	try:
		day_of_week = calendar.weekday(int(y), int(m), int(d))
	except :
		if d == "0":
			m = int(m) - 1
			x = calendar.monthrange(int(y), int(m))
			d = x[1]
		else:
			m = int(m) + 1
			d = 1

		return HttpResponseRedirect("/"+str(y)+"/"+str(m)+"/"+str(d)+"/")

	if int(day_of_week) == 0: day_of_week_string = "Monday"
	elif int(day_of_week) == 1: day_of_week_string = "Tuesday"
	elif int(day_of_week) == 2: day_of_week_string = "Wednesday"
	elif int(day_of_week) == 3: day_of_week_string = "Thursday"
	elif int(day_of_week) == 4: day_of_week_string = "Friday"
	elif int(day_of_week) == 5: return planner(request, y, m, int(d)+2)
	elif int(day_of_week) == 6: return planner(request, y, m, int(d)-2)

	classes_list = []

	for i in Event.objects.all():
		if i.day == day_of_week_string:
			classes_list.append(i)

	context = RequestContext(request, {
		'day_plus': int(d)+1,
		'day_minus': int(d)-1,
		'date': day_of_week_string,
		'real_month': m,
		'classes_list': classes_list,
		'year': y,
		'month': int(m)-1,
		'day': d,
		})

	return HttpResponse(template.render(context))

def planner_recent(request):
	date = datetime.datetime.now()
	y = date.year
	m = date.month
	d = date.day

	return HttpResponseRedirect("/"+str(y)+"/"+str(m)+"/"+str(d)+"/")