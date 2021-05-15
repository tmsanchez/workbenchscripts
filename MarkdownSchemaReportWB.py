# MySQL Workbench Python script
# Script to Generate an Markdown format Schema Report from Mysql MOdel
# Author: Tito Sanchez 
# Written in MySQL Workbench 8.0.25

from wb import *
import grt
from mforms import Utilities, FileChooser
import mforms

ModuleInfo = DefineModule(name="DBMarkdownReport", author="Tito Sanchez", version="1.0", description="Database schema in Markdown  format")

@ModuleInfo.plugin("tmsanchezplugin.markdownReportSchema", caption="Markdown format database schema report", description="Database schema report in Markdown format", input=[wbinputs.currentCatalog()], pluginMenu="Catalog")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)

def mardownDataDictionary(catalog):
    # Put plugin contents here
    markdownOut = ""
    filechooser = FileChooser(mforms.SaveFile)
    filechooser.set_extensions("Markdown File (*.md)|*.md","md");
    if filechooser.run_modal():
       markdownOut = filechooser.get_path()
    #print("HTML File: %s" % (markdownOut))
    if len(markdownOut) <= 1:
       return 1
    # iterate through columns from schema
    schema = catalog.schemata[0]
    markdownFile = open(markdownOut, "w")
    markdownFile.write(" \n")
    markdownFile.write("# Schema Report for database: %s \n" % (schema.name))
    print ( "## Table List \n", markdownFile)
    for table in schema.tables:
       markdownFile.write ( "- %s \n" % (table.name))
    markdownFile.write ( " \n")
    for table in schema.tables:
      markdownFile.write ( " \n")
      markdownFile.write ( "### Table: %s \n" % (table.name))
      markdownFile.write ( " Table Comments: %s \n" % (table.comment))
      markdownFile.write ( "|Name |Data Type |Nullable |PK |FK |Default |Comment |\n")
      markdownFile.write ( "--- | ---| --- | --- | --- | --- | ---\n")

      for column in table.columns:
        pk = ('No', 'Yes')[bool(table.isPrimaryKeyColumn(column))]
        fk = ('No', 'Yes')[bool(table.isForeignKeyColumn(column))]
        nn = ('No', 'Yes')[bool(column.isNotNull)]
        markdownFile.write ( "|%s|%s|%s|%s|%s|%s|%s|\n" % (column.name,column.formattedType,nn,pk,fk,column.defaultValue,column.comment))
      markdownFile.write (" \n")
    markdownFile.write (" \n")
    markdownFile.write (" \n")
    markdownFile.close()
    Utilities.show_message("Report generated", "Markdown Report format from current model generated in %s " % markdownOut, "OK","","")
    return 0