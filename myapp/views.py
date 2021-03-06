from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import RequestContext, redirect
from django.db.models import Q
from datetime import date, datetime
from .forms import *


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def hod(request):
    intr_count = Interview.objects.filter().count()
    vcncy_count = Vacancy.objects.filter().count()
    msg_count = Messages.objects.filter().count()
    cv_count = Personal.objects.filter().count
    context={
        'msg_count': msg_count,
        'cv_count': cv_count,
        'vcncy_count': vcncy_count,
        'intr_count' : intr_count,
    }
    return render(request, 'hod/hod.html', context)


def hod_vacancy(request):
    context = RequestContext(request)
    if request.method == 'POST':
        vacncy_form = VacancyForm(request.POST)
        if vacncy_form.is_valid():
            form = vacncy_form.save(commit=False)
            form.save()
            return redirect('/hod/hod_vacancy/succs/')
        else:
            print(vacncy_form.errors)
    else:
        vacncy_form = VacancyForm()
    return render(request, 'hod/hod_vacancy.html', {'v_form': vacncy_form}, context)


def hod_vacancy_succs(request):
    return render(request, 'hod/hod_vacancy_succs.html', {})


def hod_vacancy_test(request):
    obj = Vacancy.objects.all()
    return render(request, 'hod/test_vacancy.html', {'obj': obj})


def hod_auto_filter(request):
    return render()


def hod_cv(request):
    form = Personal.objects.all()
    # form2 = Degree.objects.all()
    return render(request, 'hod/hod_cv.html', {'form_cv': form})


def hod_inter(request):
    return render(request, 'hod/hod_inter.html', {})


def hod_inter_choose_vacancy(request):
    vacancy = Vacancy.objects.all()
    context = {
        'Vacn': vacancy,
    }
    return render(request, 'hod/hod_inter_choose_vacancy.html', context)


def hod_view_vacancy(request, ID):
    obj = Vacancy.objects.get(id=ID)
    return render(request, 'hod/hod_view_vacancy.html', {'obj': obj})


def hod_inter_create(request, vid):
    context = RequestContext(request)
    obj = Vacancy.objects.get(id=vid)
    usr = Users.objects.get(User=request.user)
    if request.method == 'POST':
        inter_form = InterviewForm(request.POST)
        if inter_form.is_valid():
            inter = inter_form.save(commit=False)
            inter.Department = usr.Department
            inter.HOD = request.user
            inter.Vacancy = obj
            inter.save()
            return redirect('/hod/hod_vacancy/test/succs/')
        else:
            print(inter_form.errors)
    else:
        inter_form = InterviewForm()
    return render(request, 'hod/hod_inter_create.html', {'inter_form': inter_form, 'obj': obj, 'vid': vid}, context)


def hod_inter_create_succs(request):
    return render(request, 'hod/hod_inter_create_succs.html', {})


def hod_inter_list_interviewer(request):
    inter = Interview.objects.all()
    return render(request, 'hod/hod_inter_list_inter.html', {'inter': inter})


def hod_pre_interviwer_list(request, iid):
    inter = Interview.objects.get(id=iid)
    a = UserRole.objects.get(Role="Interviewer")
    viewer = Users.objects.filter(UserRole=a.id)
    return render(request, 'hod/hod_inter_create_2.html', {'viewer': viewer, 'inter': inter, 'a':a})


def hod_inter_interviewer_2(request, iid, pid):
    inter = Interview.objects.get(id=iid)
    if request.method == 'POST':
        user = User.objects.get(id=pid)
        x = Interview_Interviewer(Interview=inter, Interviewer=user)
        x.save()

        subject = 'Assinged as Interviewer'
        message = 'Hi, You have been selected for Interview as Interviwer'
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('hod/hod_vacancy/test/part2/inter_list/(\d+)/(\d+)/')
    else:
        a = UserRole.objects.get(Role="Interviewer")
        viewer = Users.objects.filter(UserRole=a.id)
        i = Interview.objects.get(id=iid)
        c = Interview_Interviewer.objects.filter(Interview=i.id)
        # d = c.Interviewer
        # y= User.objects.filter(Role='Interviewer').exclude(id=d)
    return render(request, 'hod/hod_inter_create_2.html', {'viewer': viewer, 'inter': inter})


