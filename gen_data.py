"""Generates data.json for the Standards Scaffolder app.

Data model
- states: metadata + sources + pacing authority note. Add a state by adding an entry
  here, its codes on each concept, and its pacing sequences.
- concepts: one record per skill cluster per grade, shared by every state.
  codes[STATE] lists that state's standard codes for the cluster.
  prereqs: concept ids (clickable) or "G2: ..." text for skills below the covered grades.
  "Leads to" is computed in the app by reversing prereqs.
- pacing[STATE][subject][grade]: ordered units, each with weeks and concept ids.
"""
import json, os, re

STATES = {
    "NC": {
        "name": "North Carolina",
        "framework": "NC Standard Course of Study (Math 2017 K-8 and ELA 2017, the versions in effect for 2026-27)",
        "pacing_authority": "NCDPI sets standards; pacing is set by each district (LEA). The sequence here is a representative order drawn from published NC district pacing guides.",
        "sources": [
            ["NCDPI Standard Course of Study", "https://www.dpi.nc.gov/districts-schools/classroom-resources/office-teaching-and-learning/standard-course-study"],
            ["NC 4-5 Standards Planner (private Claude artifact; opens only for the owner)", "https://claude.ai/artifact/HNpqZp5qKuUZLHQ3ChhkCd"],
            ["Halifax County Schools, Grade 4 Math pacing guide (NE CARES 2023-24)", "https://www.halifax.k12.nc.us//cms/lib/NC02214542/Centricity/Domain/1022/4th%20Grade%20Math%202023%202024%20NE%20CARES%20Pacing%20Guide.pdf"],
        ],
        "test": "EOG (end of grade), late May",
        "planner": {"url": "https://claude.ai/artifact/HNpqZp5qKuUZLHQ3ChhkCd", "name": "NC 4-5 Standards Planner", "grades": [4, 5]},
    },
    "MI": {
        "name": "Michigan",
        "framework": "Michigan K-12 Standards (Common Core State Standards for Math and ELA)",
        "pacing_authority": "MDE adopts standards but publishes no state pacing guide; districts choose curricula. The sequence here follows the unit order of widely used CCSS-aligned curricula adopted by Michigan districts.",
        "sources": [
            ["MDE Academic Standards", "https://www.michigan.gov/mde/Services/academic-standards"],
            ["M-STEP Parent Guide, Grade 4 (MDE)", "https://www.michigan.gov/documents/mde/M-STEP_Parent_Guide_Grade_4_731396_7.pdf"],
        ],
        "test": "M-STEP, spring window (April-May)",
    },
    "TX": {
        "name": "Texas",
        "framework": "TEKS: Math 19 TAC Ch. 111 (2012), ELAR 19 TAC Ch. 110 (2017)",
        "pacing_authority": "TEA sets the TEKS but does not mandate pacing. Most districts use a Year at a Glance (often from the TEKS Resource System). The sequence here is a representative YAG order. Math TEKS revisions are under SBOE review, so check TEA for adopted changes.",
        "sources": [
            ["TEA: Texas Essential Knowledge and Skills", "https://tea.texas.gov/curriculum-and-instruction/texas-essential-knowledge-and-skills-teks"],
            ["19 TAC Chapter 111 (Mathematics)", "https://tea.texas.gov/laws-and-rules/texas-administrative-code/19-tac-chapter-111"],
            ["Brazos ISD, Grade 4 Math Year at a Glance 2023-24", "https://www.brazosisd.net/page/open/5205/0/4th%20Grade%20Math%20YAG%2023-24.pdf"],
        ],
        "test": "STAAR, April",
    },
}
for _k in STATES:
    STATES[_k]["group"] = "full"
from states import build as build_states
STATES.update(build_states())

C = []  # concepts


def m(id, grade, name, summary, NC, MI, TX, prereqs, steps, check, miscon, supports):
    C.append(dict(id=id, subject="math", grade=grade, name=name, summary=summary,
                  codes=dict(NC=NC, MI=MI, TX=TX), prereqs=prereqs, steps=steps,
                  check=check, misconception=miscon, supports=supports))

# ---------------- MATH GRADE 3 ----------------
m("m3-mult", 3, "Meaning of multiplication & division",
  "Interpret products as equal groups, arrays and area; interpret quotients as fair shares or as the number of groups.",
  ["NC.3.OA.1", "NC.3.OA.2", "NC.3.OA.3"], ["3.OA.A.1", "3.OA.A.2", "3.OA.A.3", "3.OA.A.4"], ["3.4D", "3.4E", "3.4K", "3.5B"],
  ["G2: Repeated addition with arrays up to 5 rows and 5 columns", "G2: Skip count by 2s, 5s, 10s and 100s"],
  ["Act out equal groups with counters and cups; say \"4 groups of 6\".",
   "Build arrays with tiles; write the matching repeated addition and multiplication sentence.",
   "Draw equal-group, array and strip diagrams for one-step word problems.",
   "Flip the question: show division as sharing (how many in each group) and as grouping (how many groups).",
   "Write and solve equations with the unknown in any position (4 × ? = 24)."],
  "Show 4 × 6 three ways (groups, array, number line) and write a story that matches it.",
  "Reading 4 × 6 as \"4 plus 6\", or seeing division only as sharing and missing the how-many-groups meaning.",
  "Sentence frame: \"___ groups of ___ is ___.\" Start with factors of 2, 5 and 10 before 6-9.")
m("m3-facts", 3, "Properties & fact fluency within 100",
  "Use commutative, associative and distributive properties and the multiplication-division relationship to know facts to 10 × 10.",
  ["NC.3.OA.5", "NC.3.OA.7"], ["3.OA.B.5", "3.OA.B.6", "3.OA.C.7"], ["3.4F", "3.4J", "3.5D"],
  ["m3-mult", "G2: Fluent addition and subtraction within 20"],
  ["Anchor facts: ×2, ×5, ×10 through skip counting and doubles.",
   "Rotate arrays to prove turnaround facts (3 × 8 = 8 × 3).",
   "Break apart arrays to derive harder facts: 7 × 8 = 5 × 8 + 2 × 8.",
   "Build fact families that link each multiplication fact to two division facts.",
   "Fluency practice with strategy talk (\"How did you get it?\") rather than speed alone."],
  "You know 5 × 7 = 35. Use it to find 6 × 7 and explain with a drawing.",
  "Applying the commutative property to division or subtraction (12 ÷ 3 = 3 ÷ 12).",
  "Fact strategy cards with array pictures; let students self-track which facts are known vs. derived.")
m("m3-twostep", 3, "Two-step problems & arithmetic patterns",
  "Solve two-step problems with all four operations, represent them with equations using a letter for the unknown, and check reasonableness.",
  ["NC.3.OA.8", "NC.3.OA.9"], ["3.OA.D.8", "3.OA.D.9"], ["3.5A", "3.5E", "3.4K"],
  ["m3-mult", "m3-place"],
  ["Retell the problem with no numbers: what is happening?",
   "Find the hidden first question that must be answered before the main one.",
   "Model both steps with a strip (bar) diagram.",
   "Write one equation with a letter for the unknown.",
   "Estimate first, then compare the answer to the estimate."],
  "A class has 4 packs of 8 markers and gives away 9. How many are left? Show the hidden question.",
  "Grabbing every number and adding them; skipping the first step.",
  "Read-draw-write routine; visual problem mats with two boxes for step 1 and step 2.")
m("m3-place", 3, "Place value, rounding & add/subtract within 1,000",
  "Round to the nearest 10 or 100 and add and subtract fluently within 1,000 using place-value strategies. Texas extends place value to 100,000.",
  ["NC.3.NBT.2", "NC.3.NBT.3"], ["3.NBT.A.1", "3.NBT.A.2", "3.NBT.A.3"], ["3.2A", "3.2B", "3.4A", "3.4B"],
  ["G2: Place value to 1,000 (hundreds, tens, ones)", "G2: Add and subtract within 1,000 using models"],
  ["Build numbers with base-ten blocks and trade 10 ones for 1 ten.",
   "Record on place-value charts and in expanded form.",
   "Round on a vertical number line: which ten or hundred is closer?",
   "Add and subtract with partial sums and open number lines.",
   "Connect each step of the standard algorithm to the blocks."],
  "Round 467 to the nearest ten and hundred, and show both on a number line.",
  "Rounding by changing digits without knowing which benchmark is closer; subtracting the smaller digit from the larger in every column.",
  "Keep blocks available during the algorithm; color-code place values.")
