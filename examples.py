"""State-style example items for each concept.

EX[concept_id][STATE] = (format, prompt, choices_or_None, answer)
Original items written in the style of each state's guidance:
  NC  -> NCDPI unpacking-document examples and EOG item formats
  MI  -> M-STEP (Smarter Balanced) formats: multi-select, two-part, constructed response
  TX  -> STAAR formats: multiple choice, "record your answer", short constructed response
They are not released test items.
"""

from passages import items_for

STYLE = {"NC": "NCDPI unpacking-style example", "MI": "M-STEP-style item", "TX": "STAAR-style item"}

MATH = {
 # ---------- Grade 3 ----------
 "m3-mult": {
  "NC": ("Model and equations", "Ms. Bell puts 24 crayons into 4 boxes with the same number in each box. Draw a model. Write a multiplication equation and a division equation for the crayons.", None, "6 crayons in each box. 4 × 6 = 24 and 24 ÷ 4 = 6."),
  "MI": ("Multi-select", "A teacher sets up 5 rows of chairs with 3 chairs in each row. Select all expressions that show the total number of chairs.", ["5 + 3", "5 × 3", "3 + 3 + 3 + 3 + 3", "15 ÷ 5", "3 × 5"], "5 × 3; 3 + 3 + 3 + 3 + 3; 3 × 5"),
  "TX": ("Multiple choice", "Rosa has 32 stickers. She puts them in groups of 4. Which equation can be used to find g, the number of groups?", ["32 + 4 = g", "32 − 4 = g", "32 ÷ 4 = g", "32 × 4 = g"], "32 ÷ 4 = g, so g = 8"),
 },
 "m3-facts": {
  "NC": ("Show your thinking", "Use a fact you know to solve 7 × 8. Show your strategy with an array or equations.", None, "56. Example: 5 × 8 = 40 and 2 × 8 = 16, so 40 + 16 = 56."),
  "MI": ("Equation", "Find the missing number: 6 × ☐ = 54. Then write a division fact from the same fact family.", None, "9; 54 ÷ 6 = 9 (or 54 ÷ 9 = 6)"),
  "TX": ("Multiple choice", "Which expression has the same value as 9 × 6?", ["9 + 6", "(5 × 6) + (4 × 6)", "(9 × 5) + 6", "6 × 6 × 3"], "(5 × 6) + (4 × 6) = 30 + 24 = 54"),
 },
 "m3-twostep": {
  "NC": ("Equation with a letter", "The library had 135 books. It got 3 boxes with 8 books in each box. Write an equation with a letter for the unknown, then solve.", None, "135 + (3 × 8) = b; b = 159 books"),
  "MI": ("Constructed response", "Jamal had $45. He spent $18 on a game and split the rest equally into 3 jars. How much money is in each jar? Use estimation to explain why your answer is reasonable.", None, "$9. 45 − 18 = 27 and 27 ÷ 3 = 9. Estimate: 50 − 20 = 30 and 30 ÷ 3 = 10, which is close to 9."),
  "TX": ("Record your answer", "A farmer planted 6 rows of tomato plants with 7 plants in each row. Then 9 plants died. How many tomato plants are left?", None, "33"),
 },
 "m3-place": {
  "NC": ("Number line", "Round 638 to the nearest ten and to the nearest hundred. Show both on a number line.", None, "Nearest ten: 640. Nearest hundred: 600."),
  "MI": ("Multi-select", "Select all numbers that round to 500 when rounded to the nearest hundred.", ["449", "451", "508", "550", "549"], "451, 508, 549"),
  "TX": ("Multiple choice", "Students collected 47,385 cans. What is the value of the digit 7 in 47,385?", ["70", "700", "7,000", "70,000"], "7,000"),
 },
 "m3-fracunit": {
  "NC": ("Number line", "Partition a number line from 0 to 1 into sixths. Label 1/6 and 5/6. How many sixths make 1 whole?", None, "Six equal spaces; 1/6 is the first mark, 5/6 the fifth; 6/6 = 1."),
  "MI": ("Constructed response", "A number line from 0 to 1 is split into 4 equal parts. Point P is on the third mark after 0. What fraction does P show? Explain.", None, "3/4. Each space is 1/4 and P is 3 spaces from 0."),
  "TX": ("Multiple choice", "A strip is divided into 8 equal parts and 3 parts are shaded. Which fraction is shaded?", ["3/5", "3/8", "5/8", "8/3"], "3/8"),
 },
 "m3-fraceq": {
  "NC": ("Model", "Use fraction strips to show that 2/4 = 1/2. Then name a fraction equal to 1/2 that has a denominator of 8.", None, "4/8"),
  "MI": ("Compare and explain", "Compare 3/8 and 3/4 using >, <, or =. Explain with a drawing.", None, "3/8 < 3/4. Both have 3 pieces, but eighths are smaller pieces than fourths."),
  "TX": ("Multiple choice", "Which fraction is equivalent to 2/3?", ["2/6", "4/6", "3/4", "4/3"], "4/6"),
 },
 "m3-area": {
  "NC": ("Two ways", "A rug is 6 feet long and 4 feet wide. Find its area by tiling and by multiplying.", None, "24 square feet"),
  "MI": ("Constructed response", "An L-shaped room is made of a 5 m by 3 m rectangle and a 2 m by 2 m rectangle. What is the total area? Show how you split the shape.", None, "15 + 4 = 19 square meters"),
  "TX": ("Multiple choice", "A rectangle has an area of 36 square units. Its length is 9 units. What is its width?", ["3 units", "4 units", "6 units", "27 units"], "4 units"),
 },
 "m3-perim": {
  "NC": ("Example", "A rectangular garden is 7 feet long and 3 feet wide. What is its perimeter?", None, "20 feet"),
  "MI": ("Constructed response", "Draw two different rectangles that each have an area of 12 square units. Find the perimeter of each.", None, "Example: 2 × 6 has perimeter 16; 3 × 4 has perimeter 14."),
  "TX": ("Record your answer", "A triangle has a perimeter of 24 centimeters. Two sides are 8 cm and 9 cm. How long is the third side, in centimeters?", None, "7"),
 },
 "m3-measure": {
  "NC": ("Number line", "Soccer practice starts at 3:45 p.m. and ends at 4:30 p.m. Use a number line to find how long practice lasts.", None, "45 minutes"),
  "MI": ("Explain", "Would you measure the water in a bathtub in milliliters or liters? Explain your choice.", None, "Liters, because a bathtub holds a large amount of water."),
  "TX": ("Multiple choice", "Recess started at 11:25 a.m. and lasted 35 minutes. What time did recess end?", ["11:50 a.m.", "11:55 a.m.", "12:00 p.m.", "12:05 p.m."], "12:00 p.m."),
 },
 "m3-data": {
  "NC": ("Scaled picture graph", "In a picture graph, each ☺ = 2 students. Pizza has 6 ☺ and tacos has 4 ☺. How many more students chose pizza than tacos?", None, "12 − 8 = 4 more students"),
  "MI": ("Graph and answer", "Make a bar graph with a scale of 5: Dogs 25, Cats 15, Fish 10. How many fewer students chose fish than dogs?", None, "15 fewer"),
  "TX": ("Record your answer", "A bar graph with a scale of 10 shows votes: Red 40, Blue 25, Green 35. How many students voted in all?", None, "100"),
 },
 "m3-shapes": {
  "NC": ("Draw and name", "Draw a quadrilateral that is not a rectangle, a square or a rhombus. Name it and explain why it belongs in the quadrilateral group.", None, "Example: a trapezoid. It has 4 sides and 4 angles."),
  "MI": ("Multi-select", "Select all shapes that are always quadrilaterals.", ["square", "triangle", "rhombus", "trapezoid", "pentagon"], "square, rhombus, trapezoid"),
  "TX": ("Multiple choice", "Which figure has 4 sides and 4 right angles but sides that are not all the same length?", ["square", "rhombus", "rectangle", "trapezoid"], "rectangle"),
 },
 "m3-finlit": {
  "TX": ("Multiple choice", "Ana planned to spend $5 on lunch. At the store she also bought a $2 snack she had not planned on. Which statement is true?", ["The snack was planned spending.", "The snack was unplanned spending, so Ana has $2 less to save.", "Unplanned spending always costs more than planned spending.", "Ana used credit to buy the snack."], "The snack was unplanned spending, so Ana has $2 less to save."),
 },
 # ---------- Grade 4 ----------
 "m4-place": {
  "NC": ("Explain", "How does the value of the 3 in 35,000 compare to the value of the 3 in 3,500?", None, "It is 10 times as much (30,000 vs 3,000)."),
  "MI": ("Equation", "Round 268,451 to the nearest thousand.", None, "268,000"),
  "TX": ("Multiple choice", "Which shows 504,230 in expanded notation?", ["500,000 + 4,000 + 200 + 30", "500,000 + 40,000 + 200 + 30", "50,000 + 4,000 + 200 + 30", "500,000 + 4,000 + 20 + 3"], "500,000 + 4,000 + 200 + 30"),
 },
 "m4-addsub": {
  "NC": ("Algorithm and check", "Solve 6,003 − 2,478 with the standard algorithm. Check your answer with addition.", None, "3,525; 3,525 + 2,478 = 6,003"),
  "MI": ("Constructed response", "A stadium had 45,672 fans on Friday and 38,915 fans on Saturday. How many more fans came on Friday?", None, "6,757"),
  "TX": ("Record your answer", "Mia ran 2.75 miles on Monday and 1.6 miles on Tuesday. How many miles did she run in all?", None, "4.35"),
 },
 "m4-mult": {
  "NC": ("Area model", "Use an area model and partial products to solve 34 × 26.", None, "600 + 80 + 180 + 24 = 884"),
  "MI": ("Equation", "A whale is 8 times as long as a dolphin. The dolphin is 6 feet long. Write an equation and find the whale's length.", None, "8 × 6 = w; w = 48 feet"),
  "TX": ("Multiple choice", "A theater has 24 rows with 35 seats in each row. How many seats are in the theater?", ["59", "720", "840", "850"], "840"),
 },
 "m4-div": {
  "NC": ("Interpret the remainder", "53 students are going on a field trip. Each van holds 7 students. How many vans are needed? Explain what the remainder means.", None, "53 ÷ 7 = 7 R4, so 8 vans. The 4 extra students still need a van."),
  "MI": ("Constructed response", "Use partial quotients to solve 1,248 ÷ 4.", None, "312"),
  "TX": ("Multiple choice", "Mr. Lee shares 196 markers equally among 8 tables. How many markers does each table get, and how many are left over?", ["24, with 4 left over", "24, with 0 left over", "23, with 12 left over", "25, with 4 left over"], "24, with 4 left over"),
 },
 "m4-factors": {
  "NC": ("Factor pairs", "List all factor pairs of 36. Is 36 prime or composite? Explain.", None, "1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6. Composite, because it has more than two factors."),
  "MI": ("Multi-select", "Select all numbers that are multiples of 6.", ["12", "16", "24", "30", "46"], "12, 24, 30"),
  "TX": ("Multiple choice", "An input-output table shows 2 → 10, 4 → 20, 6 → 30, 8 → 40. Which rule describes the table?", ["Add 8", "Multiply by 5", "Add 5", "Multiply by 10"], "Multiply by 5"),
 },
 "m4-fraceq": {
  "NC": ("Area model", "Use an area model to show why 2/3 = 8/12.", None, "Split each third into 4 equal parts: 2 × 4 = 8 shaded out of 3 × 4 = 12."),
  "MI": ("Compare and explain", "Compare 5/8 and 3/4. Explain using a common denominator or a benchmark.", None, "5/8 < 3/4, because 3/4 = 6/8."),
  "TX": ("Multiple choice", "Which fraction is greater than 1/2?", ["3/8", "2/5", "4/6", "1/4"], "4/6"),
 },
 "m4-fracops": {
  "NC": ("Mixed numbers", "Mrs. Jones has 2 3/8 pizzas. Her class eats 1 5/8 pizzas. How much pizza is left?", None, "6/8 (or 3/4) of a pizza"),
  "MI": ("Constructed response", "Write 5/6 as a sum of fractions with the same denominator in two different ways.", None, "Example: 1/6 + 1/6 + 1/6 + 1/6 + 1/6 and 2/6 + 3/6"),
  "TX": ("Record your answer", "Kai walked 3/10 mile in the morning and 5/10 mile in the afternoon. How far did he walk in all?", None, "8/10 mile"),
 },
 "m4-decimals": {
  "NC": ("Model", "Write 47/100 as a decimal and shade it on a hundredths grid.", None, "0.47"),
  "MI": ("Multi-select", "Select all comparisons that are true.", ["0.5 > 0.45", "0.30 = 0.3", "0.07 > 0.7", "0.62 < 0.6"], "0.5 > 0.45; 0.30 = 0.3"),
  "TX": ("Multiple choice", "A number line from 0 to 1 is divided into tenths. Point P is on the seventh mark. Which decimal names point P?", ["0.07", "0.17", "0.7", "7.0"], "0.7"),
 },
 "m4-angles": {
  "NC": ("Missing angle", "Two angles together form a right angle. One angle measures 38°. What is the measure of the other angle?", None, "52°"),
  "MI": ("Draw", "Draw a quadrilateral with exactly one pair of parallel sides and two right angles. Mark the parallel sides.", None, "A right trapezoid."),
  "TX": ("Multiple choice", "Which kind of triangle has one angle that measures more than 90°?", ["acute", "right", "obtuse", "equilateral"], "obtuse"),
 },
 "m4-measure": {
  "NC": ("Formula", "A rectangle has a perimeter of 30 cm and a length of 9 cm. Find its width and its area.", None, "Width 6 cm; area 54 square cm"),
  "MI": ("Table", "Complete the table: 1 foot = 12 inches; 3 feet = ☐ inches; 5 feet = ☐ inches.", None, "36; 60"),
  "TX": ("Record your answer", "A board is 4 yards long. How many feet long is the board?", None, "12"),
 },
 "m4-data": {
  "NC": ("Line plot", "A line plot shows ribbon lengths: 1/4, 1/2, 1/2, 3/4, 3/4, 3/4 inch. What is the difference between the longest and shortest ribbon?", None, "1/2 inch"),
  "MI": ("Constructed response", "Using the same line plot, what is the total length of all the 3/4-inch ribbons?", None, "9/4 = 2 1/4 inches"),
  "TX": ("Record your answer", "A stem-and-leaf plot shows 2 | 3 5 8 and 3 | 0 4. What is the difference between the greatest and least values?", None, "34 − 23 = 11"),
 },
 "m4-finlit": {
  "TX": ("Record your answer", "A lemonade stand earned $36. The supplies cost $14. What was the profit, in dollars?", None, "22"),
 },
 # ---------- Grade 5 ----------
 "m5-place": {
  "NC": ("Expanded form", "Write 3.507 in expanded form.", None, "3 + 0.5 + 0.007, or 3 × 1 + 5 × (1/10) + 7 × (1/1,000)"),
  "MI": ("Explain", "Explain why 4.3 × 10 = 43 using place value.", None, "Each digit becomes 10 times as large and moves one place to the left."),
  "TX": ("Multiple choice", "Which decimal rounds to 6.4 when rounded to the nearest tenth?", ["6.33", "6.35", "6.46", "6.48"], "6.35"),
 },
 "m5-multdiv": {
  "NC": ("Partial quotients", "Solve 1,512 ÷ 24 using partial quotients. Check with multiplication.", None, "63; 24 × 63 = 1,512"),
  "MI": ("Constructed response", "A school orders 215 boxes of pencils with 36 pencils in each box. How many pencils is that?", None, "7,740"),
  "TX": ("Record your answer", "A factory packs 2,856 cans into boxes of 24. How many boxes does it fill?", None, "119"),
 },
 "m5-decops": {
  "NC": ("Area model", "Use a hundredths grid to show 0.4 × 0.6.", None, "0.24"),
  "MI": ("Constructed response", "Sam buys 3 notebooks for $2.45 each and pays with a $10 bill. How much change does he get?", None, "$2.65"),
  "TX": ("Record your answer", "A ribbon 4.8 meters long is cut into 6 equal pieces. How long is each piece, in meters?", None, "0.8"),
 },
 "m5-fracaddsub": {
  "NC": ("Area model", "Find 2/3 + 1/4. Use an area model to find a common denominator.", None, "8/12 + 3/12 = 11/12"),
  "MI": ("Error analysis", "Maria says 1/2 + 1/3 = 2/5. Is she correct? Use a benchmark to explain, then find the correct sum.", None, "No. 2/5 is less than 1/2, so it can't be the sum. 1/2 + 1/3 = 5/6."),
  "TX": ("Multiple choice", "Jada used 3 1/2 cups of flour and 1 2/3 cups of sugar. How much more flour than sugar did she use?", ["1 5/6 cups", "2 1/6 cups", "1 1/6 cups", "2 1/2 cups"], "1 5/6 cups"),
 },
 "m5-fracmult": {
  "NC": ("Area model", "Use an area model to find 2/3 × 3/4.", None, "6/12 = 1/2"),
  "MI": ("Scaling", "Without calculating, is 5/6 × 12 greater than or less than 12? Explain.", None, "Less, because 12 is multiplied by a fraction less than 1."),
  "TX": ("Record your answer", "A recipe uses 3/4 cup of milk for each batch. How many cups of milk are needed for 6 batches?", None, "4 1/2 (18/4)"),
 },
 "m5-fracdiv": {
  "NC": ("Model", "How many 1/3-cup servings are in 4 cups of trail mix? Draw a model.", None, "12 servings; 4 ÷ 1/3 = 12"),
  "MI": ("Constructed response", "Four friends share 1/2 pound of fudge equally. How much does each friend get? Draw a model.", None, "1/8 pound; 1/2 ÷ 4 = 1/8"),
  "TX": ("Multiple choice", "What is the value of 5 ÷ 1/4?", ["5/4", "1/20", "20", "9"], "20"),
 },
 "m5-expr": {
  "NC": ("Evaluate", "Evaluate 3 × (12 − 4) + 6.", None, "3 × 8 + 6 = 30"),
  "MI": ("Write and compare", "Write an expression for \"add 7 and 5, then multiply by 4.\" Without calculating, compare its value with 7 + 5.", None, "(7 + 5) × 4; it is 4 times as large as 7 + 5."),
  "TX": ("Multiple choice", "Which number is prime?", ["21", "27", "29", "33"], "29"),
 },
 "m5-coord": {
  "NC": ("Plot and explain", "Plot (2, 5) and (5, 2) on a coordinate plane. Explain why they are different points.", None, "The first number is the distance along the x-axis and the second is along the y-axis, so switching them changes the location."),
  "MI": ("Patterns", "Rule A: start at 0 and add 2. Rule B: start at 0 and add 6. Write the first four ordered pairs (A, B) and describe the relationship.", None, "(0, 0), (2, 6), (4, 12), (6, 18). Each B term is 3 times the A term."),
  "TX": ("Multiple choice", "Point A is 4 units to the right of the origin and 7 units up. Which ordered pair names point A?", ["(7, 4)", "(4, 7)", "(4, 0)", "(0, 7)"], "(4, 7)"),
 },
 "m5-volume": {
  "NC": ("Layers", "A box has a base of 4 cm by 3 cm and a height of 5 cm. Find its volume by thinking in layers.", None, "12 cubes per layer × 5 layers = 60 cubic cm"),
  "MI": ("Composite figure", "A figure is made of a 5 × 2 × 3 prism and a 2 × 2 × 3 prism that do not overlap. What is the total volume?", None, "30 + 12 = 42 cubic units"),
  "TX": ("Record your answer", "A rectangular prism has a volume of 96 cubic inches, a length of 4 inches and a width of 3 inches. What is its height, in inches?", None, "8"),
 },
 "m5-shapes": {
  "NC": ("True or false", "True or false: every square is a rhombus. Explain using properties.", None, "True. A square has 4 equal sides, which is the property that defines a rhombus."),
  "MI": ("Multi-select", "Select all statements that are always true.", ["A rectangle is a parallelogram.", "A trapezoid is a parallelogram.", "A square is a rectangle.", "A rhombus is a square."], "A rectangle is a parallelogram; A square is a rectangle."),
  "TX": ("Multiple choice", "Which category includes squares, rectangles and rhombuses?", ["triangles", "parallelograms", "pentagons", "hexagons"], "parallelograms"),
 },
 "m5-measure-data": {
  "NC": ("Conversion", "Use a conversion chart to convert 3.5 kilometers to meters.", None, "3,500 meters"),
  "MI": ("Line plot", "A line plot shows 4 beakers holding 1/4, 1/2, 1/2 and 3/4 liter. If the water were shared equally, how much would each beaker hold?", None, "Total 2 liters ÷ 4 = 1/2 liter"),
  "TX": ("Record your answer", "A rope is 5 yards long. How many feet long is it?", None, "15"),
 },
 "m5-finlit": {
  "TX": ("Record your answer", "Ms. Cruz has a gross income of $2,400 per month. $360 is withheld for taxes. What is her net income, in dollars?", None, "2,040"),
 },
}

