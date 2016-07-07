from django.conf.urls import url
from .views import *
from erms.views import *

urlpatterns=[
    url(r'^$', hod),
    url(r'^hod_vacancy/$', hod_vacancy),
    url(r'^hod_vacancy/succs/$', hod_vacancy_succs),
    url(r'^hod_vacancy/test/$', hod_vacancy_test),
    url(r'^hod_vacancy/test/(\d+)/$', hod_inter_create),
    url(r'^hod_vacancy/test/succs/$', hod_inter_create_succs),
    url(r'^hod_vacancy/test/part2/inter_list/$', hod_inter_list_interviewer),
    url(r'^hod_vacancy/test/part2/inter_list/(\d+)/$', hod_pre_interviwer_list, name="inter1"),
    url(r'^hod_vacancy/test/part2/inter_list/(\d+)/(\d+)/$', hod_inter_interviewer_2, name="inter2"),
    url(r'^hod_vacancy/test/part2/inter_list_cv/$', hod_inter_list_cv),
    url(r'^hod_vacancy/test/part2/inter_list_cv/(\d+)/$', hod_pre_cv_list, name="cv1"),
    url(r'^hod_vacancy/test/part2/inter_list_cv/(\d+)/(\d+)/$', hod_inter_cv, name="cv2"),
    url(r'^hod_vacancy/test/vacancy/(?P<ID>[0-9]+)/$', hod_view_vacancy),
    url(r'^hod_cv/$', hod_cv),
    url(r'^hod_cv/(?P<NIC>[^/]+)/$', hod_profile),
    url(r'^hod_inter/$', hod_inter),
    url(r'^hod_inter/chs_vacn/$', hod_inter_choose_vacancy),
    url(r'^hod_vacancy/test/part2/$', hod_inter_cv),
    url(r'^hod_inter/hod_inter_overview/$', hod_inter_overview),
    url(r'^hod_inter/hod_inter_overview/view/(\d+)/$', hod_inter_view),
    url(r'^hod_inter/hod_succs$', hod_succs),
    url(r'^hod_msg/$', hod_msg),
    url(r'^hod_msg/send/succs$', hod_msg_succs),
    url(r'^hod_msg/recieve/$', hod_recieve_msg),

]