from django.conf.urls import url,include
from android.androidAPI import android_api

urlpatterns = [
url(r'^androidAPI/',include(android_api.urls)),
        ]