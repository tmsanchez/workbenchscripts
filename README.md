# Useful Scripts for MysqlWorkbench

## Plugins for  MySQLWorkbench 8.x 

### HTML Format report schema

**MarkdownSchemaReportWB.py** tested on version 8.0.23

Sample output

![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/markdownreport.png?raw=true)

 **HTMLSchemaReportWB8.py**  tested on version 8.0.23

Sample output

 ![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/htmlExample.jpg?raw=true)

### Markdown Format report schema



### Plugins for MySQLWorkbench 6.x 

 **HTMLSchemaReport.py** was tested on MysqlWorkbench version 6.3 **Note** this will not work on MysqlWorkbench 8.x

## Installing Plugins


To Install the plugin go to Scripting / Install Plugin/Module then select HTMLShemaReport.py file and restart MySQL Workbench
![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/installaPlugin.png?raw=true)


## Generatig reports

Open your model and go to Tools / Catalog and select "Database schema in HTML format" and provide a file name in save dialog.
![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/runningPlugin.png?raw=true)


Once document has been generated you will see following message:

![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/reportGenerated.png?raw=true)

Then open your HTML document and see the report:
![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/htmlExample.jpg?raw=true)

Finally I want to thank all readers for their contributions, specially to Rodrigo Schmidt who started script python.

References 
http://tmsanchezdev.blogspot.com/2015/03/html-report-from-mysqlworkbench-6x.html



## Generating a script for FirebirdSQL from MySQLWorkbench 6.x


MySQLWorkbench allows to design database model easily and also provides an option to generate the SQL script.   By default script is generated for MySQL, but, what if you need to generate a SQL script for FirebirdSQL?.

Using Python you cand create custom plugins to access to model properties  (table and columns definitions for example) please visit this link for more info Scripting and Plugin Development

So, I decided to write a plugin to generate a SQL Script for FirebirdSQL. My goal it's just to show how can we access to schemas, tables and columns properties using classes already defined by MySQLWorkbench.

![Running FBScript](https://github.com/tmsanchez/workbenchscripts/blob/master/runfbscript.jpg?raw=true)

------------
You can read more at http://tmsanchezdev.blogspot.mx/2017/04/generating-script-for-firebirdsql-from.html
