\# Testplan – TestifyHub QA-Projekt



\## 1. Ziel des Tests



Ziel ist es, die grundlegenden Funktionalitäten der Webanwendung \[https://www.saucedemo.com](https://www.saucedemo.com) zu verifizieren. Dazu zählen insbesondere Login, Produktanzeige, Warenkorb-Funktionalität und der Checkout-Prozess.



\## 2. Testumfang



\### Im Umfang:

\- Login mit verschiedenen Benutzertypen

\- Anzeige und Auswahl von Produkten

\- Hinzufügen und Entfernen von Artikeln im Warenkorb

\- Durchführung des Checkout-Prozesses

\- Logout



\### Nicht im Umfang:

\- Design- und Usability-Tests

\- Performance-Tests

\- Tests auf mobilen Geräten

\- Datenbankvalidierung



\## 3. Testmethoden



\- Black Box Testing

\- Explorative Tests

\- Smoke Testing

\- Regression Testing (später)



\## 4. Testarten



\- Funktionale Tests (Login, Warenkorb, Checkout)

\- Negative Tests (z. B. falsche Logins, leere Felder)

\- Grenzwerttests

\- Explorative Tests



\## 5. Testumgebung



\- Browser: Google Chrome (aktuelle Version)

\- Betriebssystem: Windows 11

\- Netzwerk: stabile Internetverbindung

\- Geräte: Lokaler Mini-PC

\- Tools: GitHub, Jira, Excel, Selenium, Postman



\## 6. Testdaten



Folgende vordefinierte Benutzer werden für die Tests verwendet:



| Benutzername               | Passwort       | Beschreibung              |

|---------------------------|----------------|---------------------------|

| standard\_user             | secret\_sauce   | Normales Testprofil       |

| problem\_user              | secret\_sauce   | Simuliert Fehlerfälle     |

| performance\_glitch\_user   | secret\_sauce   | Testet bei langsamer Reaktion |



\## 7. Rollen und Verantwortlichkeiten



| Rolle              | Verantwortlich         |

|--------------------|-------------------------|

| Testdurchführung   | Khalil Nasri           |

| Testplanung        | Khalil Nasri           |

| Bug Reporting      | Khalil Nasri           |

| Dokumentation      | Khalil Nasri           |



\## 8. Testkriterien



\*Eintrittskriterien:\*

\- Zugang zur Testumgebung ist gewährleistet

\- Testplan und Teststrategie sind dokumentiert

\- Jira und GitHub sind eingerichtet



\*Abnahmekriterien:\*

\- Alle kritischen Testfälle sind erfolgreich bestanden

\- Es gibt keine offenen Blocker-Bugs



\## 9. Risiken



\- Unerreichbarkeit der Anwendung (saucedemo.com)

\- Instabile API/Website

\- Browser- oder Netzwerkausfälle



\## 10. Zeitplan (geplant)



| Aktivität                 | Zeitraum         |

|---------------------------|------------------|

| Testplanung               | Woche 1          |

| Manuelle Testdurchführung| Woche 1          |

| API Testing mit Postman  | Woche 2          |

| Selenium UI-Tests        | Woche 3          |

| Abschluss \& Dokumentation| Woche 4          |

