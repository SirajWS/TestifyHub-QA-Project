# Testplan – US-001 Login-Funktion

## Ziel
Test der Login-Funktion auf https://www.saucedemo.com gemäß den Akzeptanzkriterien.

## Testumgebung
- Browser: Chrome (aktuelle Version)
- OS: Windows 10
- URL: https://www.saucedemo.com

## Testdaten
- ✅ Gültig: `standard_user` / `secret_sauce`
- ❌ Ungültig: `fake_user` / `wrongpass`

## Testfälle

### TC-001 – Login mit gültigen Daten
- Gehe zu https://www.saucedemo.com
- Eingabe: `standard_user` / `secret_sauce`
- Klick auf Login
- ✅ Erwartet: Weiterleitung zu `/inventory.html`

### TC-002 – Login mit ungültigem Passwort
- Eingabe: `standard_user` / `wrongpass`
- ✅ Erwartet: Fehlermeldung sichtbar

### TC-003 – Login mit ungültigem Benutzernamen
- Eingabe: `fake_user` / `secret_sauce`
- ✅ Erwartet: Fehlermeldung sichtbar

### TC-004 – Leerer Benutzername
- Eingabe: (leer) / `secret_sauce`
- ✅ Erwartet: Fehlermeldung sichtbar

### TC-005 – Leeres Passwort
- Eingabe: `standard_user` / (leer)
- ✅ Erwartet: Fehlermeldung sichtbar

### TC-006 – Beide Felder leer
- Eingabe: (leer) / (leer)
- ✅ Erwartet: Fehlermeldung sichtbar