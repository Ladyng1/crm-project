from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),

    # CRUD
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create-record/", views.create_record, name="create_record"),
    path("detail/<int:pk>/", views.record_detail, name="detail"),
    path("update/<int:pk>/", views.update_record, name="update"),
    path("record/<int:pk>/delete/", views.delete, name="delete"),

]