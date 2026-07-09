from django.db import models

class User(models.Model):

    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Employer', 'Employer'),
        ('Candidate', 'Candidate'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Candidate'
    )

    is_active = models.BooleanField(default=True)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.user.name


class Job(models.Model):
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate} - {self.job}"