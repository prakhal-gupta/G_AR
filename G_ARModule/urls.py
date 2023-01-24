from django.urls import path
from G_ARModule.views import *

app_name = 'G_ARModule'
urlpatterns = [
 	path('registration/room/',Room_Registration),
	path('Detail/room/',Room_Detail),
	path('Delete/room/',Faculty_detail),
	path('registration/faculty/',Faculty_Registration),
	path('Detail/faculty/',Faculty_detail),
	path('Delete/faculty/',Faculty_detail),
	path('Detail/faculty/All/',G_Faculty_All_Detail),
	path('faculty/Room/',Faculty_Room_Detail),
	path('registration/student/',Con_Student_Registration),
]