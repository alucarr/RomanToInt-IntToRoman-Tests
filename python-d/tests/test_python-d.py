import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from RomanToInt import roman_to_int

import unittest


BASE_DIR = os.path.dirname(__file__)
VALID_CASES_PATH = os.path.join(BASE_DIR, 'validcases.txt')
INVALID_CASES_PATH = os.path.join(BASE_DIR, 'invalidcases.txt')

def read_valid_cases(filename=VALID_CASES_PATH):
    cases = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            roman, val = parts
            cases[roman] = int(val)
    return cases

def read_invalid_cases(filename=INVALID_CASES_PATH):
    cases = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cases.append(line)
    return cases

class TestRomanToInt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_cases = read_valid_cases()
        cls.invalid_cases = read_invalid_cases()

    def test_valid_cases(self):
        errors = []

        with open("tests/validcases.txt", "r") as file:
            for expected_value, line in enumerate(file, start=1):
                roman = line.strip()
                try:
                    result = roman_to_int(roman)
                    self.assertEqual(result, expected_value)
                except AssertionError as e:
                    errors.append(f"❌ HATA: {roman} → {result} (beklenen: {expected_value})")

        if not errors:
            print("✅ Tüm Roman rakamları başarıyla test edildi.")
        else:
            print(f"\n❌ {len(errors)} test başarısız oldu:\n")
            for error in errors:
                print(error)

        self.assertEqual(len(errors), 0, f"{len(errors)} tane valid case başarısız oldu.")

    def test_invalid_cases(self):
        errors = []

        for roman in self.invalid_cases:
            try:
                result = roman_to_int(roman)
                if result is not None:
                    errors.append(f"❌ HATA: '{roman}' geçersiz ama {result} olarak döndü.")
            except Exception:
                continue

        if not errors:
            print("✅ Tüm invalid Roman rakamları doğru şekilde reddedildi.")
        else:
            print(f"\n❌ {len(errors)} invalid test başarısız oldu:\n")
            for error in errors:
                print(error)

        self.assertEqual(len(errors), 0, f"{len(errors)} tane invalid case hatalı şekilde kabul edildi.")


if __name__ == "__main__":
    unittest.main()
