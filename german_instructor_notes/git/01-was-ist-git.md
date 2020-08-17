---
Titel: "Was ist Git/GitHub?"
Lehre: 10
Übungen: 0
Fragen:
- "Was ist Git?"
- "Was ist GitHub?"
Ziele:
- "Erkennen, warum Versionskontrolle nützlich ist"
- "Unterscheidung zwischen Git und GitHub"
Schlüsselpunkte:
- "Versionskontrolle hilft Änderungen an Dateien und Projekten zu verfolgen"
- "Git und GitHub sind nicht dasselbe."
---

### Was ist Versionskontrolle

Versionskontrolle ist ein Name, der für Software verwendet wird, die Ihnen helfen kann, Änderungen an den Dateien in einem Verzeichnis auf Ihrem Computer aufzuzeichnen. Software und Werkzeuge zur Versionskontrolle (wie z.B. Git und Subversion/SVN) werden oft mit der Softwareentwicklung in Verbindung gebracht und werden zunehmend für die Zusammenarbeit in der Forschung und im akademischen Umfeld eingesetzt. Versionskontrollsysteme arbeiten am besten mit reinen Textdateien wie Dokumenten oder Computercode, aber moderne Versionskontrollsysteme können zur Verfolgung von Änderungen in jeder Art von Datei verwendet werden.

Auf der einfachsten Ebene hilft uns die Versionskontrollsoftware dabei, Sätze von Änderungen an Dateien auf unserem Computer zu registrieren und zu verfolgen. Wir können dann über diese Änderungen nachdenken und sie mit anderen teilen. Wenn wir im Laufe der Zeit Änderungssätze aufbauen, beginnen wir einige Vorteile zu sehen.

##### Vorteile der Verwendung von Versionskontrolle?

**Zusammenarbeit** - Versionskontrolle erlaubt es uns, formalisierte Wege zu definieren, wie wir zusammenarbeiten und das Schreiben und den Code gemeinsam nutzen können. Zum Beispiel ermöglicht das Zusammenführen von Änderungssätzen verschiedener Parteien die gemeinsame Erstellung von Dokumenten und Software in verteilten Teams.
**Versionierung** - Ein robustes und strenges Protokoll der Änderungen an einer Datei, ohne Umbenennung von Dateien (v1, v2, _final_copy_)
**Rolling Back** - Die Versionskontrolle erlaubt es uns, eine Reihe von Änderungen schnell rückgängig zu machen. Dies kann nützlich sein, wenn beim Schreiben von neuen Texten oder neuen Ergänzungen zum Code Probleme auftreten.
**Verstehen** - Die Versionskontrolle kann Ihnen helfen zu verstehen, wie der Code oder das Schreiben entstanden ist, wer bestimmte Teile geschrieben oder beigetragen hat und wen Sie bitten könnten, Ihnen zu helfen, den Code besser zu verstehen.
**Backup** - Auch wenn es nicht als Backup-Lösung gedacht ist, bedeutet die Verwendung von Versionskontrollsystemen, dass Ihr Code und Ihre Texte auf mehreren anderen Computern gespeichert werden können.

Es gibt noch viele weitere Gründe, Versionskontrolle zu verwenden, und wir werden einige davon im Bibliothekskontext untersuchen, aber lass uns zuerst ein wenig über ein beliebtes Versionskontrollwerkzeug namens Git lernen.

### Was sind Git und GitHub?

Wir hören oft die Begriffe **_Git_** und **_GitHub_**, die austauschbar verwendet werden, aber sie sind leicht verschiedene Dinge.

**_Git_** ist eines der am weitesten verbreiteten Versionskontrollsysteme der Welt. Es ist ein freies, quelloffenes Werkzeug, das auf Ihren lokalen Rechner heruntergeladen werden kann und dazu dient, alle Änderungen, die an einer Gruppe von bestimmten Computerdateien (kurz "git repository" oder "repo" genannt) über einen längeren Zeitraum hinweg vorgenommen wurden, zu protokollieren. Es kann verwendet werden, um Dateiversionen lokal von Ihnen allein auf Ihrem Computer zu kontrollieren, ist aber vielleicht am mächtigsten, wenn es zur Koordination der gleichzeitigen Arbeit an einer Gruppe von Dateien verwendet wird, die von verteilten Personengruppen gemeinsam genutzt werden. 

Anstatt Dokumente mit verfolgten Änderungen und einigen Kommentaren per E-Mail zu versenden und verschiedene Versionen von Dateien umzubenennen (example.txt, exampleV2.txt, exampleV3.text), um sie zu unterscheiden, können wir Git verwenden, um all diese Informationen mit dem Dokument selbst zu speichern (oder in der Git-Sprache "commit"). Dies macht es einfach, einen Überblick über alle Änderungen, die im Laufe der Zeit an einer Datei gemacht wurden, zu bekommen, indem man sich ein Protokoll aller Änderungen anschaut. Und alle früheren Versionen jeder Datei bleiben immer noch in ihrer ursprünglichen Form: sie werden nicht überschrieben, sollten wir jemals auf sie "zurückrollen" wollen. 

