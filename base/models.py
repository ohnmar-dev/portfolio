from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_quill.fields import QuillField

# Create your models here.
# class Typing(models.Model):
#     name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name = 'Typing Text'
#         verbose_name_plural = 'Typing Text'
#     def __str__(self):
#         return self.name

# class Hero(models.Model):
#     name = models.CharField(max_length=100)
#     typing = models.ManyToManyField(Typing)
#     description = QuillField()

#     class Meta:
#         verbose_name = "Hero"
#         verbose_name_plural = "Hero"
    
#     def __str__(self) -> str:
#         return "Hero"
# class About(models.Model):
#     short_description = models.TextField()
#     description = QuillField()
#     image = models.ImageField(upload_to = 'about')

#     class Meta:
#         verbose_name = "About Me"
#         verbose_name_plural = "About Me"
    
#     def __str__(self) -> str:
#         return "About Me"

# class Skill(models.Model):
#     title = models.CharField(max_length=50)
#     rate = models.IntegerField()

#     class Meta:
#         verbose_name = "Skill"
#         verbose_name_plural = "Skill"

#     def __str__(self):
#         return self.title

# class Contact(models.Model):
#     title = models.CharField(max_length=255)
#     address = models.CharField(max_length=250)
#     email = models.CharField(max_length=150)
#     phone = models.CharField(max_length=20)
# #   latitude = models.DecimalField(max_digits=9, decimal_places=6)
# #   longitude = models.DecimalField(max_digits=9, decimal_places=6)
  
#     class Meta:
#         verbose_name = 'Contact Me'
#         verbose_name_plural = 'Contact me'
        
#     def __str__(self):
#         return "Contact Me"

class Category(models.Model):
    name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(
            default='',
            editable=False,
            unique=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('category', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(
            default='',
            editable=False,
            unique=True
        )
    author = models.ForeignKey(User, on_delete=models.CASCADE ,default='Kyaw Soe Hla')
    content = QuillField()
    # short_content = QuillField(null=True,blank=True)
    image = models.ImageField(upload_to = 'static/%Y/%m/%d/blogimages', blank= True,null=True,default='static/assets/img/hero-bg.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    feature = models.BooleanField(default=True)
    views=models.IntegerField(default=0,null=True,blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Post'
        verbose_name_plural = 'Post'

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Album(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Album'
        verbose_name_plural = 'Album'
    
    def __str__(self):
        return '{0}'.format(self.name)

class Gallery(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE, null=True,blank=True)
    image= models.ImageField(upload_to="static/%Y/%m/%d/images")
    # caption = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        ordering = ('album',)
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
    
    def __str__(self):
        return '{0} {1}'.format(self.album, self.image)