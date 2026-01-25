# CurrencyRatesApp

## Opis projektu

Currency Rates App to aplikacja webowa umożliwiająca pobieranie, zapisywanie oraz wyświetlanie kursów walut na podstawie danych udostępnianych przez **API Narodowego Banku Polskiego (NBP)**. Dane mogą być przeglądane z podziałem na **lata, kwartały, miesiące oraz dni**.

Projekt został zrealizowany w celach edukacyjnych i skupia się na:

* architekturze frontend–backend,
* konteneryzacji przy użyciu Dockera,
* automatycznych testach jednostkowych i BDD.

---

## Technologie

### Frontend

* Angular
* TypeScript
* HTML / CSS
* Jasmine, Karma (testy jednostkowe)

### Backend

* Django Rest Framework **lub** FastAPI
* Python 3.x
* Pytest / Unittest (testy jednostkowe)

### Baza danych

* PostgreSQL (lub inna relacyjna SQL)

### Inne

* Docker
* Docker Compose
* API NBP ([https://api.nbp.pl](https://api.nbp.pl))

---

## Funkcjonalności

* Pobieranie kursów walut z API NBP
* Zapisywanie danych w bazie danych
* Wyświetlanie kursów walut w tabeli
* Filtrowanie danych według:

  * lat
  * kwartałów
  * miesięcy
  * dni
* Komunikacja frontend ↔ backend przez REST API

---

## Architektura aplikacji

Aplikacja składa się z trzech niezależnych modułów:

* **Frontend** – aplikacja Angular odpowiedzialna za interfejs użytkownika
* **Backend** – REST API obsługujące logikę biznesową i komunikację z bazą danych
* **Baza danych** – PostgreSQL przechowująca kursy walut

Każdy moduł uruchamiany jest w osobnym kontenerze Docker.

---

## Endpointy API

| Metoda | Endpoint           | Opis                                      |
| ------ | ------------------ | ----------------------------------------- |
| GET    | /currencies        | Lista dostępnych walut                    |
| GET    | /currencies/{date} | Kursy walut z wybranego dnia              |
| POST   | /currencies/fetch  | Pobranie kursów z API NBP i zapis do bazy |

---

## Testy

### Backend

* Testy endpointów API
* Testy połączenia z bazą danych
* Testy poprawności danych

### Frontend

* Testy komponentów
* Testy serwisów HTTP
* Test działania przycisków i wyświetlania danych

Testy realizowane są zgodnie z podejściem **BDD (Behavior-Driven Development)**.

---

## Uruchomienie projektu

### Wymagania

* Docker
* Docker Compose

### Instrukcja uruchomienia

```bash
git clone https://github.com/<twoj-login>/currency-rates-app.git
cd currency-rates-app
docker-compose up --build
```

Po uruchomieniu:

* Frontend: `http://localhost:4200`
* Backend API: `http://localhost:8000`

---

## Struktura projektu

```
currency-rates-app/
│
├── frontend/
├── backend/
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## Dokumentacja i rozwój

* Wszystkie etapy implementacji są dokumentowane w commitach
* Projekt jest przygotowany do demonstracji
* Możliwość dalszej rozbudowy (wykresy, cache, autoryzacja)

Kierunek / Uczelnia
Rok akademicki
