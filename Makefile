get_example_files:
	mkdir -p plain_text_file_examples

	wget -c -O plain_text_file_examples/PubMed.xml \
          "https://www.ncbi.nlm.nih.gov/pubmed/23203889?report=xml&format=text"

	wget -c -O plain_text_file_examples/CrossRef.json \
	  "https://api.crossref.org/works/10.1371/journal.pcbi.1005412"

        # https://commons.wikimedia.org/wiki/File:Community.svg
	wget -c -P plain_text_file_examples/ \
	  "https://upload.wikimedia.org/wikipedia/commons/d/db/Community.svg"

	# https://www.ncbi.nlm.nih.gov/nuccore/KM366535
	wget -c -O plain_text_file_examples/Influenza_A_virus_HA_gene_sequence.fa \
	  "https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gene_fasta&id=686467572"

	wget -c -P plain_text_file_examples/ \
	  https://raw.githubusercontent.com/openbsd/src/master/bin/ls/ls.c
