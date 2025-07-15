# Testplan – US-001: Login-Funktion

## Ziel

Die Login-Funktion von https://www.saucedemo.com soll gemäß den definierten Akzeptanzkriterien getestet werden.  
Ziel ist es, sicherzustellen, dass Benutzer sich mit gültigen Zugangsdaten einloggen können und bei ungültigen Daten eine entsprechende Fehlermeldung erscheint.

---

## Testumgebung

- Browser: Google Chrome (aktuelle Version)
- Betriebssystem: Windows 10
- URL: [https://www.saucedemo.com](https://www.saucedemo.com)

---

## Testdaten

| Art       | Benutzername    | Passwort       |
|-----------|------------------|----------------|
| Gültig    | standard_user    | secret_sauce   |
| Ungültig  | fake_user        | wrongpass      |
| Leere Eingabe | (leer)     | (leer)       |

---

## Testfälle

---

### TC-001 – Login mit gültigen Zugangsdaten

*Voraussetzung:* Login-Seite ist geöffnet  
*Eingaben:*  
- Benutzername: standard_user  
- Passwort: secret_sauce  
*Schritte:*  
1. Login-Seite öffnen  
2. Gültige Zugangsdaten eingeben  
3. Auf „Login“ klicken  
*Erwartet:* Weiterleitung zu /inventory.html  
*Status:* Offen  

---

### TC-002 – Login mit ungültigem Passwort

*Eingaben:*  
- Benutzername: standard_user  
- Passwort: wrongpass  
*Erwartet:* Fehlermeldung wird angezeigt  
*Status:* Offen  

---

### TC-003 – Login mit ungültigem Benutzernamen

*Eingaben:*  
- Benutzername: fake_user  
- Passwort: secret_sauce  
*Erwartet:* Fehlermeldung wird angezeigt  
*Status:* Offen  

---

### TC-004 – Login mit leerem Benutzernamen

*Eingaben:*  
- Benutzername: (leer)  
- Passwort: secret_sauce  
*Erwartet:* Fehlermeldung wird angezeigt  
*Status:* Offen  

---

### TC-005 – Login mit leerem Passwort

*Eingaben:*  
- Benutzername: standard_user  
- Passwort: (leer)  
*Erwartet:* Fehlermeldung wird angezeigt  
*Status:* Offen  

---

### TC-006 – Login mit beiden leeren Feldern

*Eingaben:*  
- Benutzername: (leer)  
- Passwort: (leer)  
*Erwartet:* Fehlermeldung wird angezeigt  
*Status:* Offen  

---

## Autor

- *Tester:* Khalil Nasri  
- *Erstellt am:* 15.07.2025

