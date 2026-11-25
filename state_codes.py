"""State-specific codes for states that write their own standards.

CODES[ST][concept_id] = [codes]. A concept missing from the map falls back to the
Common Core match in the app (labeled as such). An empty list means the state has
no matching benchmark at that grade.
VERIFY[ST] = concept ids whose codes still need a line-by-line check against the
final state document (shown as "Codes not yet verified").

Florida math K-6: read from FLDOE B.E.S.T. Mathematics documents (grades 5-6 also from a grade-level benchmark list).
Florida ELA: benchmark pattern from the FLDOE B.E.S.T. ELA standards document; only the
Foundations strand was read word for word, so the rest is flagged for checking.
Evidence maps to ELA.K12.EE.1.1, Florida's K-12 expectation for citing evidence.
Virginia math: 2023 Mathematics SOL (VDOE documents, including August 2023 working drafts), flagged.
Virginia ELA: 2024 English SOL, kindergarten, grade 1 and grade 4 only so far, flagged.
"""

import re

E = lambda g, key: f"e{'k' if g == 0 else g}-{key}"

# ---------------- Florida ----------------
FL_MATH = {
 "mk-count": ["MA.K.NSO.1.1", "MA.K.NSO.1.2", "MA.K.NSO.2.1"],
 "mk-howmany": ["MA.K.NSO.1.1", "MA.K.NSO.1.2"],
 "mk-compare": ["MA.K.NSO.1.4", "MA.K.NSO.2.3"],
 "mk-addsub": ["MA.K.NSO.3.1", "MA.K.NSO.3.2", "MA.K.AR.1.3"],
 "mk-decompose": ["MA.K.AR.1.1", "MA.K.AR.1.2"],
 "mk-teens": ["MA.K.NSO.2.2"],
 "mk-measure": ["MA.K.M.1.1", "MA.K.M.1.2", "MA.K.M.1.3", "MA.K.DP.1.1"],
 "mk-shapes": ["MA.K.GR.1.1", "MA.K.GR.1.2", "MA.K.GR.1.3", "MA.K.GR.1.4", "MA.K.GR.1.5"],
 "mk-finlit": [],
 "m1-addsub20": ["MA.1.AR.1.2"],
 "m1-strategies": ["MA.1.NSO.2.1", "MA.1.AR.1.1"],
 "m1-equal": ["MA.1.AR.2.2"],
 "m1-count120": ["MA.1.NSO.1.1", "MA.1.NSO.1.2"],
 "m1-placevalue": ["MA.1.NSO.1.3", "MA.1.NSO.1.4"],
 "m1-add100": ["MA.1.NSO.2.3", "MA.1.NSO.2.4", "MA.1.NSO.2.5"],
 "m1-measure": ["MA.1.M.1.1", "MA.1.M.1.2", "MA.1.M.2.1"],
 "m1-data": ["MA.1.DP.1.1", "MA.1.DP.1.2"],
 "m1-shapes": ["MA.1.GR.1.1", "MA.1.GR.1.2", "MA.1.GR.1.3", "MA.1.GR.1.4", "MA.1.FR.1.1"],
 "m1-money": ["MA.1.M.2.2", "MA.1.M.2.3"],
 "m2-addsub": ["MA.2.NSO.2.1", "MA.2.AR.1.1"],
 "m2-groups": ["MA.2.AR.3.1", "MA.2.AR.3.2"],
 "m2-place": ["MA.2.NSO.1.1", "MA.2.NSO.1.2", "MA.2.NSO.1.3"],
 "m2-addsub1000": ["MA.2.NSO.2.2", "MA.2.NSO.2.3", "MA.2.NSO.2.4"],
 "m2-length": ["MA.2.M.1.1", "MA.2.M.1.2", "MA.2.M.1.3"],
 "m2-timemoney": ["MA.2.M.2.1", "MA.2.M.2.2"],
 "m2-data": ["MA.2.DP.1.1", "MA.2.DP.1.2"],
 "m2-shapes": ["MA.2.GR.1.1", "MA.2.GR.1.2"],
 "m2-fractions": ["MA.2.FR.1.1", "MA.2.FR.1.2"],
 "m2-finlit": [],
 "m3-mult": ["MA.3.NSO.2.2", "MA.3.NSO.2.4", "MA.3.AR.2.1"],
 "m3-facts": ["MA.3.AR.1.1", "MA.3.NSO.2.4"],
 "m3-twostep": ["MA.3.AR.1.2", "MA.3.AR.3.3"],
 "m3-place": ["MA.3.NSO.1.1", "MA.3.NSO.1.2", "MA.3.NSO.1.3", "MA.3.NSO.1.4", "MA.3.NSO.2.1"],
 "m3-fracunit": ["MA.3.FR.1.1", "MA.3.FR.1.2", "MA.3.FR.1.3"],
 "m3-fraceq": ["MA.3.FR.2.1", "MA.3.FR.2.2"],
 "m3-area": ["MA.3.GR.2.1", "MA.3.GR.2.2", "MA.3.GR.2.3", "MA.3.GR.2.4"],
 "m3-perim": ["MA.3.GR.2.3", "MA.3.GR.2.4"],
 "m3-measure": ["MA.3.M.1.1", "MA.3.M.1.2", "MA.3.M.2.1", "MA.3.M.2.2"],
 "m3-data": ["MA.3.DP.1.1", "MA.3.DP.1.2"],
 "m3-shapes": ["MA.3.GR.1.1", "MA.3.GR.1.2", "MA.3.GR.1.3"],
 "m3-finlit": [],
 "m4-place": ["MA.4.NSO.1.1", "MA.4.NSO.1.2", "MA.4.NSO.1.3", "MA.4.NSO.1.4"],
 "m4-mult": ["MA.4.NSO.2.2", "MA.4.NSO.2.3", "MA.4.AR.1.1"],
 "m4-div": ["MA.4.NSO.2.4", "MA.4.AR.1.1"],
 "m4-factors": ["MA.4.AR.3.1", "MA.4.AR.3.2"],
 "m4-fraceq": ["MA.4.FR.1.1", "MA.4.FR.1.3", "MA.4.FR.1.4"],
 "m4-fracops": ["MA.4.FR.2.2", "MA.4.FR.2.3", "MA.4.FR.2.4", "MA.4.AR.1.2", "MA.4.AR.1.3"],
 "m4-decimals": ["MA.4.NSO.1.5", "MA.4.FR.1.2", "MA.4.NSO.2.6", "MA.4.NSO.2.7"],
 "m4-measure": ["MA.4.M.1.1", "MA.4.M.1.2"],
 "m4-angles": ["MA.4.GR.1.1", "MA.4.GR.1.2", "MA.4.GR.1.3"],
 "m4-data": ["MA.4.DP.1.1", "MA.4.DP.1.2", "MA.4.DP.1.3"],
 "m4-finlit": [],
 "m5-place": ["MA.5.NSO.1.1", "MA.5.NSO.1.2", "MA.5.NSO.1.3", "MA.5.NSO.1.4", "MA.5.NSO.1.5"],
 "m5-multdiv": ["MA.5.NSO.2.1", "MA.5.NSO.2.2"],
 "m5-decops": ["MA.5.NSO.2.3", "MA.5.NSO.2.4", "MA.5.NSO.2.5"],
 "m5-fracaddsub": ["MA.5.FR.2.1"],
 "m5-fracmult": ["MA.5.FR.1.1", "MA.5.FR.2.2", "MA.5.FR.2.3"],
 "m5-fracdiv": ["MA.5.FR.2.4", "MA.5.AR.1.3"],
 "m5-expr": ["MA.5.AR.2.1", "MA.5.AR.2.2", "MA.5.AR.2.3", "MA.5.AR.2.4", "MA.5.AR.3.1", "MA.5.AR.3.2"],
 "m5-coord": ["MA.5.GR.4.1", "MA.5.GR.4.2"],
 "m5-volume": ["MA.5.GR.3.1", "MA.5.GR.3.2", "MA.5.GR.3.3"],
 "m5-shapes": ["MA.5.GR.1.1", "MA.5.GR.1.2"],
 "m5-measure-data": ["MA.5.M.1.1", "MA.5.M.2.1", "MA.5.DP.1.1", "MA.5.DP.1.2"],
 "m5-finlit": [],
 "m6-ratios": ["MA.6.AR.3.1", "MA.6.AR.3.2", "MA.6.AR.3.3", "MA.6.AR.3.4", "MA.6.AR.3.5"],
 "m6-percent": ["MA.6.AR.3.4", "MA.6.AR.3.5", "MA.6.NSO.3.5"],
 "m6-fracdiv": ["MA.6.NSO.2.2"],
 "m6-numsys": ["MA.6.NSO.2.1", "MA.6.NSO.3.1"],
 "m6-integers": ["MA.6.NSO.1.1", "MA.6.NSO.1.2", "MA.6.NSO.1.3", "MA.6.NSO.1.4", "MA.6.NSO.4.1", "MA.6.NSO.4.2", "MA.6.GR.1.1", "MA.6.GR.1.2"],
 "m6-expressions": ["MA.6.AR.1.1", "MA.6.AR.1.3", "MA.6.AR.1.4", "MA.6.NSO.3.3"],
 "m6-equations": ["MA.6.AR.1.2", "MA.6.AR.2.1", "MA.6.AR.2.2", "MA.6.AR.2.3", "MA.6.AR.2.4"],
 "m6-geometry": ["MA.6.GR.2.1", "MA.6.GR.2.2", "MA.6.GR.2.3", "MA.6.GR.2.4"],
 "m6-stats": ["MA.6.DP.1.1", "MA.6.DP.1.2", "MA.6.DP.1.3", "MA.6.DP.1.4", "MA.6.DP.1.5", "MA.6.DP.1.6"],
 "m6-finlit": [],
}

