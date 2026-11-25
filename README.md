# Standards Scaffolder

A single-page app that scaffolds grades 3–5 math and ELA standards for North Carolina, Michigan and Texas, organized by representative pacing guides.

For each standard (concept) it shows the state codes, what it builds on and leads to, a scaffold ladder, a quick check, common misconceptions, supports, and state-style example items (NCDPI-, M-STEP- and STAAR-style). ELA items use original grade-level reading passages.

## Files

- `index.html`: the app. It loads `data.json` from the same folder.
- `data.json`: generated data. Don't edit by hand.
- `gen_data.py`: states, concepts, codes, prerequisites and pacing. Writes `data.json`.
- `examples.py`: example items for each concept and state.
- `passages.py`: original grade 3, 4 and 5 passages and the reading items that use them.

## Regenerate the data

```
python3 gen_data.py
```

## Run locally

```
python3 -m http.server
```

Then open http://localhost:8000.

## Notes

- None of NC, MI or TX mandates statewide pacing; it is set by districts. The sequences here are representative and cite their sources in the app.
- NC grade 4–5 codes were checked against NCDPI wording. NC grade 3 codes are not yet verified.
- All example items and passages are original, not released test items.
