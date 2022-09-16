from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *

from django.views.decorators.csrf import csrf_exempt

from django.core import serializers
from django.http import JsonResponse

from datetime import datetime
import calendar
from datetime import datetime, timedelta, time

# Create your views here.


@csrf_exempt
def docshowbydept(request):

    dept_id = request.POST.get('dept_id')
    print(dept_id)
    print(type(dept_id))

    dept_id = int(dept_id)

    doctor_list = Doctorprofile.objects.filter(connection_depertment=dept_id)
    doctor_list_ls = Doctorprofile.objects.filter(pk=dept_id)

    print('doctor_list', doctor_list)

    # doctor_list_ls = doctor_list_ls
    print('doctor_list_ls',doctor_list_ls)

    # doctor_list_ls = list(doctor_list)

    request.session['dept_id'] = dept_id
    # request.session['doctor_list'] = doctor_list_ls

    print(dept_id)
    # print(doctor_list_ls)

    # name = request.session.get('name')
    # docdate = request.session.get('docdate')

    # dept_name = request.POST.get('docnameid')

    # print('dept_name',dept_name)

    get_cat_seri = serializers.serialize('json', doctor_list)
    print(get_cat_seri)

    return JsonResponse(get_cat_seri, safe=False)


@csrf_exempt
def docshowbydept2(request):
    doc_id = request.POST.get('doc_id')

    print('doc_id', doc_id)

    request.session['doc_id'] = doc_id
    doc_info = Doctorprofile.objects.get(id=doc_id)
    print('doc_info.weekly')
    print(doc_info.weekly)
    print('doc_info.weekly')
    weekly_set = doc_info.weekly
    not_set = []
    total_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Friday']


    for i in total_week:
        if i in weekly_set:
            pass
        else:
            if i == 'Sunday':
                not_set.append(0)
            if i == 'Monday':
                not_set.append(1)
            if i == 'Tuesday':
                not_set.append(2)
            if i == 'Wednesday':
                not_set.append(3)
            if i == 'Thursday':
                not_set.append(4)
            if i == 'Saturday':
                not_set.append(5)
            if i == 'Friday':
                not_set.append(6)
    print('not_set')
    print(not_set)

    # docname1 = serializers.serialize('json', doc_name)
    return JsonResponse(not_set, safe=False)


@csrf_exempt
def docshowbydept3(request):
    print('hello')
    date_value = request.POST.get('date_value')
    print(date_value)
    print(type(date_value))

    request.session['date_value'] = date_value

    print('date_value', date_value)

    date_str = date_value
    date_object_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    print('bro')
    print(type(date_object_date))
    print('bro')
    print(date_object_date)
    print(type(date_object_date))

    print('week day', calendar.day_name[date_object_date.weekday()])

    weekly_set_day = calendar.day_name[date_object_date.weekday()]

    print('weekly_set_day', type(weekly_set_day))

    doc_id = request.session.get('doc_id')

    doctor_schedule_set = Doctorprofile.objects.filter(pk=doc_id).values('weekly')

    doctor_schedule_set = list(doctor_schedule_set)
    doctor_schedule_set = doctor_schedule_set[0]
    weekly_set = doctor_schedule_set['weekly']

    print('weekly_set',weekly_set)





    weekly_date_flag = False
    for i in weekly_set:
        if weekly_set_day == i:
            weekly_date_flag = True

    print('weekly_date_flag', weekly_date_flag)

    doctor_schedule_set_time = Doctorprofile.objects.filter(pk=doc_id).values('start_time', 'end_time')

    doctor_schedule_set_time_ls = list(doctor_schedule_set_time)

    doctor_schedule_set_time_dict = doctor_schedule_set_time_ls[0]

    start_time = doctor_schedule_set_time_dict['start_time']
    end_time = doctor_schedule_set_time_dict['end_time']

    print('start_time', type(start_time))
    print('end_time', end_time)

    all_doctor_s_avg_duration = Doctorprofile.objects.filter(pk=doc_id).values('avg_duration_min', 'avg_load_per_day')

    all_doctor_s_avg_duration_ls = list(all_doctor_s_avg_duration)

    all_doctor_s_avg_duration_dict = all_doctor_s_avg_duration_ls[0]

    avg_duration_min = all_doctor_s_avg_duration_dict['avg_duration_min']
    avg_load_per_day = all_doctor_s_avg_duration_dict['avg_load_per_day']

    print('avg_duration_min', type(avg_duration_min))
    print('avg_load_per_day', type(avg_load_per_day))

    enter_delta = timedelta(hours=start_time.hour, minutes=start_time.minute)
    exit_delta = timedelta(hours=end_time.hour, minutes=end_time.minute)

    print('enter_delta', type(enter_delta))
    print('enter_delta', enter_delta)
    print('exit_delta', type(exit_delta))
    print('exit_delta', exit_delta)

    time_slot = []

    if weekly_date_flag is True:
        while enter_delta <= exit_delta:
            # print("The train will leave at {} tomorrow".format(enter_delta.strftime('%H:%M')))
            print(enter_delta)
            time_slot.append(enter_delta)
            # time_slot_ls = datetime.time(x for x in time_slot)
            # print(time_slot_ls)

            enter_delta += timedelta(minutes=avg_duration_min)

    time_slot_12 = []
    for i in range(len(time_slot)):
        c_to_sec = time_slot[i]
        c_to_sec_str = str(c_to_sec)
        s = datetime.strptime(c_to_sec_str, "%H:%M:%S")
        hours_12 = s.strftime("%r")
        time_slot_12.append(hours_12)
    
    # print(time_slot_12)
    # print(type(time_slot_12[0]))

    # time_slot_12_2 = time_slot_12

    # time_slot_dict=zip(time_slot_12,time_slot_12_2)

    # time_slot_dict = dict(time_slot_dict)
    date_value = request.session.get('date_value')

    # find pk start
    date_value_time_query = Patientschedule.objects.filter(doc_id=doc_id).values('date_value','timeslotset')
    date_value_time_query = list(date_value_time_query)
    # date_value_time_query_specific = len(date_value_time_query)
    date_value_already_timeslot = []
    for i in date_value_time_query:
        if date_value == i['date_value']:
            date_value_already_timeslot.append(i['timeslotset'])
    
    print('date_value_already',date_value_already_timeslot)
        
    # date_value_query_pk_ls = []
    
    # for i in date_value_query_pk:
    #     date_value_query_pk_ls.append(i['id'])
    
    # date_value_query_full = Patientschedule.objects.get()
    # print('date_value_time_query_specific',date_value_time_query_specific)

    # find pk end


    # date_value_query = Patientschedule.objects.filter(doc_id=doc_id).values('date_value')

    # date_value_query = list(date_value_query)

    # print('date_value_query',date_value_query)



    # date_value_query_main_ls = []
    
    # for i in date_value_query:
    #     date_value_query_main_ls.append(i['date_value'])

    # print('time_slot_12_query_main_ls',date_value_query_main_ls)




    # time_slot_12_query = Patientschedule.objects.filter(doc_id=doc_id).values('timeslotset')

    # time_slot_12_query = list(time_slot_12_query)
    # time_slot_12_query = time_slot_12_query[0]
    # time_slot_12_query = time_slot_12_query['timeslotset']

    # print('time_slot_12_query',time_slot_12_query)

    # time_slot_12_main_ls = []

    # for i in time_slot_12_query:
    #     time_slot_12_main_ls.append(i['timeslotset'])

    

    time_slot_12_main = []


    for i in time_slot_12:
        if i not in date_value_already_timeslot:
            time_slot_12_main.append(i)
    # else:
    #     for i in time_slot_12:
    #         if i not in time_slot_12_main_ls:
    #             time_slot_12_main.append(i)

    print(time_slot_12)
    print('time_slot_12_main',time_slot_12_main)

    # time_slot_dict = serializers.serialize('json', time_slot_dict)
    # print(time_slot_12)

    return JsonResponse(time_slot_12_main, safe=False)

