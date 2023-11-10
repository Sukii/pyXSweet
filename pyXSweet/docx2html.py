
# Python script for running sequence of XSLTs on DocX to produce HTML
import sys
from pyxsl import pydocx
from zipfile import ZipFile

xsls = ["docx-extract/docx-html-extract.xsl", "docx-extract/handle-notes.xsl", "docx-extract/scrub.xsl","docx-extract/join-elements.xsl","docx-extract/collapse-paragraphs.xsl","htmlevator/hyperlink-inferencer.xsl","htmlevator/PROMOTE-lists.xsl","htmlevator/DETECT-ITEMIZE-LISTS.xsl","htmlevator/header-promotion-CHOOSE.xsl","math/xsweet_tei_omml2mml.xsl"]

# getting docx input file
docx_file = sys.argv[1]
docx = ZipFile(docx_file, "r")


xml_paths = ["word/document.xml"]
# apply sequence of xsl on docx to extract xml
xml_output = pydocx.xslDocx(docx,xml_paths[0],xsls)
