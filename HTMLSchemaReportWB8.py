# MySQL Workbench Python script
# Script to Generate an HTML Schema Report from Mysql MOdel
# Author: Tito Sanchez 
# Written in MySQL Workbench 8.0.25

from wb import *
import grt
from mforms import Utilities, FileChooser
import mforms

ModuleInfo = DefineModule(name="DBReport", author="Tito Sanchez", version="1.0", description="Database schema in HTML report format")

@ModuleInfo.plugin("tmsanchezplugin.htmlReportSchema", caption="HTML Format database schema report", description="Database schema report in HTML format", input=[wbinputs.currentCatalog()], pluginMenu="Catalog")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)

def htmlDataDictionary(catalog):
    # Put plugin contents here
    htmlOut = ""
    filechooser = FileChooser(mforms.SaveFile)
    filechooser.set_extensions("HTML File (*.html)|*.html","html");
    if filechooser.run_modal():
       htmlOut = filechooser.get_path()
    print("HTML File: %s" % (htmlOut))
    if len(htmlOut) <= 1:
       return 1
    # iterate through columns from schema
    schema = catalog.schemata[0]
    htmlFile = open(htmlOut, "w")
    htmlFile.write( "<html><head> \m")
    htmlFile.write( "<title>Schema Report for database: %s</title> \n" % (schema.name))
    htmlFile.write( """<style>
        td,th {
        text-align:left;
        vertical-align:middle;
        }
        table {
        border-collapse: collapse;
        border: 1px solid;
        }
        caption, th, td {
        padding: .2em .8em;
        border: 1px solid #000000;
        }
        caption {
        background: #D3D3D3;
        font-weight: bold;
        font-size: 1.1em;
        }
        th {
        font-weight: bold;
        background: #000000;
        color: white;
        }
        td {
        background: #FFFFFF;
        }
        </style>
      </head>
     <body>""")
    htmlFile.write("\n"  )
    htmlFile.write( "<h1>Schema Report for database: %s</h1> \n" % (schema.name) )
    htmlFile.write( "<a id=\"home\">Table List </a><br /><ul> \n " )
    for table in schema.tables:
       htmlFile.write( "<li><a href=\"#%s\">%s </a></li> \n" % (table.name,table.name) )
    htmlFile.write( "</ul> \n" )
    for table in schema.tables:
      htmlFile.write( "<a id=\"%s\"></a><table style=\"width:100%%\"><caption>Table: %s </caption> \n" % (table.name,table.name) )
      htmlFile.write( "<tr><td>Table Comments</td><td colspan=\"6\">%s</td></tr> \n" % (table.comment) )
      htmlFile.write( """<tr><td colspan=\"7\">Columns</td></tr>
        <tr>
        <th>Name</th>
        <th>Data Type</th>
        <th>Not Null</th>
        <th>PK</th>
        <th>FK</th>
        <th>Default</th>
        <th>Comment</th>
        </tr>""")
      htmlFile.write("\n ")
      for column in table.columns:
        pk = ('No', 'Yes')[bool(table.isPrimaryKeyColumn(column))]
        fk = ('No', 'Yes')[bool(table.isForeignKeyColumn(column))]
        nn = ('No', 'Yes')[bool(column.isNotNull)]
        htmlFile.write( "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr> \n" % (column.name,column.formattedType,nn,pk,fk,column.defaultValue,column.comment) )
      htmlFile.write("</table><a href=\"#home\">Table List </a></br> \n" )
    htmlFile.write("</body></html> \n")
    htmlFile.close()
    Utilities.show_message("Report generated", "HTML Report format from current model generated in %s" % htmlOut, "OK","","")
    return 0
