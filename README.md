# Standards Scaffolder

A single-page app that scaffolds kindergarten to grade 6 math and ELA standards for all 50 states and DC, organized by representative pacing guides.

North Carolina, Michigan and Texas have their own codes, pacing and state-style items. Every other state is grouped by how its standards relate to the Common Core (`states.py`): Common Core states use CCSS codes directly, Common Core-based states show the closest CCSS code, and states with their own standards (such as Florida and Virginia) are matched by skill until their codes are added.

For each standard (concept) it shows the state codes, what it builds on and leads to, a scaffold ladder, a quick check, common misconceptions, supports, and state-style example items (NCDPI-, M-STEP- and STAAR-style). ELA items use original grade-level reading passages.

## Files

- `index.html`: the app. It loads `data.json` from the same folder.
- `data.json`: generated data. Don't edit by hand.
- `gen_data.py`: states, concepts, codes, prerequisites and pacing. Writes `data.json`.
- `examples.py`: example items for each concept and state.
- `passages.py`: original grade 3, 4 and 5 passages and the reading items that use them.
- `math_k2_6.py`: math concepts, example items and pacing for grades K, 1, 2 and 6.
- `ela_k2_6.py`: ELA grade focus, passages and items for grades K, 1, 2 and 6.
- `states.py`: every state and DC, grouped by how its standards relate to the Common Core.

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
- NC grade 4–5 codes were checked against NCDPI wording. NC codes for grades K–3 and 6, and Texas ELA codes for grades K–2 and 6, follow the state numbering pattern but are marked "not yet verified" in the app.
- K–2 example items are shared classroom checks, since state tests begin in grade 3.
- All example items and passages are original, not released test items.
