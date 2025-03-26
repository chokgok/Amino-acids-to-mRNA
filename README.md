##### Included with repository are `.txt` example files, showcasing what input format is accepted and what output is printed.
```
Preferred Input: "Leucine/ Histidine/ Lysine/ Glutamic Acid/ Threonine"
---
leucine: UUA, UUG, CUU, CUC, CUA, CUG
histidine: CAU, CAC
lysine: AAA, AAG
glutamic acid: GAA, GAG
threonine: ACU, ACC, ACA, ACG
---
Output:   Leu: UUA, UUG, CUU, CUC, CUA, CUG
          His: CAU, CAC
          Lys: AAA, AAG
          Glu: GAA, GAG
          Thr: ACU, ACC, ACA, ACG

          Possible sequences:
          Leucine
          UUA, CAU, AAA, GAA, ACU
          UUG, CAU, AAA, GAA, ACU
          CUU, CAU, AAA, GAA, ACU
          CUC, CAU, AAA, GAA, ACU
          CUA, CAU, AAA, GAA, ACU
          CUG, CAU, AAA, GAA, ACU
          
          UUA, CAC, AAA, GAA, ACU
          UUG, CAC
```
