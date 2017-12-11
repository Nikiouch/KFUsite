from __future__ import unicode_literals
from django.db import models


class AddressBook(models.Model):
    country = models.CharField("Страна", max_length=32, null=True)
    region = models.CharField("Регион", max_length=32, blank=True, null=True)
    district = models.CharField("Район",max_length=32, blank=True, null=True)
    locality = models.CharField("Населенный пункт",max_length=32, null=True)

    class Meta:
        managed = True
        db_table = 'address_book'
        verbose_name = "Адресная книга"
        verbose_name_plural = "Адресные книги"

    def __str__(self):  # Для производительности можно заменить на if/else, оставлено для возможных расширений и null-полей
        full_name_list = list(filter(None, [self.locality, self.district, self.region, self.country]))
        full_name = ''
        for i in range(0, full_name_list.__len__()):
            full_name += full_name_list.pop()+' '
        return str(full_name)


class Director(models.Model):
    surname = models.CharField("Фамилия", max_length=64, null=True)
    name = models.CharField("Имя", max_length=32, null=True)
    patronymic = models.CharField("Отчество", max_length=64, null=True)
    main_post = models.CharField("Основная должность", max_length=64, null=True)
    additional_post = models.CharField("Дополнительная должность", max_length=64, blank=True, null=True)
    job_org = models.ForeignKey('Organization', models.DO_NOTHING, db_column='job_org', null=True, verbose_name="Место работы")
    degree = models.CharField("Ученая степень", max_length=64, null=True)
    phone_number = models.CharField("Тел.номер", max_length=12, null=True)
    email = models.CharField("email", max_length=64, null=True)

    class Meta:
        managed = True
        db_table = 'director'
        verbose_name = 'Научный руководитель'
        verbose_name_plural = 'Научные руководители'

    def __str__(s): # Для производительности можно заменить на if/else, оставлено для возможных расширений и null-полей
        all_fields_list = list(filter(None, [s.email, s.phone_number, s.degree, s.job_org.name, s.additional_post, s.main_post, s.patronymic, s.name,
                                             s.surname, str(s.pk)]))
        full_name = ''
        for i in range(0, all_fields_list.__len__()):
            full_name += all_fields_list.pop()+' '
        return full_name


class DirectorMember(models.Model):
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='member', null=True)
    director = models.ForeignKey(Director, models.DO_NOTHING, db_column='director', null=True)
    work = models.ForeignKey('Work', models.DO_NOTHING, db_column='work', null=True)

    class Meta:
        managed = True
        db_table = 'director_member'
        verbose_name = 'Участник-Научрук'
        verbose_name_plural = 'Участники-Научруки'
        unique_together = (('member', 'director'), )


class Documents(models.Model):
    receipt = models.CharField("Квитанция", max_length=1, null=True)
    members_sertificate = models.FileField("Сертификат участника", null=True)
    directors_sertificate = models.FileField("Сертификат научного руководителя", null=True)
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='member', null=True)

    class Meta:
        managed = True
        db_table = 'documents'
        verbose_name = 'Документы'
        verbose_name_plural = verbose_name

# Заявка
class Entry(models.Model):
    work = models.ForeignKey('Work', models.DO_NOTHING, verbose_name="Работа", db_column='work', null=True)
    member = models.ForeignKey('Member', models.DO_NOTHING, verbose_name="Участник", db_column='member', null=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, verbose_name="Секция", db_column='section', null=True)
    last_update = models.DateField("Последнее обновление", auto_now=True, null=True)
    comission_checked = models.NullBooleanField("Отметка комиссии", default=False, null=True)
    admission = models.NullBooleanField("Допуск в очный тур", default=False, null=True)
    internal_round_place = models.PositiveSmallIntegerField("Место в очном туре", default=0, null=True)

    class Meta:
        managed = True
        db_table = 'entry'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Jury(models.Model):
    surname = models.CharField("Фамилия", max_length=64, null=True)
    name = models.CharField("Имя", max_length=32, null=True)
    patronymic = models.CharField("Отчество", max_length=64, null=True)
    post = models.CharField("Должность", max_length=64, null=True)
    cathedra = models.CharField("Кафедра", max_length=64, null=True)
    degree = models.CharField("Степень", max_length=64, null=True)

    class Meta:
        managed = True
        db_table = 'jury'
        verbose_name = 'Жюри'
        verbose_name_plural = verbose_name


class JurySection(models.Model):
    id = models.IntegerField(primary_key=True)
    section = models.ForeignKey('Section', models.DO_NOTHING, verbose_name="Секция", db_column='section', null=True)
    jury = models.ForeignKey(Jury, models.DO_NOTHING, verbose_name="Жюри", db_column='jury', null=True)
    status = models.IntegerField("Статус", default=True, null=True)

    class Meta:
        managed = True
        db_table = 'jury_section'
        verbose_name = 'Секция-Жюри'
        verbose_name_plural = verbose_name