def hod_inter_list_cv(request):
    cv = Personal.objects.all()
    return render(request, 'hod/hod_inter_list_cv.html', {'cv': cv})


def hod_pre_cv_list(request, iid):
    inter = Interview.objects.get(id=iid)
    cv = Personal.objects.all()
    return render(request, 'hod/hod_inter_create_3.html', {'cv': cv, 'inter':inter})


def hod_inter_cv(request, iid, pid):
    inter = Interview.objects.get(id=iid)
    context = RequestContext(request)
    if request.method == 'POST':
        cv = Personal.objects.all()
        y=Interview.objects.filter(InterviewNo=1 )
        p = Personal_Interview_viewer.objects.filter(Q(CV_Status.objects.get(id=1))|Q(CV_Status.objects.get(id=3))) #1 means pass, 2 means failed , 3 means on hold
        person1 = p.Pesonal
        Interview.Vacancy.Post_Dept.Post
        return redirect('/hod/hod_vacancy/test/part2/inter_list/(\d+)/(\d+)/')
    else:
        cv = Personal.objects.all()

    return render(request, 'hod/hod_inter_create_3.html', {'cv': cv, 'inter': inter}, context)


def hod_view_inter(request, ID):
    vacan = Vacancy.objects.get(id=ID)
    cv = Personal.objects.all()
    inter_form_2 = InterviewForm2(request.POST)
    try:
        selected_cv = Personal.objects.get(id=request.POST['cv'])
    except (KeyError, Personal.DoesNotExist):
        return render(request, 'hod/hod_inter_create_2.html', {'error': "Person does not exist"})
    else:
        selected_cv.is_selected = True
        selected_cv.save()
        return render(request, 'hod/hod_inter_create_2.html', {'inter_form_2': inter_form_2, 'cv': cv, 'vacan':vacan})


def hod_succs(request):
    return render(request, 'hod/hod_succs.html', {})


def hod_inter_overview(request):
    inter_obj = Interview.objects.all()
    context={
        'inter_obj': inter_obj,
    }
    return render(request, 'hod/hod_inter_overview.html', context)


def hod_inter_view(request, id):
    inter_obj = Interview.objects.get(id = id)
    a = UserRole.objects.get(Role="Interviewer")
    viewer = Interview_Interviewer.objects.filter(Interview=id)
    cv = Personal_Interview.objects.filter(Interview=id)
    context = RequestContext(request)
    if request.method == 'POST':
        form = InterReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('/hod/hod_inter/hod_inter_overview/view/(\d+)/')
        else:
            print(form.errors)
    else:
        form = InterReviewForm()
    return render(request, 'hod/hod_inter_view.html', {'inter_obj': inter_obj, 'viewer': viewer, 'cv': cv, 'form': form}, context)


def hod_profile(request, NIC):
    try:
        profile = Personal.objects.get(NIC=NIC)
        context = RequestContext(request)
        if request.method == 'POST':
            hod = HodReviewForm(request.POST, request.FILES)
            if hod.is_valid():
                review = hod.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('')
            else:
                print(hod.errors)
        else:
            hod = HodReviewForm()
    except Personal.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'hod/hod_cv_profile.html', {'hod_form': hod, 'pro_form': profile}, context)


def hod_msg(request):
    return render(request, 'hod/hod_msg.html', {})



def hod_msg_succs(request):
    msg_obj = Messages()
    if request.user.is_authenticated():
        username = request.user.username
        msg_obj.Sende = username
        msg_obj.SentDate = date.today()
        msg_obj.SentTime = datetime.time()
        dsc = True
        context = {
            'dsc': dsc,
        }
    else:
        error = 'User authentication error'
        context = {
            'error': error,
        }
    return render(request, 'hod/hod_msg_succs.html', context)


def hod_recieve_msg(request):
    usr = request.user.username
    if request.user.is_authenticated():
        msg = Messages.objects.get(Recieve=usr)
        context = {
            'msg': msg,
        }
    else:
        error = 'User is not Authenticated one.'
        context = {
            'error': error,
        }
    return render(request, 'hod/hod_recieve_msg.html', context)
