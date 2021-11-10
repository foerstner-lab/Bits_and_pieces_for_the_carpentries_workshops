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

**S**structured **Q**uery **L**anguage, oder SQL (manchmal auch "Fortsetzung" ausgesprochen), ist eine mächtige Sprache, die zum Abfragen und
relationale Datenbanken zu manipulieren. 

## Relationale Datenbanken

Relationale Datenbanken bestehen aus einer oder mehreren Datentabellen. Diese Tabellen haben
_Felder_ (Spalten) und _Datensätze_ (Zeilen). Diese Tabellen können
miteinander verknüpft, wenn ein Feld in einer Tabelle mit einem Feld in einer anderen Tabelle abgeglichen werden kann. 
SQL _queries_ sind die Befehle, mit denen Ihr Daten in einer Datenbank nachschlagen könnt oder
Berechnungen auf der Grundlage von Spalten durchführt.

## Warum SQL verwenden?

SQL ist sehr etabliert und ist immer noch weit verbreitet. 
in vielen Umgebungen. 

Mit SQL könnt ihr die Daten von der Analyse getrennt halten. Es besteht kein Risiko von
versehentliche Änderung von Daten, wenn Sie diese analysieren. Wenn die Daten geändert werden,
kann eine gespeicherte Abfrage erneut ausgeführt werden, um die neuen Daten zu analysieren.

SQL ist für den Umgang mit großen Datenmengen optimiert. Hilfe zu Datentypen
Qualitätskontrolle der Eingaben - ihr erhaltet eine Fehlermeldung.

Viele Webanwendungen (einschließlich WordPress und E-Commerce-Sites wie Amazon) laufen auf einer (relationalen) SQL-Datenbank. Das Verständnis von SQL ist der erste Schritt, um schließlich kundenspezifische Webanwendungen zu erstellen, die den Benutzern Daten zur Verfügung stellen können.

> ## Welche Verwendungsmöglichkeiten gibt es für SQL in Bibliotheken?
> 
> * Sie können SQL verwenden, um Makro- oder groß angelegte Änderungen an Metadatensätzen in Bibliotheksdatenbanken vorzunehmen, z. B. um Zeitschriftennamen zu aktualisieren, damit sie in der gesamten Datenbank konsistent oder normalisiert sind.
> 
> Für Situationen, in denen Sie mit Datenbankadministratoren in Ihrer Bibliothek oder einer größeren Organisation interagieren müssen, können Sie die Grundlagen von SQL erlernen, um sich mit der Terminologie besser vertraut zu machen.
> 
> * Da die SQL-Abfrage den Abfragen in natürlicher Sprache ähnelt, können Sie damit eine Vielzahl von Projekten organisieren (z.B. Programmevaluierung) und Fragen zu den Daten stellen, bevor Sie andere Datenanalysewerkzeuge einsetzen.
> 
> * Sie können SQL verwenden, um Ihre Bibliotheksdatenbank abzufragen und neue Ansichten zu erkunden, die nicht unbedingt über die patronseitigen Schnittstellen der Bibliothekssysteme bereitgestellt werden.
> 
> * SQL kann verwendet werden, um ein Inventar von Artikeln zu führen, z.B. für den Herstellerbereich einer Bibliothek, oder es kann verwendet werden, um Lizenzen für Zeitschriften zu verfolgen.
> 
> Für Projekte, bei denen Daten von einem System in ein anderes migriert und bereinigt werden müssen, kann SQL ein praktisches Werkzeug sein.
> 
> * Bei Tabellenkalkulationen mit Daten, die über Ordner verstreut sind, kann SQL ein nützliches Werkzeug sein, um diese Daten zu verbinden und in einer Datenbank oder einem zentralen Data Warehouse zusammenzuführen, wo sie für verschiedene Rollen in der Bibliothek zugänglich sind und an einem Ort abgefragt werden können.
> 
> * Es kann auch bei der anfänglichen Exposition bei der Interaktion mit einem System helfen, in Vorbereitung auf die spätere Interaktion mit einer Anwendungsprogrammierschnittstelle oder API.
> 
> Darüber hinaus können Sie über diese beiden Perspektiven lesen:
> 
> * [Eine Einführung in SQL für Bibliothekare](http://ruthtillman.com/an-introduction-to-sql-for-librarians/)
> 
> * [Datenwissenschaft ist jetzt anders: Lernen Sie SQL](https://veekaybee.github.io/2019/02/13/data-science-is-different/)
>
{: .callout}

## Datenbank-Management-Systeme

Es gibt eine Reihe von verschiedenen Datenbankverwaltungssystemen für die Arbeit mit
relationale Daten. Wir werden heute SQLite verwenden, aber im Grunde genommen kann alles, was wir
heute machen auch auf die anderen Datenbanksysteme anwenden (z.B. MySQL,
PostgreSQL, MS Access). Die einzigen Dinge, die sich unterscheiden werden.

## Einführung in den DB Browser for SQLite

Lasst uns alle die Datenbank, die wir über das Setup heruntergeladen haben, im DB Browser for SQLite öffnen.

Ihr könnt die Tabellen in der Datenbank sehen.
Um den Inhalt einer Tabelle zu sehen, klickt ihr auf diese Tabelle und dann auf die Schaltfläche Durchsuchen 
Datenregister oberhalb der Tabellendaten.

Wenn wir eine Abfrage schreiben wollen, klicken wir auf die Registerkarte SQL ausführen.

## Beschreibung des Datensatzes

Die Daten, die wir verwenden werden, bestehen aus 5 csv-Dateien, die Tabellen mit Artikeltiteln, Zeitschriften, Sprachen, Lizenzen und Verlagen enthalten. Die Informationen in diesen Tabellen stammen aus einer Stichprobe von 51 verschiedenen Zeitschriften, die im Jahr 2015 veröffentlicht wurden.


## Ein Hinweis zu Datentypen

Die Hauptdatentypen, die in der doaj-Artikel-Probendatenbank verwendet werden, sind `INTEGER` und `TEXT`, die definieren, welchen Wert die Tabellenspalte enthalten kann. 
