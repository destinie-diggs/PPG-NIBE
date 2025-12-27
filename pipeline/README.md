# Data Curation Pipeline — Reproducibility Guide

This directory contains the scripts used to generate the PPG-NIBE dataset. The pipeline transforms VitalDB csv files (accessed via web api) into a
reproducible, analysis-ready dataset with explicit inclusion and exclusion
criteria.

Each script performs a single, documented transformation and produces a
deterministic output file.

---

## Pipeline Overview - Expected output
    Raw VitalDB lab results (35,358 BG samples)

    └─ Script 1 → labs_gluc_only_2.csv (8,847 samples)

       └─ Script 2 → labs_and_demographics.csv (8,847 samples)
   
          └─ Script 3 → labs_and_demographics2.csv (7,590 samples)
      
             └─ Script 4 → Per-sample 16 min PPG window CSVs (7,146 samples)
         
                └─ Script 5 → Recovers previously excluded samples for 8 min windows (7477 samples)
            

__For detailed pipeline review see [Wiki Data Pipeline](https://github.com/destinie-diggs/PPG-NIBE/wiki/Data-Curation-Pipeline)__
