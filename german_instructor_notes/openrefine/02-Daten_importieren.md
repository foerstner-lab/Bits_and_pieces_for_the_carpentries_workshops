Zum Inhalt springen
Suchen oder springen zu...
Pull-Anfragen
Themen
Codespaces
Marktplatz
Erforsche
 
@RabeaMue 
BibliothekZimmermannsarbeit
/
lc-open-refine
Öffentlich
Forke deine eigene Kopie von LibraryCarpentry/lc-open-refine
Code
Ausgaben
10
Pull-Anfragen
2
Aktionen
Projekte
Sicherheit
Einblicke
Du nimmst Änderungen an einem Projekt vor, auf das du keinen Schreibzugriff hast. Wenn du eine Änderung einreichst, wird sie in einen neuen Zweig in deinem Fork RabeaMue/lc-open-refine geschrieben, sodass du einen Pull-Request senden kannst.
lc-open-refine
/
_episodes
/
02-importieren-daten.md
in
LibraryCarpentry:gh-pages
 

Leerzeichen

2

Weicher Umbruch
1
---
2
Titel: "Daten in OpenRefine importieren"
3
Lehre: 10
4
Übungen: 5
5
Fragen:
6
- "Wie bekomme ich Daten in OpenRefine?"
7
Ziele:
8
- "Erfolgreich Daten in OpenRefine importieren"
9
Kernpunkte:
10
- "Verwende die Option `Projekt erstellen`, um Daten zu importieren"
11
- Du kannst den Datenimport mit den Optionen auf dem Importbildschirm steuern.
12
- Verschiedene Dateitypen können in OpenRefine importiert werden.
13
---
14

15
## Daten importieren
16

17
>## Welche Arten von Datendateien kann ich importieren?
18
>Es gibt verschiedene Möglichkeiten, deinen Datensatz in OpenRefine zu importieren. Du kannst Dateien in einer Vielzahl von Formaten hochladen oder importieren:
19
>
20
>* TSV (Tab-getrennte Werte)
21
>* CSV (Komma-getrennte Werte)
22
>* TXT
23
>* Excel
24
>* JSON (javascript object notation)
25
>* XML (erweiterbare Auszeichnungssprache)
26
>* Google Spreadsheet
27
{: .callout}
28

29
>## Erstelle dein erstes OpenRefine-Projekt (mit den bereitgestellten Daten)
30
>
31
> Um die Daten für die folgende Übung zu importieren, befolge die Anweisungen unter [Setup] (https://librarycarpentry.github.io/lc-open-refine/setup.html), um die Daten herunterzuladen und OpenRefine zu starten. *HINWEIS: Wenn OpenRefine nicht in einem Browserfenster geöffnet wird, öffne deinen Browser und gib die Adresse <http://127.0.0.1:3333/> ein, um die OpenRefine-Oberfläche aufzurufen.
32
>
33
>1. Sobald OpenRefine in deinem Browser gestartet ist, klicke im linken Menü auf "Projekt erstellen" und wähle "Daten von diesem Computer abrufen".
34
>2. klicke auf "Dateien auswählen" (oder "Durchsuchen", je nachdem, wie du es eingerichtet hast) und suche die Datei "doaj-article-sample.csv", die du heruntergeladen hast.
35
>3. klicke auf "Weiter". Auf dem nächsten Bildschirm (siehe unten) findest du Optionen, mit denen du sicherstellen kannst, dass die Daten korrekt in OpenRefine importiert werden. Die Optionen hängen von der Art der Daten ab, die du importierst.
36
>4. klicke in das Feld "Zeichenkodierung" und setze es auf "UTF-8". Dadurch wird sichergestellt, dass OpenRefine die importierten Daten korrekt als UTF-8 kodiert interpretiert. Wenn du dies nicht auswählst, kann es sein, dass einige Sonderzeichen (z. B. intelligente Anführungszeichen) nicht richtig angezeigt werden.
37
>5. Stelle sicher, dass die erste Zeile zur Erstellung der Spaltenüberschriften verwendet wird, indem du das Kontrollkästchen "Nächste 1 Zeile(n) als Spaltenüberschriften vorlesen" aktivierst.
38
>6 OpenRefine wählt automatisch "Zeichen verwenden", um Zellen, die Spaltentrennzeichen (z. B. ein Komma) enthalten, als Teil der Daten einzuschließen. So wird sichergestellt, dass OpenRefine Kommas (oder andere Zeichen) in den Spaltendaten nicht fälschlicherweise als Begrenzungszeichen interpretiert. Lass diese Option aktiviert.
39
>Ab OpenRefine 3.4 gibt es die Option, führende und nachgestellte Leerzeichen aus Strings zu entfernen, wenn trennzeichenbasierte Dateien importiert werden. Wenn du diese Option aktiviert lässt, wird sichergestellt, dass Werte wie "Englisch" und "Englisch", die sich durch ein einzelnes Leerzeichen am Ende unterscheiden, nach dem Import nicht als unterschiedliche Werte behandelt werden.
40
>8. stelle sicher, dass das Kontrollkästchen "Versuchen, Zelltext in Zahlen zu zerlegen" nicht aktiviert ist, damit OpenRefine nicht versucht, automatisch Zahlen zu erkennen, da dies zu Fehlern wie der Verwechslung von Datumsformaten führen kann (z. B. DD/MM/YYYYY vs. MM/DD/YYYYY)
41
>9. Das Feld "Projektname" in der oberen rechten Ecke enthält standardmäßig den Titel deiner importierten Datei. Klicke in das Feld "Projektname", um deinem Projekt einen anderen Namen zu geben, falls gewünscht.
42
>10. Wenn du die passenden Optionen für dein Projekt ausgewählt hast, klicke auf die Schaltfläche "Projekt erstellen" oben rechts auf dem Bildschirm. Damit wird das Projekt erstellt und für dich geöffnet. Projekte werden gespeichert, während du sie bearbeitest, du brauchst also keine Kopien zu speichern.
43
>   
Nicht ausgewählt
Füge Dateien durch Ziehen & Ablegen, Auswählen oder Einfügen hinzu.
Styling mit Markdown wird unterstützt
@RabeaMue
Änderungen vorschlagen
Commit-Zusammenfassung
02-importing-data.md erstellen
Optionale erweiterte Beschreibung
Füge eine optionale erweiterte Beschreibung hinzu...
 
Fußzeile
© 2023 GitHub, Inc.
Navigation in der Fußzeile
Bedingungen
Datenschutz
Sicherheit
Status
Docs
Kontakt zu GitHub
Preisgestaltung
API
Ausbildung
Blog
Über