m("m3-fracunit", 3, "Unit fractions & fractions on a number line",
  "Understand 1/b as one of b equal parts, build fractions from unit fractions and place them on a number line.",
  ["NC.3.NF.1", "NC.3.NF.2"], ["3.NF.A.1", "3.NF.A.2"], ["3.3A", "3.3B", "3.3C", "3.3E"],
  ["G2: Partition circles and rectangles into halves, thirds and fourths", "G2: Whole numbers on a number line"],
  ["Fold paper strips into equal parts and name one part.",
   "Name the unit fraction: 1/b is one of b equal parts of the whole.",
   "Count unit fractions: 1/4, 2/4, 3/4, 4/4.",
   "Partition 0 to 1 on a number line and label each point.",
   "Extend past 1 and connect 4/4 to 1 whole."],
  "Mark 3/4 on a number line from 0 to 2 and explain how you found the spot.",
  "Believing a bigger denominator means a bigger piece; counting tick marks instead of spaces.",
  "Fraction strips taped above the number line so both models stay visible.")
m("m3-fraceq", 3, "Equivalent & comparing fractions",
  "Explain equivalence with models and compare fractions with the same numerator or the same denominator.",
  ["NC.3.NF.3", "NC.3.NF.4"], ["3.NF.A.3"], ["3.3F", "3.3G", "3.3H"],
  ["m3-fracunit"],
  ["Lay fraction strips side by side to find pieces that cover the same length.",
   "Show equivalent fractions at the same point on a number line.",
   "Write whole numbers as fractions (3 = 3/1, 1 = 4/4).",
   "Compare same-denominator fractions by counting pieces.",
   "Compare same-numerator fractions by reasoning about piece size."],
  "Which is greater, 2/3 or 2/6? Explain without drawing the same-size whole incorrectly.",
  "Comparing fractions whose wholes are different sizes.",
  "Always draw the wholes the same size; use the language \"same size pieces\".")
m("m3-area", 3, "Area & its link to multiplication",
  "Measure area by counting unit squares, relate tiling to multiplication, and find areas of rectilinear figures by decomposing.",
  ["NC.3.MD.5", "NC.3.MD.7"], ["3.MD.C.5", "3.MD.C.6", "3.MD.C.7"], ["3.6C", "3.6D"],
  ["m3-mult", "G2: Partition a rectangle into rows and columns of same-size squares"],
  ["Cover rectangles with square tiles with no gaps or overlaps.",
   "Draw the grid in rows and columns and count by rows.",
   "Replace counting with multiplication: rows × columns.",
   "Split an L-shape into two rectangles and add the areas.",
   "Use an area model to show 6 × 7 = 6 × 5 + 6 × 2."],
  "Find the area of an L-shaped garden two different ways.",
  "Mixing up area and perimeter; counting tick marks along edges.",
  "Grid paper overlays; word wall with \"square units\" vs \"units\".")
m("m3-perim", 3, "Perimeter",
  "Find perimeters of polygons, including an unknown side, and compare rectangles with the same perimeter or area.",
  ["NC.3.MD.8"], ["3.MD.D.8"], ["3.7B"],
  ["m3-place", "G2: Measure lengths with rulers"],
  ["Walk the edge of a shape on the floor and count steps.",
   "Trace edges on grid paper and label each side length.",
   "Add side lengths; find a missing side when the total is known.",
   "Build rectangles with the same area and different perimeters."],
  "A rectangle has perimeter 18 cm and one side of 5 cm. Find the other sides.",
  "Counting squares inside a shape when asked for perimeter.",
  "Highlight edges in one color and interiors in another.")
m("m3-measure", 3, "Time, mass & liquid volume",
  "Tell time to the minute and solve elapsed-time problems; measure and estimate liquid volume and mass.",
  ["NC.3.MD.1", "NC.3.MD.2"], ["3.MD.A.1", "3.MD.A.2"], ["3.7C", "3.7D", "3.7E"],
  ["G2: Tell time to the nearest 5 minutes", "m3-place"],
  ["Read analog clocks to the minute.",
   "Model elapsed time on an open number line (jump to the hour, then minutes).",
   "Estimate and measure liquid volume with liters and mass with grams and kilograms.",
   "Solve one-step word problems with these measurements."],
  "Recess starts at 10:47 and ends at 11:15. How long is recess? Show your number line.",
  "Treating time as base ten (10:50 + 20 min = 10:70).",
  "Clock manipulatives; real containers and scales.")
m("m3-data", 3, "Scaled picture graphs, bar graphs & line plots",
  "Draw and read scaled graphs and answer one- and two-step how-many-more questions; make line plots of measurement data.",
  ["NC.3.MD.3", "NC.3.MD.4"], ["3.MD.B.3", "3.MD.B.4"], ["3.8A", "3.8B"],
  ["G2: Picture and bar graphs with single-unit scale", "m3-mult"],
  ["Collect class data and sort it into categories.",
   "Make a picture graph where each picture stands for 2 or 5.",
   "Turn it into a bar graph with a scaled axis.",
   "Ask and answer how-many-more and how-many-fewer questions."],
  "On a bar graph scaled by 5s, how many more students chose soccer than tennis?",
  "Reading the scale as 1 per gridline.",
  "Color the scale labels; start with familiar data like class favorites.")
m("m3-shapes", 3, "Classify quadrilaterals & partition shapes",
  "Sort shapes by attributes, recognize categories of quadrilaterals and partition shapes into equal-area parts.",
  ["NC.3.G.1"], ["3.G.A.1", "3.G.A.2"], ["3.6A", "3.6B", "3.6E"],
  ["G2: Recognize and draw shapes with given attributes", "m3-fracunit"],
  ["Sort a mixed set of shapes and name the sorting rule.",
   "Find the attributes all quadrilaterals share.",
   "Sort quadrilaterals into rhombuses, rectangles and squares and find overlaps.",
   "Partition shapes into equal-area parts and name each part as a unit fraction."],
  "Draw a quadrilateral that is not a rhombus, rectangle or square.",
  "Thinking a square is not a rectangle; judging shapes by orientation.",
  "Venn diagrams with physical shapes students can move.")
m("m3-finlit", 3, "Personal financial literacy",
  "Connect work to income, explain scarcity and cost, compare planned and unplanned spending, saving and credit.",
  [], [], ["3.9A", "3.9B", "3.9C", "3.9D", "3.9E", "3.9F"],
  ["G2: Count and add money", "m3-place"],
  ["Discuss jobs and the skills that earn income.",
   "Role-play a store with limited items to show scarcity and cost.",
   "Plan a budget and compare with an unplanned purchase.",
   "Explain saving and lending with simple stories."],
  "Explain why a scarce toy might cost more.",
  "Believing credit is free money.",
  "Classroom economy or play-money simulation.")

# ---------------- MATH GRADE 4 ----------------
m("m4-place", 4, "Place value & rounding to 1,000,000",
  "Recognize that a digit is 10 times what it represents to its right; read, write, compare and round multi-digit whole numbers.",
  ["NC.4.NBT.1", "NC.4.NBT.2", "NC.4.NBT.7"], ["4.NBT.A.1", "4.NBT.A.2", "4.NBT.A.3"], ["4.2A", "4.2B", "4.2C", "4.2D"],
  ["m3-place"],
  ["Build 1, 10, 100, 1,000 with blocks and name the times-ten pattern.",
   "Write numbers in standard, word and expanded form.",
   "Compare numbers with place-value charts and symbols.",
   "Round to any place using a number line and benchmarks."],
  "How is the 4 in 4,000 related to the 4 in 400?",
  "Comparing by the first digit regardless of number length.",
  "Place-value chart with period commas; read numbers aloud by periods.")
m("m4-addsub", 4, "Fluent multi-digit addition & subtraction",
  "Add and subtract multi-digit whole numbers with the standard algorithm. Texas also includes decimals to hundredths.",
  ["NC.4.NBT.4"], ["4.NBT.B.4"], ["4.4A"],
  ["m3-place", "m4-place"],
  ["Review partial sums and differences with blocks.",
   "Link each regroup in the algorithm to a block trade.",
   "Subtract across zeros by regrouping from the next nonzero place.",
   "Estimate first and check with the inverse operation."],
  "Solve 6,003 − 2,478 and check by adding.",
  "Regrouping errors across zeros; misaligned columns.",
  "Graph paper for column alignment; worked examples with one error to find.")
