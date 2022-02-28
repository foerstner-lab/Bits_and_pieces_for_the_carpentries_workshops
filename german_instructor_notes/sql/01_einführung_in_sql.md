---
Titel: "Einführung in SQL".
Unterricht: 15
Übungen: 0
Fragen:
- "Was ist SQL?"
- "Warum ist es signifikant?"
- "Was ist die Beziehung zwischen einer relationalen Datenbank und SQL?"
Ziele:
- "Definieren Sie eine relationale Datenbank."
- "Erklären Sie, was SQL ist und warum man es verwenden sollte."
- "Identifizieren Sie Bibliotheks- und Informationskenntnisse, die sich auf die Verwendung von SQL beziehen".
Schlüsselpunkte:
- "SQL ist eine mächtige Sprache zum Abfragen und Manipulieren von relationalen Datenbanken".
- "Personen, die in bibliotheks- und informationsbezogenen Funktionen arbeiten, verfügen über Fähigkeiten, die es ihnen ermöglichen, SQL zum Organisieren von und Zugreifen auf Daten zu verwenden.
---

## Was ist SQL?

**S**tructured **Q**uery **L**anguage, oder SQL ist eine mächtige Sprache, um
relationale Datenbanken abzufragen und zu bearbeiten. 

## Relationale Datenbanken

Relationale Datenbanken bestehen aus einer oder mehreren Datentabellen. Diese Tabellen haben
_Felder_ (Spalten) und _Datensätze_ (Zeilen). Diese Tabellen können
miteinander verknüpft werden, wenn ein Feld in einer Tabelle mit einem Feld in einer anderen Tabelle abgeglichen werden kann. 
SQL _queries_ sind die Befehle, mit denen Ihr Daten in einer Datenbank abfragen könnt oder
Berechnungen auf der Grundlage von Spalten durchführen könnt.

## Warum SQL verwenden?

- SQL ist sehr etabliert und ist immer noch weit verbreitet. in vielen Umgebungen. (In jedem Smartphone, und Rechner verbaut)
- Mit SQL könnt ihr die Daten von der Analyse getrennt halten. Es besteht kein Risiko von 
versehentliche Änderung von Daten, wenn Sie diese analysieren. Wenn die Daten geändert werden, 
kann eine gespeicherte Abfrage erneut ausgeführt werden, um die neuen Daten zu analysieren.
- SQL ist für den Umgang mit großen Datenmengen optimiert. Hilfe zu Datentypen 
Qualitätskontrolle der Eingaben - ihr erhaltet eine Fehlermeldung.

Viele Webanwendungen (wie Amazon oder WordPress) laufen auf einer SQL-Datenbank. Das Verständnis von SQL ist der erste Schritt, um schließlich kundenspezifische Webanwendungen zu erstellen, die den Benutzern Daten zur Verfügung stellen können. https://sqlite.org/mostdeployed.html

## Welche Verwendungsmöglichkeiten gibt es für SQL in Bibliotheken?
 - Ihr könnt SQL verwenden, um Makro- oder groß angelegte Änderungen an Metadatensätzen in Bibliotheksdatenbanken vorzunehmen, z. B. um Zeitschriftennamen zu aktualisieren, damit sie in der gesamten Datenbank konsistent oder normalisiert sind.
- Zur Kommunikation mit Datenbankadministratoren in eurer Bibliothek
- Da die SQL-Abfrage den Abfragen in natürlicher Sprache ähnelt, könnt ihr damit eine Vielzahl von Projekten organisieren und Fragen zu den Daten stellen, bevor ihr andere Datenanalysewerkzeuge wie Pandas (Python) einsetzt.
- Ihr könnt mit SQL eure Bibliotheksdatenbank abzufragen 
- Bei Tabellenkalkulationen mit Daten, die über Ordner verstreut sind, kann SQL ein nützliches Werkzeug sein, um diese Daten zu verbinden und in einer Datenbank zusammenzuführen, wo sie für verschiedene Rollen in der Bibliothek zugänglich sind und an einem Ort abgefragt werden können.
- mehr dazu
  - [Eine Einführung in SQL für Bibliothekare](http://ruthtillman.com/an-introduction-to-sql-for-librarians/)
  - [Datenwissenschaft ist jetzt anders: Lernen Sie SQL](https://veekaybee.github.io/2019/02/13/data-science-is-different/)

## Datenbank-Management-Systeme

Es gibt eine Reihe von verschiedenen Datenbankverwaltungssystemen für die Arbeit mit
relationale Daten. Wir werden heute SQLite verwenden, aber im Grunde genommen kann alles, was wir
heute machen auch auf die anderen Datenbanksysteme anwenden (z.B. MySQL,
PostgreSQL, MS Access). 

## Einführung in den DB Browser for SQLite

Lasst uns alle die Datenbank, die wir über das Setup heruntergeladen haben, im DB Browser for SQLite öffnen.

Ihr könnt die Tabellen über den Reiter "Datenbankstruktur". Wenn ihr die Tabellennamen anklickt könnt ihr die Indexspalte der Tabelle sehen und welche Datentypen in den einzelnen Spalten enthalten sind. Die Hauptdatentypen, die in unserer Datenbank verwendet werden, sind INTEGER und TEXT. Wenn wir auf "Daten durchsuchen" klicken können wir uns die Daten in den Tabellen genauer anschauen. Oben links können wir zwischen den verschiedenen Tabellen wechseln.

Wenn wir eine Abfrage schreiben wollen, klicken wir auf die Registerkarte "SQL ausführen".

## Beschreibung des Datensatzes

Die Daten, die wir verwenden werden, bestehen aus 5 csv-Dateien, die Tabellen mit Artikeltiteln, Zeitschriften, Sprachen, Lizenzen und Verlagen enthalten. Die Informationen in diesen Tabellen stammen aus einer Stichprobe von 51 verschiedenen Zeitschriften, die im Jahr 2015 veröffentlicht wurden.

 