# ---------- ELA (shared across grades 3-5; {g} is the grade) ----------
THEO = "Theo's kite snagged in the oak tree for the third time. He kicked the dirt, then stared at the knotted string. Slowly, he began to untie each knot."
BEES = "Honeybees do more than make honey. As they move from flower to flower, they carry pollen that helps plants make seeds. Farmers depend on bees to pollinate crops such as apples and almonds."

ELA = {
 "evidence": {
  "NC": ("Text evidence", f"Read: “{THEO}” What can you infer about Theo? Give two details from the text that support your inference.", None, "He is frustrated but does not give up. “He kicked the dirt” shows frustration; “Slowly, he began to untie each knot” shows determination."),
  "MI": ("Two-part (Part A / Part B)", f"Read: “{THEO}” Part A: What does Theo's action at the end show? Part B: Which sentence best supports your answer to Part A?", ["He gives up on the kite.", "He is patient and determined.", "He is angry at a friend.", "He wants a new kite."], "Part A: He is patient and determined. Part B: “Slowly, he began to untie each knot.”"),
  "TX": ("Multiple choice", f"Read: “{THEO}” Which sentence best shows that Theo is frustrated?", ["Theo's kite snagged in the oak tree for the third time.", "He kicked the dirt, then stared at the knotted string.", "Slowly, he began to untie each knot.", "The kite was red."], "He kicked the dirt, then stared at the knotted string."),
 },
 "theme": {
  "NC": ("Theme statement", "After reading the fable “The Ant and the Grasshopper,” write the theme as a complete sentence and give two details that support it.", None, "Example: It is wise to prepare for hard times. The ant stores food all summer; the grasshopper has nothing when winter comes."),
  "MI": ("Two-part (Part A / Part B)", "Part A: Which statement best expresses a theme of “The Ant and the Grasshopper”? Part B: Which detail best supports your answer?", ["Grasshoppers like to sing.", "Hard work now can help you later.", "Winter is the coldest season.", "Ants live in large groups."], "Part A: Hard work now can help you later. Part B: The ant gathers food all summer while the grasshopper plays."),
  "TX": ("Short constructed response", "What is a theme of “The Ant and the Grasshopper”? Use evidence from the fable to support your answer.", None, "Scored on a stated theme plus text evidence, for example: plan ahead, because the ant stores grain and survives the winter."),
 },
 "character": {
  "NC": ("Describe in depth", f"Read: “{THEO}” Describe how Theo changes from the beginning to the end of this scene. Use specific details. (Grade 5: compare Theo with another character you have read about.)", None, "He moves from frustrated (kicks the dirt) to calm and determined (slowly unties each knot)."),
  "MI": ("Selected response + evidence", f"Read: “{THEO}” Which word best describes Theo at the end? Then quote the words that show it.", ["careless", "persistent", "jealous", "shy"], "persistent; “Slowly, he began to untie each knot.”"),
  "TX": ("Multiple choice", "In a story set in a windy park, Theo's kite keeps getting stuck in trees. How does the setting affect the plot?", ["The wind causes the problem with the kite.", "The park is where Theo lives.", "The trees make the story happy.", "The setting does not matter."], "The wind causes the problem with the kite."),
 },
 "mainidea": {
  "NC": ("Main idea and details", f"Read: “{BEES}” What is the main idea? Which two details support it?", None, "Bees are important to plants and farms. Details: they carry pollen that helps plants make seeds; farmers depend on them to pollinate crops."),
  "MI": ("Two-part (Part A / Part B)", f"Read: “{BEES}” Part A: What is the main idea? Part B: Which sentence best supports it?", ["Bees make honey.", "Bees are important pollinators for plants and crops.", "Apples grow on trees.", "Farmers like bees."], "Part A: Bees are important pollinators for plants and crops. Part B: “Farmers depend on bees to pollinate crops such as apples and almonds.”"),
  "TX": ("Multiple choice", f"Read: “{BEES}” Which sentence best states the central idea of the paragraph?", ["Honeybees make honey.", "Bees help plants and farms by carrying pollen.", "Almonds are a kind of crop.", "Flowers have pollen."], "Bees help plants and farms by carrying pollen."),
 },
 "structure": {
  "NC": ("Identify structure", "Read: “Because the river flooded every spring, the town built a levee. As a result, homes stayed dry the next year.” Name the text structure and the signal words.", None, "Cause and effect; “because” and “as a result.”"),
  "MI": ("Multi-select", "Read the same paragraph. Select all words or phrases that signal a cause-and-effect structure.", ["Because", "the town", "As a result", "next year", "homes"], "Because; As a result"),
  "TX": ("Multiple choice", "How does the author organize the paragraph about the flooded river?", ["chronological order", "compare and contrast", "cause and effect", "description"], "cause and effect"),
 },
 "vocab": {
  "NC": ("Context clues", "Read: “The hikers were exhausted after the long climb, so they rested by the stream.” What does exhausted mean? Which words helped you?", None, "Very tired; “after the long climb” and “so they rested.”"),
  "MI": ("Two-part (Part A / Part B)", "Part A: In the sentence about the hikers, what does exhausted mean? Part B: Which phrase helps the reader understand it?", ["excited", "very tired", "lost", "hungry"], "Part A: very tired. Part B: “so they rested by the stream.”"),
  "TX": ("Multiple choice", "The prefix un- in unbreakable means —", ["again", "not", "before", "full of"], "not"),
 },
 "figlang": {
  "NC": ("Explain", "Explain the simile in this sentence: “The new snow was as soft as a blanket.” What does it help you picture?", None, "It compares snow to a blanket to show the snow is soft and thick."),
  "MI": ("Multiple choice", "Which sentence uses a metaphor?", ["The classroom was a zoo after lunch.", "The dog ran like the wind.", "She walked slowly to the bus.", "The sun was very hot."], "The classroom was a zoo after lunch."),
  "TX": ("Multiple choice", "Read: “The wind whispered through the trees.” The author uses personification to —", ["show the wind was loud", "help the reader imagine a soft, quiet sound", "explain where trees grow", "describe the weather report"], "help the reader imagine a soft, quiet sound"),
 },
 "genre": {
  "NC": ("Explain structure", "Explain two ways a drama is different from a story. Use the words cast of characters, dialogue or stage directions.", None, "Dramas list a cast of characters and tell the story through dialogue and stage directions instead of a narrator."),
  "MI": ("Constructed response", "A story is told by a narrator who says “I” and “me.” What point of view is it? How would the story change if another character told it?", None, "First person. Another narrator would share different thoughts and feelings and might describe events differently."),
  "TX": ("Multiple choice", "In a poem, a group of lines set apart from other lines is called a —", ["paragraph", "stanza", "scene", "chapter"], "stanza"),
 },
 "compare": {
  "NC": ("Compare texts", "Read two articles about sea turtles. Explain one way the information is the same and one way it is different.", None, "Answers name a shared fact (both say turtles lay eggs on beaches) and a difference (only one explains how lights confuse hatchlings)."),
  "MI": ("Research-style constructed response", "Using both articles, explain why sea turtles need protection. Use one detail from each source.", None, "Scored on combining information from both sources with a detail from each."),
  "TX": ("Multiple choice", "“The Ant and the Grasshopper” and “The Tortoise and the Hare” are alike because both —", ["take place in winter", "teach a lesson through animal characters", "have a narrator who says “I”", "are informational texts"], "teach a lesson through animal characters"),
 },
 "opinion": {
  "NC": ("Writing task", "Should recess be longer? Write an opinion piece. State your opinion, give reasons supported by facts and details, use linking words, and write a conclusion.", None, "Look for: clear opinion, logically ordered reasons with facts, linking words (for example, because, therefore) and a concluding section."),
  "MI": ("Performance task", "You read two articles about school gardens. Write an opinion essay for your principal about whether your school should start a garden. Use information from both articles.", None, "Scored on purpose and organization, evidence and elaboration, and conventions."),
  "TX": ("Extended constructed response", "Read two passages about weekend homework. Write an argumentative essay that states your position and supports it with evidence from both passages.", None, "Scored on development and organization of ideas and on conventions."),
 },
 "informative": {
  "NC": ("Writing task", "Write an informative piece that explains how a volcano forms. Group related information in paragraphs, use headings and include domain words such as magma and crust.", None, "Look for: introduction, grouped facts, precise vocabulary, linking words, concluding statement."),
  "MI": ("Performance task", "Using the sources about honeybees, write an informational article for the school newsletter explaining how bees help farms.", None, "Scored on purpose and organization, evidence and elaboration, and conventions."),
  "TX": ("Extended constructed response", "Read the passages about recycling. Write an informational essay that explains how recycling helps a community. Use evidence from the passages.", None, "Scored on development and organization of ideas and on conventions."),
 },
 "narrative": {
  "NC": ("Writing task", "Write a personal narrative about a time you learned something new. Use dialogue, sensory details and transition words to show the order of events.", None, "Look for: a clear situation, dialogue, description, a logical sequence and a conclusion."),
  "MI": ("Performance task", "Write a narrative that continues the kite story from the oak tree's point of view.", None, "Scored on narrative focus, development with dialogue and description, and conventions."),
  "TX": ("TEKS classroom task", "Compose a personal narrative about a challenge you faced. Develop the story with a beginning, middle and end and specific details. (Narrative writing is taught in the TEKS but is not a STAAR essay type.)", None, "Look for: focused structure, engaging details, and edited conventions."),
 },
 "process": {
  "NC": ("Edit", "Edit this sentence: “me and jake goes to the park yesterday.”", None, "Jake and I went to the park yesterday."),
  "MI": ("Multiple choice", "Which revision correctly fixes this run-on? “Our class visited the museum we saw dinosaur bones.”", ["Our class visited the museum, we saw dinosaur bones.", "Our class visited the museum. We saw dinosaur bones.", "Our class visited, the museum we saw dinosaur bones.", "Our class visited the museum we, saw dinosaur bones."], "Our class visited the museum. We saw dinosaur bones."),
  "TX": ("Revising and editing", "Sentence 3 of a student draft reads: “The team practiced every day, they won the championship.” What is the best way to correct sentence 3?", ["Change the comma to a period and capitalize they", "Delete the comma", "Change practiced to practice", "No change is needed"], "Change the comma to a period and capitalize they"),
 },
 "research": {
  "NC": ("Research task", "Research question: How do bats find food at night? Take notes from two sources in your own words and list both sources.", None, "Notes are paraphrased (echolocation, insects) and both sources are listed."),
  "MI": ("Multiple choice", "A student is researching how bats find food. Which source would be most useful?", ["a poem about the night sky", "a science website about echolocation", "a story about a vampire", "a map of caves"], "a science website about echolocation"),
  "TX": ("Multiple choice", "A student is researching the Alamo. Which is a primary source?", ["a letter written by a defender in 1836", "an encyclopedia article", "a textbook chapter", "a movie made in 2004"], "a letter written by a defender in 1836"),
 },
 "foundations": {
  "NC": ("Word analysis", "Read the word unbelievable by breaking it into parts. Name the prefix and suffix.", None, "un / be / liev / able; prefix un-, suffix -able."),
  "MI": ("Fluency check", "Read a grade {g} passage aloud for one minute. The teacher records words correct per minute and rates expression.", None, "Compare words correct per minute to grade {g} norms and note phrasing and expression."),
  "TX": ("Decoding", "Divide transportation and invisible into syllables, then read each word.", None, "trans / por / ta / tion; in / vis / i / ble"),
 },
}