FL_ELA_PAT = {
 "evidence": lambda g: ["ELA.K12.EE.1.1"],
 "theme": lambda g: ([f"ELA.{g}.R.1.2"] if g != "K" else []) + [f"ELA.{g}.R.3.2"],
 "character": lambda g: [f"ELA.{g}.R.1.1"],
 "mainidea": lambda g: [f"ELA.{g}.R.2.2"],
 "structure": lambda g: [f"ELA.{g}.R.2.1"],
 "vocab": lambda g: [f"ELA.{g}.V.1.1", f"ELA.{g}.V.1.2", f"ELA.{g}.V.1.3"],
 "figlang": lambda g: [f"ELA.{g}.R.3.1"],
 "genre": lambda g: ([f"ELA.{g}.R.1.3"] if g != "K" else []) + [f"ELA.{g}.R.1.4"],
 "compare": lambda g: [f"ELA.{g}.R.3.3"],
 "opinion": lambda g: [f"ELA.{g}.C.1.3", f"ELA.{g}.R.2.4"],
 "informative": lambda g: [f"ELA.{g}.C.1.4"],
 "narrative": lambda g: [f"ELA.{g}.C.1.2"],
 "process": lambda g: [f"ELA.{g}.C.1.5", f"ELA.{g}.C.3.1"],
 "research": lambda g: [f"ELA.{g}.C.4.1"],
}
FL_F = {0: ["ELA.K.F.1.1", "ELA.K.F.1.2", "ELA.K.F.1.3", "ELA.K.F.1.4"], 1: ["ELA.1.F.1.1", "ELA.1.F.1.2", "ELA.1.F.1.3", "ELA.1.F.1.4"]}
for _g in (2, 3, 4, 5):
    FL_F[_g] = [f"ELA.{_g}.F.1.3", f"ELA.{_g}.F.1.4"]

