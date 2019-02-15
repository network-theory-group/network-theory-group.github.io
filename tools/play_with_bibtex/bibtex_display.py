# -*- coding: utf-8 -*-
import codecs  # handle utf-8 inputs
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import re
from jinja2 import Environment as JinjaEnvironment
from jinja2.loaders import FileSystemLoader
import yaml


def bibtex_reader(bibtex_filename):
    """
    """
    with codecs.open(bibtex_filename, encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=True, interpolate_strings=False)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        return bib_database.entries


def display_as_markdown(entries, md_filename):
    jinja_templateEnv = JinjaEnvironment(loader=FileSystemLoader('templates/'))
    TEMPLATE_FILE = 'template_bibtex.md.jinja'
    jinja_template = jinja_templateEnv.get_template(TEMPLATE_FILE)
    with codecs.open(md_filename, mode='w', encoding='utf-8') as md_file:
        md_file.write(
            jinja_template.render(
                {'entries': entries}
            )
        )


def dump_as_yaml(entry):
    return yaml.dump(entry, default_flow_style=False)


if __name__ == "__main__":
    entries = bibtex_reader('../../bibs/paper_pool.bib')
    # display_as_markdown(entries, 'paper_list.md')
    with codecs.open('test.yml', mode='w', encoding='utf-8') as yml_file:
        for entry in entries:
            yml_file.write(dump_as_yaml(entry))
            yml_file.write("\n\n")
