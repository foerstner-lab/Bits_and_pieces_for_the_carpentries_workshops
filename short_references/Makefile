pdf:
	pandoc \
          --pdf-engine xelatex \
	  --variable mainfont="DejaVu Sans" \
	  --variable sansfont="DejaVu Sans" \
          -V geometry:"top=3cm, bottom=3cm, left=3.2cm, right=3.2cm" \
	  -V fontsize=11pt \
          -V papersize:a4 \
	  -o python_de.pdf \
	  python_de.md

	pandoc \
          --pdf-engine xelatex \
	  --variable mainfont="DejaVu Sans" \
	  --variable sansfont="DejaVu Sans" \
          -V geometry:"top=3cm, bottom=3cm, left=3.2cm, right=3.2cm" \
	  -V fontsize=11pt \
          -V papersize:a4 \
	  -o python_en.pdf \
	  python_en.md

	pandoc \
          --pdf-engine xelatex \
	  --variable mainfont="DejaVu Sans" \
	  --variable sansfont="DejaVu Sans" \
          -V geometry:"top=3cm, bottom=3cm, left=3.2cm, right=3.2cm" \
	  -V fontsize=11pt \
          -V papersize:a4 \
	  -o git_de.pdf \
	  git_de.md

	pandoc \
          --pdf-engine xelatex \
	  --variable mainfont="DejaVu Sans" \
	  --variable sansfont="DejaVu Sans" \
          -V geometry:"top=3cm, bottom=3cm, left=3.2cm, right=3.2cm" \
	  -V fontsize=11pt \
          -V papersize:a4 \
	  -o shell_de.pdf \
	  shell_de.md

	pandoc \
          --pdf-engine xelatex \
	  --variable mainfont="DejaVu Sans" \
	  --variable sansfont="DejaVu Sans" \
          -V geometry:"top=3cm, bottom=3cm, left=3.2cm, right=3.2cm" \
	  -V fontsize=11pt \
          -V papersize:a4 \
	  -o markdown_de.pdf \
	  markdown_de.md

clean:
	rm -f *pdf *~