FL = dict(FL_MATH)
FL_VERIFY = set()
for g in range(7):
    lab = "K" if g == 0 else str(g)
    for key, fn in FL_ELA_PAT.items():
        FL[E(g, key)] = fn(lab)
        if not (key == "character" and g >= 3):
            FL_VERIFY.add(E(g, key))
    if g <= 5:
        FL[E(g, "foundations")] = FL_F[g]

# ---------------- Virginia ----------------
VA_MATH = {
 "mk-count": ["K.NS.1", "K.NS.2"], "mk-howmany": ["K.NS.1", "K.NS.2"], "mk-compare": ["K.NS.2"],
 "mk-addsub": ["K.CE.1"], "mk-decompose": ["K.CE.1"], "mk-teens": ["K.NS.1"],
 "mk-measure": ["K.MG.1", "K.PS.1"], "mk-shapes": ["K.MG.2"],
 "m1-addsub20": ["1.CE.1"], "m1-strategies": ["1.CE.1"], "m1-equal": ["1.CE.1"], "m1-count120": ["1.NS.1"],
 "m1-placevalue": ["1.NS.1", "1.NS.2"], "m1-measure": ["1.MG.1", "1.MG.3"], "m1-data": ["1.PS.1"],
 "m1-shapes": ["1.MG.2", "1.NS.3"], "m1-money": ["1.NS.1"],
 "m2-addsub": ["2.CE.1"], "m2-groups": ["2.NS.1"], "m2-place": ["2.NS.2"], "m2-addsub1000": ["2.CE.1"],
 "m2-length": ["2.MG.1"], "m2-timemoney": ["2.MG.2", "2.NS.4"], "m2-data": ["2.PS.1"],
 "m2-shapes": ["2.MG.3", "2.MG.4"], "m2-fractions": ["2.NS.3"], "m2-finlit": ["2.NS.4"],
 "m3-mult": ["3.CE.2"], "m3-facts": ["3.CE.2"], "m3-twostep": ["3.CE.1", "3.PFA.1"], "m3-place": ["3.NS.1", "3.CE.1"],
 "m3-fracunit": ["3.NS.3"], "m3-fraceq": ["3.NS.3"], "m3-area": ["3.MG.2"], "m3-perim": ["3.MG.2"],
 "m3-measure": ["3.MG.1", "3.MG.3"], "m3-data": ["3.PS.1"], "m3-shapes": ["3.MG.4"], "m3-finlit": ["3.NS.4"],
 "m4-place": ["4.NS.1", "4.NS.2", "4.CE.1"], "m4-addsub": ["4.CE.1"], "m4-mult": ["4.CE.2"], "m4-div": ["4.CE.2"],
 "m4-factors": ["4.CE.2", "4.PFA.1"], "m4-fraceq": ["4.NS.3"], "m4-fracops": ["4.CE.3"],
 "m4-decimals": ["4.NS.4", "4.NS.5", "4.CE.4"], "m4-angles": ["4.MG.4"], "m4-measure": ["4.MG.1", "4.MG.2", "4.MG.3"], "m4-data": ["4.PS.1"],
 "m5-place": ["5.NS.1"], "m5-multdiv": ["5.CE.1"], "m5-decops": ["5.CE.3"], "m5-fracaddsub": ["5.CE.2"], "m5-fracmult": ["5.CE.2"],
 "m5-expr": ["5.CE.4", "5.NS.2", "5.PFA.1", "5.PFA.2"], "m5-volume": ["5.MG.2"], "m5-shapes": ["5.MG.3"],
 "m5-measure-data": ["5.MG.1", "5.PS.1", "5.PS.2"],
 "m6-percent": ["6.NS.1"], "m6-fracdiv": ["6.CE.1"], "m6-integers": ["6.NS.2"], "m6-expressions": ["6.NS.3", "6.CE.3"],
}
VA_ELA = {
 0: dict(evidence=["K.RL.1", "K.RI.1"], theme=["K.RL.1"], character=["K.RL.1"], mainidea=["K.RI.1"], structure=["K.RI.2"],
         vocab=["K.RV.1"], compare=["K.RL.3", "K.RI.3"], informative=["K.W.1"], narrative=["K.W.1"], opinion=["K.W.1"],
         process=["K.W.2", "K.LU.1", "K.LU.2"], research=["K.R.1"], foundations=["K.FFR.3", "K.DSR.1"]),
 1: dict(evidence=["1.RL.1", "1.RI.1"], theme=["1.RL.1"], character=["1.RL.1", "1.RL.3"], mainidea=["1.RI.1"], structure=["1.RI.2"],
         vocab=["1.RV.1"], figlang=["1.RV.1"], compare=["1.RL.3", "1.RI.3"], opinion=["1.W.1"], informative=["1.W.1"], narrative=["1.W.1"],
         process=["1.W.2", "1.W.3", "1.LU.1", "1.LU.2"], research=["1.R.1"], foundations=["1.FFR.3", "1.DSR"]),
 4: dict(evidence=["4.RL.1", "4.RI.1"], theme=["4.RL.1"], character=["4.RL.1", "4.RL.2", "4.RL.3"], mainidea=["4.RI.1"],
         structure=["4.RI.2", "4.RI.3"], vocab=["4.RV.1"], figlang=["4.RV.1"], genre=["4.RL.2"], compare=["4.RL.3", "4.RI.3"],
         opinion=["4.W.1"], informative=["4.W.1"], narrative=["4.W.1"], process=["4.W.2", "4.W.3", "4.LU.1", "4.LU.2"],
         research=["4.R.1"], foundations=["4.FFR.3", "4.DSR"]),
}
# Grades 2, 3, 5 and 6 follow the same strand numbering as grades 1 and 4 (pattern-filled, flagged like all VA ELA).
_sub = lambda m, g: {k: [f"{g}." + c.split(".", 1)[1] for c in v] for k, v in m.items()}
VA_ELA[2] = _sub(VA_ELA[1], 2)
VA_ELA[3] = _sub(VA_ELA[4], 3)
VA_ELA[5] = _sub(VA_ELA[4], 5)
VA_ELA[6] = {k: v for k, v in _sub(VA_ELA[4], 6).items() if k != "foundations"}
VA = dict(VA_MATH)
for g, m in VA_ELA.items():
    for key, codes in m.items():
        VA[E(g, key)] = codes

