---
Titel: "Daten nachschlagen"
Unterricht: 20
Übungen: 10
Fragen:
- "Wie hole ich Daten von einer Anwendungsprogrammierschnittstelle (API), um sie in OpenRefine zu verwenden?"
- "Wie gleiche ich meine Daten mit maßgeblichen Datensätzen ab?
- "Wie installiere ich Erweiterungen für OpenRefine?
Ziele:
- "URLs verwenden, um Daten aus dem Web zu holen, die auf Spalten in einem OpenRefine-Projekt basieren"
- "Spalten hinzufügen, um JSON-Daten zu parsen, die von Webdiensten zurückgegeben werden"
- Verstehen, wie Reconciliation Services zur Validierung von Daten verwendet werden.
- Funktionalitäten mit OpenRefine-Erweiterungen hinzufügen".
Keypoints:
- "OpenRefine kann benutzerdefinierte URLs nachschlagen, um Daten basierend auf dem Inhalt eines OpenRefine-Projekts abzurufen"
- "Solche API-Aufrufe können individuell erstellt werden, oder man kann bestehende Reconciliation Services nutzen, um Daten anzureichern.
- OpenRefine kann durch die Installation von Erweiterungen weiter verbessert werden.
---

## Abrufen von Daten aus einer URL

OpenRefine kann Daten von URLs abrufen. Dies kann auf verschiedene Weise genutzt werden, z. B. um zusätzliche Informationen von einem entfernten 
Dienst abzurufen, die auf den Informationen in deinen OpenRefine-Daten basieren.

So kannst du zum Beispiel Namen mit der Virtual International Authority File (VIAF) abgleichen und zusätzliche Informationen wie Geburts- 
und Sterbedaten und Identifikatoren abrufen.

In der Regel ist dies ein zweistufiger Prozess, bei dem du erstens Daten von einem externen Dienst abrufst und zweitens die relevanten 
Informationen aus den abgerufenen Daten extrahierst.

Um Daten aus einer externen Quelle abzurufen, wählst du im Dropdown-Menü einer beliebigen Spaltenüberschrift die Option 
‘Edit column->Add column by fetching URLs’.

Daraufhin wirst du aufgefordert, einen GREL-Ausdruck einzugeben, um eine URL zu erstellen. Normalerweise ist dies eine URL, 
die bestehende Werte in deinen Daten verwendet, um eine Abfrage zu erstellen. Wenn die Abfrage ausgeführt wird, fragt OpenRefine 
jede URL (für jede Zeile) ab und ruft die Daten ab, die zurückgegeben werden (oft sind es strukturierte Daten, aber es kann auch HTML sein).

Die abgerufenen Daten werden in einer Zelle in der neuen Spalte gespeichert, die dem Projekt hinzugefügt wurde. Du kannst dann 
OpenRefine-Transformationen verwenden, um relevante Informationen aus den abgerufenen Daten zu extrahieren. Zwei spezielle OpenRefine-Funktionen, 
die dafür verwendet werden, sind:

* parseHtml()
* parseJson()

Die Funktion 'parseHtml()' kann auch verwendet werden, um Daten aus XML zu extrahieren.

Die nächste Übung demonstriert diesen zweistufigen Prozess in vollem Umfang.

