
from django.db.models.signals import post_save
# from django.dispatch import receiver

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Admins


def admin_profile(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name='admins')
        instance.groups.add(group)
        Admins.objects.create(
            user=instance,
            username = instance.username,
            )
        print('profile created')
post_save.connect(admin_profile, sender=User.username)

# @receiver(post_save, sender=User)     
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#         print('Profile created')

# # post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User)  
# def update_profile(sender, instance, created, **kwargs):
    
#     if created == False:
#         instance.customer.save()
#         print('Profile updated!')
#         # try:
#         #     instance.customer.save()
#         #     print('Profile created')
#         # except:
#         #     Customer.objects.create(user=instance)
#         #     print('Profile created for existing user!')

# # post_save.connect(update_profile, sender=User)

# group = Group.objects.get(name='customer')
# user.groups.add(group)

# Customer.objects.create(
#     user=user,
#     name = user.username,
# )
