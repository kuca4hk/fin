# Úkol - Finitimi

## Před spuštěním
Před spuštěním aplikace je potřeba mít nainstalovaný DOCKER, conda(venv), python 3.10 a postgresql

## Instalace requirements
Pro instalaci requirements použijte následující příkaz:
```
pip install -r requirements.txt
```

## ENV
Pro správné fungování aplikace je potřeba mít nastavené proměnné, které najdete v souboru .env-sample, vytvořte si nový soubor s názvem .env

## Docker
Pro správnou funkčnost aplikace je nejprve třeba spustit docker container s PostreSQL, pomocí následujících příkazů:

```
docker-compose up
```
Spuštění DB
```
docker-compose up db
```
Po ukončení testů, je možné DB smazat pomocí následujícího příkazu:
```
docker-compose down -v
```
## Migrace
Pro správnou funkčnost DB, je nutné provést migrace, pomocí následujícího příkazu:
```
python manage.py migrate
```
## Spuštění aplikace
Pro spuštění aplikace použijte následující příkaz
```
python manage.py runserver
```
## Testovací data

Jako první je potřeba vytvořit superusera, pomocí následujícího příkazu:
```
python manage.py createsuperuser
```
Dále je potřeba vytvořit store, v adminu.

Data jsem si nahrával přes POSTMANA, pomoci POST requestu ve formátu:
```json
{
    "brand": "{nazev_znacky}",
    "model": "{nazev_modelu}",
    "price": {cena},
    "manufacturing_year": "{rok_vyroby}"
}

```
je potřeba mít vytvořeného druhého uživatele(který nebude mít práva superuser, je potřeba pro správný testing endpointu se statistikama a logováním) , vytvoříte si ho pomoci příkazu:
```
python manage.py createsuperuser
```
a následně použít v POSTMANU autentizaci BASIC_AUTH.

## API - POST Nákup auta obchodem
Pro nákup auta obchodem použijte následující odkaz:

http://127.0.0.1:8000/v1/api/cars/store-buy-car/

## API - POST Prodej auta obchodem
Pro prodej auta obchodem použijte následující odkaz:

http://127.0.0.1:8000/v1/api/cars/store-sell-car/<int:id>/

## API - GET 10 Nejdražší auta
Pro získání dat o 10 nejdrazších autech použijte následující odkaz:

http://127.0.0.1:8000/v1/api/cars/most-expensive/

## API - GET 10 Nejstarší aut

Pro získání dat o 10 nejstarších autech použijte následující odkaz:

http://127.0.0.1:8000/v1/api/cars/oldest/


## API - GET  Logs
Pro získání logů z prodejů a nákupů použijte následující odkaz:

http://127.0.0.1:8000/v1/api/store/store-log/


## API - GET  Statistiky
Pro získání statistik z prodejů a nákupů použijte následující odkaz:

http://127.0.0.1:8000/v1/api/store/store-log/

## API - přehled endpointů
Pro získání přehledu endpointů použijte následující odkaz:

http://127.0.0.1:8000/swagger/

