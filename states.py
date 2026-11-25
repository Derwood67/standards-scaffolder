"""Every U.S. state and DC, grouped by how their K-6 math and ELA standards relate to the data in this app.

group:
  "full"        own codes, pacing and examples in gen_data (NC, MI, TX)
  "ccss"        adopted the Common Core State Standards as written; CCSS codes apply directly
  "ccss-based"  standards built on CCSS with state revisions; CCSS codes shown as the closest match
  "own"         state-written standards with their own numbering; skills are mapped by content only

Non-"full" states borrow Michigan's CCSS codes, representative CCSS pacing and CCSS-style
items ("same_as": "MI"). Test names are listed only where well established; otherwise a
generic note is used. Confirm everything against the state's current documents.
"""

CCSS_SRC = ["Common Core State Standards (official site)", "https://www.thecorestandards.org/"]

CCSS = {
 "CA": ("California", "California Common Core State Standards", "CAASPP (Smarter Balanced), spring"),
 "CT": ("Connecticut", "Connecticut Core Standards (CCSS)", "Smarter Balanced, spring"),
 "DE": ("Delaware", "Common Core State Standards", "Smarter Balanced (DeSSA), spring"),
 "DC": ("District of Columbia", "Common Core State Standards", None),
 "HI": ("Hawaii", "Hawaii Common Core Standards", "Smarter Balanced, spring"),
 "IL": ("Illinois", "Illinois Learning Standards (CCSS)", None),
 "MD": ("Maryland", "Maryland College and Career Ready Standards (CCSS)", "MCAP, spring"),
 "NV": ("Nevada", "Nevada Academic Content Standards (CCSS)", "Smarter Balanced, spring"),
 "NM": ("New Mexico", "Common Core State Standards", None),
 "RI": ("Rhode Island", "Common Core State Standards", "RICAS, spring"),
 "VT": ("Vermont", "Common Core State Standards", "Smarter Balanced, spring"),
 "WA": ("Washington", "Washington K-12 Learning Standards (CCSS)", "Smarter Balanced, spring"),
}

BASED = {
 "AK": "Alaska", "AR": "Arkansas", "AZ": "Arizona", "CO": "Colorado", "IA": "Iowa", "ID": "Idaho",
 "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "MA": "Massachusetts", "ME": "Maine",
 "MO": "Missouri", "MS": "Mississippi", "MT": "Montana", "ND": "North Dakota", "NH": "New Hampshire",
 "NJ": "New Jersey", "NY": "New York", "OH": "Ohio", "OR": "Oregon", "PA": "Pennsylvania",
 "SD": "South Dakota", "TN": "Tennessee", "UT": "Utah", "WI": "Wisconsin", "WV": "West Virginia", "WY": "Wyoming",
}
BASED_TEST = {"MA": "MCAS, spring", "NY": "NYS Grades 3-8 tests, spring", "OH": "Ohio's State Tests, spring",
              "PA": "PSSA, spring", "TN": "TCAP, spring", "OR": "Smarter Balanced, spring", "ID": "ISAT (Smarter Balanced), spring",
              "SD": "Smarter Balanced, spring"}

OWN = {
 "FL": ("Florida", "Florida B.E.S.T. Standards", "FAST, three windows a year", "https://www.fldoe.org/academics/standards/"),
 "VA": ("Virginia", "Virginia Standards of Learning (SOL)", "SOL tests, spring", "https://www.doe.virginia.gov/"),
 "GA": ("Georgia", "Georgia's K-12 Mathematics Standards and Georgia ELA Standards", "Georgia Milestones, spring", "https://gadoe.org/"),
 "OK": ("Oklahoma", "Oklahoma Academic Standards", "OSTP, spring", "https://oklahoma.gov/education.html"),
 "IN": ("Indiana", "Indiana Academic Standards", "ILEARN, spring", "https://www.in.gov/doe/"),
 "SC": ("South Carolina", "South Carolina College- and Career-Ready Standards", "SC READY, spring", "https://ed.sc.gov/"),
 "AL": ("Alabama", "Alabama Course of Study", "ACAP, spring", "https://www.alabamaachieves.org/"),
 "NE": ("Nebraska", "Nebraska College and Career Ready Standards", "NSCAS, spring", "https://www.education.ne.gov/"),
 "MN": ("Minnesota", "Minnesota K-12 Academic Standards", "MCA, spring", "https://education.mn.gov/"),
}

GENERIC_TEST = "State tests begin in grade 3; check the state education agency for the current name and window"
PACE = "Pacing is set by districts. The sequence shown is a representative CCSS curriculum order, the same one used for Michigan."


def build():
    out = {}
    for k, (name, fw, test) in CCSS.items():
        out[k] = dict(name=name, framework=fw, group="ccss", same_as="MI", test=test or GENERIC_TEST,
                      pacing_authority=PACE, sources=[CCSS_SRC],
                      code_note="This state adopted the Common Core, so these CCSS codes apply directly.")
    for k, name in BASED.items():
        out[k] = dict(name=name, framework=f"{name} standards, built on the Common Core with state revisions", group="ccss-based", same_as="MI",
                      test=BASED_TEST.get(k, GENERIC_TEST), pacing_authority=PACE, sources=[CCSS_SRC],
                      code_note=f"{name}'s standards are based on the Common Core but revised. Codes shown are the CCSS match; your state's wording or numbering may differ.")
    for k, (name, fw, test, url) in OWN.items():
        out[k] = dict(name=name, framework=fw, group="own", same_as="MI", test=test,
                      pacing_authority=PACE + f" {name} writes its own standards, so its order may differ more.",
                      sources=[[f"{name} state education agency", url], CCSS_SRC],
                      code_note=f"{name} uses its own standards and numbering. State codes are not mapped yet; the skill matches the CCSS codes shown.")
    return out