CODES = {"FL": FL, "VA": VA}
VERIFY = {"FL": FL_VERIFY, "VA": set(VA)}


def _load(st):
    """state_maps/ST.txt lines: 'concept-id: CODE, CODE' with a trailing ' ?' when the code needs a check."""
    import os
    codes, verify = {}, set()
    for line in open(os.path.join(os.path.dirname(__file__), "state_maps", st + ".txt")):
        if ":" not in line: continue
        cid, rest = (x.strip() for x in line.split(":", 1))
        if rest.endswith("?"): verify.add(cid); rest = rest[:-1].strip()
        if rest in ("", "-"): continue
        codes[cid] = [c.strip() for c in rest.split(",")]
    return codes, verify


for _st in ("GA", "OK", "IN", "SC", "AL", "NE", "MN"):
    CODES[_st], VERIFY[_st] = _load(_st)
    # ELA: state_maps/ST_ELA<g>.txt keyed by skill (evidence, theme, ...). Every ELA match is a judgment call, so all are flagged.
    import glob, os, re
    for _f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "state_maps", _st + "_ELA*.txt"))):
        _g = int(re.search(r"_ELA(\d)", _f).group(1))
        _m, _ = _load(os.path.basename(_f)[:-4])
        for _k, _v in _m.items():
            CODES[_st][E(_g, _k)] = _v
            VERIFY[_st].add(E(_g, _k))

