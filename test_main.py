import unittest

from main import bewerte, InvalidSchnitzel, durchschnitt

class TestMain(unittest.TestCase):

	def test_eingabe_3_ist_gueltig(self):
		# arrange
		zahl = 3
		# act
		result = bewerte(zahl)
		# assert
		self.assertEqual(result, "Befriedigend")

	def test_eingabe_1_ist_gueltig(self):
		# arrange
		zahl = 1
		# act
		result = bewerte(zahl)
		# assert
		self.assertEqual(result, "Mangelhaft")


	def test_eingabe_6_ist_nicht_gueltig(self):
		# arrange
		zahl = 6
		# act
		# assert
		self.assertRaises(InvalidSchnitzel, bewerte, zahl)

	def test_string_eingabe_ungueltig(self):
		# arrange
		input = "test"
		# act
		# assert
		self.assertRaises(InvalidSchnitzel, bewerte, input)

	def test_durchschnittsbewertung(self):
		# arrange
		bewertungen = [3,5,1,2,4]
		# act
		result = durchschnitt(bewertungen)
		# assert
		self.assertEqual(result, 3.0)

# test

if __name__ == "__main__":
	unittest.main()
