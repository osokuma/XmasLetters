from django.db import models

# Create your models here.
class user_kid(models.Model):
    name = models.CharField(max_length=30)
    parent = models.CharField(max_length=30)
    parent_mail = models.ForeignKey()
    # esto, como se envia al mail del padre?
    your letter = models.ManyToManyField('app.letter_databases')


class letter (models.Model):
    your letter = models.ManyToManyField('app.letter_databases')
    letters_from the world = models.ManyToManyField('app.letter_databases'))
    parent_mail = models.ForeignKey('app.parent_mail')



class letter_databases (models.Model):    
	# Yo no se que va aqui ¯\_(ツ)_/¯
	# Yo no se que va aqui ¯\_(ツ)_/¯
	# Pero supongo que es algo así

	your letter = models.CharField(max_length=700)
	# + una key para identifcar cada una de las cartas

	letters_from the world = models.CharField(max_length=800)
	# + un metodo que nos de una opcion aleatoreamente

	databses = 
	# + las keys necesarias  y no tengo idea de que más

	# No se si nada de esto es correcto ¯\_(ツ)_/¯
	# No se si nada de esto es correcto ¯\_(ツ)_/¯


class providers (models.Model):
	# Para que les repito lo mismo ¯\_(ツ)_/¯
