import requests

# Функція для завантаження JSON-файла
def get_vulnerabilities():
    URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

    # Отримання даних з URL та перетворення їх у JSON-формат
    response = requests.get(URL).json()
    
    # Пошук даних, вони мають містити ключ "vulnerabilities", 
    # якщо йог не буде, то повернеться порожній список
    vulnerabilities = response.get("vulnerabilities", [])

    # Повертається результат змінної response (її вміст)
    return vulnerabilities