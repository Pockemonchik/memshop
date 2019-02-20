from django.db import models
from django.contrib.auth.models import User
from django.conf.urls import url
from django.urls import reverse
from profiles.models import UserProfile

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def get_absolute_url(self):
        return reverse('shop:List_shop_by_category',
                        args=[self.slug])


    def __str__(self):
        return self.name

class mem(models.Model):
    author=models.ForeignKey(UserProfile,related_name='mems_of_profile',on_delete=models.CASCADE)
    disctiption=models.TextField()
    mem_img=models.ImageField(upload_to='mems', blank=True, null=True)
    cost=models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, blank=True, null=True,related_name='mem',on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    class Meta:
        index_together = (('id', 'slug'),)
    # def get_absolute_url(self):
    #     return reverse('shop:List_shop', args=[str(self.id)])
    def __str__(self):
        return 'mem: {0},by user: {1}'.format(self.disctiption,self.author.user)
