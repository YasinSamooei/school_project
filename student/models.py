from django.db import models

class Grade(models.Model):
    grade = models.SmallIntegerField("grade")

    class Meta:
        verbose_name = 'grade'
        verbose_name_plural ='grades'

    def __str__(self):
        return str(self.grade)

class StudentsList(models.Model):
    fullname = models.CharField("fullname",max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="students",verbose_name="grade")

    class Meta:
        verbose_name = 'student'
        verbose_name_plural ='students'

    def __str__(self):
        return self.fullname

class PresenceOrAbsence(models.Model):
    date = models.DateTimeField("date")
    absent = models.ManyToManyField(StudentsList,"absents")
    present = models.ManyToManyField(StudentsList,"presents")

    def __str__(self):
        return self.date
