# Download example file
wget https://upload.wikimedia.org/wikipedia/commons/b/b7/ASUCLA_SOU_October_1974.pdf

# Extract first page
qpdf --empty --pages ASUCLA_SOU_October_1974.pdf 1  -- first_page.pdf 

# OCR
ocrmypdf -l eng first_page.pdf first_page_OCR.pdf
