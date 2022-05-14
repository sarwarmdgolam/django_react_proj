from django.db import models


class Candidate(models.Model):
    name = models.CharField("Name", max_length=240)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField("Name", max_length=240)

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        related_name='applied_candidate',
        on_delete=models.CASCADE,
    )
    job = models.ForeignKey(
        Job,
        related_name='applied_job',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    document = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name