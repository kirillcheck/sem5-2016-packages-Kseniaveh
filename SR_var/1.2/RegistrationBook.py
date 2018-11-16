class Registration:
    """Создаем конструктор, где его свойство participants - пустой список"""
    def __init__(self):
        self.participants = list()

    """Создаем метод "Добавление участника", где его входные значения - имя, фамилия, возраст и почта"""
    def AddingMember(self, name, surname, age, email):
        self.participants.append({"Participant name": name,
                                 "participant surname": surname,
                                 "participant age": age,
                                 "participant email": email})
    
    """Создаем метод "Удаление участника", где удаление участника идет по почте, 
    так как email - это уникаьное значение"""
    def DeleteMember(self, name):
        for participant in self.participants:
            if participant.get("participant email") == email:
                self.participants.remove(participant)

    """Создаем метод - Запись в файл"""
    def RecordFile(self):
        import json # чтобы преобразовать в json из dict в котором list
        with open("./new_file.json", 'a') as file:
            json_data = { "all_participant": self.participants } 
            # dumps = сделай мне пожалуйста из dict json
            # indent = количество пробелов в отступах
            file.write(json.dumps(json_data, indent=4))
            
if __name__ == "__main__":
    GuestBook = Registration()
    GuestBook.AddingMember("Ksenia", "Vehov", 20, "ksen@gmail.com")
    GuestBook.AddingMember("IaIaIa", "Foool", 200, "iafoool@gmail.com")
    GuestBook.RecordFile()