m("m4-mult", 4, "Multiplicative comparison & multi-digit multiplication",
  "Interpret \"times as many\" comparisons and multiply up to 4-digit by 1-digit and 2-digit by 2-digit numbers using place-value strategies.",
  ["NC.4.OA.1", "NC.4.NBT.5"], ["4.OA.A.1", "4.OA.A.2", "4.NBT.B.5"], ["4.4B", "4.4C", "4.4D", "4.4G"],
  ["m3-facts", "m3-area", "m4-place"],
  ["Model \"3 times as many\" with comparison strip diagrams.",
   "Multiply by 10 and 100 and explain the place-value shift.",
   "Use area models to multiply 2-digit by 2-digit (four partial products).",
   "Record partial products, then compress to the standard algorithm.",
   "Estimate products by rounding to check reasonableness."],
  "Use an area model to solve 23 × 46 and connect each part to the algorithm.",
  "Treating comparison as additive (3 times as many as 5 = 8); dropping the zero in 20 × 6.",
  "Area-model templates; color each partial product.")
m("m4-div", 4, "Division with remainders",
  "Find quotients up to 4-digit dividends and 1-digit divisors and interpret remainders in context.",
  ["NC.4.OA.3", "NC.4.NBT.6"], ["4.OA.A.3", "4.NBT.B.6"], ["4.4E", "4.4F", "4.4H"],
  ["m3-mult", "m3-facts", "m4-mult"],
  ["Share base-ten blocks equally and trade when stuck.",
   "Use an area model with a missing side length.",
   "Record partial quotients (\"How many groups can I take out?\").",
   "Decide what the remainder means: drop it, round up or report it.",
   "Check by multiplying and adding the remainder."],
  "25 students ride in vans that hold 6. How many vans are needed? Explain the remainder.",
  "Ignoring the context of the remainder; remainder larger than the divisor.",
  "Remainder decision chart with three picture examples.")
m("m4-factors", 4, "Factors, multiples & patterns",
  "Find factor pairs to 100, identify prime and composite numbers and generate patterns from a rule.",
  ["NC.4.OA.4", "NC.4.OA.5"], ["4.OA.B.4", "4.OA.C.5"], ["4.5A", "4.5B"],
  ["m3-facts"],
  ["Build all rectangles with 12 tiles to find its factor pairs.",
   "Sort numbers by how many rectangles they make (prime vs composite).",
   "Generate a pattern from a rule and look for features the rule does not state.",
   "Use input-output tables to describe a rule."],
  "Is 51 prime or composite? Prove it.",
  "Calling 1 prime; confusing factors and multiples.",
  "Hundreds-chart sieve activity. Texas formally teaches prime and composite in grade 5 (5.4A).")
m("m4-fraceq", 4, "Equivalent fractions & comparing",
  "Explain why multiplying numerator and denominator by the same number makes an equivalent fraction; compare fractions with unlike denominators.",
  ["NC.4.NF.1", "NC.4.NF.2"], ["4.NF.A.1", "4.NF.A.2"], ["4.3C", "4.3D"],
  ["m3-fraceq"],
  ["Split each piece of a fraction strip again and name the new fraction.",
   "Describe the pattern: n × a / n × b.",
   "Compare to benchmarks 0, 1/2 and 1.",
   "Rename to a common denominator or numerator to compare."],
  "Order 3/8, 2/3 and 1/2 and explain using a benchmark.",
  "Comparing numerators and denominators separately (3/8 > 2/3 because 8 > 3).",
  "Benchmark number line on desk; fraction tiles.")
m("m4-fracops", 4, "Add & subtract fractions; fraction times whole number",
  "Decompose fractions into unit fractions, add and subtract like denominators and mixed numbers, and multiply a fraction by a whole number (NC, MI).",
  ["NC.4.NF.3", "NC.4.NF.4"], ["4.NF.B.3", "4.NF.B.4"], ["4.3A", "4.3B", "4.3E"],
  ["m3-fracunit", "m4-fraceq", "m4-mult"],
  ["Decompose 5/6 as 1/6 + 1/6 + 1/6 + 1/6 + 1/6 and in other ways.",
   "Add and subtract like denominators on a number line.",
   "Rename mixed numbers to add and subtract them.",
   "Model 3 × 2/5 as 3 groups of 2/5 (NC, MI)."],
  "Show 2 1/4 − 3/4 on a number line.",
  "Adding denominators (1/4 + 2/4 = 3/8).",
  "Say the unit aloud: \"one fourth plus two fourths is three fourths\". Texas multiplies a fraction by a whole number in grade 5 (5.3I).")
m("m4-decimals", 4, "Decimals to hundredths",
  "Write tenths and hundredths as decimals, relate them to fractions and money, and compare decimals.",
  ["NC.4.NF.6", "NC.4.NF.7"], ["4.NF.C.5", "4.NF.C.6", "4.NF.C.7"], ["4.2E", "4.2F", "4.2G", "4.2H"],
  ["m4-fraceq", "m4-place"],
  ["Shade tenths and hundredths grids; rename 3/10 as 30/100.",
   "Connect to money: dimes and pennies.",
   "Place decimals on a number line from 0 to 1.",
   "Compare decimals with grids and place-value charts."],
  "Which is greater, 0.5 or 0.45? Show with a grid.",
  "Thinking longer decimals are larger (0.45 > 0.5).",
  "Decimal grids and money; always say \"five tenths\" instead of \"point five\".")
m("m4-angles", 4, "Lines, angles & symmetry",
  "Draw and identify lines, rays and angles; measure angles with a protractor; classify figures by parallel and perpendicular sides and angles; find lines of symmetry.",
  ["NC.4.G.1", "NC.4.G.2", "NC.4.G.3", "NC.4.MD.6"], ["4.G.A.1", "4.G.A.2", "4.G.A.3", "4.MD.C.5", "4.MD.C.6", "4.MD.C.7"], ["4.6A", "4.6B", "4.6C", "4.6D", "4.7A", "4.7C", "4.7D", "4.7E"],
  ["m3-shapes"],
  ["Model rays and angles with arms or straws.",
   "Compare angles to a right-angle corner (smaller, equal, larger).",
   "Treat an angle as a turn: 1/360 of a circle is 1 degree.",
   "Measure and draw angles with a protractor; find missing angles by addition.",
   "Classify triangles and quadrilaterals by angles and parallel or perpendicular sides."],
  "Two angles together make a right angle. One is 35°. Find the other.",
  "Reading the wrong protractor scale; thinking longer rays make bigger angles.",
  "Paper protractors with one scale highlighted.")
m("m4-measure", 4, "Measurement conversions, area & perimeter formulas",
  "Convert larger units to smaller ones and apply area and perimeter formulas for rectangles.",
  ["NC.4.MD.1", "NC.4.MD.2", "NC.4.MD.3", "NC.4.MD.8"], ["4.MD.A.1", "4.MD.A.2", "4.MD.A.3"], ["4.5C", "4.5D", "4.8A", "4.8B", "4.8C"],
  ["m3-area", "m3-perim", "m3-measure", "m4-mult"],
  ["Make conversion tables (1 ft = 12 in, 2 ft = 24 in...).",
   "Solve measurement word problems with strip diagrams.",
   "Derive A = l × w and P = 2l + 2w from grids.",
   "Find an unknown side from a known area or perimeter."],
  "A rug is 3 ft by 5 ft. What is its area in square inches?",
  "Dividing instead of multiplying when converting to smaller units.",
  "Two-column conversion charts; real rulers and yardsticks.")
m("m4-data", 4, "Line plots with fractions",
  "Make line plots of measurements in fractions of a unit and solve problems with the data.",
  ["NC.4.MD.4"], ["4.MD.B.4"], ["4.9A", "4.9B"],
  ["m3-data", "m4-fracops"],
  ["Measure objects to the nearest 1/2, 1/4 or 1/8 inch.",
   "Build a line plot with fractional tick marks.",
   "Answer questions that need adding or subtracting the fractions."],
  "What is the difference between the longest and shortest pencil on the plot?",
  "Unequal spacing between fraction marks.",
  "Pre-marked number lines for the first plots.")
