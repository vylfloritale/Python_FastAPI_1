from fastapi import APIRouter

from utils import get_vulnerabilities

router = APIRouter(tags=['10 latest CVEs'])

@router.get("/get/new")
def latest_cve():

    # З функції "get_vulnerabilities" повертається 10 останніх значень.
    # Тут немає потреби в сортуванні, тому що останні CVE є найновішими за замовчуванням
    return get_vulnerabilities()[:10]