NOTES = {
 "FL": dict(note="Florida B.E.S.T. benchmark codes are shown where they have been mapped. Scaffolds, items and pacing follow the Common Core version of the skill. Where a Florida code is not mapped yet, the Common Core match is shown instead.",
            sources=[["FLDOE B.E.S.T. Standards for Mathematics", "https://www.fldoe.org/academics/standards/subject-areas/math-science/mathematics"],
                     ["FLDOE B.E.S.T. ELA Standards (PDF)", "https://www.fldoe.org/core/fileparse.php/7539/urlt/elabeststandardsfinal.pdf"]]),
 "VA": dict(note="Virginia SOL codes (2023 Mathematics, 2024 English) are shown where they have been mapped. English codes for grades 2, 3, 5 and 6 follow the strand numbering of the grades read directly, so they are flagged for a check. Scaffolds, items and pacing follow the Common Core version of the skill. Where a Virginia code is not mapped yet, the Common Core match is shown instead.",
            sources=[["VDOE Standards of Learning for Mathematics", "https://doe.virginia.gov/teaching-learning-assessment/instruction/mathematics/standards-of-learning-for-mathematics"],
                     ["VDOE 2024 English Standards of Learning", "https://doe.virginia.gov/teaching-learning-assessment/k-12-standards-instruction/english-reading-literacy/standards-of-learning/2024-english-standards-of-learning"]]),
}

