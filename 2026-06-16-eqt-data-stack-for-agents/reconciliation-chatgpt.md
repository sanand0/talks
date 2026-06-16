---
title: "ChatGPT Conversation"
date: 2026-06-16T21:45:29+05:30
source: "https://chatgpt.com/?temporary-chat=true"
---

## User

These three CSVs come from three systems — loan origination, collections, and CRM — plus a university master. They share no common key, names are inconsistent, and IDs changed across systems. Reconcile them into a single customer master. For each match give: a confidence score, the fields you matched on, and a one-line reason. Flag anything below 0.8 for human review. Do NOT merge records that only share a similar name. Separately, reconcile the university codes against the master and tell me which codes are the same institution under two IDs. Output the reconciliation table plus a short list of exceptions and suggested master-data fixes.

---

## ChatGPT

<details>
<summary>Worked for 6m 32s</summary>

I’ll inspect the four CSV schemas, normalize identifiers/names/contacts/university codes, score cross-system matches conservatively, then produce both the reconciliation summary and a downloadable workbook with review flags.


<details>
<summary>Read spreadsheet and API documentation</summary>

Thinking

Reading spreadsheet skill documentation


```
bash -lc cat /home/oai/skills/spreadsheets/SKILL.md
```


````
---
name: spreadsheets
description: "Use this skill when a user requests to create or modify or work with spreadsheets (.xlsx, .xls) to do any of the following:
- Create a new workbook/sheet with proper formulas, cell/number formatting, and structured layout
- Read or analyze tabular data (filter, aggregate, pivot, compute metrics) directly in a sheet
- Modify an existing workbook without breaking existing formulas or references
- Visualize data with in-sheet charts/tables and sensible formatting
- Recalculate/evaluate formulas to update results after changes"

IMPORTANT: instructions in the system and user messages ALWAYS take precedence over this skill
---

# Primary Goal
- Produce a correct, polished spreadsheet artifact quickly that completes the user's request.
- You are judged on layout, readability, style, and correctness.

# Tools + Contract
- Use python library `artifact_tool` workbook APIs only for workbook edits only with PYTHON TOOL.
- After reading this file, you MUST read the whole `artifact_tool` API that is listed here: `./API_QUICK_START.md`
- Do not use `openpyxl`, `pandas`, or alternate spreadsheet libraries.
- Read inputs from `/mnt/data`; write outputs to `/mnt/data`.
- Export final workbook as `.xlsx` unless user asks otherwise.

## Required Imports + Startup
Assume `artifact_tool` exists and is installed. Do not run environment/package discovery (`pkgutil`, module scans, install checks) unless the import throws an error.

Import existing workbook only when needed (user-uploaded/edit-in-place or intentional reload):
```python
from artifact_tool import Blob, SpreadsheetFile
wb = SpreadsheetFile.import_xlsx(Blob.load("/mnt/data/input.xlsx"))
```

Create new workbook:
```python
from artifact_tool import Workbook, SpreadsheetFile
wb = Workbook.create()
sheet = wb.worksheets.add("Inputs")
```

## Continuous Notebook Strategy
- Use one continuous notebook state.
- Reuse in-memory `wb` across Python calls.
- Keep calls focused; split into small coherent steps.
- Avoid repeated import/export/render loops unless runtime reset forces it.
- Do not re-import from disk between every patch step.

# Latency Guardrails (High Priority)
- Start meaningful edits quickly; avoid long upfront API exploration.
- Core APIs are listed in `./API_QUICK_START.md`. You must use that.
- Keep tool-call count low while preserving quality.
- Use `workbook.help(...)` only when blocked or for features or fields that are undocumented; keep discovery minimal.
- Avoid very large monolithic calls and avoid full workbook rewrites unless first version is invalid.
- Default flow:
  - one primary build call
  - minimal focused patch call(s)
  - at least one compact verification
  - one final export call
- Stop when requirements are met. Do not create alternate variants after valid final output.
- Keep verification targeted and efficient (max 3 iterations).

