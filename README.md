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
Release 1.0  

### How do I get set up? ###

* Summary of set up  
  
See top of catchup and cron python code to configure the system.  You can specify the LDM
directory where the MRMS levels are being delivered, and the output directory for the
obs_sequence and plots to go into.  This system was built to run when initiated from a crontab
on a Linux workstation.  It works fine using the experimental 5 km resolution MRMS feed
from NSSL Virtual MRMS system.  To use the operational MRMS feed at 1 km (available over normal
LDM delivery) one will need to test whether it is fast enough.  Here processing of the 5 km
data for 10 vertical levels ~ 30 sec, much of that is the plotting.  

* Dependencies  
Matplotlib  
Basemap  
pyART  
pyProj  

### Who do I talk to? ###

* Repo owner 
Use at your own risk.  
I may or may not have time to answer questions.  
Louis.Wicker@noaa.gov  
