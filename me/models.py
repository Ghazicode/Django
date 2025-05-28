from django.db import models

#Contact Me

class Social_media(models.Model):
    Github = models.CharField(max_length=70)
    Instagram = models.CharField(max_length=70)
    Telegram = models.CharField(max_length=70)

    def __str__(self):
        return self.Github

class Contact_Me(models.Model):
    PhoneNumber = models.CharField(max_length=11)
    Location = models.TextField()
    Email = models.EmailField(max_length=100)
    Website = models.CharField(max_length=100)

    def __str__(self):
        return self.PhoneNumber
    
class Form(models.Model):
    Name = models.CharField(max_length=60)
    Email = models.EmailField(max_length=100)
    Body = models.TextField()

    def __str__(self):
        return self.Name
    
    #Contact Me

#About Me

class About_language(models.Model):
    language1 = models.CharField(max_length=20)
    language2 = models.CharField(max_length=20)
    language3 = models.CharField(max_length=20)
    language4 = models.CharField(max_length=20)
    language5 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.language1



class About_Me(models.Model):
    Experience = models.CharField(max_length=20)
    Country = models.CharField(max_length=10)
    Age = models.CharField(max_length=3)
    Favorite_language = models.CharField(max_length=10)
    Degree = models.CharField(max_length=10)


    #About Me
