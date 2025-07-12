\# Teststrategie – TestifyHub QA-Projekt



\## 1. Ziel der Teststrategie



Diese Teststrategie beschreibt das Vorgehen zur Sicherstellung der Qualität der Testanwendungen im Projekt TestifyHub. Ziel ist es, systematisch funktionale und nicht-funktionale Anforderungen zu überprüfen – sowohl manuell als auch automatisiert.



\## 2. Testobjekte



\- Webanwendung \[SauceDemo](https://www.saucedemo.com)

\- RESTful API \[Reqres.in](https://reqres.in/)



\## 3. Testarten



\- \*Funktionale Tests\*: Login, Warenkorb, Checkout

\- \*Negative Tests\*: Ungültige Logins, leere Felder

\- \*Explorative Tests\*: Freies Testen neuer Funktionen

\- \*API-Tests\*: GET, POST, PUT, DELETE Requests mit Postman

\- \*Automatisierte UI-Tests\*: Mit Selenium (Login, Warenkorb, Checkout)



\## 4. Testmethoden



\- Black Box Testing

\- Smoke Testing

\- Explorative Testing

\- Regression Testing (in späteren Phasen)



\## 5. Testwerkzeuge



\- \*Manuelle Tests\*: Jira, Excel

\- \*Automatisierte Tests\*: Selenium + Python

\- \*API-Tests\*: Postman

\- \*Versionierung\*: Git \& GitHub

\- \*Editor\*: Visual Studio Code



\## 6. Testdaten



Die Tests nutzen vordefinierte Benutzerdaten von SauceDemo:



\- standard\_user / secret\_sauce

\- problem\_user / secret\_sauce

\- performance\_glitch\_user / secret\_sauce



\## 7. Testumgebung



\- \*Browser\*: Google Chrome (aktuelle Version)

\- \*OS\*: Windows 11

\- \*Netzwerk\*: stabile Internetverbindung

\- \*Testgeräte\*: Lokaler Mini-PC



\## 8. Risiken



\- Temporäre Nichterreichbarkeit von SauceDemo oder Reqres.in

\- API-Änderungen oder Downtime

\- Netzwerkprobleme bei automatisierten Tests



\## 9. Qualitätsziele



\- Alle kritischen Funktionen sind vollständig getestet

\- Kein Blocker-Bug bleibt ungeklärt

\- API-Endpunkte funktionieren zuverlässig (Status 200 / 201 / 204)

\- Automatisierte UI-Tests laufen fehlerfrei durch

