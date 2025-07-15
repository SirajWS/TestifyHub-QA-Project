# Testplan – US-002: Produktseite anzeigen

## Ziel

Nach erfolgreichem Login soll der Nutzer eine vollständige Produktseite sehen.  
Dieser Testplan stellt sicher, dass alle Produkte korrekt geladen, angezeigt und dargestellt werden.

---

## Testumgebung

- Browser: Google Chrome (aktuelle Version)
- Betriebssystem: Windows 10
- URL: [https://www.saucedemo.com/inventory.html](https://www.saucedemo.com/inventory.html)

---

## Voraussetzung

- Erfolgreicher Login mit gültigen Zugangsdaten:
  - Benutzername: standard_user
  - Passwort: secret_sauce

---

## Testfälle

---

### TC-007 – Produkte werden angezeigt

*Schritte:*  
1. Login durchführen  
2. Weiterleitung zur Produktseite abwarten  

*Erwartet:*  
Die Produktliste wird vollständig angezeigt (6 Produkte sichtbar).

*Status:* Offen  

---

### TC-008 – Produktnamen sind sichtbar und korrekt

*Schritte:*  
1. Auf der Produktseite die Namen aller Produkte prüfen  

*Erwartet:*  
Alle Produktnamen sind lesbar, eindeutig und stimmen mit den Daten im System überein (z. B. „Sauce Labs Backpack“).

*Status:* Offen  

---

### TC-009 – Produktbilder laden korrekt

*Schritte:*  
1. Auf der Produktseite die Produktbilder prüfen  

*Erwartet:*  
Alle Bilder sind sichtbar, nicht verzerrt und korrekt geladen (keine gebrochenen Bildsymbole).

*Status:* Offen  

---

### TC-010 – Preisangaben stimmen mit Produktdaten überein

*Schritte:*  
1. Produktpreise mit den vorgesehenen Standardwerten vergleichen  

*Erwartet:*  
Jedes Produkt zeigt den richtigen Preis an (z. B. „$29.99“ bei „Sauce Labs Backpack“).

*Status:* Offen  

---

## Autor

- *Tester:* Khalil Nasri  
- *Erstellt am:* 15.07.2025

