class InvalidSchnitzel(Exception):
	pass

bewertungsNamen = {
	1 : "Mangelhaft",
	2 : "Ausreichend",
	3 : "Befriedigend",
	4 : "Gut",
	5 : "Sehr Gut"
}

def bewerte(zahl):

	try:
		zahl = int(zahl)
	except(ValueError):
		raise InvalidSchnitzel


	if zahl > 0 and zahl <= 5:
		return bewertungsNamen[zahl]
	else:
		raise InvalidSchnitzel
		

def durchschnitt(zahlen):
	summe = 0
	for x in zahlen:
		summe += x

	ergebnis = summe / len(zahlen)
	return ergebnis