m("m4-finlit", 4, "Personal financial literacy",
  "Distinguish fixed and variable expenses, calculate profit, compare saving options, and describe budgets and financial institutions.",
  [], [], ["4.10A", "4.10B", "4.10C", "4.10D", "4.10E"],
  ["m3-finlit", "m4-addsub"],
  ["Sort household expenses as fixed or variable.",
   "Calculate profit for a lemonade stand.",
   "Compare saving at home vs at a bank.",
   "Build a simple budget."],
  "A stand earns $45 and spends $18. What is the profit?",
  "Confusing revenue with profit.",
  "Use classroom-business simulations.")

# ---------------- MATH GRADE 5 ----------------
m("m5-place", 5, "Decimal place value to thousandths",
  "Understand that each place is 10 times the place to its right and 1/10 of the place to its left; read, write, compare and round decimals.",
  ["NC.5.NBT.1", "NC.5.NBT.3"], ["5.NBT.A.1", "5.NBT.A.2", "5.NBT.A.3", "5.NBT.A.4"], ["5.2A", "5.2B", "5.2C"],
  ["m4-decimals", "m4-place"],
  ["Extend the place-value chart to thousandths with base-ten models.",
   "Show multiplying and dividing by 10, 100, 1,000 as moving digits.",
   "Write decimals in expanded form, including fraction form.",
   "Compare and round decimals on number lines."],
  "Round 4.376 to the nearest tenth and hundredth.",
  "Thinking 0.125 > 0.13 because it has more digits.",
  "Hundredths and thousandths grids; place-value sliders.")
m("m5-multdiv", 5, "Multi-digit multiplication & division",
  "Multiply fluently with the standard algorithm and divide up to 4-digit dividends by 2-digit divisors.",
  ["NC.5.NBT.5", "NC.5.NBT.6"], ["5.NBT.B.5", "5.NBT.B.6"], ["5.3A", "5.3B", "5.3C"],
  ["m4-mult", "m4-div"],
  ["Review area models and partial products.",
   "Move to the standard algorithm and name each partial product.",
   "Divide by 2-digit divisors with partial quotients and estimation.",
   "Compare strategies and check with the inverse."],
  "Solve 1,428 ÷ 34 two ways.",
  "Underestimating partial quotients and getting stuck.",
  "Multiples list for the divisor at the top of the page.")
m("m5-decops", 5, "Operations with decimals",
  "Add, subtract, multiply and divide decimals to hundredths using models, place value and properties.",
  ["NC.5.NBT.7"], ["5.NBT.B.7"], ["5.3D", "5.3E", "5.3F", "5.3G", "5.3K"],
  ["m5-place", "m5-multdiv", "m4-addsub"],
  ["Add and subtract decimals with grids, lining up like places.",
   "Model 0.3 × 0.4 with an area model on a hundredths grid.",
   "Model division of decimals as equal groups of hundredths.",
   "Use estimation to place the decimal point and check."],
  "Explain why 0.3 × 0.4 is 0.12 and not 1.2.",
  "Lining up the last digits instead of the places; expecting multiplication to always make bigger.",
  "Decimal grids; estimation before computation every time.")
m("m5-fracaddsub", 5, "Add & subtract fractions with unlike denominators",
  "Replace fractions with equivalent fractions to add and subtract, including mixed numbers, and judge reasonableness with benchmarks.",
  ["NC.5.NF.1"], ["5.NF.A.1", "5.NF.A.2"], ["5.3H", "5.3K"],
  ["m4-fraceq", "m4-fracops"],
  ["Model 1/2 + 1/3 with fraction strips and find a common piece size.",
   "Use area models to find common denominators.",
   "Add and subtract mixed numbers, regrouping when needed.",
   "Estimate with benchmarks (1/2 + 3/8 is a little less than 1)."],
  "Is 2/3 + 1/4 more or less than 1? Prove it, then compute.",
  "Adding numerators and denominators (1/2 + 1/3 = 2/5).",
  "Fraction-strip kits; benchmark number line.")
m("m5-fracmult", 5, "Multiply fractions & fractions as division",
  "Interpret a/b as a ÷ b, multiply fractions and whole numbers by fractions, and reason about scaling.",
  ["NC.5.NF.3", "NC.5.NF.4"], ["5.NF.B.3", "5.NF.B.4", "5.NF.B.5", "5.NF.B.6"], ["5.3I"],
  ["m4-fracops", "m3-area"],
  ["Share 3 sandwiches among 4 people to see 3 ÷ 4 = 3/4.",
   "Model a fraction of a whole number with equal groups.",
   "Use area models to multiply fraction by fraction.",
   "Predict whether a product will be larger or smaller than a factor (scaling)."],
  "Without computing, is 7/8 × 15 more or less than 15? Why?",
  "Believing multiplication always makes a number bigger.",
  "Area-model grids. Texas limits grade 5 to whole number × fraction (5.3I).")
m("m5-fracdiv", 5, "Divide with unit fractions",
  "Divide unit fractions by whole numbers and whole numbers by unit fractions using models.",
  ["NC.5.NF.7"], ["5.NF.B.7"], ["5.3J", "5.3L"],
  ["m5-fracmult", "m3-mult"],
  ["Ask \"how many 1/3s are in 2?\" and model with strips.",
   "Model 1/3 ÷ 4 as sharing one-third into 4 equal parts.",
   "Write the matching multiplication equation to check.",
   "Solve word problems and decide which division meaning fits."],
  "How many 1/4-cup servings are in 3 cups? Draw it.",
  "Dividing the wrong number by the other; expecting the quotient to be smaller.",
  "Measuring cups for real-world modeling.")
m("m5-expr", 5, "Numerical expressions, patterns & prime numbers",
  "Write and evaluate expressions with parentheses, generate two related patterns and graph the pairs. Texas adds prime and composite numbers.",
  ["NC.5.OA.2", "NC.5.OA.3"], ["5.OA.A.1", "5.OA.A.2", "5.OA.B.3"], ["5.4A", "5.4B", "5.4C", "5.4D", "5.4E", "5.4F"],
  ["m4-factors", "m3-twostep"],
  ["Translate words into expressions (\"three times the sum of 5 and 2\").",
   "Evaluate expressions with grouping symbols.",
   "Generate two patterns from rules and compare corresponding terms.",
   "Graph the ordered pairs and describe the relationship."],
  "Write an expression for \"double 8, then add 7\" and another for \"add 8 and 7, then double\". Compare.",
  "Working strictly left to right and ignoring grouping symbols.",
  "Color-code grouping symbols; expression-to-words matching cards.")
m("m5-coord", 5, "Coordinate plane",
  "Graph points in the first quadrant and interpret coordinates in real-world problems.",
  ["NC.5.G.1"], ["5.G.A.1", "5.G.A.2"], ["5.8A", "5.8B", "5.8C"],
  ["m4-angles", "m5-expr", "m2-length"],
  ["Build two perpendicular number lines on the floor.",
   "Walk to points: over on x, then up on y.",
   "Plot points from a table of values.",
   "Interpret points in a context (time and distance)."],
  "Plot (3, 5) and (5, 3). Why are they different points?",
  "Reversing x and y.",
  "Mnemonic: \"run before you jump\". Floor grid with tape.")
m("m5-volume", 5, "Volume of rectangular prisms",
  "Understand volume as unit cubes, use l × w × h and B × h, and add volumes of composite figures.",
  ["NC.5.MD.4", "NC.5.MD.5"], ["5.MD.C.3", "5.MD.C.4", "5.MD.C.5"], ["5.4G", "5.4H", "5.6A", "5.6B"],
  ["m3-area", "m4-measure", "m5-multdiv"],
  ["Pack boxes with unit cubes and count.",
   "Count layers: area of the base times the number of layers.",
   "Generalize to V = l × w × h and V = B × h.",
   "Find volumes of composite figures by adding."],
  "A box has a base of 12 cubes and is 5 layers tall. What is its volume?",
  "Confusing surface area or area with volume; using square units.",
  "Snap cubes and nets of boxes.")
