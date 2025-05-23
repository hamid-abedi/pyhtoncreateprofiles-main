import unittest
import csv
import json

class TestData(unittest.TestCase):
    def test_csv_columns(self):
        with open('profiles1.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            self.assertEqual(len(headers), 12, "CSV file should have 12 columns")

    def test_csv_rows(self):
        with open('profiles1.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            row_count = sum(1 for row in reader) - 1  # Subtract header
            self.assertGreater(row_count, 900, "CSV file should have more than 900 rows")

    def test_json_properties(self):
        with open('data.json', 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            expected_properties = ['Givenname', 'Surname', 'Streetaddress', 'City', 'Zipcode', 'Country', 'CountryCode', 'NationalId', 'TelephoneCountryCode', 'Telephone', 'Birthday', 'ConsentToContact']
            for item in data:
                self.assertTrue(all(prop in item for prop in expected_properties), 
                               f"JSON missing required properties: {item}")

    def test_json_rows(self):
        with open('data.json', 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            self.assertGreater(len(data), 900, "JSON file should have more than 900 rows")

if __name__ == '__main__':
    unittest.main()