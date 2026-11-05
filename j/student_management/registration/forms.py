from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'first_name',
            'last_name',
            'gender_name',
            'date_of_birth',
            'contact_number',
        ]
        labels = {
            'gender_name': 'Gender',
            'contact_number': 'Contact Number',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
