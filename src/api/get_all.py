from fastapi import APIRouter
from datetime import datetime, timedelta

from utils import get_vulnerabilities

router = APIRouter(tags=['Up to 40 CVE in the last 5 days'])

@router.get("/get/all")
def last_five_days_cve():
    # Отримання поточного часу 
    current_date = datetime.now()

    # Отримання дати, яка була 5 днів тому
    last_five_days = current_date - timedelta(days=5)

    # Форматування дати last_five_days до формату YYYY-MM-DD
    last_five_days_format = last_five_days.strftime('%Y-%m-%d')

    # Створення порожнього списка
    last_five_days_vuln = []

    # Перебір усіх вразливостей, отриманих з функції "get_vulnerabilities"
    for vuln in get_vulnerabilities():
        # Перевірка, чи є ключ "dateAdded"
        if 'dateAdded' in vuln:
            # Якщо дата вразливості більша або дорівнює даті 5 днів тому, 
            # cve додається в попередньо створений список
            if vuln['dateAdded'] >= last_five_days_format:
                last_five_days_vuln.append(vuln)

    # Повертається перші 40 результатів
    return last_five_days_vuln[:40]
