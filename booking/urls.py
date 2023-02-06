from django.urls import path
from .views import StoreList, StaffList, StaffCalender, Booking, MyPage, MyPageWithPk, MyPageCalendar, MyPageDetail, MyPageSchedule, MyPageScheduleDelete, my_page_holiday_add
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', StoreList.as_view(), name='store_list'),
    path('store/<int:pk>/staffs/', StaffList.as_view(), name='staff_list'),
    path('staff/<int:pk>/staffs/', StaffCalender.as_view(), name='calendar'),
    path('staff/<int:pk>/calendar/<int:year>/<int:month>/<int:day>/', StaffCalender.as_view(), name='calendar'),
    path('staff/<int:pk>/booking/<int:year>/<int:month>/<int:day>/<int:hour>/', Booking.as_view(), name='booking'),
    path('login/', LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('mypage/', MyPage.as_view(), name='my_page'),
    path('mypage/<int:pk>/', MyPageWithPk.as_view(), name='my_page_with_pk'),
    path('mypage/<int:pk>/calendar/', MyPageCalendar.as_view(), name='my_page_calendar'),
    path('mypage/<int:pk>/calendar/<int:year>/<int:month>/<int:day>', MyPageCalendar.as_view(), name='my_page_calendar'),
    path('mypage/<int:pk>/detail/<int:year>/<int:month>/<int:day>/', MyPageDetail.as_view(), name='my_page_day_detail'),
    path('mypage/schedule/<int:pk>/', MyPageSchedule.as_view(), name='my_page_schedule'),
    path('mypage/schedule/<int:pk>/delete/', MyPageScheduleDelete.as_view(), name='my_page_schedule_delete'),
    path('mypage/holiday/add/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>/', my_page_holiday_add, name='my_page_holiday_add'),
]