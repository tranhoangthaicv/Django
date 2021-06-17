from django.db.models import fields
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees


# Biến đổi cấu trúc dữ liệu thành một định dạng để lưu trữ ( Python ) -> Từ python chuyển dạng database thành dữ liệu JSON để xữ lý với front end
# Tạo định nghĩa cho API
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')

