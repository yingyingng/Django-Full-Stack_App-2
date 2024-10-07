from django.urls import path
from .views import GuestLoginView

urlpatterns = [
    #path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    #path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    #path("<int:id>", views.index, name = 'index')
    path('guest-login/', GuestLoginView.as_view(), name='guest-login')
    
]
