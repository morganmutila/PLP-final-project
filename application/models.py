from django.db import models
from django.urls import reverse

class Setting(models.Model):
    school_name = models.CharField(max_length = 255, blank=False)
    location = models.TextField(blank=False)
    email = models.EmailField(max_length = 255, blank=False)
    phone = models.CharField(max_length = 255, blank=False)
    tagline = models.TextField(max_length = 255, blank=False)
    hero_title = models.CharField(max_length = 255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'settings'

    def __str__(self):
        return self.school_name

class Testimonial(models.Model):
    name = models.CharField(max_length = 255, blank=False)
    title = models.CharField(max_length = 255, blank=True)
    body =  models.TextField(blank=False)

    class Meta:
        verbose_name_plural = 'testimonials'
        ordering = ('-name',)

    def __str__(self):
        return self.name



class StudyCategory(models.Model):
    name = models.CharField(max_length = 255, blank=False)

    class Meta:
        verbose_name_plural = 'studyCategories'

    def __str__(self):
        return self.name

class Lecture(models.Model):
    name = models.CharField(blank=False, max_length=100, null=True)
    image = models.ImageField(upload_to='lectures/')

    class Meta:
        verbose_name_plural = 'lectures'
        ordering = ('-name',)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length = 255, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=True)
    study_level = models.ForeignKey(StudyCategory, default=1, on_delete=models.CASCADE, null=True)
    lectures = models.ForeignKey("Lecture", null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'programs'
        ordering = ('-name',)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('program_detail', kwargs={ 'slug' :self.slug })

class Contact(models.Model):
    fullname = models.CharField(blank=False, max_length=200)
    email = models.EmailField(max_length=254, blank=False)
    subject = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=False)

    class Meta:
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.fullname



class Course(models.Model):
    name = models.CharField(blank=False, max_length=200)
    programs = models.ForeignKey('Program', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name