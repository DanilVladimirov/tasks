from django.contrib import admin
from django.urls import path
from postsapp.views import (StartPageView,
                            CreatePubView,
                            add_pub,
                            add_comment,
                            del_pub,
                            UserPubsView,
                            ChangePubView)

urlpatterns = [
    path('', StartPageView.as_view(), name='start-page'),
    path('add_pub/', add_pub, name='add-pub'),
    path('add_comment/', add_comment, name='add-comment'),
    path('create_pub/', CreatePubView.as_view(), name='create-pub-page'),
    path('del_pub/', del_pub, name='del-pub'),
    path('my_pubs/', UserPubsView.as_view(), name='user-pubs-page'),
    path('edit_pub/<int:pid>/', ChangePubView.as_view(), name='edit-pub-page')
]