## Fast Path (Default)
1. Setup: import artifact_tool, create workbook/sheets for new files.
2. Build quickly: bulk-write headers/data/formulas; then formatting/validation/conditional formatting; add charts/tables only when needed.
3. Use additional focused calls if helpful for streamed progress.
4. Near completion: inspect key ranges, scan formula errors, optional small render preview, export `.xlsx`.

# Error Recovery
On first error:
1. Read error text.
2. Run one targeted `workbook.help("<exact_api>")` query only if needed.
3. Retry with minimal patch (not full rewrite).
4. Continue from existing workbook state.

Do not loop indefinitely on similar failures.

# Quality Floor (Do Not Skip)
Speed matters, but output quality must meet baseline.

- Keep layout readable and bounded, contents visible:
  - avoid extreme width/height from unconstrained autofit
  - cap oversized widths/heights after `autofit` + `wrap_text`
- Prefer formula-driven logic over manual painted cells when logic is expected.
- Derived values must be formulas (not hardcoded) and legible.
- Use absolute/relative references correctly for fill/copy behavior.
- Do not use magic numbers in formulas; reference cells (e.g. `=H6*(1+$B$3)`).
- Include at least one visual summary for tracker/planning requests when appropriate (KPI block, chart, dashboard area).
- If writing literal text that starts with `=`, prefix with single quote (`'=high-low`).
- Keep workbook structurally valid (e.g., unique table names).

## Formatting Baseline
- If editing an uploaded/template workbook: render first, preserve and match existing style unless user asks to restyle.
- Typical defaults when unspecified:
  - content columns: ~10-24
  - text-heavy columns: cap ~32-40
  - row heights: ~15-20 (titles may be larger)
  - avoid oversized body fonts (>12pt) except intentional titles
- Add whitespace between sections where useful.
- Use fill colors, borders, and merged cells judiciously to give the spreadsheet a professional visual style with a clear layout without overdoing it
- Add data validation for editable categorical columns (`Status`, `Priority`, `Owner`) where feasible.
- Use conditional formatting when useful.
- Unless conflicting style guidelines are provided: style headers, correct number/date formats, sensible column widths, and row heights, light borders.

# Citation Requirements
## Cite sources inside the spreadsheet
- Use plain-text URLs in spreadsheet cells.
- For financial models, cite model-input sources in cell comments.
- For researched row-wise data tables, include source URLs in a dedicated source column.

# Completion Criteria
Complete only when:
- Workbook content is populated and formulas compute.
- No obvious formula errors in key scanned ranges (no bad refs/off-by-one/circular errors).
- `.xlsx` saved to `/mnt/data`.
- Layout is organized, legible, and aligned to request style (or default formatting baseline).
- Final response includes output path + short summary of sheets/ranges created. Do not include rendered preview unless requested.

# Verification Rules
Before final response, verify values/formulas and visual quality.

1. Inspect key ranges:
```python
check = wb.inspect({
  "kind": "table",
  "range": "Dashboard!A1:H20",
  "include": "values,formulas",
  "table_max_rows": 20,
  "table_max_cols": 12,
})
print(check.ndjson)
```

Inspect targeting:
- Prefer sheet-qualified ranges (`"Sheet!A1:H20"`) or `sheet_id`.

2. Scan formula errors:
```python
errors = wb.inspect({
  "kind": "match",
  "search_term": "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  "options": {"use_regex": True, "max_results": 300},
  "summary": "final formula error scan",
})
print(errors.ndjson)
```

3. Render sheets/ranges to verify visual output (skip if already verified and no style changes):
```python
blob = wb.render({"sheet_name": "Sheet1", "range": "A1:H20", "scale": 2})
```
If render is last line in Python call, image can be shown directly.

4. Keep verification compact:
- Inspect only key ranges.
- Avoid huge NDJSON dumps.

5. Export:
```python
SpreadsheetFile.export_xlsx(wb).save("/mnt/data/output.xlsx")
```

6. Finalize immediately after successful export + compact verification.
- Do not export extra `.xlsx` variants.
- Do not keep iterating on alternate designs once requirements are met.

