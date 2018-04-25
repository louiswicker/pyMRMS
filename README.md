# README #

Documentation for the pyMRMS processing

### What is this repository for? ###

* Quick summary
The code here will take netCDF output, from an LDM feed of the MRMS data and convert it to a suitable
form for DART.  The code specifies the layers wanted from the vertical grid at the top, retrives
those levels, sets a threshold for min dBZ, and outputs both dBZ and zero-dBZ in a thinned manner.
It can creates 2 panel plot with one panel plotting reflectivity from a fixed height, the second is composite reflectivity
with zeros plotting.  The automated processing is controled by the cron_script, and the retrospective processing
is controled by the "catchup" script.  To use the scripts, please examine the macro definitions at the top of the script.
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up

* Configuration

* Dependencies
pyMRMS:  matplotlib, numpy, pyART, and pyProj as dependencies.

* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
Use at your own risk - I might answer questions if I have time.  
Louis.Wicker@noaa.gov
* Other community or team contact
