# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
        {'id': 1,
        'first_name': u'Тетяна',
        'last_name': u'Оберишин',
        'ticket': 254,
        'image': 'img/me.jpg'},
        {'id': 2,
        'first_name': u'Оля',
        'last_name': u'Якубовська',
        'ticket': 212,
        'image': 'img/me2.jpg'},
        {'id': 3,
        'first_name': u'Ірина',
        'last_name': u'Кравець',
        'ticket': 213,
        'image': 'img/me3.jpg'},
    )
    return render(request, 'students/students_list.html', 
        {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


