get_example_files:
	mkdir -p plain_text_file_examples

	wget -O plain_text_file_examples/PubMed.xml \
          "https://www.ncbi.nlm.nih.gov/pubmed/23203889?report=xml&format=text"

	wget -O plain_text_file_examples/CrossRef.json \
	  "https://api.crossref.org/works/10.1371/journal.pcbi.1005412"

        # https://commons.wikimedia.org/wiki/File:Community.svg
	wget -P plain_text_file_examples/ \
	  "https://upload.wikimedia.org/wikipedia/commons/d/db/Community.svg"