m("m5-shapes", 5, "Classify 2D figures in a hierarchy",
  "Classify two-dimensional figures in a hierarchy based on their properties.",
  ["NC.5.G.3"], ["5.G.B.3", "5.G.B.4"], ["5.5A"],
  ["m4-angles", "m3-shapes"],
  ["Sort shapes by side and angle properties.",
   "Build a hierarchy diagram for quadrilaterals.",
   "Use \"all, some, none\" statements to justify placements."],
  "True or false: all rhombuses are parallelograms. Justify.",
  "Treating categories as exclusive (a square is not a rhombus).",
  "Nested-box graphic organizer.")
m("m5-measure-data", 5, "Unit conversions & line plots",
  "Convert units within a system in multi-step problems and use line plots of fractional data. Texas adds stem-and-leaf plots and scatterplots.",
  ["NC.5.MD.1", "NC.5.MD.2"], ["5.MD.A.1", "5.MD.B.2"], ["5.7A", "5.9A", "5.9B", "5.9C"],
  ["m4-measure", "m4-data", "m5-decops"],
  ["Build metric conversion charts tied to place value.",
   "Solve multi-step conversion problems.",
   "Create line plots of fractional measurements and redistribute evenly.",
   "Interpret other data displays (TX: stem-and-leaf, scatterplot)."],
  "Convert 3.5 kg to grams and explain using place value.",
  "Multiplying when they should divide in conversions.",
  "Metric staircase visual.")
m("m5-finlit", 5, "Personal financial literacy",
  "Define taxes, compare payment methods, balance a budget and describe gross and net income.",
  [], [], ["5.10A", "5.10B", "5.10C", "5.10D", "5.10E", "5.10F"],
  ["m4-finlit", "m5-decops"],
  ["Sort taxes (income, payroll, sales, property).",
   "Compare cash, debit, credit and electronic payments.",
   "Find net income from gross income and deductions.",
   "Balance a simple budget."],
  "A paycheck is $600 with $90 withheld. What is net income?",
  "Thinking gross pay is what you take home.",
  "Budget simulations with realistic local prices.")

# ---------------- MATH K, 1, 2 and 6 (math_k2_6.py) ----------------
import math_k2_6 as MK
for _row in MK.CONCEPTS:
    m(*_row)
for _c in C:
    if _c["id"] in MK.G3_PREREQS:
        _c["prereqs"] = MK.G3_PREREQS[_c["id"]]
    if _c["grade"] in (0, 1, 2, 6):
        _c["verify"] = ["NC"]
    elif _c["grade"] == 3:
        _c["verify"] = ["NC"]

