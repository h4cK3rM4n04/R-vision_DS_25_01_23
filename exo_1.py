#Q1 : Compléter une fonction limite_amplitude qui prend en paramètre un nombre x ainsi que deux nombres x_min et x_max avec x_min <= x_max  et qui renvoie :
#x si x est compris entre x_min et x_max,
#x_min si x est plus petit que x_min,
#x_max si x est plus grand que x_max.

def limite_amplitude(x, x_min, x_max) :
    ''' renvoie une valeur écrétée entre x_min et x_max'''
    # YOUR CODE HERE
    if x_min < x and x_max > x or x_min > x and x_max < x:
        return x
    elif x < x_min:
        return x_min
    elif x > x_max:
        return x_max
print(limite_amplitude(180, -150, 150))

#assert limite_amplitude(34, -150, 150) == 34
#assert limite_amplitude(-187, -150, 150) == -150
#assert limite_amplitude(180, -150, 150) == 150