class Member(models.Model):
    surname = models.CharField("Фамилия", max_length=64, null=True, unique=True)
    name = models.CharField("Имя", max_length=32, null=True, unique=True)
    patronymic = models.CharField("Отчество", max_length=64, null=True, unique=True)
    birthday = models.DateField("Дата рождения", null=True)
    passport = models.CharField("Паспорт (серия/номер)", max_length=12, blank=True, null=True, unique=True)
    passport_issued = models.CharField("Кем выдан", max_length=128, blank=True, null=True, unique=True)
    issue_date = models.DateField("Дата выдачи", blank=True, null=True, unique=True)
    address = models.CharField("Адрес", max_length=256, null=True)
    organization = models.ForeignKey('Organization', verbose_name="Направляющая организация",
                                     db_column='organization', blank=True, null=True)
    grade = models.CharField("Класс", max_length=3, null=True, unique=True)
    phone_number = models.CharField("Тел.номер", max_length=12, null=True, unique=True)
    email = models.CharField("email", max_length=64, null=True)
    login = models.CharField("Логин", max_length=32, null=True)
    password = models.CharField("Пароль", max_length=32, null=True)

    class Meta:
        managed = True
        db_table = 'member'
        unique_together = (('surname', 'phone_number'),)
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        ordering = ['-id']

    def get_full_name(self):
        return self.surname+' '+self.name+' '+self.patronymic

    def __str__(s):
        all_fields = list(filter(None, [str(s.pk), '['+s.get_full_name(), s.grade+' класс]', str(s.birthday), s.phone_number, s.email, s.address,
                                        '['+str(s.passport)+']', s.login, s.password]))
        all_fields.reverse()
        full_name = ''
        for i in range(0, all_fields.__len__()):
            full_name += str(all_fields.pop())+' '
        return full_name
        # return str(s.member_id)+' '+s.get_full_name()+' '+s.login+' '+s.password+' '+s.email+' '+s.grade+' класс'


class Organization(models.Model):
    name = models.CharField("Название", max_length=128, null=True)
    location = models.ForeignKey(AddressBook, models.DO_NOTHING, verbose_name="Местонахождение", db_column='location', null=True)
    #location_district = models.ForeignKey(AddressBook, models.DO_NOTHING, verbose_name="Местонахождение", db_column='location', null=True)
    #location_locality = models.ForeignKey(AddressBook, models.DO_NOTHING, verbose_name="Местонахождение", db_column='location', null=True)
    address = models.CharField("Адрес", max_length=128, null=True)  # Тупо улица
    phone_number = models.CharField("Тел.номер", max_length=12, null=True)
    email = models.CharField("email", max_length=64, null=True)

    class Meta:
        managed = True
        db_table = 'organization'
        verbose_name = 'Направляющая организация'
        verbose_name_plural = 'Направляющие организации'
    def __str__(self):
        return str(self.pk) + ' ' + self.name


class Review(models.Model):
    criterion1 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 1', null=True)
    criterion2 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 2', null=True)
    criterion3 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 3', null=True)
    criterion4 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 4', null=True)
    criterion5 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 5', null=True)
    criterion6 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 6', null=True)
    criterion7 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 7', null=True)
    criterion8 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 8', null=True)
    criterion9 = models.PositiveSmallIntegerField(default=0, verbose_name='Критерий 9', null=True)
    review_text = models.TextField("Текст резенции", null=True)
    jury_surname = models.CharField("Фамилия проверяющего", max_length=64, null=True)
    status = models.NullBooleanField("Статус", default=None, null=True)

    class Meta:
        managed = True
        db_table = 'review'
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'


class Section(models.Model):
    name = models.CharField("Название", max_length=32, null=True)
    institute = models.CharField("Институт", max_length=64, null=True)
    status = models.IntegerField("Статус", default=True, null=True)
    login = models.CharField("Логин", max_length=32, null=True)
    password = models.CharField("Пароль", max_length=32, null=True)

    class Meta:
        managed = True
        db_table = 'section'
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'

    def __str__(self):
        return str(self.pk) + " " + self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return str(instance.pk)

class Work(models.Model):
    name = models.CharField("Название", max_length=128, null=True)
    theses = models.FileField("Тезисы", upload_to=user_directory_path, null=True)
    review = models.ForeignKey(Review, models.DO_NOTHING, verbose_name="Рецензия", db_column='review', null=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, verbose_name="Направляющая организация", db_column='organization', null=True)

    class Meta:
        managed = True
        db_table = 'work'
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        if self.name is not None:
            return str(self.pk) + " " + self.name
        else:
            return "Некорректная работа"