>## Abrufen von Zeitschriftendetails aus CrossRef über ISSN
>Weil das Abrufen von Daten aus externen URLs Zeit braucht, zielt diese Übung auf eine einzelne Zeile in den Daten ab. In Wirklichkeit würdest du viele Zeilen abfragen wollen (und wahrscheinlich etwas anderes tun, während die Übung läuft).
>
>* Wähle eine einzelne Zeile aus dem Datensatz aus, die eine ISSN enthält, indem du:
> * Klick auf das Sternsymbol der entsprechenden Zeile in der ersten Spalte
> * Facette nach Stern
> * Wähle die einzelne Zeile aus
>* Wähle in der ISSN-Spalte im Dropdown-Menü die Option "Edit column->Add column by fetching URLs".
>* Gib der Spalte einen Namen, z. B. "Journal-Details".
>* In das Feld "expression " musst du eine GREL eingeben, deren Ausgabe eine URL ist, die zum Abrufen von Daten verwendet werden kann (das Format der Daten kann HTML, XML, JSON oder ein anderes Textformat sein)
>
>In diesem Fall verwenden wir die CrossRef API: [https://api.crossref.org/](https://api.crossref.org/). Lies mehr über den CrossRef-Dienst: [https://crossref.org](https://crossref.org). 
>Beachte, dass API-Anbieter möglicherweise Ratenbeschränkungen auferlegen oder andere Anforderungen für die Nutzung ihrer Daten stellen, 
>daher ist es wichtig, dass du die Dokumentation der Website liest. Um die API-Ratenbeschränkungen einzuhalten, kannst du mit der Einstellung 
>Drosselverzögerung die Anzahl der Millisekunden zwischen den URL-Anfragen festlegen. 
>CrossRef [bittet Benutzer](https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/#pick-the-right-service-level) zum Beispiel darum, 
>"einen User-Agent-Header anzugeben, der dein Skript oder Tool richtig identifiziert und die Möglichkeit bietet, dich per E-Mail 
>über 'mailto:' zu kontaktieren." User-Agent-Header versorgen Administratoren mit Benutzerinformationen, die eine bessere Verwaltung und 
>Moderation der API ermöglichen, und es gehört generell zum guten Ton, bei jeder API-Anfrage einen Header anzugeben.
>
>Um deinen User-Agent-Header zu bearbeiten:
>* Klicke auf "Show" (neben "HTTP-Header, die beim Abrufen von URLs verwendet werden"). Beachte, dass OpenRefine das Feld 'User-Agent' bereits mit Informationen über die von dir verwendete Version von OpenRefine ausgefüllt hat; es sollte ungefähr so aussehen: ``` OpenRefine 3... [...]`` (die Informationen, die auf ``OpenRefine``` folgen, hängen von der Version von OpenRefine ab, die du verwendest).
>* Füge am Ende des bestehenden Textes ```; mailto:address@library.edu``` ein und verwende deine eigene E-Mail-Adresse. Das vollständige User-Agent-Feld sollte nun so aussehen wie ``` OpenRefine 3... [...]; mailto:address@library.edu```, aber mit deinen Versionsinformationen und deiner E-Mail-Adresse.
>
>Die Syntax für die Anforderung von Zeitschrifteninformationen bei CrossRef lautet ```https://api.crossref.org/journals/{ISSN}```, wobei {ISSN} durch die ISSN der Zeitschrift ersetzt wird
>
>* In das Expression gibst du den GREL ```""https://api.crossref.org/journals/"+value``` ein
>
>
>* Klicke auf "OK".
>
>
>Oben auf dem OpenRefine-Bildschirm solltest du eine Meldung sehen, die anzeigt, dass es Daten abruft und der Fortschritt den prozentualen Anteil der erfolgreich abgerufenen Datenzeilen anzeigt. Warte, bis der Vorgang abgeschlossen ist. Das Abrufen von Daten für eine einzelne Zeile sollte nur etwa zehn Sekunden dauern, aber das Abrufen von Daten für alle Zeilen wird länger dauern. Du kannst dies beschleunigen, indem du die Einstellung "Drosselverzögerung" im Dialogfeld "Spalte durch Abrufen von URLs hinzufügen" änderst, die die Verzögerung zwischen den einzelnen URL-Anfragen von OpenRefine steuert. Die Standardeinstellung ist mit 5000 Millisekunden (5 Sekunden) recht hoch.
>
>Jetzt solltest du eine neue Zelle haben, die eine lange Textzeichenkette im Format "JSON" enthält (das steht für JavaScript Object Notation, wird aber nur selten vollständig buchstabiert).
>
>OpenRefine verfügt über eine Funktion, mit der du Daten aus JSON extrahieren kannst (manchmal auch als "Parsen" von JSON bezeichnet). Die Funktion "parseJson" wird unter [https://docs.openrefine.org/manual/grelfunctions/#format-based-functions-json-html-xml](https://docs.openrefine.org/manual/grelfunctions/#format-based-functions-json-html-xml) genauer erklärt.
>
>* Verwende in der neuen Spalte, die du gerade hinzugefügt hast, das Dropdown-Menü, um auf "Edit column->Add column based on this column" zuzugreifen.
>* Gib einen Namen für die neue Spalte ein, z.B. "Journal-Title".
>* Gib in das Feld "Ausdruck" den GREL-Wert ````value.parseJson().message.title``` ein
>* In der Vorschau solltest du sehen, dass der Journal-Titel angezeigt wird
>
>Der Grund für die Verwendung von "Spalte basierend auf dieser Spalte hinzufügen" ist, dass du so das vollständige JSON behalten und bei Bedarf weitere Daten daraus extrahieren kannst.
> Wenn du nur den Titel und keine weiteren Informationen aus dem JSON benötigst, kannst du "Zellen bearbeiten->Transformieren..." mit demselben GREL-Ausdruck verwenden.
{: .challenge}

## Abgleichsdienste
Mit den Abgleichsdiensten kannst du Begriffe aus deinen Daten in OpenRefine mit externen Diensten abgleichen und Werte aus den externen 
Diensten in deinen Daten verwenden. Das offizielle Benutzerhandbuch enthält 
[detaillierte Informationen über die Abgleichsfunktion] (https://docs.openrefine.org/manual/reconciling).

Abgleichsdienste können ausgefeilter und oft schneller sein als die oben beschriebene Methode zum Abrufen von Daten aus einer URL. 
Um die "Reconciliation"-Funktion in OpenRefine nutzen zu können, muss die externe Ressource jedoch den notwendigen Dienst unterstützen, 
damit OpenRefine damit arbeiten kann. Das bedeutet, dass du den "Reconciliation"-Ansatz nur nutzen kannst, wenn der Dienst, den du nutzen möchtest, 
einen solchen Dienst unterstützt.

Es gibt einige wenige Dienste, bei denen du eine OpenRefine Reconciliation-Option finden kannst. Wikidata hat zum Beispiel einen Reconciliation-Dienst
unter [https://wikidata.reconci.link/](https://wikidata.reconci.link/).

In anderen Fällen haben Leute für einen bestimmten Dienst Abgleichsanwendungen entwickelt, die du selbst herunterladen und ausführen kannst. 
Diese unterscheiden sich darin, wie sie funktionieren und was man braucht, um sie lokal auszuführen. Zum Beispiel gibt es mehrere 
Abstimmungsanwendungen für VIAF. Selbst für ein und denselben Dienst (z. B. VIAF) können verschiedene Abstimmungsanwendungen 
(die von verschiedenen Personen geschrieben wurden) auf unterschiedliche Weise funktionieren und möglicherweise unterschiedliche Ergebnisse liefern 
- also Vorsicht!

Eine der gebräuchlichsten Möglichkeiten, die Abgleichsoption in OpenRefine zu nutzen, ist eine Erweiterung 
(siehe unten für weitere Informationen zu Erweiterungen von OpenRefine), die verknüpfte Datenquellen für den Abgleich nutzen kann. 
Die RDF-Erweiterung von Stuart Kenny kann unter 
[https://github.com/stkenny/grefine-rdf-extension/releases](https://github.com/stkenny/grefine-rdf-extension/releases) heruntergeladen werden.

Es gibt noch weitere Erweiterungen, die den Abgleich mit lokalen Daten wie csv-Dateien 
(siehe [http://okfnlabs.org/reconcile-csv/](http://okfnlabs.org/reconcile-csv/)) und gepflegten Wertelisten 
(siehe [http://okfnlabs.org/projects/nomenklatura/index.html](http://okfnlabs.org/projects/nomenklatura/index.html)) ermöglichen.

Weitere Informationen zur Verwendung von Reconciliation Services findest du unter 
[https://docs.openrefine.org/manual/reconciling](https://docs.openrefine.org/manual/reconciling).

>## Reconciliate Publisher-Namen mit VIAF-IDs
>In dieser Übung wirst du den VIAF Reconciliation Service von [Jeff Chiu](https://twitter.com/absolutelyjeff) verwenden. 
>Jeff bietet zwei Möglichkeiten, den Reconciliation Service zu nutzen - entweder über einen öffentlichen Dienst, den er 
>unter [http://refine.codefork.com/](http://refine.codefork.com/) betreibt, oder indem du den Dienst lokal installierst 
>und mit Hilfe der Anweisungen unter [https://github.com/codeforkjeff/conciliator](https://github.com/codeforkjeff/conciliator) ausführst.
>
>Wenn du viel abgleichen willst, installiere bitte deinen eigenen lokalen Abgleichdienst und führe ihn gemäß den
> Anweisungen unter [https://github.com/codeforkjeff/conciliator](https://github.com/codeforkjeff/conciliator#running-conciliator-on-your-own-computer) aus.
>
>Wenn du dich für einen Dienst entschieden hast, solltest du ihn nutzen:
>
>* Wähle in der Spalte "Publisher" im Dropdown-Menü "Reconcile->Start Reconciling".
>* Wenn du diesen Service zum ersten Mal verwendest, musst du jetzt die Details des Services hinzufügen
> * Klicke auf "Standarddienst hinzufügen..." und gib in dem erscheinenden Dialogfeld
> * "https://refine.codefork.com/reconcile/viaf" für Jeffs öffentlichen Dienst
> * "http://localhost:8080/reconcile/viaf", wenn du den Dienst lokal ausführst
>* In der Liste auf der linken Seite des Abstimmungsdialogs sollte nun eine Überschrift mit dem Namen "VIAF" erscheinen.
>* Klicke darauf, um diesen Abstimmungsdienst zu verwenden
>* Im mittleren Feld des Abstimmungsdialogs wirst du möglicherweise gefragt, welche Art von "Entität" du abstimmen möchtest - das heißt, nach welcher Art von Sache du suchst. Die Liste variiert je nachdem, welchen Abstimmungsdienst du verwendest.
> In diesem Fall wählst du "Corporate Name" (der VIAF Reconciliation Service scheint hier etwas intelligent zu sein und bietet nur Optionen an, die relevant sind).
>* Im Feld auf der rechten Seite des Abstimmungsdialogs kannst du auswählen, ob andere Spalten verwendet werden sollen, damit der Abstimmungsdienst einen Abgleich vornehmen kann - allerdings ist es manchmal schwer zu sagen, ob und wie der Abstimmungsdienst diese zusätzlichen Spalten verwendet
>* Unten im Abgleichsdialog gibt es die Option "Kandidaten mit hohem Vertrauen automatisch abgleichen". Das kann eine Zeitersparnis sein, aber in diesem Fall deaktivierst du sie, damit du die Ergebnisse sehen kannst, bevor ein Abgleich vorgenommen wird
>* Klicke jetzt auf "Abgleich starten".
>
>Der Abgleich ist ein Vorgang, der ein wenig Zeit in Anspruch nehmen kann, wenn du viele Werte nachschlagen musst. In diesem Fall sind jedoch nur 6 Verlage zu prüfen, so dass es recht schnell gehen sollte.
>
>Nach Abschluss des Abgleichs sollten automatisch zwei Facetten erstellt werden:
>* Verlag: Urteilsvermögen
>* Verleger: Bewertung des besten Kandidaten
>
>Dies sind zwei von mehreren spezifischen Abstimmungsfacetten und -aktionen, die du über das Menü "Abstimmen" (aus dem Dropdown-Menü der Spalte) aufrufen kannst.
>
>* Schließe die Facette 'Herausgeber: Bestes Ergebnis des Kandidaten', aber lass die Facette 'Herausgeber: Beurteilung' offen
>
>Wenn du dir die Spalte "Verleger" ansiehst, solltest du sehen, dass einige Zellen eine oder mehrere Übereinstimmungen gefunden haben - die potenziellen Übereinstimmungen werden in jeder Zelle in einer Liste angezeigt. Neben jeder potenziellen Übereinstimmung gibt es ein "Häkchen" und ein "Doppelhäkchen". Um einen Abgleich zu akzeptieren, kannst du die "Häkchen"-Optionen in den Zellen verwenden. Das "Häkchen" akzeptiert die Übereinstimmung für die einzelne Zelle, das "Doppelhäkchen" akzeptiert die Übereinstimmung für alle identischen Zellen.
>
>* Erstelle eine Textfacette in der Spalte "Herausgeber".
>* Wähle 'International Union of Crystallography'.
>
>In der Spalte "Herausgeber" solltest du die verschiedenen möglichen Übereinstimmungen sehen können. Wenn du auf eine Übereinstimmung klickst, gelangst du auf die VIAF-Seite für diese Entität.
>
>* Klicke auf ein "Doppelhäkchen" in einer der Zellen der Spalte Herausgeber für die Option "International Union of Crystallography".
>* Dadurch wird dies als Übereinstimmung für alle Zellen akzeptiert - die anderen Optionen sollten verschwinden
>* Überprüfe die Facette "Herausgeber: Urteil". Sie sollte nun anzeigen, dass 858 Einträge "übereinstimmen" (wenn sich diese Anzeige nicht aktualisiert, versuche, die Facetten zu aktualisieren)
>
> Wir könnten sie einzeln durchgehen, aber wenn wir mit den Übereinstimmungen zufrieden sind, gibt es die Option, alle zu akzeptieren:
>
>* Entferne alle Filter/Facetten aus dem Projekt, damit alle Zeilen angezeigt werden.
>* Wähle in der Spalte "Herausgeber" aus dem Dropdown-Menü "Abgleichen->Aktionen->Jede Zelle mit dem besten Kandidaten abgleichen".
>
>Der Abgleich kann zwei Dinge für dich tun. Erstens erhält er eine Standardform des Namens oder der Bezeichnung für die Entität. Zweitens erhält er eine ID für die Entität - in diesem Fall eine VIAF-ID. Diese ist in der Standardansicht verborgen, kann aber extrahiert werden:
>
>* Wähle in der Spalte "Herausgeber" im Dropdown-Menü die Option "Spalte bearbeiten->Spalte basierend auf dieser Spalte hinzufügen...".
>* Gib der Spalte den Namen "VIAF-ID".
>* Gib in das Feld GREL-Ausdruck ```Zelle.recon.match.id``` ein
>* Dadurch wird eine neue Spalte erstellt, die die VIAF-ID für die übereinstimmende Entität enthält
{: .challenge}

## Verwendung der 'cross'-Funktion zum Nachschlagen von Daten in anderen OpenRefine-Projekten
Mit den oben beschriebenen Methoden kannst du nicht nur Daten in externen Systemen abfragen, 
sondern auch in anderen OpenRefine-Projekten auf demselben Computer. Dies geschieht mit der Funktion "cross".

Die 'cross'-Funktion nimmt einen Wert aus dem OpenRefine-Projekt, an dem du gerade arbeitest, und sucht diesen Wert 
in einer Spalte in einem anderen OpenRefine-Projekt. Wenn sie eine oder mehrere übereinstimmende Zeilen im zweiten OpenRefine-Projekt findet, 
gibt sie ein Array mit den übereinstimmenden Zeilen zurück.

Da sie für jede Übereinstimmung die gesamte Zeile zurückgibt, kannst du eine Transformation verwenden, 
um die Werte aus einer beliebigen Spalte des zweiten Projekts zu extrahieren.

Du kannst diese Funktion nutzen, um die Inhalte zweier OpenRefine-Projekte zu vergleichen oder um Daten zwischen den beiden Projekten zu verwenden.

Die VIB-Bits-Erweiterung fügt OpenRefine eine Reihe von sehr nützlichen Funktionen hinzu. 
Eine davon ist "Spalte(n) aus anderen Projekten hinzufügen...", die ein Dialogfenster bereitstellt, das dir hilft, mit der Funktion `cross` mit weniger Tipparbeit zu arbeiten.

>## Erweiterungen
>Die Funktionalität von OpenRefine kann durch "Erweiterungen" erweitert werden, die heruntergeladen und installiert werden können, 
>um deine OpenRefine-Installation um zusätzliche Funktionen zu ergänzen.
>
>Eine (nicht notwendigerweise vollständige) Liste der Erweiterungen findest du auf der OpenRefine-Downloadseite 
>unter [http://openrefine.org/download.html](http://openrefine.org/download.html).
{: .callout}