_ELA4 = " ELA codes are mapped for grade 4 only, and each is flagged because the skill match is a judgment call."
_TAIL = " Scaffolds, items and pacing follow the Common Core version of the skill. Where a code is not mapped yet, the Common Core match is shown instead."
NOTES.update({
 "GA": dict(note="Georgia K-12 Mathematics Standards (2023) codes are shown for kindergarten, grade 1 and grade 3. Other grades are not mapped yet." + _ELA4 + " ELA follows Georgia's K-12 ELA Standards (2025-26)." + _TAIL,
            sources=[["GaDOE Mathematics Curriculum Maps (2023, PDF)", "https://sparchives.gadoe.org/Curriculum-Instruction-and-Assessment/Curriculum-and-Instruction/Documents/Mathematics/Georgia-K12-Mathematics-Standards/Georgia-Mathematics-Curriculum-Maps/GA-Mathematics-Curriculum-Maps-2023.pdf"]]),
 "OK": dict(note="Oklahoma Academic Standards for Mathematics (2022) codes are shown. They were mapped from a standards index, not the OSDE document, so each one is flagged for a check." + _ELA4 + " ELA follows the 2021 Oklahoma Academic Standards for ELA." + _TAIL,
            sources=[["Oklahoma math standards index (Common Planner)", "https://www.commonplanner.com/standards/oklahoma-ece7c5b8/mathematics/grade-4-7b1e7d06"]]),
 "IN": dict(note="Indiana Academic Standards for Mathematics (2023) codes are shown, from IDOE correlation guides. Indiana's 2026 standards begin in 2027-28." + _ELA4 + _TAIL,
            sources=[["IDOE Mathematics standards", "https://secure.in.gov/doe/students/indiana-academic-standards/mathematics"],
                     ["IDOE Grade 3 Math 2023 IAS-CCSS correlation guide (PDF)", "https://in.gov/doe/files/Grade-3-Math-2023-IAS-CCSS-Correlation-Guide.pdf"]]),
 "SC": dict(note="2025 South Carolina College- and Career-Ready Mathematics Standards codes are shown. K-3 come from the SCDE document; grades 4-6 come from a standards index and are flagged for a check." + " ELA codes from the 2024 SC CCR ELA Standards are mapped for kindergarten through grade 2 and flagged; grades 3-6 are not mapped yet." + _TAIL,
            sources=[["SCDE 2025 SC CCR Mathematics Standards", "https://ed.sc.gov/instruction/standards/mathematics/standards/2025-south-carolina-college-and-career-ready-mathematics-standards/"]]),
 "AL": dict(note="Alabama Course of Study: Mathematics (2019) codes are shown for kindergarten. Other grades are not mapped yet." + _ELA4 + " ELA follows the 2021 Alabama Course of Study." + _TAIL,
            sources=[["2019 Alabama Course of Study: Mathematics (PDF)", "https://www.alabamaachieves.org/wp-content/uploads/2021/03/2019-Alabama-Mathematics-COS-Rev.-6-2021.pdf"]]),
 "NE": dict(note="Nebraska College and Career Ready Standards for Mathematics (2022) codes are shown." + " ELA codes are mapped for grade 4 reading literature only (theme, characters, genre), from an NSCAS item specification draft, and are flagged." + _TAIL,
            sources=[["Nebraska Mathematics Standards, adopted 2022 (PDF, district copy)", "https://www.dusters.org/wp-content/uploads/2022/12/6212NDE_Mathematics_Standards9-2-22_ADOPTED10-2022.pdf"]]),
 "MN": dict(note="Minnesota 2007 mathematics benchmark codes (adopted 2008) are shown for grades 1-6, from a standards index, so each is flagged. Minnesota's 2022 standards must be in place by 2027-28 and have no grade codes published yet." + _ELA4 + " ELA follows Minnesota's 2020 ELA standards." + _TAIL,
            sources=[["Minnesota math benchmarks index (Common Planner)", "https://www.commonplanner.com/standards/minnesota-1ff740cd/mathematics/grade-4-4429e683"],
                     ["Minn. R. 3501.0750 (2022 standards)", "https://www.revisor.mn.gov/rules/3501.0750/version/2025-09-03T14:20:17-05:00"]]),
})

_ELA_SRC = {
 "GA": ["Georgia K-12 ELA Standards, grade 4 (Common Planner index)", "https://www.commonplanner.com/standards/georgia-172f1305/english-language-arts/grade-4-db1c87e2"],
 "OK": ["Oklahoma ELA standards, grade 4 (Common Planner index)", "https://www.commonplanner.com/standards/oklahoma-ece7c5b8/english-language-arts/grade-4-6e302674"],
 "IN": ["IDOE 2023 IAS ELA correlation guide, grade 4 (PDF)", "https://www.in.gov/doe/files/2023-IAS-Correlation-Guide_-ELA-Grade-4.pdf"],
 "SC": ["SCDE 2024 SC CCR ELA Standards", "https://www.ed.sc.gov/instruction/standards/english-language-arts/standards/"],
 "AL": ["Alabama 2021 ELA Course of Study (ALSDE)", "https://alabamaachieves.org/acad-stand/cas_202353_2021-alabama-course-of-study-english-language-arts_v1-0"],
 "NE": ["NDE English Language Arts Standards", "https://www.education.ne.gov/ela/english-language-arts-standards/"],
 "MN": ["Minnesota ELA standards, grade 4 (Common Planner index)", "https://www.commonplanner.com/standards/minnesota-1ff740cd/english-language-arts/grade-4-323a83e6"],
}
for _st, _src in _ELA_SRC.items():
    NOTES[_st]["sources"].append(_src)
