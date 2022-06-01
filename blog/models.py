from django.db import models
from django.contrib.auth.models import User
from showcase.models import Category


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):

    category = models.ForeignKey(Category, on_delete= models.DO_NOTHING, default='1')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    url = models.fields.URLField( blank=True, null=True)
    url1 = models.fields.URLField( blank=True, null=True)
    url2 = models.fields.URLField( blank=True, null=True)
    url3 = models.fields.URLField( blank=True, null=True)
    image1 = models.ImageField(upload_to='static/uploaded/blog/img', null=True, blank=True)
    image2 = models.ImageField(upload_to='static/uploaded/blog/img', null=True, blank=True)
    image3 = models.ImageField(upload_to='static/uploaded/blog/img', null=True, blank=True)
    image4 = models.ImageField(upload_to='static/uploaded/blog/img', null=True, blank=True)
    image5 = models.ImageField(upload_to='static/uploaded/blog/img', null=True, blank=True)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

        