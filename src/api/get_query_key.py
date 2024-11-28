from fastapi import APIRouter

from utils import get_vulnerabilities

router = APIRouter(tags=['CVEs that contain the keyword'])

@router.get("/get")
def cve_by_keyword(keywordSearch):

    filtered_vul = []

    for vuln in get_vulnerabilities():
        if 'shortDescription' in vuln:
            # Якщо ключове слово міститься в описі вразливості,
            # cve додається в попередньо створений список
            # При чому, запит користувача та опис вразилвості 
            # перетворюється в нижній регістр
            if keywordSearch.lower() in vuln['shortDescription'].lower():
                filtered_vul.append(vuln)

    return filtered_vul