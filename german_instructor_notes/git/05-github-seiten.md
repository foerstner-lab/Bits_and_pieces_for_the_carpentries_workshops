---
Titel: "GitHub Pages"
Unterricht: 15
Übungen: 20
Fragen:
- "Was ist GitHub Pages?"
- "Wie kann ich GitHub Pages benutzen, um zusammenzuarbeiten und meine Arbeit zu teilen?"
Ziele:
- "Erstellen Sie einen GitHub Pages-Zweig und schieben Sie eine Datei dorthin."
- "mit einem Partner, experimentieren Sie mit der Zusammenarbeit auf einer GitHub Pages Website"
- "den Workflow zwischen lokalen und entfernten Repositories anwenden, um auf einer Website zusammenzuarbeiten"
Schlüsselpunkte:
- "GitHub Pages bieten eine automatisierte Möglichkeit, eine Website zu erstellen, die versionskontrolliert und für die Zusammenarbeit zugänglich ist".
- "Die Zusammenarbeit auf einer GitHub Pages Webseite verwendet den gleichen Git/GitHub Workflow, den Sie für die Zusammenarbeit über ein GitHub Repository gelernt haben".
---
~ GitHub Pages ~

GitHub Pages ist ein einfacher Dienst, um eine Webseite direkt auf GitHub aus einem Git-Repository zu veröffentlichen.
Sie fügen einige Dateien und Ordner zu einem Repository hinzu und GitHub Pages verwandelt es in eine Webseite.
Sie können direkt HTML verwenden, wenn Sie möchten, aber sie stellen auch Jekyll zur Verfügung,
die Markdown in HTML rendert und die Einrichtung eines Blogs oder einer Template-basierten Website wirklich einfach macht.

### Warum GitHub Pages fantastisch ist!

GitHub Pages ermöglicht Ihnen die Versionskontrolle Ihrer Website. Dies ist aus vielen verschiedenen Gründen nützlich. Es erlaubt Ihnen 
dokumentieren Sie, welche Änderungen Sie vorgenommen haben. Es ermöglicht es Menschen, Ihre Website zu einem bestimmten Zeitpunkt zu referenzieren. 
und (wenn Sie Ihren Quellcode offenlegen), um zu sehen, wie es zu diesem bestimmten Zeitpunkt war. Dies ist sehr nützlich für 
akademische Zitate. Die meisten Menschen haben die Erfahrung gemacht, einem Verweis auf eine Website nachzugehen und entweder eine 
404 Fehler oder etwas völlig anderes zu sehen. Obwohl die Verwendung von Versionen auf Ihrer Website nicht garantiert, dass dies nicht 
passieren, macht es die Verwaltung alter Versionen Ihrer Website einfacher.

GitHub Pages bedeutet auch, dass Sie mit vielen Leuten an einer Website zusammenarbeiten können, ohne dass jeder 
endlos hin und her kommunizieren, welche Änderungen vorgenommen werden müssen oder bereits vorgenommen wurden. Sie können 
Probleme' (Dinge, die diskutiert oder behoben werden müssen), listen Sie Dinge auf, die in Zukunft zu tun sind, und erlauben Sie anderen Personen, Ihre 
Website, um schnell Änderungen vorzuschlagen und durch Pull-Requests zu implementieren.

### Einrichten einer Website

Jetzt sind wir alle davon überzeugt, wie fantastisch GitHub Pages ist (oder Sie haben einige fatale Fehler in meiner Argumentation identifiziert), es 
wäre es sinnvoll, mit einigen Dingen zu spielen, die wir damit machen können. Das wird uns helfen, das zu zementieren, was wir 
haben in der vorhergehenden Stunde gelernt und können helfen, eine Diskussion für den letzten Abschnitt dieser Sitzung anzuregen.

Es gibt verschiedene Optionen für die Einrichtung einer GitHub Pages Seite. Lassen Sie uns jetzt ein paar davon durchgehen.

### Der gh-pages Zweig

GitHub Pages verwendet einen speziellen Zweig in Ihrem GitHub-Repository, um nach Website-Inhalten zu suchen,
und standardmäßig ist dies der Zweig mit dem Namen 'gh-pages'.
Sie können dies unter den Repository-Einstellungen tatsächlich ändern, um z.B. den Hauptzweig zu verwenden,
aber bleiben wir erst mal bei der Vorgabe.

