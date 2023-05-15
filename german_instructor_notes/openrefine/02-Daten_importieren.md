---
Titel: "Daten in OpenRefine importieren"
Unterricht: 10
Übungen: 5
Fragen:
- "Wie bekomme ich Daten in OpenRefine?"
Ziele:
- "Erfolgreich Daten in OpenRefine importieren"
Stichpunkte:
- "Verwende die Option "Projekt erstellen", um Daten zu importieren".
- Du kannst den Datenimport mit Hilfe der Optionen auf dem Importbildschirm steuern.
- "Es können verschiedene Dateitypen in OpenRefine importiert werden."
---

## Daten importieren

>## Welche Arten von Datendateien kann ich importieren?
>Es gibt mehrere Möglichkeiten, deinen Datensatz in OpenRefine zu importieren. Du kannst Dateien in einer Vielzahl von Formaten hochladen oder importieren:
>
>* TSV (Tab-getrennte Werte)
>* CSV (Komma-getrennte Werte)
>* TXT
>* Excel
>* JSON (javascript object notation)
>* XML (Extensible Markup Language)
>* Google Spreadsheet
{: .callout}

>## Erstelle dein erstes OpenRefine-Projekt (mit den bereitgestellten Daten)
>
> Um die Daten für die folgende Übung zu importieren, befolge die Anweisungen unter [Setup] (https://librarycarpentry.github.io/lc-open-refine/setup.html), um die Daten herunterzuladen und OpenRefine zu starten. *HINWEIS: Wenn OpenRefine nicht in einem Browserfenster geöffnet wird, öffne deinen Browser und gib die Adresse <http://127.0.0.1:3333/> ein, um die OpenRefine-Oberfläche aufzurufen.
>
>1. Sobald OpenRefine in deinem Browser gestartet ist, klicke im linken Menü auf "Projekt erstellen" und wähle "Daten von diesem Computer abrufen".
>2. klicke auf "Dateien auswählen" (oder "Durchsuchen", je nachdem, wie du es eingerichtet hast) und suche die Datei "doaj-article-sample.csv", die du heruntergeladen hast.
>3. klicke auf "Weiter". Auf dem nächsten Bildschirm (siehe unten) erhältst du Optionen, um sicherzustellen, dass die Daten korrekt in OpenRefine importiert werden. Die Optionen hängen von der Art der Daten ab, die du importierst.
>4. klicke in das Feld "Zeichenkodierung" und setze es auf "UTF-8". Dadurch wird sichergestellt, dass OpenRefine die importierten Daten korrekt als UTF-8 kodiert interpretiert. Wenn du dies nicht auswählst, kann es sein, dass einige Sonderzeichen (z.B. intelligente Anführungszeichen) nicht richtig angezeigt werden.
>5. Stelle sicher, dass die erste Zeile zur Erstellung der Spaltenüberschriften verwendet wird, indem du das Kästchen "Nächste 1 Zeile(n) als Spaltenüberschriften vorlesen" aktivierst.
>6. OpenRefine wählt automatisch die Option “Use character”, um Zellen, die Spaltentrennzeichen (z. B. ein Komma) enthalten, als Teil der Daten einzuschließen. So wird sichergestellt, dass OpenRefine Kommas (oder andere Zeichen) in den Spaltendaten nicht fälschlicherweise als Trennzeichen interpretiert. Lass diese Option aktiviert.
>Ab OpenRefine 3.4 gibt es die Option, führende und nachgestellte Leerzeichen aus Strings zu entfernen, wenn du trennzeichenbasierte Dateien importierst. Wenn du diese Option aktivierst, wird sichergestellt, dass Werte wie `English` und `English`, die sich durch ein einzelnes Leerzeichen am Ende unterscheiden, nach dem Import nicht als unterschiedliche Werte behandelt werden.
>Vergewissere dich, dass das Kontrollkästchen "Attempt to parse cell text into numbers" nicht aktiviert ist, damit OpenRefine nicht versucht, automatisch Zahlen zu erkennen, da dies zu Fehlern wie der Verwechslung von Datumsformaten führen kann (z. B. DD/MM/YYYYY vs. MM/DD/YYYYY)
>9. Das Feld "Projektname" in der oberen rechten Ecke ist standardmäßig mit dem Titel deiner importierten Datei vorbelegt. Klicke in das Feld "Projektname", um deinem Projekt einen anderen Namen zu geben, falls gewünscht.
>10. Wenn du die passenden Optionen für dein Projekt ausgewählt hast, klicke auf die Schaltfläche "Projekt erstellen" oben rechts auf dem Bildschirm. Damit wird das Projekt erstellt und für dich geöffnet. Projekte werden gespeichert, während du sie bearbeitest, du brauchst also keine Kopien zu speichern.
>   
> ![Screenshot des Bildschirms Open Refine Projekt erstellen](../assets/img/openrefine_ui.png)
{: .checklist}

Um ein bestehendes Projekt in OpenRefine zu öffnen, klickst du im Hauptfenster von OpenRefine (im linken Menü) auf "Projekt öffnen". Wenn du darauf klickst, siehst du eine Liste der bestehenden Projekte und kannst auf den Namen eines Projekts klicken, um es zu öffnen.

### Weiter geht's
* Schau dir die anderen Optionen auf dem Importbildschirm an - ändere einige dieser Optionen und sieh nach, wie sich die Vorschau verändert und wie die Daten nach dem Import erscheinen.
* Hast du Zugriff auf JSON- oder XML-Daten? Wenn ja, wirst du in der ersten Phase des Importvorgangs aufgefordert, einen "Datensatzpfad" auszuwählen - das sind die Teile der Datei, die die Datenzeilen im OpenRefine-Projekt bilden werden.