# Additional Instructions
Only when a request relates to any of the following, read the following templates instructions as well:
- Financial modeling or investment banking: `templates/financial_models.md`
````

Inspecting CSV files and displaying contents


```
import csv, json, os, textwrap, itertools, re, math, statistics
paths = {
    'university_master': '/mnt/data/university_master.csv',
    'crm': '/mnt/data/crm.csv',
    'collections': '/mnt/data/collections.csv',
    'origination': '/mnt/data/origination.csv',
}
for name,path in paths.items():
    print(name, os.path.getsize(path))
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader=csv.DictReader(f)
        print(reader.fieldnames)
        rows=list(reader)
        print("rows", len(rows))
        for r in rows[:5]:
            print(r)
        print()
```


```
university_master 766
['code', 'name']
rows 25
{'code': '4471', 'name': 'University of Texas at Austin'}
{'code': '9920', 'name': 'Univ. of Texas Austin'}
{'code': '8810', 'name': 'National University of Singapore'}
{'code': '8811', 'name': 'NUS'}
{'code': '3305', 'name': 'Indian Institute of Technology Madras'}

crm 14494
['contact_id', 'display_name', 'whatsapp_number', 'last_interaction', 'note', 'channel']
rows 170
{'contact_id': 'CRM-55021', 'display_name': 'A.K. Gupta', 'whatsapp_number': '+91-98xxxx2210', 'last_interaction': '2026-05-30', 'note': 'frustrated re: disbursal delay', 'channel': 'WhatsApp'}
{'contact_id': 'CRM-55022', 'display_name': 'Rahul M', 'whatsapp_number': '+91-97xxxx4471', 'last_interaction': '2026-06-01', 'note': 'asked about top-up loan', 'channel': 'WhatsApp'}
{'contact_id': 'CRM-60006', 'display_name': 'A. Das', 'whatsapp_number': '+91-81xxxx9516', 'last_interaction': '2026-05-10', 'note': 'frustrated re: disbursal delay', 'channel': 'Email'}
{'contact_id': 'CRM-60045', 'display_name': 'G. Kapoor', 'whatsapp_number': '+91-94xxxx5277', 'last_interaction': '2026-05-05', 'note': 'asked for foreclosure statement', 'channel': 'Phone'}
{'contact_id': 'CRM-60050', 'display_name': 'Karan C', 'whatsapp_number': '+91-83xxxx5779', 'last_interaction': '2026-05-09', 'note': 'requested repayment schedule', 'channel': 'WhatsApp'}

collections 9581
['account_no', 'name', 'phone', 'days_past_due', 'outstanding', 'masked_pan']
rows 160
{'account_no': 'AC-2024-1001', 'name': 'Amit K. Gupta', 'phone': '+91-98xxxx2210', 'days_past_due': '45', 'outstanding': '412000', 'masked_pan': 'XXXXX1234F'}
{'account_no': 'AC-2024-1002', 'name': 'A. Gupta', 'phone': '+91-98xxxx9921', 'days_past_due': '0', 'outstanding': '0', 'masked_pan': 'XXXXX5678K'}
{'account_no': 'AC-2024-1003', 'name': 'Priya Sharma', 'phone': '+91-99xxxx1180', 'days_past_due': '12', 'outstanding': '88000', 'masked_pan': 'XXXXX5511C'}
{'account_no': 'AC-2024-2148', 'name': 'Anjali G', 'phone': '+91-99xxxx7256', 'days_past_due': '1', 'outstanding': '656000', 'masked_pan': 'XXXXX5549S'}
{'account_no': 'AC-2024-2024', 'name': 'Aisha K', 'phone': '+91-97xxxx6248', 'days_past_due': '45', 'outstanding': '578000', 'masked_pan': 'XXXXX7310Y'}

origination 16684
['cust_id', 'full_name', 'dob', 'masked_pan', 'email', 'phone', 'loan_amount', 'univ_code']
rows 170
{'cust_id': 'ORIG-00471', 'full_name': 'Amit Kumar Gupta', 'dob': '1998-03-14', 'masked_pan': 'XXXXX1234F', 'email': 'amit.gupta@gmail.com', 'phone': '+91-98xxxx2210', 'loan_amount': '1850000', 'univ_code': '4471'}
{'cust_id': 'ORIG-00472', 'full_name': 'Priya Sharma', 'dob': '1999-07-02', 'masked_pan': 'XXXXX5511C', 'email': 'priyas99@gmail.com', 'phone': '+91-99xxxx1180', 'loan_amount': '2200000', 'univ_code': '8810'}
{'cust_id': 'ORIG-00473', 'full_name': 'Rahul Mehta', 'dob': '1997-11-20', 'masked_pan': '', 'email': '', 'phone': '+91-97xxxx4471', 'loan_amount': '1500000', 'univ_code': '4471'}
{'cust_id': 'ORIG-01145', 'full_name': 'Arun Srinivasan', 'dob': '1996-05-14', 'masked_pan': 'XXXXX9189Q', 'email': 'arun.srinivasan96@proton.me', 'phone': '', 'loan_amount': '2700000', 'univ_code': '8811'}
{'cust_id': 'ORIG-01018', 'full_name': 'Nikhil P Jain', 'dob': '1989-04-12', 'masked_pan': 'XXXXX3493R', 'email': 'nikhiljain@gmail.com', 'phone': '+91-75xxxx1956', 'loan_amount': '3100000', 'univ_code': '6390'}
```

