import codecs  # handle utf-8 inputs
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import re


def title_reformat(title_text):
    """Remove "{" and "}" in title
    """
    pat = re.compile('({|})')
    return pat.sub('', title_text)


def file_extract(file_entry):
    """Extract filename
    """
    i = file_entry.find('.pdf')
    if i == -1:
        return ""
    else:
        k = file_entry.rfind('/', 0, i)
        if k == -1:
            return file_entry[:i] + '.pdf'
        else:
            return file_entry[(k+1):i] + '.pdf'


def bibtex_reformat(bibtex_filename):
    """
    """
    with codecs.open(bibtex_filename, encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=True, interpolate_strings=False)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        for i, entry in enumerate(bib_database.entries):
            for key in entry:
                if key.find('title') != -1:
                    bib_database.entries[i][key] = title_reformat(entry[key])
                elif key == 'file':
                    bib_database.entries[i][key] = file_extract(entry[key])
        bib_database.entries.sort(key=lambda entry:
                                  entry['year'], reverse=True)
        writer = BibTexWriter()
        with codecs.open('processed_' + bibtex_filename, mode='w', encoding='utf-8') as processed_bibtex_file:
            for entry in bib_database.entries:
                db = BibDatabase()
                db.entries = [entry]
                processed_bibtex_file.write(writer.write(db))


if __name__ == "__main__":
    bibtex_reformat("jim.bib")
