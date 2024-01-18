class Phonebook:
    def __init__(self, filename='book.txt') -> None:
        self.filename = filename
        self.phonebook = self.read_phonebook()
    def read_phonebook(self):
        phonebook = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split('; ')
                    phonebook[phone_number] = name
        except FileNotFoundError:
            print("Brak pliku.")
        return phonebook

phonebook = Phonebook()

print(phonebook)