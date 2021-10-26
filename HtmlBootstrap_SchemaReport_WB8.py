# MySQL Workbench Python script (Plugin/Module)
# Script to Generate an HTML Schema Report from Mysql Model
# Author: Tito Sanchez
# Update by: Fernando Gil
# Written in MySQL Workbench 8.0.25

# To install this Plugin on MySQL Workbench version 8.0:
# 1. Download this file wuth a Python extension (.py)
# 2. Go to "Scripting" Menu on MySQL Workbench, and select "Install Plugin/Module" option
# 3. Find and select the file downloaded on step 1. Then restart MySQL Workbench
# 5. You can trigger the report from "Tools/Catalog" Menu, option "HTML Database Schema Report"

from wb import *
import grt
from mforms import Utilities, FileChooser
import mforms

ModuleInfo = DefineModule(
    name="DBReportHTML",
    author="Tito Sanchez",
    version="1.0",
    description="Database Schema Report in HTML format (with Bootstrap)",
)


@ModuleInfo.plugin(
    "tmsanchezplugin.dbReportHtml",
    caption="DB Report in HTML",
    description="Database Schema Report in HTML format (with Bootstrap)",
    input=[wbinputs.currentCatalog()],
    pluginMenu="Catalog",
)
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)
def htmlDataDictionary(catalog):
    # Put plugin contents here
    htmlOut = ""
    filechooser = FileChooser(mforms.SaveFile)
    filechooser.set_extensions("HTML File (*.html)|*.html", "html")
    if filechooser.run_modal():
        htmlOut = filechooser.get_path()
    print("HTML File: %s" % (htmlOut))
    if len(htmlOut) <= 1:
        return 1
    
    schema = catalog.schemata[0]
    
    # Start HTML
    htmlFile = open(htmlOut, "w")
    htmlFile.write("<html><head>")
    htmlFile.write("<title>Schema Report for database: %s</title> \n" % (schema.name))
    htmlFile.write(
        """
        <!doctype html><html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
            <title>%s - Schema Report</title>
        </head>
        <body>
        """
        % (schema.name)
    )

    # Header and Navigation
    htmlFile.write(
        """
        <header>
            <nav class="navbar navbar-dark bg-primary">
             <div class="container-fluid">
               <span class="navbar-brand mb-0 h1"><h1>Schema Report for Database: %s</h1></span>
             </div>
            </nav>
        </header>
        """
        % (schema.name)
    )

     # List of Tables
    htmlFile.write(
        """
        <div class="container">
          <div class="my-5">
            <span id="home" class="fs-1 text-decoration-none">Table List </span>
            <ul class="list-group">
        """
    )
    for table in schema.tables:
        htmlFile.write(
            '<li class="list-group-item"><a class="fw-bold text-decoration-none" href="#%s">%s </a></li> \n'
            % (table.name, table.name)
        )
    htmlFile.write("</ul> </div>\n")

    # Table details
    for table in schema.tables:
        htmlFile.write(
            """
        <span id="%s" class="fs-3 text-decoration-none">Table: %s</span><br>
        <p class="fw-bold mt-3">Description/Comments</p>
        <p class="fw-light">%s</p><hr>
        """
            % (table.name, table.name, table.comment)
        )

        htmlFile.write(
            """
        <table class="table table-bordered table-striped">
        <tr>
        <th>Name</th>
        <th>Data Type</th>
        <th>Not Null</th>
        <th>PK</th>
        <th>FK</th>
        <th>Default</th>
        <th>Comment</th>
        </tr>
        """
        )

        for column in table.columns:
            pk = ("No", "Yes")[bool(table.isPrimaryKeyColumn(column))]
            fk = ("No", "Yes")[bool(table.isForeignKeyColumn(column))]
            nn = ("No", "Yes")[bool(column.isNotNull)]
            htmlFile.write(
                "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr> \n"
                % (
                    column.name,
                    column.formattedType,
                    nn,
                    pk,
                    fk,
                    column.defaultValue,
                    column.comment,
                )
            )
        htmlFile.write(
            """
        </table>
        <a href=\"#home\" class="btn btn-primary">Back to Table List</a></br></br></br>
        """
        )

    # footer
    htmlFile.write("</body></html>\n")
    htmlFile.close()
    Utilities.show_message(
        "Report generated",
        "HTML Report format from current model generated in %s" % htmlOut,
        "OK",
        "",
        "",
    )
    return 0