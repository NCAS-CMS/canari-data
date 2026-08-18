# CANARI Large Ensemble

The page contains information for users and developers of the CANARI Large Ensemble.
Basic properties and the experiment design of this Large Ensemble are described [here](https://canari.ac.uk/resources_new/tools).

## Accessing the output

### Priority and derived output on JASMIN CANARI group workspace

A subset of the complete output is retrieved from the JASMIN Elastic Tape to this location:
`/gws/nopw/j04/canari/shared/large-ensemble/priority`.
The available priority variables are listed [here](/metadata/20240303-canari-le-priority-variables.xlsx); the spreadsheet contains:
  - the priority UMatmos variables, 
  - priority NEMO variables ("Priority 1" monthly and 2D daily only), and
  - priority CICE variables (all CICE output is included in the priority output).

**Note:** an unfortunate change in the names of four variables occurred during the HIST2 runs. The spreadsheet referenced above details the variable naming for the currently extracted ensemble members and indicates where the names switch. Variable naming is consistent within an ensmeble member.


Alongside the `priority` directory, derived diagnostics are shared by the CANARI community, and you are encouraged to share your own in an appropriate location, e.g., adding to `/gws/nopw/j04/canari/shared/large-ensemble/derived`. Management of this shared space is very light-touch, and **different users can write** to it, so please make sure you either keep a private copy of your data for small datasets, or that you can easily reproduce these derived diagnostics should the need arise.

### Full output on the JASMIN Elastic Tape

Variables not contained in the priority output can be retrieved from the JASMIN Elastic Tape. In order to do this, you need to
  - know how to read from the ET, using the so-called JDMA tool. This is explained [here](https://help.jasmin.ac.uk/category/196-long-term-archive-storage).
  - know the ET batches corresponding to the ensemble members your are looking for. These are detailed [below](#canari-hist2-production-suites) for the historical ("HIST2") simulations.

### Ancillary files

Commonly used ancillary files, such as for the land fraction and orography, are available at `/gws/nopw/j04/canari/shared/large-ensemble/ancil`.

## CANARI SSP3-7.0 Production Suites

### Completed Ensemble Members

| 1 - 10 | 11 - 20 | 21 - 30 | 31 - 40 |
| --- | --- | --- | --- |
| [01 - u-de814](ssp370/1-de814) | [11 - u-de934](ssp370/11-de934) | [21 - u-df933](ssp370/21-df933) | [31 - u-di511](ssp370/31-di511) |
| [02 - u-de436](ssp370/2-de436) | [12 - u-de937](ssp370/12-de937) | [22 - u-df934](ssp370/22-df934) | [32 - u-di512](ssp370/32-di512) |
| [03 - u-de724](ssp370/3-de724) | [13 - u-de938](ssp370/13-de938) | [23 - u-df935](ssp370/23-df935) | [33 - u-di513](ssp370/33-di513)  |
| [04 - u-de815](ssp370/4-de815) | [14 - u-de939](ssp370/14-de939) | [24 - u-df936](ssp370/24-df936) | [34 - u-di514](ssp370/34-di514) |
| [05 - u-df220](ssp370/5-df220) | [15 - u-de940](ssp370/15-de940) | [25 - u-df937](ssp370/25-df937) | [35 - u-di515](ssp370/35-di515) |
| [06 - u-de830](ssp370/6-de830) | [16 - u-df299](ssp370/16-df299) | [26 - u-dh412](ssp370/26-dh412) | [36 - u-di703](ssp370/36-di703) |
| [07 - u-de831](ssp370/7-de831) | [17 - u-df300](ssp370/17-df300) | [27 - u-dh413](ssp370/27-dh413) | [37 - u-di704](ssp370/37-di704) |
| [08 - u-de832](ssp370/8-de832) | [18 - u-df301](ssp370/18-df301) | [28 - u-dh415](ssp370/28-dh415) | [38 - u-di705](ssp370/38-di705) |
| [09 - u-de850](ssp370/9-de850) | [19 - u-df302](ssp370/19-df302) | [29 - u-dh416](ssp370/29-dh416) | [39 - u-di706](ssp370/39-di706) |
| [10 - u-de851](ssp370/10-de851) | [20 - u-df303](ssp370/20-df303) | [30 - u-dh417](ssp370/30-dh417) | [40 - u-di707](ssp370/40-di707) |

## CANARI HIST2 Production Suites

### Completed Ensemble Members

| 1 - 10 | 11 - 20 | 21 - 30 | 31 - 40 |
| --- | --- | --- | --- |
| [01 - u-cv575](hist2/1-cv575) | [11 - u-cy375](hist2/11-cy375) | [21 - u-da179](hist2/21-da179) | [31 - u-cz475](hist2/31-cz475) |
| [02 - u-cv625](hist2/2-cv625) | [12 - u-cy376](hist2/12-cy376) | [22 - u-da190](hist2/22-da190) | [32 - u-cz568](hist2/32-cz568) |
| [03 - u-cw345](hist2/3-cw345) | [13 - u-cy537](hist2/13-cy537) | [23 - u-da191](hist2/23-da191) | [33 - u-cz647](hist2/33-cz647) |
| [04 - u-cw356](hist2/4-cw356) | [14 - u-cy811](hist2/14-cy811) | [24 - u-da192](hist2/24-da192) | [34 - u-cz648](hist2/34-cz648) |
| [05 - u-cv827](hist2/5-cv827) | [15 - u-cy866](hist2/15-cy866) | [25 - u-da193](hist2/25-da193) | [35 - u-cz649](hist2/35-cz649) |
| [06 - u-cv976](hist2/6-cv976) | [16 - u-cy873](hist2/16-cy873) | [26 - u-db291](hist2/26-db291) | [36 - u-dd436](hist2/36-dd436) |
| [07 - u-cz547](hist2/7-cz547) | [17 - u-cy877](hist2/17-cy877) | [27 - u-db301](hist2/27-db301) | [37 - u-dd438](hist2/37-dd438) |
| [08 - u-cy436](hist2/8-cy436) | [18 - u-cy879](hist2/18-cy879) | [28 - u-db303](hist2/28-db303) | [38 - u-dd439](hist2/38-dd439) |
| [09 - u-cw342](hist2/9-cw342) |  [19 - u-cy880](hist2/19-cy880) | [29 - u-db304](hist2/29-db304) | [39 - u-dd441](hist2/39-dd441) |
| [10 - u-cw343](hist2/10-cw343) | [20 - u-cy881](hist2/20-cy881) | [30 - u-db305](hist2/30-db305) | [40 - u-dd442](hist2/40-dd442) |

####  Abandoned Suites:
* [03 - u-cv608](hist2/3-cv608)
* [04 - u-cv830](hist2/4-cv830)
* [07 - u-cw083](hist2/7-cw083)
* [08 - u-cw085](hist2/8-cw085)

## CANARI HIST1 Production Suites

* [u-cu600](u-cu600)
* u-cv592
* [u-cv247](HIST1-RI36-u-cv247-runlog.md)
* [u-cv281](u-cv281)
* [u-cw263](u-cw263)
* [u-cw264](u-cw264)

## Documents related to suite running

* [Setting up to run a CANARI production suite](setup)
* [Setting up to run a CANARI SSP3-7.0 production suite](setup-ssp370)
* [CANARI suite description](suite-description)
* [ARCHER2 OS Upgrade - Suite Restart Instructions](archer2-os-upgrade)
* [Troubleshooting](troubleshooting)
* [Frequently Asked Questions](faq)
* [Known issues affecting more than suite suite](hist2-known-issues)

# Importing from canari-data/README.md

# canari-data
Documents and code for canari data management

This repo will eventually include 
- all the documents which describe the CANARI Large Ensemble data environment,
- all the code we use to manipulate data in the CANARI workflow

Meanwhile, [this](https://docs.google.com/document/d/1oYErv41Ai5535LMHfU5wCUTFEnRFr39LbVoaKDHEZNg) is the draft file attributes specification.

## CANARI Ensemble Design and Simulation Identification by Variant Label

#### First Tranch
We will be doing the following HIST runs from 1950, with SSP370 continuation to 2100
- there are two parent/child relationships here (CMIP6 HIST -> CANARI HIST2 and CANARI HIST2 -> SSP370)
- branch method: "micro initialisation from CMIP6 macro parent" for the first one set, "continuation" for the second.
- Note that the HIST compoenent should be stored as HIST1, which is a variant of the CMIP HIST run, which differs only in the duration.
- (note the slight change in the experiment name, which is only about duration)
- the branch time in the parent and child will be the same
- branch method: "micro perturbed atmosphere initialisation" for the first one, "continuation" for the second.
- (note that the hash in the variant labels should be replaced by the realization index)
- note that P2 is used because we have the corrected ozone runs so this isn't quite vanilla HadGEM3-GC31.

| Variant Label | Parent | Initialisation Index | Realiisation Index | Notes |
| -- | -- | -- | -- | -- |
| r#i1f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.historical.r1i1p1f3 | 1 | 1-5 | Five variants iniitialised by perturbing initial atmosphere | 
| r#i2f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.historical.r2i1p1f3 | 2 | 6-10 | Five variants iniitialised by perturbing initial atmosphere | 
| r#i3f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.historical.r3i1p1f3 | 3 | 11-15 | Five variants iniitialised by perturbing initial atmosphere | 
| r#i4f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.historical.r4i1p1f3 | 4 | 16-20 | Five variants iniitialised by perturbing initial atmosphere | 

#### Macro Tranch

We need an additional four simulations to provide initial conditions from different ocean states, these run from 1850 to 1950.
- these runs are initialised from PICONTROL at 50 year intervals
- there is one parent/child relationships here (PICONTROL -> CANARI HIST1)
- branch method "50 year intervals in PICONTROL to get diverse ocean states"
- Note that these ones, unlike all the other ones, will have a different branch time in the child than in the parent, the children start date will always be 1850 the parent start date will be whatever is selected.
- Note that these should be stored as HIST1, which is a variant of the CMIP HIST run, which differs only in the duration.

| Variant Label | Parent | InitialisationRealisation Index | RealisationI Index | Notes |
| -- | -- | -- | -- | -- |
| r21i5f1p1 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 5 | 21 | Just the one run but check ocean state at start |
| r26i6f1p1 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 6 | 26 | Just the one run but check ocean state at start |
| r31i7f1p1 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 7 | 31 | Just the one run but check ocean state at start|
| r36i8f1p1 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 8 | 36 | Just the one run but check ocean state at start|

#### Second Tranch - Core

These are then continued by another set of runs, the second tranch core-set
- there are two parent/child relationships here (CANARI HIST1 -> CANARI HIST2 and CANARI HIST2 -> SSP370)
- branch method = continuation
- can start when a) the macro parent is finishd, and b) checked to have a different state

| Variant Label | Parent | InitialisationRealisation Index | RealisationI Index | Notes |
| -- | -- | -- | -- | -- |
| r21i5f1p2 | CANARI-LE.NCAS.HadGEM3-GC31-MM.hist1.r#i5f1p1 | 5 | 21 | Continues without perturbation |
| r26i6f1p2 | CANARI-LE.NCAS.HadGEM3-GC31-MM.hist1.r#i6f1p1 | 6 | 26 | Continues without perturbation |
| r31i7f1p2 | CANARI-LE.NCAS.HadGEM3-GC31-MM.hist1.r#i7f1p1 | 7 | 31 | Continues without perturbation |
| r36i8f1p2 | CANARI-LE.NCAS.HadGEM3-GC31-MM.hist1.r#i8f1p1 | 8 | 36 | Continues without perturbation |


#### Second Tranch - Perturbed

We will be doing an additional set of HIST runs from 1950, with SSSP370 continuation based on the Macro Tranch.

- there are two parent/child relationships here (CANARI HIST1 -> CANARI HIST2 and CANARI HIST2 -> SSP370)
- branch method for the first set:  "micro perturbed atmosphere initialisation"; "continuation" for the second set
- can start when a) the macro parent is finishd, and b) checked to have a different state

| Variant Label | Parent | Initialisation Index | Realisation Index | Notes |
| -- | -- | -- | -- | -- |
| r#i5f1p2 | CANARI-LE.NCAS.HadGEM3-GC31-MM.hist1.r#i5f1p2 | 5 | 22-25 | Four variants iniitialised by perturbing initial atmosphere | 
| r#i61p2 | CANARI-LE.NCAS.HadGEM3-GC31-MM.hist1.r#i6f1p2 | 6 | 27-30  | Four variants iniitialised by perturbing initial atmosphere | 
| r#i7f1p2 | CANARI-LE.NCAS.HadGEM3-GC31-MM.hist1.r#i7f1p2 | 7 | 32-35 | Four variants iniitialised by perturbing initial atmosphere | 
| r#i8f1p2 | CANARI-LE.NCAS.HadGEM3-GC31-MM.hist11.r#i8f1p2 | 8 | 37-40 | Four variants iniitialised by perturbing initial atmosphere | 





