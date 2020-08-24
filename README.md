# Useful Scripts for MysqlWorkbench
Scripts for Mysql Workbench
------------

## HTML Report from MySQLWorkbench 6.x Schema Model

I wrote **HTMLSchemaReport.py** a Python pluging to generate an HTML Schema Report from a database model.
 
To Install the plugin go to Scripting / Install Plugin/Module then select HTMLShemaReport.py file and restart MySQL Workbench
![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/installaPlugin.png?raw=true)

Open your model and go to Tools / Catalog and select "Database schema in HTML format" and provide a file name in save dialog.
![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/runningPlugin.png?raw=true)


Once document has been generated you will see following message:
![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/reportGenerated.png?raw=true)

Then open your HTML document and see the report:
![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/htmlExample.jpg?raw=true)

Finally I want to thank all readers for their contributions, specially to Rodrigo Schmidt who started script python.

Refernces 
http://tmsanchezdev.blogspot.com/2015/03/html-report-from-mysqlworkbench-6x.html


## Generating a script for FirebirdSQL from MySQLWorkbench


MySQLWorkbench allows to design database model easily and also provides an option to generate the SQL script.   By default script is generated for MySQL, but, what if you need to generate a SQL script for FirebirdSQL?.

Using Python you cand create custom plugins to access to model properties  (table and columns definitions for example) please visit this link for more info Scripting and Plugin Development

So, I decided to write a plugin to generate a SQL Script for FirebirdSQL. My goal it's just to show how can we access to schemas, tables and columns properties using classes already defined by MySQLWorkbench.

![Install Plugin](https://github.com/tmsanchez/workbenchscripts/blob/master/runfbscript.jpg?raw=true)

------------
You can read more at http://tmsanchezdev.blogspot.mx/2017/04/generating-script-for-firebirdsql-from.html