Git wurde ursprünglich entwickelt, um Softwareentwicklern bei der gemeinsamen Arbeit an Softwareprojekten zu helfen, aber es kann und wird für die Verwaltung von Revisionen an jedem Dateityp auf einem Computersystem verwendet, einschließlich Textdokumenten. Einmal installiert, erfolgt die Interaktion mit Git über die Eingabeaufforderung in Windows oder das Terminal auf Mac/Linux. Da Word-Dokumente spezielle Formatierungen enthalten, kann Git diese leider nicht versionskontrollieren, noch kann es PDFs versionskontrollieren, obwohl beide Dateitypen in Git-Repositories gespeichert werden können.   

*Wie kann das Verständnis von Git bei der Arbeit in Bibliotheken helfen?*
* Ermöglicht es Ihnen, zu digitalen Forschungsprojekten beizutragen, an ihnen zusammenzuarbeiten und sie zu unterstützen 
* Ermöglicht es Ihnen, Änderungen an Ihren Dateien im Laufe der Zeit zu kontrollieren, ohne mehrere Kopien dieser Dateien zu behalten

**_GitHub_** auf der anderen Seite ist eine beliebte Website für das Hosting und die gemeinsame Nutzung von Git-Repositories per Fernzugriff. Sie bietet ein Webinterface und bietet Funktionalität und eine Mischung aus kostenlosen und kostenpflichtigen Diensten für die Arbeit mit solchen Repositories. Der Großteil der Inhalte, die GitHub hostet, ist Open-Source-Software, obwohl sie zunehmend auch für andere Projekte wie Open-Access-Zeitschriften (z.B. [Journal of Open Source Software] (https://joss.theoj.org/)), Blogs und ständig aktualisierte Lehrbücher verwendet wird. 

*Wie kann GitHub bei der Arbeit in Bibliotheken helfen?* 
*Ein Ort, an dem eine große Menge an offen lizenzierten digitalen Projekten und Open-Source-Software entdeckt und wiederverwendet werden kann ("fork")
* Ein neues und alternatives Mittel zur Veröffentlichung von Inhalten im Internet. Jedes GitHub-Repository kann seine eigene Projekt-Website, seinen Blog und sein Wiki mit GitHub Pages haben.  


### Verwendungen in einem Bibliothekskontext

Betrachten Sie diese gängigen Szenarien der Bibliothekswelt: 

#### Szenario 1: Lokale Bibliothek will ein Crowdsourcing-Projekt starten.

Ein örtlicher Bibliothekar möchte Tausende von historischen Fotos der Gegend online stellen, damit die Gemeinde bei der Identifizierung der abgebildeten Personen und Orte helfen kann. Sie durchkämmt das Web nach Beispielen bestehender Crowdsourcing-Projekte, und obwohl sie alle für jede Einrichtung einzigartig erscheinen, stellt sie fest, dass einige davon fast genau die gleiche Funktionalität und Struktur zu haben scheinen. Anstatt selbst eine ganz neue Version von Grund auf zu erstellen, wünscht sie sich, es gäbe einen Weg, einfach den Code einer bestehenden Version zu kopieren und ihn so zu modifizieren, dass er ihr Projekt widerspiegelt. Sie bemerkt das [GitHub-Icon](https://github.com/logos) am unteren Rand eines der Projekte, das ihr gefällt, aber ein Klick auf den Link bringt sie nur zu einem verwirrenden Verzeichnis von Dateien und seltsam beschrifteten Knöpfen wie "Fork".  

GitHub beherbergt viele offen-lizenzierte Projekte und erlaubt jedem Benutzer, jedes öffentliche Projekt zu forken. Durch das Klicken auf den "fork"-Button kann jeder GitHub-Benutzer fast sofort seine eigene Version eines existierenden Projekts erstellen. Dieses "abgezweigte" Projekt kann als Basis für ein neues Projekt verwendet werden, oder es kann dazu verwendet werden, neue Features zu erarbeiten, die wieder in das Original eingebunden werden können. (Von: [GitHub für Akademiker](https://hybridpedagogy.org/push-pull-fork-github-for-academics/) )

#### Szenario 2: Mehrere Personen bearbeiten Metadaten für eine Sammlung

Ein Metadaten-Spezialist hat ein Arbeitsblatt aus einem Repository zur Bereinigung und Bearbeitung exportiert. Sie arbeitet mit einer Gruppe von Bibliotheksmitarbeitern und Studenten zusammen, die sicherstellen müssen, dass die Bearbeitungen nicht in Konflikt stehen. Außerdem müssen sie in der Lage sein, alle Bearbeitungen rückgängig zu machen und die ursprünglichen Metadaten zu erhalten. Nach Abschluss der Bearbeitungen möchte die gesamte Gruppe die Änderungen überprüfen, bevor die Metadaten-Tabelle erneut in das Repository eingefügt wird.

Das Team kann wählen, Git selbst zu verwenden, um Änderungen zu verfolgen und Konflikte zu lösen, oder sie können GitHub als Host für das Projekt verwenden, damit die Benutzer im Web zusammenarbeiten und Änderungen überprüfen können. Git bewahrt sowohl die ursprünglichen Metadaten als auch alle Bearbeitungen. GitHub wird die Diskussion darüber erleichtern, welche Änderungen vorgenommen werden sollten, wer sie machen sollte und warum.
