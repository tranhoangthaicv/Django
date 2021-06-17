from django.conf.urls import url
from EmployeeApp import views

# Xác định đường dẫn URL và ánh xạ nó đến API
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # url department sẽ thực hiện API tương ứng  
    url(r'^department/$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),
    # url employee sẽ thực hiện API tương ứng  
    url(r'^employee/$',views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeApi),
    url(r'^SaveFile$', views.SaveFile)    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
# Cho phép người dùng tải lên file tĩnh  