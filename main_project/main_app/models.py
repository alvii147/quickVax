from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class PatientManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, address_line_1, city, province, postal_code, password = None, middle_initial = "", address_line_2 = "", active = True, admin = False):
        if not email:
            raise ValueError("Patients must have an email address")

        if not password:
            raise ValueError("Patients must have a password")

        patient = self.model(
            email = self.normalize_email(email)
        )
        patient.set_password(password)
        patient.first_name = first_name
        patient.last_name = last_name
        patient.middle_initial = middle_initial
        patient.date_of_birth = date_of_birth
        patient.address_line_1 = address_line_1
        patient.address_line_2 = address_line_2
        patient.city = city
        patient.province = province
        patient.postal_code = postal_code
        patient.active = active

        patient.save(using = self._db)

        return patient

class Patient(AbstractBaseUser):
    email = models.EmailField(max_length = 255, unique = True)
    first_name = models.CharField(max_length = 255, blank = True)
    last_name = models.CharField(max_length = 255, blank = True)
    middle_initial = models.CharField(max_length = 255, blank = True)
    date_of_birth = models.DateField()
    address_line_1 = models.CharField(max_length = 255, blank = True)
    address_line_2 = models.CharField(max_length = 255, blank = True)
    city = models.CharField(max_length = 255, blank = True)
    province = models.CharField(max_length = 255, blank = True)
    postal_code = models.CharField(max_length = 7, blank = True)
    active = models.BooleanField(default = True)
    admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'address_line_1', 'city', 'province', 'postal_code']

    objects = PatientManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return (self.first_name + ' ' + self.last_name).strip()

    def get_short_name(self):
        return self.first_name.strip()

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin