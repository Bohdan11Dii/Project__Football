from operator import mod
from statistics import mode
from django.db import models

class Model(models.Model):
    name = models.CharField("Ім'я",max_length=50)
    date_of_birth = models.DateField("Дата народження")
    Comand = models.CharField("Команда", max_length=150)
    place_of_birth = models.CharField("Місце народження",max_length=150)
    place_now = models.CharField("Місце проживання",max_length=150)
    growth = models.CharField("Ріст",max_length=50)
    number = models.IntegerField("Номер")
    started_playing = models.CharField("Почав грати",max_length=50)
    goals_scored = models.IntegerField("Забиті голи")
    transfer_head = models.IntegerField("Передачі головою")
    own_goals = models.IntegerField("Автоголи")
    yellow_cards = models.IntegerField("Жовті карточки")
    red_cards = models.IntegerField("Червоні карточки")
    goals_from_the_penalty_spot = models.IntegerField("Голи з пенальті")
    average_time_on_the_field = models.CharField("Час на полі",max_length=50)
    # number_of_games_played = models.IntegerField("Кількість зіграних ігор")
    # replaced = models.IntegerField("Вийшов на заміну")
    # number_of_replacements = models.IntegerField("Кількість замін")
    facts =  models.TextField('Факти')
    images = models.URLField()
    
    def __str__(self):
        return self.name
 
    class Meta():
        verbose_name = "Ігроки"
        verbose_name_plural = "Ігроки"




class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name