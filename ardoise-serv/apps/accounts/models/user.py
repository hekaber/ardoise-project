from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from apps.accounts.managers import ArdoiseUserManager
from apps.contacts.models import Contact


class ArdoiseUser(AbstractBaseUser):

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, null=True, on_delete=models.SET_NULL)

    objects = ArdoiseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'ardoise_user'

    def save(self, *args, **kwargs):
        created = self.pk is None
        if created:
            contact = Contact.objects.create(
                email=self.email
            )
            self.contact = contact
        super(ArdoiseUser, self).save(*args, **kwargs)

    def get_full_name(self):

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):

        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):

        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):

        return self.is_admin
