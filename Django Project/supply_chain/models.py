from django.db import models


class Council(models.Model):
    name = models.CharField(max_length=100)

    contact = models.CharField(max_length=100)
    contact_email = models.EmailField()

    slug = models.SlugField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} Council'


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    budget = models.IntegerField()

    council = models.ForeignKey(Council, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    council = models.ForeignKey(Council, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
