# CANARI Regional Storm Simulations

This page contains information for users of the CANARI regional storm simulations.
These simulations provide regional downscaling of selected storm events from the CANARI Large Ensemble via nested 12km and 2.2km domains.

## Simulations

Individual simulations are named as `Domain_EnsMem_CaseID` where:

* `Domain` is the regional model domain, one of `UK-12km`, `UK-2p2km`, `NAEW-12km`, `NAEW-2p2km`
* `EnsMem` is the CANARI Large Ensemble member
* `CaseID` identifies the storm case, typically of the form `YYYYMMDD-X`
where `YYYYMMDD` is the date and `X` is one of `W` (wind events) or `P` (precipitation events).

Simulations are grouped into batches ("run lists") as follows:

* [CANARI-RM_WindStorms-HIST2](runlists/CANARI-RM_WindStorms-HIST2.txt)
* [CANARI-RM_WindStorms-SSP370](runlists/CANARI-RM_WindStorms-SSP370.txt)
* [CANARI-RM_PrecipStormsUKIR](runlists/CANARI-RM_PrecipStormsUKIR.txt)
* [CANARI-RM_PrecipStormsWidespreadFloods](runlists/CANARI-RM_PrecipStormsWidespreadFloods.txt)
* [CANARI-RM_PrecipStormsSummer](runlists/CANARI-RM_PrecipStormsWidespreadFloods.txt)

## Quicklook galleries

Quicklook plots from the regional simulations are available 
[here](https://gws-access.jasmin.ac.uk/public/canari/storms/downscaling_galleries)

## Accessing the output

### Priority output on JASMIN CANARI group workspace

The full output list is described [here](https://docs.google.com/spreadsheets/d/1UkfNZj6iDPreSL_VHmADgLAw7fWohs31/edit?usp=sharing&ouid=114953017409305087326&rtpof=true&sd=true)

A subset of the complete output (indicated priority in the spreadsheet) is stored on the CANARI GWS here: `/gws/ssde/j25b/canari/shared/regional/priority/<runlist>`

### Full output on the JASMIN Elastic Tape

Variables not contained in the priority output can be retrieved from the JASMIN Elastic Tape using [NLDS](https://help.jasmin.ac.uk/docs/short-term-project-storage/nlds/).
In contrast to the LE output (which uses JDMA), there is no need to be GWS manager to access this data.

Each run list is in a separate NLDS holding, named after the run list.

Some example NDLS commands: *Note: the use of wildcards is currently unavailable in the NLDS system*
* List all the CANARI regional model holdings: `nlds list -Ax -g canari -l "CANARI-RM.*"`
* List all files in one holding: `nlds find -A -g canari -l <holding_name>`
* List all files for one variable from a holding, e.g.: `nlds find -Ax -g canari -l <holding_name> -p “.*_<stash_code>_.*”`
* List all files for one simulation (all variables): `nlds find -Ax -g canari -l <holding_name> -p “.*/<simulation_name>/.*”`
* Retrieve a single file to <target_dir> (must have g+w permissions): `nlds get -A -g canari -l <holding_name> -r <target_dir> <filename>`
* Retrieve all files for one simulation: `nlds get -A x-g canari -l <holding_name> -r <target_dir> “.*/<simulation_name>/.*”`
* To check status of get commands: `nlds stat -0`

### Ancillary files

The model ancillary files are available at `/gws/ssde/j25b/shared/regional/ancil`