Es ist möglich, einen neuen Zweig direkt auf GitHub zu erstellen, aber wir werden jetzt die Kommandozeile benutzen.
Also gehen wir zurück zur Kommandozeile und tippen

~~~
$ git Kasse -b gh-Seiten
$ Git Push
~~~
{: .bash)
~~~
fatal: Der aktuelle Zweig gh-pages hat keinen Upstream-Zweig.
Um den aktuellen Zweig zu pushen und die Fernbedienung als Upstream zu setzen, verwenden Sie

    git push --set-upstream Ursprung gh-Seiten
~~~
{: .output}

Autsch, das lief nicht so, wie wir wollten, wir haben einen fatalen Fehler!
Mal sehen, was Git uns sagt.
Es sagt, dass es nicht weiß, wo es die Änderungen vornehmen soll.
Aber es ist auch freundlich genug, uns zu sagen, was wir am ehesten tun wollen,
die auf den `gh-Seiten`-Zweig bei "Ursprung" zu schieben ist.
(denken Sie daran, dass "Ursprung" in unserem Fall nur ein Spitzname für unser GitHub-Repository ist).

Also lass uns das machen:

~~~
$ git push --set-upstream Herkunft gh-pages
~~~
{: .bash)
~~~
Gesamt 0 (Delta 0), wiederverwendet 0 (Delta 0)
Auf https://github.com/danmichaelo/hello-world.git
 * gh-Seiten -> gh-Seiten
Verzweigungs-GH-Seiten, die so eingerichtet sind, dass sie die GH-Seiten der entfernten Verzweigungen vom Ursprung aus verfolgen.
~~~
{: .output}

Du erinnerst dich vielleicht noch von früher, dass wir `git push -u origin master` gemacht haben, um
den Hauptzweig einzurichten. Das `-u` ist die Abkürzung für `--set-upstream`, also
oben hätten Sie auch `git push -u origin gh-pages` eingeben können.

Und denken Sie daran, dass wir dies nur tun müssen, wenn wir das erste Mal auf einen neuen Zweig drücken.
Das nächste Mal können wir einfach "Git-Push" machen.

### Betrachten Sie Ihre Seite

Wenn wir jetzt `https://some-librarian.github.io/hello-world/` besuchen,
sollten wir den Inhalt der Datei index.md sehen, die zuvor erstellt wurde.
Normalerweise ist sie sofort verfügbar, aber es kann ein paar Sekunden und im schlimmsten Fall ein paar Minuten dauern, wenn GitHub sehr beschäftigt ist.

> ## Herausforderung: Zu einer Seite beitragen, die jemand anderem gehört (etwas einfacherer Weg)
>
> Um den Umgang mit Git, GitHub-Seiten und Markdown zu üben, können wir zu einer GitHub-Seiten-Seite beitragen.
> Bilden Sie Zweiergruppen (oder mehr, falls nötig) und machen Sie die untenstehenden Übungen gemeinsam.
> 
> 1. Gehen Sie auf https://github.com/some-librarian/hello-world, wobei "some-librarian" der Benutzername Ihres Übungspartners ist.

