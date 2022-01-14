import numpy as np

from pylatex import Document, Section, Subsection, Table, Math, TikZ, Axis, \
    Plot, Figure, Package
from pylatex.utils import italic, escape_latex


doc = Document()
doc.packages.append(Package('geometry', options=['tmargin=1cm',
                                                 'lmargin=10cm']))

with doc.create(Section("Test Section")):
    with doc.create(Subsection("test subsectoin")):
        doc.append("HALLO")


doc.generate_pdf()
