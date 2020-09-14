#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	return v1[0]*v2[0] + v1[1]*v2[1] == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	sum = 0
	neg = 0
	for v in values:
		if(v < 0):
			neg += 1
			continue
		sum += v
	return sum / (len(values) - neg)

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	# twenties = 0
	# tens = 0
	# fives = 0
	# ones = 0
	# while value != 0:
	# 	if value >= 20:
	# 		twenties = value // 20
	# 		value %= 20
	# 	elif value >= 10:
	# 		tens = value // 10
	# 		value %= 10
	# 	elif value >= 5:
	# 		tens = value // 5
	# 		value %= 5
	# 	elif value >= 1:
	# 		ones = value
	# 		value %= 1
	bill_values = [20, 10, 5, 1]
	result = []
	for bill in bill_values:
		if(value >= bill):
			result += [value // bill]
			value %= bill

	return result

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