> 2. Klicken Sie auf "Fork" im oberen rechten Teil des Bildschirms, um eine Kopie des Projektarchivs auf Ihrem Account zu erstellen. Sobald Sie einen Fork > des Repositorys Ihres Partners haben, können Sie die Dateien in Ihrem eigenen Fork direkt bearbeiten.
> 3. klicken Sie auf die Datei "index.md" und dann auf das Symbol "Stift bearbeiten":
> 
> ![GitHub-Bleistift bearbeiten](../fig/github-edit-pencil.png)
> 
> 4. Jetzt ist eine gute Gelegenheit, die Markdown-Syntax auszuprobieren.
> Probieren Sie einige Beispiele unter [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).
> Sie können sich eine Vorschau ansehen, wie es aussehen wird, bevor Sie Änderungen übertragen.
> 5. Wenn Sie bereit sind, die Änderungen zu übertragen, geben Sie eine kurze Nachricht ein,
> wählen Sie "Einen neuen Zweig für diesen Commit erstellen und eine Pull-Anfrage starten".
> und drücken Sie "Dateiänderung vorschlagen".
> 
> ![Commit und Pull-Request erstellen](../fig/github-commit-pr.png)
> 
> 8. Sie erhalten nun die Möglichkeit, die Änderungen zu überprüfen und eine zusätzliche
> Erklärung vor dem Absenden der Pull-Anfrage (dies ist besonders
> wenn Sie eine einzelne Pull-Anfrage für mehrere Commits stellen).
> 9. Ihr Partner sollte nun eine Pull-Anfrage unter dem "Pull-Anfragen"-Reiter sehen
> und kann dort die Änderungen übernehmen ("Merge pull request"). Versuchen Sie dies.
> 
> Dieser ganze Prozess der Erstellung einer Gabelung und einer Pull-Anforderung mag etwas umständlich erscheinen.
> Versuchen Sie zu überlegen, warum es nötig war? Und wieso es "Abrufanfrage" genannt wird?
>
> > ## Lösung
> > Wir haben eine Gabelung und einen Pull-Antrag gestellt, weil wir keine Erlaubnis hatten, die
> > (oder Commit) das Repository direkt. Ein Fork ist eine Kopie des Projektarchivs, die
> > wir *können* sie bearbeiten. Bei einer Pull-Anfrage fragen wir den Eigentümer des Repositoriums, ob
> > sie möchten die Änderungen von unserer Abspaltung (unserer Kopie) akzeptieren (einziehen) in
> > ihre Version. Der Eigentümer kann dann die Änderungen überprüfen und sich entscheiden, ob er sie akzeptiert oder
> > sie abzuweisen.
> >
> > Sie können Pull-Requests auf jedem Repository öffnen, das Sie auf GitHub finden. Wenn Sie ein
> > Gruppe von Menschen, die eine enge Zusammenarbeit planen, auf der anderen Seite,
> > es ist praktischer, stattdessen jedem den direkten Zugriff auf Commits zu gewähren.
> >
> {: .solution}
{: .challenge}

> ## Optionale Herausforderung: Zu einer Seite beitragen, die jemand anderem gehört (etwas kompliziertere Art)
>
> Anstatt Änderungen auf der GitHub Webseite vorzunehmen, können Sie den Fork auf Ihren lokalen Rechner 'klonen'.
> und dort zu arbeiten.
>
> Versuchen Sie, den Rest der Schritte unter "Zeit für die Einreichung Ihres ersten PR" zu befolgen.
> in diesem Leitfaden: <https://www.thinkful.com/learn/github-pull-request-tutorial/Writing-a-Good-Commit-Message#Time-to-Submit-Your-First-PR>
>
> (Wenn Sie Schritt 1 und 2 in der vorherigen Herausforderung befolgt haben, haben Sie bereits eine Gabelung und können
> Überspringen Sie die Erstellung einer neuen Gabel, wenn Sie möchten. Sie können mehrere Pull-Anforderungen mit demselben Fork einreichen).
>
{: .challenge}


> ## Optionale Herausforderung: Hinzufügen einer HTML-Seite
>
> GitHub Pages ist nicht auf Markdown beschränkt. Wenn Sie sich mit HTML auskennen, versuchen Sie, eine HTML-Seite hinzuzufügen.
> zu Ihrem Repository. Du könntest dies auf der Kommandozeile oder direkt auf GitHub tun. Die
> Die folgenden Schritte sind für die Arbeit direkt auf GitHub:
>
> 1. Vergewissern Sie sich, dass Sie auf dem Zweig "gh-pages" arbeiten. Wenn nicht, wählen Sie ihn aus dem Menü aus:
>
> ![Verzweigungswähler auf GitHub](../fig/github-gh-pages.png)
>
> 2. Um eine neue Datei direkt auf GitHub hinzuzufügen, drücken Sie den "Create new file" Knopf. 
>
> ![Neue Datei auf GitHub erstellen](../fig/github-create-new-file.png)
>
> 3. nennen Sie es 'test.html', fügen Sie etwas HTML hinzu und klicken Sie auf "Neue Datei übertragen".
> 4. Versuchen Sie, `https://some-librarian.github.io/hello-world/test` zu öffnen.
> (ersetzen Sie "some-librarian" mit Ihrem Benutzernamen).
> Beachten Sie, dass die HTML-Erweiterung nicht enthalten ist.
>
{: .challenge}
