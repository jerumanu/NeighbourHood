from django.db import models
from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
from django.dispatch import receiver


class Flashcard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='flashcard')
    notes = models.TextField(max_length=500, default="Here are my notes...", blank=True)
    title = models.CharField(blank=True, max_length=120)


    def __str__(self):
        return f'{self.user.username} flashcard'

    @receiver(post_save, sender=User)
    def create_user_flashcard(sender, instance, created, **kwargs):
        if created:
            Flashcard.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_flashcard(sender, instance, **kwargs):
        instance.flashcard.save()

    def save_flashcard(self):
        self.user

    def delete_flashcard(self):
        self.delete()

    @classmethod
    def search_flashcard(cls, title):
        return cls.objects.filter(user__username__icontains=title).all()


class Post(models.Model):
    title = models.CharField(max_length=250, blank=True)
    note = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(Flashcard, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"


    def __str__(self):
        return f'{self.user.name} Post'


