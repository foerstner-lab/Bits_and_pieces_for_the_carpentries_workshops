---
Titel: "Einführung in OpenRefine"
Unterricht: 15
Übungen: 0
Fragen:
- "Was ist OpenRefine? Was kann es leisten?"
Ziele:
- "Erklären Sie, was die OpenRefine Software macht"
- Erklären Sie, wie die OpenRefine-Software bei der Arbeit mit Datendateien helfen kann.
Kernpunkte:
- OpenRefine ist "ein Werkzeug für die Arbeit mit unordentlichen Daten".
- "OpenRefine funktioniert am besten mit Daten in einem einfachen Tabellenformat".
- OpenRefine kann Ihnen helfen, Daten in feinere Teile aufzuteilen.
- OpenRefine kann Ihnen helfen, lokale Daten mit anderen Datensätzen abzugleichen.
- OpenRefine kann Ihnen helfen, einen Datensatz mit Daten aus anderen Quellen anzureichern.
---

## Was ist OpenRefine?
 OpenRefine ist eine Desktop-Anwendung, die Ihren Webbrowser als grafische Schnittstelle nutzt. Es wird als "ein leistungsstarkes Werkzeug für die Arbeit mit unordentlichen Daten" beschrieben ([David Huynh](http://web.archive.org/web/20141021040915/http://davidhuynh.net/spaces/nicar2011/tutorial.pdf)) - aber was bedeutet das? Es ist wahrscheinlich am einfachsten, die Arten von Daten zu beschreiben, mit denen OpenRefine gut arbeiten kann, und die Arten von Problemen, die es Ihnen oder Ihrem Team bei der Lösung helfen kann.

OpenRefine ist am nützlichsten, wenn Sie Daten in einem einfachen Tabellenformat wie einer Tabellenkalkulation, einer durch Kommata getrennten Wertedatei (csv) oder einer tabulatorgetrennten Datei (tsv) haben, aber interne Inkonsistenzen entweder in den Datenformaten, oder wo Daten erscheinen, oder in der verwendeten Terminologie. OpenRefine kann verwendet werden, um Daten in Ihrer Datei zu standardisieren und zu bereinigen. Es kann Ihnen helfen:

* einen Überblick über einen Datensatz zu erhalten
* Inkonsistenzen in einem Datensatz aufzulösen, z. B. die Datumsformatierung zu standardisieren
* Aufteilung von Daten in feinere Teile, z. B. Aufteilung von Zellen mit mehreren Autoren in separate Zellen
* Abgleich lokaler Daten mit anderen Datensätzen - z. B. beim Abgleich von Formen von Personennamen mit Namensautoritätsdatensätzen in der Virtual International Authority File (VIAF)
* Anreicherung eines Datensatzes mit Daten aus anderen Quellen

Einige häufige Szenarien könnten sein:

* Wenn Sie wissen möchten, wie oft ein bestimmter Wert (Name, Verlag, Thema) in einer Spalte Ihrer Daten erscheint
* Sie möchten wissen, wie die Werte über Ihren gesamten Datensatz verteilt sind.
* Sie haben eine Liste von Datumsangaben, die auf unterschiedliche Weise formatiert sind, und möchten alle Datumsangaben in der Liste in ein einziges gemeinsames Datumsformat ändern. Zum Beispiel:

| Daten, die Sie haben | Gewünschte Daten |
|-----------------|:-------------|
| 1. Januar 2014 | 2014-01-01 |
| 01/01/2014 | 2014-01-01 |
| 1. Januar 2014 | 2014-01-01 |
| 2014-01-01 | 2014-01-01 |

* Wenn Sie eine Liste von Namen oder Begriffen haben, die sich voneinander unterscheiden, sich aber auf dieselben Personen, Orte oder Konzepte beziehen. Zum Beispiel:

| Daten, die Sie haben | Gewünschte Daten |
|-----------------|:-------------|
| London | London | London
| London]         | London | London | London
| London,] | London |
| london | London | London |

* Wenn Sie mehrere Datenbits in einer einzigen Spalte zusammengefasst haben und diese in einzelne Datenbits aufteilen möchten, wobei für jedes Datenbit eine Spalte vorgesehen ist. Ein Beispiel: Von einem einzigen Adressfeld (in der ersten Spalte) wird jeder Teil der Adresse in ein separates Feld übertragen:

| Adresse in einem einzigen Feld | Institution | Name der Bibliothek | Adresse 1 | Adresse 2 | Ort | Region | Land | Postleitzahl |
|-------------------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|
| University of Wales, Llyfrgell Thomas Parry Library, Llanbadarn Fawr, ABERYSTWYTH, Ceredigion, SY23 3AS, United Kingdom | University of Wales | Llyfrgell Thomas Parry Library | Llanbadarn Fawr | | Aberystwyth | Ceredigion | United Kingdom | SY23 3AS |
| University of Aberdeen, Queen Mother Library, Meston Walk, ABERDEEN, AB24 3UE, Vereinigtes Königreich | University of Abderdeen | Queen Mother Library | Meston Walk | | Aberdeen | | Vereinigtes Königreich | AB24 3UE |
| University of Birmingham, Barnes Library, Medical School, Edgbaston, BIRMINGHAM, West Midlands, B15 2TT, Vereinigtes Königreich | University of Birmingham | Barnes Library | Medical School | Edgbaston | Birmingham | West Midlands | Vereinigtes Königreich | B15 2TT |
| University of Warwick, Library, Gibbett Hill Road, COVENTRY, CV4 7AL, Vereinigtes Königreich | University of Warwick | Library | Gibbett Hill Road | | Coventry | | Vereinigtes Königreich | CV4 7AL |

* Wo Sie Ihre Daten aus einer externen Datenquelle ergänzen möchten:

| Daten, die Sie haben | Geburtsdatum aus VIAF (Virtual International Authority File) | Sterbedatum aus VIAF (Virtual International Authority File) |
|-----------------|:-------------|:-------------|
| Braddon, M. E. (Mary Elizabeth) | 1835 | 1915 |
| Rossetti, William Michael | 1829 | 1919 |
| Prest, Thomas Peckett | 1810 | 1879 |

## Was sollte ich bei der Arbeit mit OpenRefine beachten?
* Es wird keine Internetverbindung benötigt, und keine der Daten oder Befehle, die Sie in OpenRefine eingeben, werden an einen Remote-Server gesendet.
* Sie ändern NICHT die Original-/Rohdaten.
* Die Projekte werden alle fünf Minuten und beim ordnungsgemäßen Beenden von OpenRefine (Strg+C) automatisch gespeichert. Siehe [History im Benutzerhandbuch] (https://docs.openrefine.org/manual/running/#history-undoredo) für Details.
* Dateien werden lokal gespeichert, d.h. wenn Sie auf zwei Computern arbeiten, müssen Sie Dateien/Projekte exportieren/importieren.
