from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),

    path('about-us/', about_us, name="about_us"),
    path('structure/', structure_of_company, name="structure"),
    path('culture/', corporative_culture, name="culture"),
    path('management/', ManagementList.as_view(), name="management"),

]