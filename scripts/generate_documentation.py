import numpy as np
import os

from pylatex import Document, Section, Subsection, Table, Math, TikZ, Axis, \
    Plot, Figure, Package
from pylatex.utils import italic, escape_latex


image_file = os.path.join(os.path.dirname('../dat/images/'), 'husky.jpg')
print(image_file)

doc = Document()
#doc.packages.append(Package('geometry', options=['tmargin=1cm',
 #                                                'lmargin=10cm']))

with doc.create(Section("Test Section")):
    with doc.create(Subsection("test subsectoin")):
        doc.append(italic('Insert project details here'))


with doc.create(Subsection('Example image')):
    with doc.create(Figure(position='h')) as image:
        image.add_image('../data/images/husky.jpg', width='200px')
        image.add_caption('This is a husky')


doc.generate_pdf('../data/documentation/duckies_and_fishies', clean_tex=False)
