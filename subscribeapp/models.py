from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription')
    # project에서 구독과 관련된 이름을 어떤식으로 가져올 건지 - related_name
    # One user - One Subscription

    # 외부 정보들
    class Meta:
        unique_together = ['user', 'project']
        # 어떤 조합 쌍이 unique 하도록


