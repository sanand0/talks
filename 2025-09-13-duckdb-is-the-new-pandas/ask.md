Answer with a single elegant, concise, readable DuckDB SQL.

DuckDB is loaded with these tables:

## judgements

Indian high courts judgements

- year: int
- court: 19_16
- bench: str High court ID
- title: case name
- description
- judge
- date_of_registration: str dd-mm-yyyy with errors (e.g. year 01-01-0012 instead of 01-01-2012)
- decision_date: date
- disposal_nature: str - DISMISSED, DISPOSED OF, ALLOWED, Disposed Off, BAIL GRANTED (various mis-spellings)
- pdf_link:
- raw_html

## elections

Indian elections data

- State: str, e.g.
- Constituency: str
- Party: str
- Candidate: str
- Votes: str but contains int
- State ID: str, e.g. S01
- Constituency ID: int

## pc

Indian parliamentary constituencies

- st_name: str, e.g. Himachal Pradesh
- pc_name: str, e.g. Kangra
- pc_category: str, e.g. GEN, SC, ST
- wikidata_qid: str, e.g. Q6362861
- geom: GEOMETRY

## districts

- DISTRICT: str, e.g Adilabad
- ST_NM: str, e.g. Andhra Pradesh
- geom: GEOMETRY
