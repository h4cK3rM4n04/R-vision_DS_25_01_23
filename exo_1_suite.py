#Q2 : Ecrire la fonction secrete qui prend en paramètre un tableau de valeurs ainsi 
#que x_min et x_max avec x_min <= x_max et renvoie un tableau des valeurs écrêtées entre x_min et x_max.
#On utilisera la fonction limite_amplitude programmée à la question 1.

def limite_amplitude(x, x_min, x_max) :
    ''' renvoie une valeur écrétée entre x_min et x_max'''
    # YOUR CODE HERE
    if x_min < x and x_max > x or x_min > x and x_max < x:
        return x
    elif x < x_min:
        return x_min
    elif x > x_max:
        return x_max
print('limite_aplitude:	', limite_amplitude(180, -150, 150))
print("")

liste_donne = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
def ecrete(valeurs,x_min,x_max):
	valeur_secretes = []
	for i in valeurs:
		valeur_secretes.append(limite_amplitude(i, x_min, x_max))
	return valeur_secretes
print(ecrete(liste_donne,-150, 150))


#valeurs = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
#assert ecrete( valeurs, -150, 150) == [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]

#==========INSPIR2 PAR LE CODE DE MR JAUR7S=====
print("")