# ---------------- ELA (templates shared by grades K-6) ----------------
ELA = [
  # key, name, summary, cc codes (NC/MI) fn, NC override fn, TX fn, prereq keys, grade-2 text, focus by grade, steps, check, miscon, supports
  dict(key="evidence", name="Cite text evidence & make inferences",
       summary="Ask and answer questions, refer to details and quote accurately to support what the text says and what can be inferred.",
       cc=lambda g: [f"RL.{g}.1", f"RI.{g}.1"], tx=lambda g: [f"{g}.6F", f"{g}.7C"],
       pre=[], g2="G2: Ask and answer who, what, where, when, why questions about key details",
       focus={3: "Refer explicitly to the text as the basis for answers.", 4: "Refer to details and examples when explaining and drawing inferences.", 5: "Quote accurately when explaining and drawing inferences."},
       steps=["Think-aloud: model noticing a clue and saying what it makes you think.",
              "It Says / I Say / And So chart with partners.",
              "Highlight the exact words that prove an answer.",
              "Write answers with a frame: \"I think ___ because the text says ___.\"",
              "Independently answer inference questions with quoted evidence."],
       check="Answer an inference question about a short passage and quote the line that proves it.",
       mis="Giving evidence from background knowledge rather than the text; quoting a line that is related but does not prove the point.",
       sup="Sentence frames, color-coded highlighting, partner talk before writing."),
  dict(key="theme", name="Theme, central message & summary",
       summary="Determine the theme or central message of a story, poem or drama and summarize the text.",
       cc=lambda g: [f"RL.{g}.2"], tx=lambda g: [f"{g}.8A", f"{g}.7D"],
       pre=["evidence", "character"], g2="G2: Recount stories and determine their central message",
       focus={3: "Recount fables and folktales and determine the central message, lesson or moral.", 4: "Determine a theme from details and summarize the text.", 5: "Determine a theme, including how characters respond to challenges, and summarize."},
       steps=["Separate topic (friendship) from theme (true friends tell the truth).",
              "Track what the main character learns or how they change.",
              "Turn the lesson into a statement that applies to anyone.",
              "Summarize with Somebody-Wanted-But-So-Then.",
              "Compare themes across two texts."],
       check="State the theme of a fable in a full sentence and give two details that support it.",
       mis="Naming a one-word topic as the theme; retelling every event instead of summarizing.",
       sup="Theme word bank, topic-to-theme sorting cards, short fables first."),
  dict(key="character", name="Characters, setting & plot",
       summary="Describe characters, their motivations and changes, and how setting and events shape the story.",
       cc=lambda g: [f"RL.{g}.3"], tx=lambda g: [f"{g}.8B", f"{g}.8C", f"{g}.8D"],
       pre=["evidence"], g2="G2: Describe how characters respond to major events",
       focus={3: "Describe characters (traits, motivations, feelings) and how their actions affect events.", 4: "Describe a character, setting or event in depth using specific details.", 5: "Compare and contrast two or more characters, settings or events."},
       steps=["Act out a scene and name what the character feels.",
              "Separate outside traits from inside traits with evidence.",
              "Map the plot: problem, events, climax, resolution.",
              "Explain how the setting influences the problem.",
              "Compare two characters with a Venn diagram and evidence."],
       check="How does the main character change from beginning to end? Use two pieces of evidence.",
       mis="Listing physical traits only; confusing feelings with traits.",
       sup="Character trait word bank; plot mountain organizer."),
  dict(key="mainidea", name="Main idea & key details",
       summary="Determine the main or central idea of an informational text and explain how key details support it.",
       cc=lambda g: [f"RI.{g}.2"], tx=lambda g: [f"{g}.9D(i)", f"{g}.6G"],
       pre=["evidence"], g2="G2: Identify the main topic of a multi-paragraph text",
       focus={3: "Determine the main idea and recount key details.", 4: "Determine the main idea, explain how details support it, and summarize.", 5: "Determine two or more main ideas and explain how details support them."},
       steps=["Sort details under a given main idea (table and legs).",
              "Ask \"What is this mostly about?\" for each paragraph.",
              "Combine paragraph gists into a main idea statement.",
              "Explain how each key detail supports the main idea.",
              "Summarize without opinions."],
       check="Write the main idea of an article in one sentence and list three supporting details.",
       mis="Picking an interesting detail as the main idea; stating only the topic.",
       sup="Main-idea table graphic organizer; shorter texts with headings."),
  dict(key="structure", name="Text structure & features",
       summary="Use text features and describe overall structure (chronology, comparison, cause/effect, problem/solution).",
       cc=lambda g: [f"RI.{g}.3", f"RI.{g}.5", f"RI.{g}.7"], tx=lambda g: [f"{g}.9D(ii)", f"{g}.9D(iii)", f"{g}.10B", f"{g}.10C"],
       pre=["mainidea"], g2="G2: Use text features to locate key facts",
       focus={3: "Use text features and search tools to locate information.", 4: "Describe the overall structure of events, ideas or information.", 5: "Compare the overall structure in two or more texts."},
       steps=["Text-feature scavenger hunt in a nonfiction book.",
              "Introduce signal words for each structure.",
              "Match paragraphs to structure graphic organizers.",
              "Explain why the author chose that structure.",
              "Compare structures across two texts on one topic."],
       check="Identify the structure of a paragraph and name the signal words that show it.",
       mis="Choosing a structure from one signal word; ignoring the purpose.",
       sup="Signal-word anchor chart; structure graphic organizers."),
  dict(key="vocab", name="Vocabulary in context",
       summary="Determine meanings of words using context, affixes, roots and reference materials.",
       cc=lambda g: [f"L.{g}.4", f"L.{g}.6", f"RL.{g}.4", f"RI.{g}.4"], tx=lambda g: [f"{g}.3A", f"{g}.3B", f"{g}.3C"],
       pre=[], g2="G2: Use sentence-level context and common prefixes to determine meaning",
       focus={3: "Use context and common prefixes and suffixes.", 4: "Use context, Greek and Latin affixes and roots.", 5: "Use context (cause/effect, comparisons), Greek and Latin affixes and roots."},
       steps=["Model a think-aloud with context clues.",
              "Teach a context clue type (definition, example, contrast).",
              "Break words into prefix, root and suffix.",
              "Confirm meaning with a dictionary or glossary.",
              "Use the new word in speaking and writing."],
       check="Figure out the meaning of an unfamiliar word in a passage and explain the clue you used.",
       mis="Guessing from the first letter; ignoring sentences around the word.",
       sup="Affix word walls; picture glossaries for ELLs."),
  dict(key="figlang", name="Figurative language & word relationships",
       summary="Interpret similes, metaphors, idioms and other figurative language and explain how word choice creates meaning.",
       cc=lambda g: [f"L.{g}.5"], tx=lambda g: [f"{g}.10D", f"{g}.3D"],
       pre=["vocab"], g2="G2: Identify words and phrases that supply rhythm and meaning in a poem",
       focus={3: "Distinguish literal and nonliteral meanings.", 4: "Explain similes, metaphors, idioms, adages and proverbs.", 5: "Interpret figurative language and explain word relationships."},
       steps=["Sort phrases into literal and figurative.",
              "Draw what an idiom says vs what it means.",
              "Identify similes and metaphors and say what is being compared.",
              "Explain why the author used the figure of speech.",
              "Use figurative language in writing."],
       check="Explain the meaning of a simile in a poem and why the poet used it.",
       mis="Interpreting idioms literally.",
       sup="Idiom picture cards; bilingual idiom comparisons for ELLs."),
  dict(key="genre", name="Poetry, drama & point of view",
       summary="Describe how poems and dramas are structured and how a narrator's point of view shapes a story.",
       cc=lambda g: [f"RL.{g}.5", f"RL.{g}.6"], tx=lambda g: [f"{g}.9B", f"{g}.9C", f"{g}.10E"],
       pre=["character", "figlang"], g2="G2: Describe the overall structure of a story",
       focus={3: "Refer to parts of stories, dramas and poems (chapter, scene, stanza) and distinguish their own view from the narrator's.", 4: "Explain major differences between poems, drama and prose; compare first- and third-person narration.", 5: "Explain how chapters, scenes or stanzas fit together; describe how a narrator's point of view influences events."},
       steps=["Read a poem, a script and a story about the same idea.",
              "Label parts: stanza, line, scene, stage directions, chapter.",
              "Identify the narrator and their pronouns.",
              "Retell a scene from another character's point of view.",
              "Explain how the form changes the reader's experience."],
       check="Explain how a story would change if told by a different character.",
       mis="Confusing the author with the narrator.",
       sup="Readers' theater; point-of-view pronoun charts."),
  dict(key="compare", name="Compare & synthesize across texts",
       summary="Compare themes, topics and information across texts and integrate information from several sources.",
       cc=lambda g: [f"RL.{g}.9", f"RI.{g}.9"], tx=lambda g: [f"{g}.6H", f"{g}.7E"],
       pre=["theme", "mainidea"], g2="G2: Compare two versions of the same story",
       focus={3: "Compare themes, settings and plots of stories by the same author; compare key points of two texts on a topic.", 4: "Compare treatment of similar themes and topics across cultures; integrate two texts on one topic.", 5: "Compare stories in the same genre on their approach to themes; integrate several texts."},
       steps=["Read two texts on one topic and list facts from each.",
              "Mark what is the same and what is different.",
              "Explain what you learn from both together that neither gives alone.",
              "Write a short synthesis paragraph citing both texts."],
       check="Use two articles to answer one question, citing both.",
       mis="Summarizing each text separately with no comparison.",
       sup="Two-column notes; color code by source."),
  dict(key="opinion", name="Opinion writing",
       summary="Write opinion pieces that state a point of view and support it with reasons and evidence.",
       cc=lambda g: [f"W.{g}.1", f"RI.{g}.8"], tx=lambda g: [f"{g}.12C", f"{g}.9E"],
       pre=["evidence"], g2="G2: Write opinion pieces with reasons and linking words",
       focus={3: "Introduce the topic, state an opinion, give reasons, use linking words and conclude.", 4: "Support reasons with facts and details; group related ideas logically.", 5: "Logically order reasons supported by facts; link opinion and reasons with phrases and clauses."},
       steps=["Debate a classroom question orally first.",
              "State an opinion and list reasons on a planner.",
              "Find facts or examples that support each reason.",
              "Draft with linking words (because, for example, therefore).",
              "Revise for a strong conclusion."],
       check="Write an opinion paragraph with a clear claim, two reasons and evidence for each.",
       mis="Listing reasons without evidence; switching opinions mid-piece.",
       sup="OREO planner (Opinion, Reason, Example, Opinion); sentence starters."),
  dict(key="informative", name="Informative writing",
       summary="Write informative and explanatory texts that examine a topic and convey ideas and information clearly.",
       cc=lambda g: [f"W.{g}.2"], tx=lambda g: [f"{g}.12B"],
       pre=["mainidea", "structure"], g2="G2: Write informative pieces with facts and a concluding statement",
       focus={3: "Introduce a topic, group related information, develop with facts and conclude.", 4: "Group information in paragraphs and sections; include formatting, illustrations and precise vocabulary.", 5: "Develop with facts, definitions and quotations; link ideas across categories."},
       steps=["Choose a topic you know well; list facts.",
              "Sort facts into categories (future paragraphs).",
              "Write a topic sentence for each category.",
              "Add details, definitions and domain words.",
              "Write an introduction and conclusion; add text features."],
       check="Write two paragraphs explaining a topic with a clear introduction and precise vocabulary.",
       mis="Writing a list of facts with no organization; adding personal opinion.",
       sup="Mentor texts; paragraph frames; graphic organizers with categories."),
  dict(key="narrative", name="Narrative writing",
       summary="Write narratives with a situation, characters, dialogue, description and a clear sequence of events.",
       cc=lambda g: [f"W.{g}.3"], tx=lambda g: [f"{g}.12A"],
       pre=["character"], g2="G2: Write narratives that recount a sequence of events with details and an ending",
       focus={3: "Establish a situation and narrator, use dialogue and descriptions, use temporal words.", 4: "Use dialogue and description to develop experiences; use concrete words and sensory details.", 5: "Use pacing, dialogue and description; manage sequence with transitions."},
       steps=["Tell the story orally to a partner first.",
              "Plan beginning, middle and end on a story map.",
              "Draft a strong lead and add dialogue.",
              "Revise to show feelings through actions and senses.",
              "Edit and share."],
       check="Write a personal narrative scene that uses dialogue and a sensory detail.",
       mis="Bed-to-bed stories that list every event at the same pace.",
       sup="Story maps; mentor sentences for leads and endings."),
  dict(key="process", name="Writing process & conventions",
       summary="Plan, draft, revise and edit with guidance; use grade-level grammar, capitalization, punctuation and spelling.",
       cc=lambda g: [f"W.{g}.4", f"W.{g}.5", f"L.{g}.1", f"L.{g}.2", f"L.{g}.3"], nc=lambda g: [f"W.{g}.4", f"L.{g}.1", f"L.{g}.2", f"L.{g}.3"],
       tx=lambda g: [f"{g}.11A", f"{g}.11B", f"{g}.11C", f"{g}.11D", f"{g}.11E"],
       pre=[], g2="G2: Revise and edit with guidance; use grade 2 conventions",
       focus={3: "Use nouns, verbs, adjectives, and adverbs correctly; form and use simple verb tenses.", 4: "Use relative pronouns, progressive tenses and modal auxiliaries; correct run-ons and fragments.", 5: "Use conjunctions, prepositions and interjections; verb tense shifts; commas in series and introductory elements."},
       steps=["Plan with a genre-matched organizer.",
              "Draft quickly without stopping to fix spelling.",
              "Revise with a single focus (add, remove, move, substitute).",
              "Edit with a checklist for the conventions taught this unit.",
              "Publish and reflect."],
       check="Revise one paragraph with ARMS and edit it with the unit checklist.",
       mis="Treating revising and editing as the same thing.",
       sup="ARMS / CUPS checklists; peer conferencing protocols."),
  dict(key="research", name="Short research projects",
       summary="Conduct short research projects, gather information from print and digital sources, take notes and list sources.",
       cc=lambda g: [f"W.{g}.7", f"W.{g}.8"], nc=lambda g: [f"W.{g}.5", f"W.{g}.6"],
       tx=lambda g: [f"{g}.13A", f"{g}.13B", f"{g}.13C", f"{g}.13E", f"{g}.13G", f"{g}.13H"],
       pre=["informative", "compare"], g2="G2: Participate in shared research and recall information",
       focus={3: "Build knowledge about a topic; take brief notes and sort into categories.", 4: "Investigate different aspects of a topic; paraphrase in notes and list sources.", 5: "Use several sources; summarize or paraphrase; provide a list of sources."},
       steps=["Generate questions about a topic.",
              "Locate two to three kid-friendly sources.",
              "Take notes in your own words (paraphrase, not copy).",
              "Sort notes into categories and draft.",
              "Present findings and cite sources."],
       check="Paraphrase a paragraph from a source in your own words and record the source.",
       mis="Copying sentences word for word.",
       sup="Note-taking templates; curated source sets."),
  dict(key="foundations", name="Phonics, word analysis & fluency",
       summary="Decode multisyllabic words, read grade-level texts accurately and fluently with expression.",
       cc=lambda g: [f"RF.{g}.3", f"RF.{g}.4"], nc=lambda g: [f"RF.{g}.4", f"RF.{g}.5"], tx=lambda g: [f"{g}.2A", f"{g}.4"],
       pre=[], g2="G2: Decode two-syllable words with long vowels; read with accuracy and expression",
       focus={3: "Decode words with common Latin suffixes and multisyllable words; read irregularly spelled words.", 4: "Use letter-sound correspondences, syllabication and morphology to read unfamiliar multisyllabic words.", 5: "Use combined knowledge of syllabication and morphology to read unfamiliar words accurately."},
       steps=["Explicitly teach syllable types and division rules.",
              "Practice decoding words in isolation, then in sentences.",
              "Model fluent reading; echo and choral read.",
              "Repeated reading with timed feedback.",
              "Apply in independent connected text."],
       check="Read a grade-level passage aloud; check words correct per minute and expression.",
       mis="Guessing from pictures or first letters instead of decoding.",
       sup="Small-group decoding intervention; decodable texts for older readers."),
]