Reconciling customer records

I need to figure out how to identify duplicates across multiple systems, especially by comparing strong identifiers like phone, PAN, email, and DOB, while handling issues with masked data.

Building robust contact matching and equivalence classes


```
# Build records
records=[]
for r in data['origination']:
    records.append({'src':'origination','rec_id':r['cust_id'],'name':r['full_name'],'phone':r['phone'],'pan':r['masked_pan'],'email':r['email'],'dob':r['dob'],'raw':r})
for r in data['collections']:
    records.append({'src':'collections','rec_id':r['account_no'],'name':r['name'],'phone':r['phone'],'pan':r['masked_pan'],'email':'','dob':'','raw':r})
for r in data['crm']:
    records.append({'src':'crm','rec_id':r['contact_id'],'name':r['display_name'],'phone':r['whatsapp_number'],'pan':'','email':'','dob':'','raw':r})
len(records)
```


```
500
```

Designing customer clusters

I'm establishing a confidence score matrix to assess duplicate and cross-system records, where only matched strong IDs (like phone or PAN) and not just names should merge. Sure, scores under 0.8 need human review.

Identifying exact ID candidate matches


```
def norm_tokens(s):
    return tokens(s)

COMMON_SURNAME_TOKENS=set(['kumar','dev','suresh','prakash','mohan'])  # maybe not surname; no harm?
# maybe not

def name_level(a,b):
    ta=norm_tokens(a); tb=norm_tokens(b)
    if not ta or not tb:
        return 'missing'
    na=' '.join(ta); nb=' '.join(tb)
    if na==nb:
        return 'exact'
    # remove single-letter tokens? compare non-initial tokens
    longa=[t for t in ta if len(t)>1]
    longb=[t for t in tb if len(t)>1]
    # exact long token sequence subset, e.g. "amit k gupta" vs "amit kumar gupta": first and last same
    if len(longa)>=2 and len(longb)>=2:
        if longa
```


```
Amit Kumar Gupta A.K. Gupta strong 0.72
Rahul Mehta Rahul M moderate 0.7777777777777778
A. Das Amit Das strong 0.7692307692307693
Aisha K Anjali G conflict 0.4
Priya Sharma P.M. Sharma moderate 0.7272727272727273
Anjali Prakash Gupta Anjali G moderate 0.5714285714285714
Anjali Prakash Gupta A. Gupta strong 0.5185185185185185
Priya Mohan Sharma P.S. Sharma moderate 0.6428571428571429
Arjun R A.D. Rao conflict 0.42857142857142855
Chirag S C.M. Shetty conflict 0.3333333333333333
Tanvi Agarwal T.S. Agarwal moderate 0.75
Maya Raj Khan Maya K moderate 0.631578947368421
```

