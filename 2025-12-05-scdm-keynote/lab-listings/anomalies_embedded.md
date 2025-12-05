# Embedded anomalies (verification)

Seed: **240604**

This file lists exactly what was embedded and where, so you can verify your anomaly detector.


## 1) TEMPORAL PATTERN — elevated ALT on Tuesdays 2–4pm

- Site_ID: `002`
- Trigger: `Test_Name=ALT` AND Tuesday AND `Time_Collected` in `14:00`–`16:00`
- Effect: ALT × **1.35**

## 2) GENDER BIAS — female creatinine higher at Site 007

- Site_ID: `007`
- Sex encoding: creatinine normal range differs by sex (F: 0.50–1.10, M: 0.70–1.30 mg/dL)
- Trigger: female patients inferred by Creatinine `Normal_Range_High=1.10`
- Effect: creatinine × **1.15** at all visits
- Affected Patient_IDs:
  - 007-001
  - 007-005
  - 007-006
  - 007-007
  - 007-008
  - 007-009
  - 007-011
  - 007-012
  - 007-013
  - 007-014
  - 007-017
  - 007-018
  - 007-020

## 3) SEQUENCE EFFECT — every 5th patient enrolled at Site 003 has borderline high bilirubin at Baseline

- Site_ID: `003`
- Trigger: `Visit_Name=Baseline` AND (enrollment order within Site 003) % 5 == 0
- Effect: bilirubin set to uniform(1.21, 1.35) mg/dL
- Affected Patient_IDs: `003-005`, `003-010`, `003-015`, `003-020`

## 4) SEASONAL DRIFT — HbA1c at Site 009 drifts upward 0.1% per calendar month

- Site_ID: `009`
- Trigger: all `Test_Name=HbA1c` rows
- Effect: HbA1c += `0.1 × month_index` where Jan=0, Feb=1, ...
- Generator note: Site 009 has no underlying improvement trend so you can see the drift clearly.

## 5) CORRELATION ANOMALY — Site 005 ALT>60 ⇒ AST always lower than ALT

- Site_ID: `005`
- Trigger: ALT > 60
- Effect: AST forced to be ALT − [1..10]

## 6) EXTRA — Technician digit-preference rounding

- Site_ID: `006`
- Lab_Technician_ID: `LT-006-02`
- Trigger: `Test_Name in {FPG, Glucose}`
- Effect: results rounded to nearest 5 mg/dL

## 7) EXTRA — Bilirubin reference-range decimal bug

- Site_ID: `004`
- Trigger: `Test_Name=Bilirubin` in Feb+Mar 2024, ~25% probability
- Effect: `Normal_Range_High` incorrectly set to **12.0** (should be 1.2)
- Count unique (Patient_ID, Visit_Name, Visit_Date): **13**

- Examples (first 40):
  - 004-004 | Week 4 | 2024-02-07
  - 004-008 | Week 4 | 2024-02-07
  - 004-013 | Week 4 | 2024-02-07
  - 004-001 | Week 4 | 2024-02-08
  - 004-006 | Week 4 | 2024-02-11
  - 004-007 | Week 8 | 2024-03-06
  - 004-009 | Week 8 | 2024-03-06
  - 004-012 | Week 8 | 2024-03-06
  - 004-015 | Week 8 | 2024-03-06
  - 004-008 | Week 8 | 2024-03-08
  - 004-016 | Week 8 | 2024-03-08
  - 004-006 | Week 8 | 2024-03-10
  - 004-014 | Week 8 | 2024-03-10

## 8) EXTRA — Enzyme specimen swap at Site 010, Week 8

- Site_ID: `010`
- Visit_Name: `Week 8`
- Swapped tests: ALT and AST
- Patient pairs:
  - `010-007` ⇄ `010-008`
  - `010-014` ⇄ `010-015`
- Metadata for involved patients:
  - 010-007 | 2024-03-04 | 10:24 | LT-010-04
  - 010-008 | 2024-03-04 | 10:24 | LT-010-04
  - 010-014 | 2024-03-06 | 08:45 | LT-010-02
  - 010-015 | 2024-03-06 | 08:45 | LT-010-02
