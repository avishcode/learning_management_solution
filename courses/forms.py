from django import forms
from .models import Course, CourseCategory

class AddCoursesForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ("name", "short_desc", "category", "long_description", "thumbnail")



class AddCourseCategoryForm(forms.ModelForm):
    
    class Meta:
        model = CourseCategory
        fields = '__all__'
