from fastapi import APIRouter

from utils import get_vulnerabilities

router = APIRouter(tags=['10 known CVEs'])

@router.get("/get/known")
def known_cve():

    known_vul = []

    for vuln in get_vulnerabilities():
        # Перевірка, чи є ключ "knownRansomwareCampaignUse"
        if 'knownRansomwareCampaignUse' in vuln:
            # Якщо значення ключа knownRansomwareCampaignUse містить "Known",
            # Результат додається в змінну known_vul
            if "Known" in vuln['knownRansomwareCampaignUse']:
                known_vul.append(vuln)

    return known_vul[:10]