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

| Variant Label | Macro Parent | Initialisation Index | Realiisation Index | Notes |
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

| Variant Label | Macro Parent | InitialisationRealisation Index | RealisationI Index | Notes |
| -- | -- | -- | -- | -- |
| r21i5f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 5 | 21 | Just the one variant, but three logical components |
| r26i6f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 6 | 26 | Just the one variant, but three logical components |
| r31i7f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 7 | 31 | Just the one variant, but three logical components|
| r36i8f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 8 | 36 | Just the one variant,  but three logical components|

#### Second Tranch - Core

These are then continued by another set of runs, the second tranch core-set
- there are two parent/child relationships here (CANARI HIST1 -> CANARI HIST2 and CANARI HIST2 -> SSP370)
- branch method = continuation
- can start when a) the macro parent is finishd, and b) checked to have a different state

| Variant Label | Macro Parent | InitialisationRealisation Index | RealisationI Index | Notes |
| -- | -- | -- | -- | -- |
| r21i5f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 5 | 21 | Continues without perturbation |
| r26i6f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 6 | 26 | Continues without perturbation |
| r31i7f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 7 | 31 | Continues without perturbation |
| r36i8f1p2 | CMIP6.CMIP.MOHC.HadGEM3-GC31-MM.piControl.r1i1p1f1 | 8 | 36 | Continues without perturbation |


#### Second Tranch - Perturbed

We will be doing an additional set of HIST runs from 1950, with SSSP370 continuation based on the Macro Tranch.

- there are two parent/child relationships here (CANARI HIST1 -> CANARI HIST2 and CANARI HIST2 -> SSP370)
- branch method for the first set:  "micro perturbed atmosphere initialisation"; "continuation" for the second set
- can start when a) the macro parent is finishd, and b) checked to have a different state

| Variant Label | Macro Parent | Initialisation Index | Realisation Index | Notes |
| -- | -- | -- | -- | -- |
| r#i5f1p2 | CANARI-LE/HIST/r#i5f1p2 | 5 | 22-25 | Four variants iniitialised by perturbing initial atmosphere | 
| r#i61p2 | CANARI-LE/HIST/r#i6f1p2 | 6 | 27-30  | Four variants iniitialised by perturbing initial atmosphere | 
| r#i7f1p2 | CANARI-LE/HIST/r#i7f1p2 | 7 | 32-35 | Four variants iniitialised by perturbing initial atmosphere | 
| r#i8f1p2 | CANARI-LE/HIST/r#i8f1p2 | 8 | 37-40 | Four variants iniitialised by perturbing initial atmosphere | 