STYLE["ALL"] = "K–2 classroom check"


def ela_items(g):
    """Reading and writing items for one grade, keyed by concept key."""
    if g in (3, 4, 5):
        return items_for(g)
    import ela_k2_6 as EK
    d = dict(EK.R[g])
    if g == 6:
        import passages
        passages.W[6] = EK.W6
        passages.TEXTS[6] = EK.TEXTS[6]
        w = passages.writing_items(6)
        w.pop("foundations")
        fix = lambda t: t if not isinstance(t, str) else (t.replace("Write an opinion piece. State your opinion", "Write an argument. State a claim")
                                                           .replace("Write an opinion essay", "Write an argumentative essay")
                                                           .replace("clear opinion", "clear claim"))
        w["opinion"] = {st: tuple(fix(x) for x in it) for st, it in w["opinion"].items()}
        d.update(w)
    else:
        d.update(EK.k2_writing(g))
    return d


def build(concepts):
    from math_k2_6 import EX as MATH_MORE
    out = {}
    for c in concepts:
        if c["subject"] == "math":
            src = MATH.get(c["id"]) or MATH_MORE.get(c["id"], {})
        else:
            key = c["id"].split("-", 1)[1]
            src = {st: (it[0], it[2], it[3], it[4], it[1]) for st, it in ela_items(c["grade"])[key].items()}
        if "ALL" in src:
            src = {st: src["ALL"] for st in ("NC", "MI", "TX") if c["codes"][st]}
            shared = True
        else:
            shared = False
        ex = {}
        for st, item in src.items():
            fmt, prompt, choices, answer = item[:4]
            text = item[4] if len(item) > 4 else None
            if choices and choices[0] == answer and c["subject"] == "ela":
                k = (c["grade"] + len(st) + len(prompt)) % len(choices)
                choices = choices[k:] + choices[:k]
            ex[st] = dict(style=STYLE["ALL" if shared else st], format=fmt, prompt=prompt, choices=choices, answer=answer, text=text)
            if shared:
                ex[st]["shared"] = True
        out[c["id"]] = ex
    return out