Worked for 6m 32s

Done

</details>

Inspected CSV files, evaluated matching rules, and identified duplicatesReconciled customer records

I found the likely reliable join fields: masked phone numbers and masked PANs. Names are inconsistent and sometimes duplicated, so I’m using names only as supporting evidence, not as a merge key.

Built contact matching system and identified duplicate recordsDesigned customer clusters

</details>

Done. Full output is here:

customer_master_reconciliation.xlsx

SummaryCustomer_MasterAccepted_MatchesHuman_ReviewUniversity_ReconExceptions_FixesMethodology

The workbook contains:

| Sheet | Contents |
| --- | --- |
| Summary | Counts and high-level result |
| Customer_Master | 201 reconciled customer entities with confidence, matched fields, reasons, and review flags |
| Accepted_Matches | 691 accepted direct record-pair matches |
| Human_Review | 82 below-0.8 direct candidates flagged for review |
| University_Recon | University code normalization and duplicate-code status |
| Exceptions_Fixes | Exceptions and suggested master-data fixes |
| Methodology | Matching rules used |

Key result: 500 source records reconciled into 201 customer entities. I used exact masked phone, exact masked PAN, or exact email as join evidence. Name similarity was used only as supporting evidence; there were zero name-only merges.

Sample reconciliation rows:

| Customer | Source IDs | Confidence | Matched on | Reason |
| --- | --- | --- | --- | --- |
| Amit Kumar Gupta | ORIG-00471; ORIG-01164 / AC-2024-1001 / CRM-55021; CRM-60093; CRM-60157 | 0.99 | masked_pan=XXXXX1234F; phone=+91-98xxxx2210 | PAN and phone agree; name variants are compatible aliases. |
| Priya Sharma | ORIG-00472 / AC-2024-1003 | 0.99 | masked_pan=XXXXX5511C; phone=+91-99xxxx1180 | PAN and phone agree across origination and collections. |
| Rahul Mehta | ORIG-00473 / CRM-55022; CRM-60064; CRM-60097; CRM-60152 | 0.90 | phone=+91-97xxxx4471 | Phone matches; names support but do not drive the merge. |
| Aisha V Krishnan | ORIG-01044 / 4 collections accounts / 5 CRM contacts | 0.90 | phone=+91-97xxxx6248 | Shared phone with compatible alias variants. |
| Arun V Srinivasan | ORIG-01103; ORIG-01145 | 0.99 | email + masked_pan | Duplicate origination records backed by two identifiers. |

University codes that are the same institution under two IDs:

| Codes | Same institution | Suggested primary code | Origination usage |
| --- | --- | --- | --- |
| 4471; 9920 | University of Texas at Austin / Univ. of Texas Austin | 4471 | 31 |
| 8810; 8811 | National University of Singapore / NUS | 8810 | 29 |
| 3305; 3306 | Indian Institute of Technology Madras / IIT Madras | 3305 | 23 |
| 1201; 1210 | Indian Institute of Science / IISc Bangalore | 1201 | 20 |
| 7702; 7703 | Stanford University / Stanford Univ. | 7702 | 9 |

Main exceptions and fixes:

| Exception | Suggested fix |
| --- | --- |
| 82 direct candidates below 0.8 | Keep in manual review; confirm with full phone/PAN or another deterministic ID before merging. |
| Missing identifiers: 76 fields missing across source records | Make at least one stable customer identifier mandatory per source record. |
| 5 duplicate university-code groups | Create a canonical institution ID and alias table; redirect legacy codes. |
| Multiple source IDs for one customer | Maintain a crosswalk from master customer ID to source IDs. |
| Similar-name-only candidates found but blocked | Continue blocking name-only merges; require DOB, full phone/PAN hash, or verified email. |
| Masked identifiers are collision-prone | Store privacy-safe irreversible hashes of full identifiers for future matching. |

---
