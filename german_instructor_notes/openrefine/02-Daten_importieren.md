---
Titel: "Daten in OpenRefine importieren"
Unterricht: 10
Übungen: 5
Fragen:
- "Wie bekomme ich Daten in OpenRefine?"
Ziele:
- "Erfolgreicher Import von Daten in OpenRefine"
Stichpunkte:
- "Verwenden Sie die Option "Projekt erstellen", um Daten zu importieren".
- Sie können die Art und Weise des Datenimports mit Hilfe von Optionen auf dem Importbildschirm steuern.
- "Verschiedene Dateitypen können in OpenRefine importiert werden."
---

## Importieren von Daten

>## Welche Arten von Datendateien kann ich importieren?
>Es gibt mehrere Möglichkeiten, Ihren Datensatz in OpenRefine zu importieren. Sie können Dateien in einer Vielzahl von Formaten hochladen oder importieren:
>
>* TSV (Tabulator-getrennte Werte)
>* CSV (Komma-getrennte Werte)
>* TXT
>* Excel
>* JSON (javascript object notation)
>* XML (erweiterbare Auszeichnungssprache)
>* Google Tabellenkalkulation
{: .callout}

>## Erstellen Sie Ihr erstes OpenRefine-Projekt (mit den bereitgestellten Daten)
>
> Um die Daten für die folgende Übung zu importieren, folgen Sie den Anweisungen unter [Setup] (https://librarycarpentry.github.io/lc-open-refine/setup.html), um die Daten herunterzuladen und OpenRefine zu starten. *HINWEIS: Wenn OpenRefine nicht in einem Browserfenster geöffnet wird, öffnen Sie Ihren Browser und geben Sie die Adresse <http://127.0.0.1:3333/> ein, um zur OpenRefine-Schnittstelle zu gelangen.
>
>1. Sobald OpenRefine in Ihrem Browser gestartet ist, klicken Sie im linken Menü auf "Projekt erstellen" und wählen "Daten von diesem Computer abrufen".
>2. klicken Sie auf "Dateien auswählen" (oder "Durchsuchen", je nach Einrichtung) und suchen Sie die Datei "doaj-article-sample.csv", die Sie heruntergeladen haben
>3. klicken Sie auf "Weiter", wo Ihnen der nächste Bildschirm (siehe unten) Optionen bietet, um sicherzustellen, dass die Daten korrekt in OpenRefine importiert werden. Die Optionen hängen von der Art der Daten ab, die Sie importieren.
>4. klicken Sie in das Feld "Zeichenkodierung" und setzen Sie es auf "UTF-8". Dadurch wird sichergestellt, dass OpenRefine die importierten Daten korrekt als UTF-8 kodiert interpretiert. Wenn Sie dies nicht auswählen, kann es sein, dass einige Sonderzeichen (z. B. intelligente Anführungszeichen) nicht korrekt angezeigt werden.
>5. Stellen Sie sicher, dass die erste Zeile zur Erstellung der Spaltenüberschriften verwendet wird, indem Sie das Kontrollkästchen "Nächste 1 Zeile(n) als Spaltenüberschriften vorlesen" aktivieren.
>6) OpenRefine wählt automatisch die Option "Zeichen verwenden", um Zellen, die Spaltentrennzeichen (z. B. ein Komma) enthalten, als Teil der Daten einzuschließen. Dadurch wird sichergestellt, dass OpenRefine keine Kommas (oder andere Zeichen) innerhalb der Spaltendaten als Trennzeichen missversteht. Lassen Sie diese Option aktiviert.
>Ab OpenRefine 3.4 gibt es die Option, beim Import von trennzeichenbasierten Dateien führende und nachfolgende Leerzeichen aus Strings zu entfernen. Wenn Sie diese Option aktiviert lassen, wird sichergestellt, dass Werte wie `English` und `English`, die sich durch ein einzelnes Leerzeichen am Ende unterscheiden, nach dem Import nicht als unterschiedliche Werte behandelt werden.
>8. stellen Sie sicher, dass das Kontrollkästchen "Versuchen, Zellentext in Zahlen zu analysieren" nicht aktiviert ist, damit OpenRefine nicht versucht, automatisch Zahlen zu erkennen, da dies zu Fehlern wie der Verwechslung von Datumsformaten führen kann (z. B. DD/MM/YYYYY vs. MM/DD/YYYYY)
>9. Das Feld "Projektname" in der oberen rechten Ecke ist standardmäßig mit dem Titel Ihrer importierten Datei vorbelegt. Klicken Sie in das Feld "Projektname", um Ihrem Projekt einen anderen Namen zu geben, falls gewünscht.
>10. Wenn Sie die entsprechenden Optionen für Ihr Projekt ausgewählt haben, klicken Sie auf die Schaltfläche "Projekt erstellen" oben rechts auf dem Bildschirm. Dadurch wird das Projekt erstellt und für Sie geöffnet. Die Projekte werden während der Bearbeitung gespeichert, Sie brauchen also keine Kopien zu speichern.
>   
> ![Screenshot des Bildschirms Open Refine Projekt erstellen](../assets/img/openrefine_ui.png)
{: .checklist}

Um ein bestehendes Projekt in OpenRefine zu öffnen, klicken Sie im Hauptfenster von OpenRefine (im linken Menü) auf "Projekt öffnen". Wenn Sie darauf klicken, sehen Sie eine Liste der vorhandenen Projekte und können auf den Namen eines Projekts klicken, um es zu öffnen.

### Weiter gehend
* Versuchen Sie, einige dieser Optionen zu ändern, um zu sehen, wie sich die Vorschau ändert und wie die Daten nach dem Import erscheinen.
* Haben Sie Zugriff auf JSON- oder XML-Daten? Wenn ja, werden Sie in der ersten Phase des Importvorgangs aufgefordert, einen "Datensatzpfad" auszuwählen - das sind die Teile der Datei, die die Datenzeilen im OpenRefine-Projekt bilden werden.