import ela_k2_6 as EK


def gid(g):
    return "k" if g == 0 else str(g)


def glab(g):
    return "K" if g == 0 else str(g)


def tx6(codes):
    """Grade 6 TEKS ELAR drops the beginning-reading strand, so strands 3-13 shift down by one."""
    out = []
    for x in codes:
        mm = re.match(r"^6\.(\d+)(.*)$", x)
        n = int(mm.group(1))
        if n == 2:
            continue
        out.append(f"6.{n - 1}{mm.group(2)}")
    return out


for g in (0, 1, 2, 3, 4, 5, 6):
    for e in ELA:
        key = e["key"]
        if g == 6 and key == "foundations":
            continue  # no foundational skills strand after grade 5
        cid = f"e{gid(g)}-{key}"
        pre = [f"e{gid(g)}-{k}" for k in e["pre"]]
        pre = ([EK.PREK] if g == 0 else [f"e{gid(g - 1)}-{key}"]) + pre
        focus = e["focus"].get(g) or EK.FOCUS[key][g]
        cc = e["cc"](glab(g))
        nc = (e.get("nc") or e["cc"])(glab(g))
        tx = e["tx"](glab(g))
        if key == "process" and g <= 2:
            cc = [x for x in cc if x != f"W.{glab(g)}.4"]
            if g <= 1:
                cc = [x for x in cc if x != f"L.{glab(g)}.3"]
                nc = [x for x in nc if x != f"L.{glab(g)}.3"]
        if g == 6:
            tx = tx6(tx)
        name = e["name"].replace("Opinion writing", "Argument writing") if g == 6 else e["name"]
        c = dict(id=cid, subject="ela", grade=g, name=name,
                 summary=e["summary"] + " Grade focus: " + focus,
                 codes=dict(NC=nc, MI=cc, TX=tx),
                 prereqs=pre, steps=e["steps"], check=e["check"],
                 misconception=e["mis"], supports=e["sup"])
        if g in (0, 1, 2, 6):
            c["verify"] = ["NC", "TX"]
        elif g == 3:
            c["verify"] = ["NC"]
        C.append(c)


def U(title, weeks, ids, note=None):
    d = dict(title=title, weeks=weeks, concepts=ids)
    if note:
        d["note"] = note
    return d


PACING = {"NC": {"math": {}, "ela": {}}, "MI": {"math": {}, "ela": {}}, "TX": {"math": {}, "ela": {}}}

# NC math
PACING["NC"]["math"][3] = [
    U("Place value, rounding & add/subtract", 4, ["m3-place"]),
    U("Meaning of multiplication & division", 5, ["m3-mult"]),
    U("Fact strategies & two-step problems", 5, ["m3-facts", "m3-twostep"]),
    U("Area & perimeter", 4, ["m3-area", "m3-perim"]),
    U("Fractions", 7, ["m3-fracunit", "m3-fraceq"]),
    U("Measurement & data", 4, ["m3-measure", "m3-data"]),
    U("Geometry", 3, ["m3-shapes"]),
    U("Review & EOG", 4, [], "Spiral review of fractions and multiplication before the EOG."),
]
PACING["NC"]["math"][4] = [
    U("Place value & add/subtract", 4, ["m4-place", "m4-addsub"]),
    U("Multiplication & multiplicative comparison", 6, ["m4-mult", "m4-factors"]),
    U("Division", 5, ["m4-div"]),
    U("Fraction equivalence & comparison", 4, ["m4-fraceq"]),
    U("Fraction operations", 5, ["m4-fracops"]),
    U("Decimals", 3, ["m4-decimals"]),
    U("Measurement & data", 4, ["m4-measure", "m4-data"]),
    U("Geometry & angles", 3, ["m4-angles"]),
    U("Review & EOG", 2, []),
]
PACING["NC"]["math"][5] = [
    U("Decimal place value", 3, ["m5-place"]),
    U("Whole-number multiplication & division", 5, ["m5-multdiv"]),
    U("Decimal operations", 6, ["m5-decops"]),
    U("Add & subtract fractions", 5, ["m5-fracaddsub"]),
    U("Multiply & divide fractions", 6, ["m5-fracmult", "m5-fracdiv"]),
    U("Volume", 3, ["m5-volume"]),
    U("Expressions & coordinate plane", 4, ["m5-expr", "m5-coord"]),
    U("Geometry, measurement & data", 4, ["m5-shapes", "m5-measure-data"]),
]
# MI math (order of common CCSS-aligned curricula)
PACING["MI"]["math"][3] = [
    U("Introduction to multiplication", 4, ["m3-mult", "m3-data"]),
    U("Area & multiplication", 4, ["m3-area", "m3-facts"]),
    U("Add & subtract within 1,000", 5, ["m3-place"]),
    U("Relating multiplication to division", 6, ["m3-mult", "m3-facts", "m3-twostep"]),
    U("Fractions as numbers", 6, ["m3-fracunit", "m3-fraceq"]),
    U("Measuring length, time, liquid volume & weight", 4, ["m3-measure", "m3-data"]),
    U("2D shapes & perimeter", 4, ["m3-shapes", "m3-perim"]),
    U("Putting it all together", 3, ["m3-twostep"], "Fluency and two-step problem review before M-STEP."),
]
PACING["MI"]["math"][4] = [
    U("Factors & multiples", 3, ["m4-factors"]),
    U("Fraction equivalence & comparison", 4, ["m4-fraceq"]),
    U("Extending operations to fractions", 6, ["m4-fracops", "m4-data"]),
    U("From hundredths to hundred-thousands", 5, ["m4-decimals", "m4-place", "m4-addsub"]),
    U("Multiplicative comparison & measurement", 4, ["m4-mult", "m4-measure"]),
    U("Multiplying & dividing multi-digit numbers", 7, ["m4-mult", "m4-div"]),
    U("Angles & angle measurement", 4, ["m4-angles"]),
    U("Putting it all together", 3, []),
]
PACING["MI"]["math"][5] = [
    U("Finding volume", 3, ["m5-volume"]),
    U("Fractions as quotients & fraction multiplication", 5, ["m5-fracmult"]),
    U("Multiplying & dividing fractions", 5, ["m5-fracmult", "m5-fracdiv"]),
    U("Multi-digit multiplication & division", 4, ["m5-multdiv"]),
    U("Place value patterns & decimal operations", 7, ["m5-place", "m5-decops"]),
    U("More decimal & fraction operations", 5, ["m5-fracaddsub", "m5-measure-data"]),
    U("Shapes on the coordinate plane", 4, ["m5-coord", "m5-shapes"]),
    U("Putting it all together", 3, ["m5-expr"]),
]
# TX math (representative Year at a Glance)
PACING["TX"]["math"][3] = [
    U("Place value to 100,000", 3, ["m3-place"]),
    U("Add & subtract; money & financial literacy", 4, ["m3-place", "m3-finlit"]),
    U("Multiplication", 5, ["m3-mult", "m3-facts"]),
    U("Division & two-step problems", 5, ["m3-mult", "m3-facts", "m3-twostep"]),
    U("Fractions", 6, ["m3-fracunit", "m3-fraceq"]),
    U("Geometry & measurement", 5, ["m3-shapes", "m3-area", "m3-perim", "m3-measure"]),
    U("Data analysis", 2, ["m3-data"]),
    U("STAAR review", 3, [], "STAAR is given in April."),
    U("Post-STAAR: financial literacy & extension", 3, ["m3-finlit"]),
]
PACING["TX"]["math"][4] = [
    U("Place value: whole numbers & decimals", 4, ["m4-place", "m4-decimals"]),
    U("Add & subtract whole numbers & decimals", 3, ["m4-addsub"]),
    U("Multiplication", 5, ["m4-mult"]),
    U("Division & patterns", 5, ["m4-div", "m4-factors"]),
    U("Fractions", 5, ["m4-fraceq", "m4-fracops"]),
    U("Geometry & angles", 4, ["m4-angles"]),
    U("Measurement", 3, ["m4-measure"]),
    U("Data & financial literacy", 2, ["m4-data", "m4-finlit"]),
    U("STAAR review", 3, [], "STAAR is given in April."),
    U("Post-STAAR extension", 2, []),
]
PACING["TX"]["math"][5] = [
    U("Decimal place value", 3, ["m5-place"]),
    U("Add & subtract decimals; financial literacy", 3, ["m5-decops", "m5-finlit"]),
    U("Whole-number multiplication & division", 5, ["m5-multdiv"]),
    U("Multiply & divide decimals", 4, ["m5-decops"]),
    U("Add & subtract fractions", 4, ["m5-fracaddsub"]),
    U("Multiply & divide fractions", 4, ["m5-fracmult", "m5-fracdiv"]),
    U("Algebraic reasoning & coordinate plane", 4, ["m5-expr", "m5-coord"]),
    U("Geometry & measurement", 4, ["m5-volume", "m5-shapes", "m5-measure-data"]),
    U("STAAR review", 3, [], "STAAR is given in April."),
    U("Post-STAAR extension", 2, []),
]

