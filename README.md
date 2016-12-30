# geot
## Geotechnical data, logs and sections ##

Geot defines a simple database format for fast logging and display of site investigation and laboratory testing data.  Based on AS 1726-1993.

*Compatible with Python 3.6 only.*

### Roadmap ###
* Database schema
    * Export mappers to AGS3.1, AGS4, specific gINT libraries
    * Import mappers from specific AGS or gINT files (poorly standardised)
    * Web browser interface (Flask|Web2py|Django)
* Graphics
    * Section and log elements
    * Display onscreen (SVG?)
    * Export to PDF and DXF
    * Define layout with serial data format e.g. JSON, YAML