# MySQL Workbench Python script
# Script to Generate a Firebird Script from a MySql Workbench Model
# Author: Tito Sanchez (tmsanchez@gmail.com)
# Written in MySQL Workbench 6.3.6

from wb import *
import grt
from mforms import Utilities, FileChooser
import mforms


ModuleInfo = DefineModule(name="GenerateFirebirdScript", author="Tito Sanchez", version="1.0", description="Database schemas to Firebird Script")

@ModuleInfo.plugin("tmsanchez.firebird", caption="Database schema to Firebird Script", description="Generate Firebird script from MySQL Workbench Model", input=[wbinputs.currentCatalog()], pluginMenu="Catalog")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)

def mysqltoirebird(currentcatalog):
    firebirdScript = ""
    filechooser = FileChooser(mforms.SaveFile)
    filechooser.set_extensions("SQL File (*.sql)|*.sql", "sql");
    if filechooser.run_modal():
        firebirdScript = filechooser.get_path()
    print "HTML File: %s" % (firebirdScript)
    if len(firebirdScript) <= 1:
        return 1
    # iterate through columns from schema
    thegenerators = ""
    theforeignkey = ""
    theprimaarykey = ""
    firebirdScript = open(firebirdScript, "w")
    print >> firebirdScript, "/* Firebird Script from Mysql Model */"
    print >> firebirdScript, "\n"
    for schema in grt.root.wb.doc.physicalModels[0].catalog.schemata:
        print >> firebirdScript, "CREATE DATABASE  '%s.fdb' page_size 8192; " % (schema.name)
        print >> firebirdScript, "\n"
        print >> firebirdScript, "\n"
        for table in schema.tables:
            print >> firebirdScript, "CREATE TABLE %s (" % (table.name)
            numberofcolumns = len(table.columns)
            columncounter = 0
            for column in table.columns:
                notnull = ('', 'NOT NULL')[bool(column.isNotNull)]
                mysqlType = column.formattedType
                firebirdType = column.formattedType
                if mysqlType == "INT(11)":
                   firebirdType = "INTEGER"
                elif mysqlType == "TINYINT":
                   firebirdType = "SMALLINT"
                print >> firebirdScript, " %s  %s   %s," % (column.name, firebirdType, notnull)
                # if column is defined as AUTO_INCREMENT in mysql then add it to generators
                if column.autoIncrement == 1:
                   thegenerators = thegenerators + "CREATE GENERTATOR GEN_" + table.name + ";" + "\r\n"
            # define primary key constraint
            theprimarykey = ""
            numberofcolumnsinpk = len(table.primaryKey.columns) - 1
            primarykeycounter = 0
            for primarykeycolumn in table.primaryKey.columns:
                theprimarykey = theprimarykey + primarykeycolumn.referencedColumn.name
                if primarykeycounter < numberofcolumnsinpk:
                    theprimarykey = theprimarykey + ","
                primarykeycounter = primarykeycounter + 1
            if len(table.primaryKey.columns) > 0:
                theprimarykey = "CONSTRAINT %s_PK PRIMARY KEY (%s) " % (table.name, theprimarykey)
                if len(table.foreignKeys) > 0:
                    theprimarykey = theprimarykey + ", "
                print >> firebirdScript, theprimarykey
            # define foreign key constraints
            theforeignkey = ""
            numberofforeignkeys = len(table.foreignKeys) - 1
            foreignkeycounter = 0
            for foreignkey in table.foreignKeys:
                theforeignkey = theforeignkey + " CONSTRAINT %s_%s_FK FOREIGN KEY (" % (
                table.name, foreignkey.referencedTable.name)
                for colTable in foreignkey.columns:
                    theforeignkey = theforeignkey + colTable.name
                theforeignkey = theforeignkey + ") REFERENCES " + foreignkey.referencedTable.name + " ( "
                for referencedColumn in foreignkey.referencedColumns:
                    theforeignkey = theforeignkey + referencedColumn.name
                theforeignkey = theforeignkey + ")"
                if (foreignkeycounter < numberofforeignkeys):
                    theforeignkey = theforeignkey + ", "
                theforeignkey = theforeignkey + "\r\n"
                foreignkeycounter = foreignkeycounter + 1
            print >> firebirdScript, theforeignkey
            print >> firebirdScript, ");"
        print >> firebirdScript, "\n"
        print >> firebirdScript, "\n"
        print >> firebirdScript, "--- GENERATORS"
        print >> firebirdScript, thegenerators
        print >> firebirdScript, ""
    Utilities.show_message("Script Migrated", "Migration from Mysql to Firebird Finished", "OK", "", "")
    return 0
