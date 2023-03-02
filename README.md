# canari-data
Documents and code for canari data management

This repo will eventually include 
- all the documents which describe the CANARI Large Ensemble data environment,
- all the code we use to manipulate data in the CANARI workflow

Meanwhile, [this](https://docs.google.com/document/d/1oYErv41Ai5535LMHfU5wCUTFEnRFr39LbVoaKDHEZNg) is the draft file attributes specification.

## CANARI Ensemble Design and Simulation Identification

(Reinhard to add text and edit the table, in particular to replace the "relevant CMIP6 DRS-ID with the appropriate hist run)

We will be doing the following HIST runs from 1950, with SSP370 continuation
- there are two parent/child relationships here (CMIP6 HIST -> CANARI HIST and CANARI HIST -> SSP370)

| Variant Label | Macro Parent | Realisation Index | Initialisation Index | Notes |
| -- | -- | -- | -- | -- |
| r1i-f1p1 | Relevant CMIP6 HIST DRS-ID | 1 | 1-5 | Five variants iniitialised by perturbing initial atmosphere | 
| r2i-f1p1 | Relevant CMIP6 HIST DRS-ID | 2 | 6-10 | Five variants iniitialised by perturbing initial atmosphere | 
| r3i-f1p1 | Relevant CMIP6 HIST DRS-ID | 3 | 11-15 | Five variants iniitialised by perturbing initial atmosphere | 
| r4i-f1p1 | Relevant CMIP6 HIST DRS-ID | 4 | 16-20 | Five variants iniitialised by perturbing initial atmosphere | 

We will be doing the following HIST runs from 1850, with SSP370 continuation
- these runs are initialised from PICONTROL at 30 year intervals
- there are three parent/child relationships here (PICONTROL -> CANARI HIST, CANARI HIST -> CANARI HIST, and CANARI HIST -> SSP370)
- (or not, we need to discuss the nomenclature)

| Variant Label | Macro Parent | Realisation Index | Initialisation Index | Notes |
| -- | -- | -- | -- | -- |
| r5i21f1p1 | Relevant CMIP6 PICONTROL DRS-ID | 5 | 21 | Just the one variant, but three logical components |
| r6i22f1p1 | Relevant CMIP6 PICONTROL DRS-ID | 6 | 22 | Just the one variant, but three logical components |
| r7i23f1p1 | Relevant CMIP6 PICONTROL DRS-ID | 7 | 23 | Just the one variant, but three logical components|
| r8i24f1p1 | Relevant CMIP6 PICONTROL DRS-ID | 8 | 24 | Just the one variant,  but three logical components|

We will be doing an additional set of HIST runs from 1950, with SSSP370 continuation:
- there are two parent/child relationships here (CANARI HIST -> CANARI HIST and CANARI HIST -> SSP370)

| Variant Label | Macro Parent | Realisation Index | Initialisation Index | Notes |
| -- | -- | -- | -- | -- |
| r1i-f1p1 | CANARI-LE/HIST/r5i26f1p1 | 5 | 25-28 | Four variants iniitialised by perturbing initial atmosphere | 
| r2i-f1p1 | CANARI-LE/HIST/r5i26f1p1 | 6 | 29-32  | Four variants iniitialised by perturbing initial atmosphere | 
| r3i-f1p1 | CANARI-LE/HIST/r5i26f1p1 | 7 | 33-36 | Four variants iniitialised by perturbing initial atmosphere | 
| r4i-f1p1 | CANARI-LE/HIST/r5i26f1p1 | 8 | 37-40 | Four variants iniitialised by perturbing initial atmosphere | 





