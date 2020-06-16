pdf:
	xelatex Git_intro.tex

pdf_follow_changes:
	latexmk -xelatex -pvc Git_intro.tex

clean:
	rm -f *aux *log *nav *snm *out *toc *pdf *.fdb_latexmk *.fls *~

get_images:
	wget -c -O images/laptop.svg "https://publicdomainvectors.org/download.php?file=ericlemerdy_laptop_1.svg"
	convert images/laptop.svg images/laptop.pdf

	wget -c -O images/cloud.svg "https://publicdomainvectors.org/download.php?file=1400625045.svg"	
	convert images/cloud.svg images/cloud.pdf

	wget -c -O images/arrow.svg "https://publicdomainvectors.org/download.php?file=arrow-down.svg"
	convert images/arrow.svg images/arrow.pdf