@csrf_exempt
def docshowbydept4(request):
    timeslotset = request.POST.get('timeslotset')

    print('timeslotset', timeslotset)

    request.session['timeslotset'] = timeslotset

    # docname1 = serializers.serialize('json', doc_name)

    return JsonResponse(timeslotset, safe=False)


    # docname1 = serializers.serialize('json', doc_name)

    # return JsonResponse(date_value, safe=False)


# def index2(request):
#     doctor_list_ls = request.session.get('doctor_list_ls')
#     print('index2 doctor_list_ls',doctor_list_ls)
    # return redirect('index1')
    # return HttpResponseRedirect(reverse_lazy('index1'))
    # return HttpResponseRedirect('/')
    # success_url = reverse_lazy('index1')
    # if len(doctor_list_ls) > 0:
    #     return HttpResponseRedirect(reverse('index1'))
    # return redirect('index1')
    # return render(request, 'index1.html')
    # return HttpResponse('')
    # return HttpResponseRedirect(reverse('index1'))


def appointment(request):
    departments = Depertment.objects.all()

    # if request.method == 'POST':

    #     department_id = request.GET.get('departmentname')

    #     request.session['department_id'] = department_id
    # department_id = None
    # if request.method == 'POST':

    # department_id = request.POST.get('departmentname')

    # request.session['department_id'] = department_id

    print('next1')

    dept_id = request.session.get('dept_id')
    doc_id = request.session.get('doc_id')

    timeslotset = request.session.get('timeslotset')

    date_value = request.session.get('date_value')

    phone = request.POST.get('phone')
    fullname = request.POST.get('fullname')
    email = request.POST.get('email')
    message = request.POST.get('message')


    # doctor_list_ls = request.session.get('doctor_list_ls')

    print('dept_id', dept_id)
    print('doc_id index1', doc_id)
    print('timeslotset index1', timeslotset)
    print('timeslotset index1', type(timeslotset))
    print('date_value',date_value)

    print('next2')

    print(dept_id)
    print(type(dept_id))

    success_message = ''

    if dept_id is not None:
        dept_id = int(dept_id)
        print(type(dept_id))
        print(dept_id)
        if fullname is not None and phone is not None:

            user = Patientschedule(dept_id=dept_id, doc_id=doc_id, date_value=date_value, timeslotset=timeslotset, phone=phone, fullname=fullname, email=email, message=message)
            user.save()
            success_message = 'Successfully Submitted'
            # return redirect('index2')

    # doctor_list = Doctorprofile.objects.all()

    # doctor_list_ls = []
    # request.session['doctor_list_ls'] = doctor_list_ls

    # for i in doctor_list:
    #     if department_id == i.connection_depertment.id:
    #         doctor_list_ls.append(i.doctor_name)

    # print(doctor_list_ls)

    # if len(doctor_list_ls) > 0:
    #     context = {
    #         'departments':departments,
    #     }
    #     return redirect('index2')

    context = {
        'departments': departments,
        'success_message':success_message,
    }
    return render(request, 'appoinments/appoinment.html', context)


# def index2(request):
#     department_id = request.session.get('department_id')
#     department_id = int(department_id)
#     print('index2 department_id',type(department_id))
#     print('index2 department_id',department_id)
#     return render(request, 'index2.html')

