# Testplan – US-003: Checkout-Prozess starten

## Ziel

Benutzer sollen in der Lage sein, Produkte in den Warenkorb zu legen und den Checkout-Prozess erfolgreich zu starten.  
Dieser Testplan prüft alle Kernfunktionen des Warenkorbs bis zum Übergang zur Zahlungsseite.

---

## Testumgebung

- Browser: Google Chrome (aktuelle Version)
- Betriebssystem: Windows 10
- URL: [https://www.saucedemo.com](https://www.saucedemo.com)

---

## Voraussetzung

- Erfolgreicher Login mit gültigen Zugangsdaten:
  - Benutzername: standard_user
  - Passwort: secret_sauce
- Mindestens ein Produkt wird auf der Produktseite angezeigt

---

## Testfälle

---

### TC-011 – Produkt zum Warenkorb hinzufügen

*Schritte:*  
1. Login durchführen  
2. Ein beliebiges Produkt auswählen  
3. Auf „Add to cart“ klicken  
4. Warenkorb-Icon oben rechts überprüfen  

*Erwartet:*  
Warenkorb zeigt „1“ an. Produkt wurde korrekt hinzugefügt.

*Status:* Offen  

---

### TC-012 – Warenkorb öffnet sich mit dem richtigen Produkt

*Schritte:*  
1. Auf das Warenkorb-Symbol klicken  

*Erwartet:*  
Produktübersicht im Warenkorb zeigt genau das gewählte Produkt mit Namen, Preis und Bild an.

*Status:* Offen  

---

### TC-013 – Checkout-Button funktioniert korrekt

*Schritte:*  
1. Im Warenkorb auf „Checkout“ klicken  

*Erwartet:*  
Weiterleitung zur Seite /checkout-step-one.html erfolgt erfolgreich.

*Status:* Offen  

---

### TC-014 – Checkout-Seite zeigt Eingabemaske korrekt

*Schritte:*  
1. Nach Klick auf „Checkout“  
2. Formular für Vorname, Nachname, Postleitzahl erscheint  

*Erwartet:*  
Formularfelder sind sichtbar und beschriftet. Kein Darstellungsfehler.

*Status:* Offen  

---

### TC-015 – „Zurück“-Button bringt Nutzer zur Produktseite

*Schritte:*  
1. Auf der Checkout-Seite auf „Cancel“ klicken  

*Erwartet:*  
Benutzer wird zurück zur Produktübersicht /inventory.html geleitet.

*Status:* Offen  

---

## Autor

- *Tester:* Khalil Nasri  
- *Erstellt am:* 15.07.2025

