from django.db import models
from django.conf import settings

# Create your models here.


class Application(models.Model):
    id_application = models.AutoField(auto_created=True, primary_key=True)
    client_name = models.CharField(max_length=50)
    client_phone_number = models.CharField(max_length=20)
    client_message = models.TextField()
    status = models.CharField(default='Новая заявка', max_length=11)

    def __str__(self):
        return (
            self.client_name, self.client_phone_number,
            self.client_name, self.status
        )


class Reviews(models.Model):
    id_review = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    review = models.TextField()
    status = models.CharField(default='Новый', max_length=11)

    def __str__(self):
        return (
            self.name, self.email, self.review
        )


class Payed(models.Model):
    id_payed = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sum = models.IntegerField()
    time = models.IntegerField()
    status = models.CharField(default='not paid', max_length=11)
    use_status = models.CharField(default='не использован', max_length=50)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    id_certificate = models.AutoField(auto_created=True, primary_key=True)
    certificate_category = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    certificate_number = models.CharField(max_length=7)
    status = models.CharField(default='выпущен', max_length=11)

    def __str__(self):
        return self.certificate_number, self.status


class ActiveCertificate(models.Model):
    id_certificate = models.AutoField(auto_created=True, primary_key=True)
    certificate_name = models.CharField(max_length=256)
    certificate_image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return f'{self.certificate_name} {self.certificate_image}'


class Aboniment(models.Model):
    id_aboniment = models.AutoField(auto_created=True, primary_key=True)
    aboniment_category = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    aboniment_number = models.CharField(max_length=7)

    def __str__(self):
        return self.aboniment_number


class ActiveAboniment(models.Model):
    id_aboniment = models.AutoField(auto_created=True, primary_key=True)
    aboniment_name = models.CharField(max_length=256)
    certificate_image = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.aboniment_name} {self.certificate_image}'


class Massages(models.Model):
    id_serv = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)
    img = models.ImageField()
    description = models.TextField()
    price1 = models.IntegerField()
    time1 = models.IntegerField()
    price2 = models.IntegerField()
    time2 = models.IntegerField()
    price3 = models.IntegerField()
    time3 = models.IntegerField()
    price4 = models.IntegerField()
    time4 = models.IntegerField()

    def __str__(self):
        return self.name


class Spa(models.Model):
    id_serv = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)
    img = models.ImageField()
    description = models.TextField()
    price1 = models.IntegerField()
    time1 = models.IntegerField()
    price2 = models.IntegerField()
    time2 = models.IntegerField()
    price3 = models.IntegerField()
    time3 = models.IntegerField()
    price4 = models.IntegerField()
    time4 = models.IntegerField()

    def __str__(self):
        return self.name


class Spafortwo(models.Model):
    id_serv = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)
    img = models.ImageField()
    description = models.TextField()
    price1 = models.IntegerField()
    time1 = models.IntegerField()
    price2 = models.IntegerField()
    time2 = models.IntegerField()
    price3 = models.IntegerField()
    time3 = models.IntegerField()
    price4 = models.IntegerField()
    time4 = models.IntegerField()

    def __str__(self):
        return self.name


class Workers(models.Model):
    id_worker = models.AutoField(auto_created=True, primary_key=True)
    worker_name = models.CharField(max_length=40)
    worker_img = models.ImageField(upload_to='images/')
    worker_desc = models.TextField()

    def __str__(self):
        return self.worker_name


class PayClient(models.Model):
    id_client = models.AutoField(auto_created=True, primary_key=True)
    client_email = models.CharField(max_length=200)

    def __str__(self):
        return self.client_email


class Photo(models.Model):
    id_photo = models.AutoField(auto_created=True, primary_key=True)
    img = models.ImageField()

    def __str__(self):
        return 'photo'


class Hamam(models.Model):
    id_hamam = models.AutoField(auto_created=True, primary_key=True)
    img = models.ImageField()
    description_1 = models.TextField()
    description_2 = models.TextField()
    name = models.CharField(max_length=100)
    price_1 = models.IntegerField()
    time_1 = models.IntegerField()
    price_2 = models.IntegerField()
    time_2 = models.IntegerField()

    def __str__(self):
        return self.name


class Salt(models.Model):
    id_salt = models.AutoField(auto_created=True, primary_key=True)
    img = models.ImageField()
    description_1 = models.TextField()
    description_2 = models.TextField()
    name = models.CharField(max_length=100)
    desc_price_1 = models.CharField(max_length=100)
    price_1_1 = models.IntegerField()
    time_1_1 = models.IntegerField()
    price_1_2 = models.IntegerField()
    time_1_2 = models.IntegerField()
    desc_price_2 = models.CharField(max_length=100)
    price_2_1 = models.IntegerField()
    time_2_1 = models.IntegerField()
    price_2_2 = models.IntegerField()
    time_2_2 = models.IntegerField()
    desc_price_3 = models.CharField(max_length=100)
    price_3_1 = models.IntegerField()
    time_3_1 = models.IntegerField()
    price_3_2 = models.IntegerField()
    time_3_2 = models.IntegerField()
    desc_price_4 = models.CharField(max_length=100)
    price_4_1 = models.IntegerField()
    time_4_1 = models.IntegerField()
    price_4_2 = models.IntegerField()
    time_4_2 = models.IntegerField()

    def __str__(self):
        return self.name


class Hidromassage(models.Model):
    id_hidromassage = models.AutoField(auto_created=True, primary_key=True)
    img = models.ImageField()
    description_1 = models.TextField()
    description_2 = models.TextField()
    name = models.CharField(max_length=100)
    price_1 = models.IntegerField()
    time_1 = models.IntegerField()

    def __str__(self):
        return self.name


class Actions(models.Model):
    id_action = models.AutoField(auto_created=True, primary_key=True)
    action_img = models.ImageField(upload_to='images/')
    action_name = models.CharField(max_length=50)

    def __str__(self):
        return self.action_name
