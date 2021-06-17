from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    
    # Lấy thông tin trang web     
    if request.method =='GET':
        # Truy xuất tất cả tối tượng trong database
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        # Cho phép bất kỳ đối tượng đối tượng nào cũng có thể nhận đc response
        return JsonResponse(departments_serializer.data , safe=False)
    
    # Thêm mới 1 đối tượng cho trang web    
    elif request.method =='POST':
        # Đổi request rừ JSON thành int
        department_data = JSONParser().parse(request)
        # chuyển đổi kiểu int thành kiểu giống với lớp serialier
        department_serializer = DepartmentSerializer(data=department_data)
        # Nếu kiểm tra xem data có hợp lệ hay không
        if department_serializer.is_valid():
            department_serializer.save()
        # Cho phép bất kỳ đối tượng đối tượng nào cũng có thể nhận đc response
            return JsonResponse("Add Successfully !!",safe=False)
        return JsonResponse("Failed to Add !!",safe=False)
    
    # Cập nhật 1 đối tượng
    elif request.method =='PUT':
        department_data = JSONParser().parse(request)
        # Lấy data từ database ( DepartmentId )
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        # Chuyển đối kiểu int và đồng bộ dữ liệu với class serialier
        department_serializer = DepartmentSerializer(department , data= department_data)
        # Kiểm tra data có hợp lệ hay không
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse(" Failed to Update !!" , safe=False )

    # Xóa 
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        print(department)
        department.delete()
        return JsonResponse("Deleted Succeffully !!", safe=False)


# Create your views here.
@csrf_exempt
def employeeApi(request,id=0):
    # Lấy thông tin trang web     
    if request.method =='GET':
        # Truy xuất tất cả tối tượng trong database
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees,many=True)
        # Cho phép bất kỳ đối tượng đối tượng nào cũng có thể nhận đc response
        return JsonResponse(employees_serializer.data , safe=False)
    
    # Thêm mới 1 đối tượng cho trang web    
    elif request.method =='POST':
        # Đổi request rừ JSON thành int
        employee_data = JSONParser().parse(request)
        # chuyển đổi kiểu int thành kiểu giống với lớp serialier
        employee_serializer = EmployeeSerializer(data=employee_data)
        # Nếu kiểm tra xem data có hợp lệ hay không
        if employee_serializer.is_valid():
            employee_serializer.save()
        # Cho phép bất kỳ đối tượng đối tượng nào cũng có thể nhận đc response
            return JsonResponse("Add Successfully !!",safe=False)
        return JsonResponse("Failed to Add !!",safe=False , status = status.HTTP_401_UNAUTHORIZED)
     
  
    # Cập nhật 1 đối tượng
    elif request.method =='PUT':
        employee_data = JSONParser().parse(request)
        # Lấy data từ database ( DepartmentId )
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        # Chuyển đối kiểu int và đồng bộ dữ liệu với class serialier
        employee_serializer = EmployeeSerializer(employee , data= employee_data)
        # Kiểm tra data có hợp lệ hay không
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse(" Failed to Update !!" , safe=False )

    # Xóa 
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully !!", safe=False)
        
@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)