# ELA pacing
def ela_nc(g):
    p = lambda *k: [f"e{g}-{x}" for x in k]
    return [
        U("Building a reading community & narrative", 6, p("foundations", "evidence", "narrative", "process")),
        U("Literary analysis: characters & theme", 6, p("character", "theme", "evidence", "vocab")),
        U("Informational reading & writing", 6, p("mainidea", "structure", "informative", "vocab")),
        U("Opinion reading & writing", 6, p("opinion", "evidence", "compare")),
        U("Poetry, drama & figurative language", 6, p("genre", "figlang", "theme")),
        U("Research & synthesis", 6, p("research", "compare", "process"), "Includes EOG reading review in May."),
    ]

def ela_mi(g):
    p = lambda *k: [f"e{g}-{x}" for x in k]
    return [
        U("Launching readers & writers", 5, p("foundations", "evidence", "process")),
        U("Narrative reading & writing", 6, p("character", "narrative", "vocab")),
        U("Informational texts & expert writing", 7, p("mainidea", "structure", "informative")),
        U("Opinion & persuasive writing", 6, p("opinion", "evidence", "compare")),
        U("Theme, poetry & figurative language", 6, p("theme", "genre", "figlang")),
        U("Research clubs", 6, p("research", "compare", "process"), "M-STEP in spring."),
    ]

def ela_tx(g):
    p = lambda *k: [f"e{g}-{x}" for x in k]
    return [
        U("Reading community & personal narrative", 5, p("foundations", "evidence", "narrative", "process")),
        U("Literary fiction: characters & plot", 6, p("character", "theme", "vocab")),
        U("Informational text & expository writing", 6, p("mainidea", "structure", "informative")),
        U("Poetry & drama", 5, p("genre", "figlang")),
        U("Argumentative text & opinion writing", 5, p("opinion", "compare", "evidence")),
        U("STAAR review", 3, p("evidence", "process"), "STAAR RLA in April includes constructed responses."),
        U("Inquiry & research", 5, p("research", "compare")),
    ]

_ids = {c["id"] for c in C}


def _keep(units, g):
    for u in units:
        u["concepts"] = [x for x in u["concepts"] if x in _ids]
        if g <= 2:
            u.pop("note", None)  # notes mention grade 3+ state tests
    if g <= 2:
        units = [u for u in units if u["title"] != "STAAR review"]
    return units


for g in (0, 1, 2, 3, 4, 5, 6):
    PACING["NC"]["ela"][g] = _keep(ela_nc(gid(g)), g)
    PACING["MI"]["ela"][g] = _keep(ela_mi(gid(g)), g)
    PACING["TX"]["ela"][g] = _keep(ela_tx(gid(g)), g)
for st in ("NC", "MI", "TX"):
    PACING[st]["math"].update(MK.PACING[st])

# Validate references
ids = {c["id"] for c in C}
for c in C:
    for p in c["prereqs"]:
        assert p in ids or re.match(r"^(PreK|G\d):", p), (c["id"], p)
for s, subj in PACING.items():
    for sub, grades in subj.items():
        for g, units in grades.items():
            for u in units:
                for cid in u["concepts"]:
                    assert cid in ids, (s, sub, g, cid)

# State-specific codes for states with their own standards (state_codes.py).
# Stored on the concept as codes[ST]; scaffolds, items and pacing still come from the CCSS version.
from state_codes import CODES as STATE_CODES, NOTES as STATE_NOTES, VERIFY as STATE_VERIFY
_allids = {c["id"] for c in C}
for _st, _map in STATE_CODES.items():
    assert set(_map) <= _allids, (_st, set(_map) - _allids)
    for _c in C:
        if _c["id"] in _map:
            _c["codes"][_st] = _map[_c["id"]]
            if _c["id"] in STATE_VERIFY[_st]:
                _c.setdefault("verify", []).append(_st)
    STATES[_st]["mapped"] = True
    STATES[_st]["code_note"] = STATE_NOTES[_st]["note"]
    STATES[_st]["sources"] = STATE_NOTES[_st]["sources"] + [s for s in STATES[_st]["sources"] if s[1] not in {u for _, u in STATE_NOTES[_st]["sources"]}]

from examples import build as build_examples
EXS = build_examples(C)
for c in C:
    c["examples"] = EXS[c["id"]]
    for st in ("NC", "MI", "TX"):
        assert (st in c["examples"]) == bool(c["codes"][st]), (c["id"], st)

from passages import TEXTS as _T35
TEXTS = {**_T35, **EK.TEXTS}
PASS = {g: {"topic": t["topic"], **{k: {"title": t[k][0], "text": t[k][1].strip()} for k in ("story", "article", "poem")}} for g, t in TEXTS.items()}
out = dict(version="2026-11-25", grades=[0, 1, 2, 3, 4, 5, 6], states=STATES, concepts=C, pacing=PACING, passages=PASS)
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "data.json"), "w") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
print(len(C), "concepts", os.path.getsize(os.path.join(here, "data.json")), "bytes")
