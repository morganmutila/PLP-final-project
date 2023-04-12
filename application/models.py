from django.db import models

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

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length = 255, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=True)
    study_level = models.ForeignKey(StudyCategory, default=1, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = 'programs'
        ordering = ('-name',)


    def __str__(self):
        return self.name

class Contact(models.Model):
    fullname = models.CharField(blank=False, max_length=200)
    email = models.EmailField(max_length=254, blank=False)
    subject = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=False)

    class Meta:
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.fullname

