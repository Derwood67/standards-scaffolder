"""Original grade-level ELA passages (grades 3-5) and the state-style items that use them.

Each grade has three texts on one topic: a story, an informational article and a poem.
ITEMS[grade][concept_key][STATE] = (format, text_ref, prompt, choices_or_None, answer)
text_ref: "story" | "article" | "poem" | "pair" (story + article) | None
"""

TEXTS = {
 3: {
  "topic": "Seeds",
  "story": ("The Seed Swap", """Every spring, Grandma Rose hosted a seed swap on her front porch. Neighbors brought envelopes of seeds and traded them like baseball cards.

This year, Lila wanted to bring something special. She had saved seeds from her sunflower, the tallest one on Maple Street. But when she opened her jar, the seeds were gray and fuzzy with mold.

"They're ruined," Lila said. Her chin wobbled.

Grandma Rose looked at the jar. "Seeds need to stay dry," she said gently. "Next fall, we'll dry them on a screen first."

Lila sat on the steps while neighbors traded. She had nothing to give. Then Mr. Okafor waved her over. "I have too many pepper seeds," he said. "Would you help me count them into envelopes?"

Lila counted carefully, ten seeds in each envelope. By the end of the afternoon, she had filled twenty envelopes. Mr. Okafor handed her one. "For your hard work," he said.

That night, Lila wrote a label for a new jar: DRY FIRST."""),
  "article": ("How Seeds Travel", """Plants cannot walk, but their seeds still find new places to grow. Seeds travel in several ways.

Some seeds ride the wind. A dandelion seed has a fluffy top that works like a parachute. A gust of wind can carry it far across a field.

Other seeds hitch a ride on animals. Burdock seeds are covered in tiny hooks. When a dog brushes past, the hooks catch its fur. Later, the seeds fall off in a new spot.

Some seeds float. A coconut has a hard, waterproof shell, so it can drift across the ocean and land on a faraway beach.

Animals also move seeds by eating fruit. A bird eats a berry, flies away, and drops the seed somewhere new.

Because seeds spread out, young plants do not have to compete with their parent plant for sunlight and water."""),
  "poem": ("Sunflower", """I am a ladder of green
climbing up to the sky,
my face a bright yellow clock
that follows the sun going by.

In the morning I look east,
at night I bow my head;
the bees hum their thank-you songs
as I tuck my seeds to bed."""),
 },
 4: {
  "topic": "Sea turtles",
  "story": ("Turtle Patrol", """At sunrise, Marcus and his older cousin Jada walked the beach at Emerald Isle with a clipboard and a flashlight. They were volunteers on the Turtle Patrol.

"Look for tracks that look like a tractor drove out of the ocean," Jada said.

Marcus yawned. He had wanted to sleep in. Walking in cold sand at six in the morning did not feel like summer vacation.

Then he saw them: two wide lines of flipper marks leading from the waves to the dunes. At the end, the sand was piled in a messy circle.

"A nest!" Marcus shouted, forgetting to be tired.

Jada showed him how to place wooden stakes and orange tape around the nest so no one would step on it. Marcus wrote the date and location on the clipboard, pressing hard so his letters were neat.

For the rest of the summer, Marcus woke up before his alarm. He checked the nest every morning. Sixty days later, he watched tiny turtles, each one smaller than his palm, scramble toward the moonlit water.

"Go on," he whispered. "We kept your spot safe." """),
  "article": ("Sea Turtle Hatchlings: A Risky Start", """Loggerhead sea turtles nest on North Carolina beaches every summer. A female crawls onto the sand at night, digs a hole, and lays about 100 eggs. Then she returns to the sea and never sees her babies.

After about two months, the hatchlings break out of their shells. They usually leave the nest at night, when the sand is cool and fewer predators are awake. The hatchlings find the ocean by crawling toward the brightest horizon, which is normally the moonlight on the water.

Today, that instinct can cause problems. Lights from houses and streets can confuse hatchlings, so they crawl the wrong way. Ghost crabs and birds also hunt them.

People can help. Many beach towns ask residents to turn off outdoor lights during nesting season. Volunteers mark nests so they are not disturbed. Scientists estimate that only about 1 in 1,000 hatchlings survives to adulthood, so every protected nest matters."""),
  "poem": ("The Ocean at Night", """The ocean is a restless giant
who breathes in, then breathes out,
his silver blanket of moonlight
rumpled and tossed about.

He hums a low and salty song
to the dunes along the shore,
and little turtles answer him
by racing to his door."""),
 },
 5: {
  "topic": "Learning from failure",
  "story": ("Twelve Seconds", """The robot rolled three feet, beeped, and spun in a slow circle until it crashed into the table leg.

"Again?" groaned Priya. The regional robotics competition was in four days, and their robot, Bolt, still could not finish the twelve-second course.

Andre slumped in his chair. "Maybe we should just drop out. The other teams have been building since August."

Priya didn't answer right away. She was staring at the laptop screen, where line after line of code glowed. Mr. Haynes, their coach, had told them that every crash was information. At the time, it had sounded like something adults say to make you feel better. Now Priya wondered if he meant it.

"Every time it spins, it's after the second turn," she said slowly. "What if the turn isn't the problem? What if it's the sensor reading the black tape?"

Andre sat up. They tested the sensor with a flashlight, then with the lights off. The readings jumped wildly whenever the room got brighter.

It took two more afternoons and one shoebox, taped around the sensor like a tiny tunnel, but on Friday, Bolt crossed the finish line in eleven seconds.

Andre grinned. "Information," he said."""),
  "article": ("Failing Forward: How Engineers Learn from Mistakes", """When people picture inventors, they often imagine a brilliant idea that works on the first try. In reality, engineers expect their designs to fail, and they plan for it.

Engineers follow a process often called the engineering design cycle. First, they define the problem and research what has already been tried. Next, they brainstorm ideas and build a prototype, a simple early model. Then they test the prototype, collect data, and look for weaknesses. Finally, they improve the design and test again. The cycle may repeat dozens of times.

Failure gives engineers useful data. When the Wright brothers' early gliders did not lift as much as they expected, the brothers built a small wind tunnel in 1901 and tested about 200 wing shapes. Those measurements helped them design the 1903 Wright Flyer, which made the first powered, controlled airplane flight.

Many engineering teams today test parts until they break on purpose. By finding the weakest point in a safe test, they can make the final product stronger. As one saying puts it, it is better to fail early, fail small, and learn fast."""),
  "poem": ("Prototype", """My first try was a paper boat
that sank before it sailed;
my second was a cardboard kite
that dove, and twirled, and failed.

But every crumpled, soggy wreck
was whispering a clue,
a stepping stone of "not quite yet"
that led me to "it's true!"

So call my failures what they are:
a map, a ladder, a key,
each one a door I opened up
to the builder I will be."""),
 },
}

R = {}  # reading items: R[g][key][state]

R[3] = {
 "evidence": {
  "NC": ("Text evidence", "story", "How does Lila feel when she opens her jar of seeds? Use two details from the story to explain how you know.", None, "Upset or disappointed. She says, \"They're ruined,\" and \"Her chin wobbled.\""),
  "MI": ("Two-part (Part A / Part B)", "story", "Part A: Why does Mr. Okafor give Lila an envelope of seeds? Part B: Which sentence from the story best supports your answer to Part A?", ["He feels sorry that her seeds got moldy.", "He wants to thank her for her hard work.", "He has no room left for his seeds.", "Grandma Rose asked him to."], "Part A: He wants to thank her for her hard work. Part B: \"For your hard work,\" he said."),
  "TX": ("Multiple choice", "story", "Which sentence from the story shows that Lila learned from her mistake?", ["Every spring, Grandma Rose hosted a seed swap on her front porch.", "Lila sat on the steps while neighbors traded.", "Lila counted carefully, ten seeds in each envelope.", "That night, Lila wrote a label for a new jar: DRY FIRST."], "That night, Lila wrote a label for a new jar: DRY FIRST."),
 },
 "theme": {
  "NC": ("Central message", "story", "What is the central message of \"The Seed Swap\"? Explain how Lila's actions show this message.", None, "Example: A mistake can teach you something, and you can still find a way to help. Lila helps Mr. Okafor and learns to dry her seeds first."),
  "MI": ("Two-part (Part A / Part B)", "story", "Part A: Which statement best describes the central message of the story? Part B: Which detail best supports your answer?", ["Seeds are easy to grow.", "When something goes wrong, you can still learn and help others.", "Neighbors should trade baseball cards.", "Sunflowers grow very tall."], "Part A: When something goes wrong, you can still learn and help others. Part B: Lila helps count seeds and writes DRY FIRST on a new jar."),
  "TX": ("Short constructed response", "story", "What lesson does Lila learn in \"The Seed Swap\"? Use evidence from the story to support your answer.", None, "Scored on a clear lesson with text evidence, for example: seeds must be dried before saving, shown by Grandma Rose's advice and the DRY FIRST label."),
 },
 "character": {
  "NC": ("Describe a character", "story", "Describe Lila at the beginning and at the end of the story. How do her actions change what happens?", None, "At first she is upset and has nothing to trade. By helping Mr. Okafor she earns pepper seeds and makes a plan for next year."),
  "MI": ("Selected response + evidence", "story", "Which word best describes Lila when she helps Mr. Okafor? Then copy the sentence that shows it.", ["careless", "hardworking", "jealous", "bored"], "hardworking; \"Lila counted carefully, ten seeds in each envelope.\""),
  "TX": ("Multiple choice", "story", "How does Grandma Rose help Lila?", ["She buys Lila new sunflower seeds.", "She explains why the seeds got moldy and how to save them next time.", "She trades the moldy seeds for pepper seeds.", "She tells Lila to go inside."], "She explains why the seeds got moldy and how to save them next time."),
 },
 "mainidea": {
  "NC": ("Main idea and key details", "article", "What is the main idea of \"How Seeds Travel\"? Recount two key details that support it.", None, "Seeds travel to new places in different ways. Details: dandelion seeds ride the wind; burdock seeds hook onto animal fur."),
  "MI": ("Two-part (Part A / Part B)", "article", "Part A: What is the main idea of the article? Part B: Which sentence best supports it?", ["Dandelions have fluffy tops.", "Seeds move to new places in different ways.", "Dogs have thick fur.", "Coconuts have hard shells."], "Part A: Seeds move to new places in different ways. Part B: \"Seeds travel in several ways.\""),
  "TX": ("Multiple choice", "article", "Which detail best supports the idea that some seeds travel by water?", ["A dandelion seed has a fluffy top.", "Burdock seeds are covered in tiny hooks.", "A coconut has a hard, waterproof shell, so it can drift across the ocean.", "A bird eats a berry."], "A coconut has a hard, waterproof shell, so it can drift across the ocean."),
 },
 "structure": {
  "NC": ("Text features", "article", "How does the author organize \"How Seeds Travel\"? Which paragraphs would you read to learn how animals move seeds?", None, "Each paragraph explains one way seeds travel. Paragraphs 3 and 5 explain how animals move seeds."),
  "MI": ("Multi-select", "article", "Select all the ways seeds travel that the article describes.", ["riding the wind", "hooking onto animal fur", "floating on water", "being eaten by animals", "rolling downhill"], "riding the wind; hooking onto animal fur; floating on water; being eaten by animals"),
  "TX": ("Multiple choice", "article", "Why does the author include the last paragraph?", ["To describe how dandelions look", "To explain why it helps plants when seeds spread out", "To tell a story about a dog", "To compare birds and coconuts"], "To explain why it helps plants when seeds spread out"),
 },
 "vocab": {
  "NC": ("Context and word parts", "article", "In paragraph 4 of \"How Seeds Travel,\" what does waterproof mean? Explain the clues that helped you.", None, "Water cannot get in. The word parts water + proof and the clue that the coconut can drift across the ocean."),
  "MI": ("Two-part (Part A / Part B)", "article", "Part A: What does hitch mean in \"Other seeds hitch a ride on animals\"? Part B: Which words help you understand it?", ["to tie a knot", "to catch or get", "to fix something", "to jump high"], "Part A: to catch or get. Part B: \"the hooks catch its fur.\""),
  "TX": ("Multiple choice", "story", "In the story, Lila \"counted carefully.\" The suffix -ly in carefully tells —", ["how she counted", "when she counted", "where she counted", "who counted"], "how she counted"),
 },
 "figlang": {
  "NC": ("Nonliteral language", "poem", "The poet writes, \"my face a bright yellow clock.\" What does this help you understand about the sunflower?", None, "The flower is round and yellow, and it moves with the time of day as it follows the sun."),
  "MI": ("Multiple choice", "poem", "Which line compares the sunflower to something else?", ["I am a ladder of green", "In the morning I look east", "at night I bow my head", "as I tuck my seeds to bed"], "I am a ladder of green"),
  "TX": ("Multiple choice", "poem", "The poet says the bees \"hum their thank-you songs.\" This helps the reader picture —", ["bees buzzing happily around the flower", "bees singing in a choir", "bees leaving the garden", "bees sleeping at night"], "bees buzzing happily around the flower"),
 },
 "genre": {
  "NC": ("Parts of a poem", "poem", "How many stanzas are in \"Sunflower\"? Name one way a poem is different from a story like \"The Seed Swap.\"", None, "Two stanzas. A poem is written in lines and stanzas, often with rhyme; a story is written in paragraphs."),
  "MI": ("Constructed response", "poem", "Who is speaking in \"Sunflower\"? How is that different from who tells \"The Seed Swap\"?", None, "The sunflower speaks, using \"I.\" \"The Seed Swap\" is told by a narrator who is not a character."),
  "TX": ("Multiple choice", "poem", "Which pair of words from the poem rhyme?", ["sky / by", "green / east", "clock / morning", "bees / songs"], "sky / by"),
 },
 "compare": {
  "NC": ("Compare texts", "pair", "\"The Seed Swap\" and \"How Seeds Travel\" are both about seeds. Write one fact you learned from the article and one thing the story shows about seeds.", None, "Article: seeds travel by wind, animals and water. Story: seeds must be dried before they are saved, and people trade seeds."),
  "MI": ("Constructed response", "pair", "Using both texts, explain how people and nature help seeds get to new places.", None, "People trade seeds at the swap; in nature, wind, water and animals carry seeds."),
  "TX": ("Multiple choice", "pair", "How are \"The Seed Swap\" and \"How Seeds Travel\" alike?", ["Both are poems.", "Both show ways seeds get to new places.", "Both are about a dog.", "Both take place at night."], "Both show ways seeds get to new places."),
 },
}

R[4] = {
 "evidence": {
  "NC": ("Text evidence", "story", "What can you infer about how Marcus feels about the Turtle Patrol by the end of the story? Refer to details and examples in the text.", None, "He cares about it now. He wakes up before his alarm, checks the nest every morning and whispers to the hatchlings."),
  "MI": ("Two-part (Part A / Part B)", "story", "Part A: How does Marcus feel at the beginning of the story? Part B: Which detail best supports your answer?", ["excited", "tired and unhappy to be up early", "afraid of the ocean", "proud of his clipboard"], "Part A: tired and unhappy to be up early. Part B: \"Marcus yawned. He had wanted to sleep in.\""),
  "TX": ("Multiple choice", "article", "Which detail from the article best supports the idea that people can protect hatchlings?", ["A female lays about 100 eggs.", "Ghost crabs and birds also hunt them.", "Many beach towns ask residents to turn off outdoor lights during nesting season.", "The hatchlings break out of their shells."], "Many beach towns ask residents to turn off outdoor lights during nesting season."),
 },
 "theme": {
  "NC": ("Theme and summary", "story", "Determine a theme of \"Turtle Patrol\" from details in the text. Then write a short summary of the story.", None, "Theme: Caring for something can change how you feel about hard work. Summary: Marcus doesn't want to patrol, finds a nest, helps protect it all summer and watches the turtles hatch."),
  "MI": ("Two-part (Part A / Part B)", "story", "Part A: Which statement best expresses a theme of the story? Part B: Which detail best supports it?", ["Summer vacation should be relaxing.", "Taking responsibility for something can make you care about it.", "Turtles are hard to find.", "Cousins always get along."], "Part A: Taking responsibility for something can make you care about it. Part B: \"For the rest of the summer, Marcus woke up before his alarm.\""),
  "TX": ("Short constructed response", "story", "What theme does the author develop in \"Turtle Patrol\"? Use evidence from the story to support your answer.", None, "Scored on a stated theme with evidence, for example: helping others gives you purpose, shown by Marcus checking the nest every day."),
 },
 "character": {
  "NC": ("Describe in depth", "story", "Describe Marcus in depth using specific details. How do his thoughts and actions change during the story?", None, "He starts sleepy and reluctant (yawns, wants to sleep in). Finding the nest excites him, and he becomes responsible and caring."),
  "MI": ("Selected response + evidence", "story", "What event causes Marcus to change? Quote the sentence that shows his change in feeling.", ["Jada gives him a flashlight.", "He finds the turtle tracks and nest.", "He writes on the clipboard.", "The sun rises."], "He finds the turtle tracks and nest; \"'A nest!' Marcus shouted, forgetting to be tired.\""),
  "TX": ("Multiple choice", "story", "How does the setting of an early-morning beach affect Marcus at the start of the story?", ["It makes him feel tired and unhappy.", "It makes him want to swim.", "It scares him.", "It makes him forget the clipboard."], "It makes him feel tired and unhappy."),
 },
 "mainidea": {
  "NC": ("Main idea and summary", "article", "Determine the main idea of \"Sea Turtle Hatchlings: A Risky Start\" and explain how key details support it. Then summarize the article.", None, "Hatchlings face many dangers, but people can help. Details: lights confuse them; crabs and birds hunt them; towns turn off lights and volunteers mark nests."),
  "MI": ("Two-part (Part A / Part B)", "article", "Part A: What is the main idea of the article? Part B: Which two details best support it?", ["Loggerheads live in North Carolina.", "Hatchlings face dangers, and people can help them survive.", "Ghost crabs live on beaches.", "Turtles lay eggs at night."], "Part A: Hatchlings face dangers, and people can help them survive. Part B: lights confuse hatchlings; towns ask residents to turn off outdoor lights."),
  "TX": ("Multiple choice", "article", "Which sentence best states the central idea of the article?", ["Female turtles lay about 100 eggs.", "Sea turtle hatchlings face many dangers, but people can help protect them.", "Ghost crabs hunt at night.", "Moonlight shines on the ocean."], "Sea turtle hatchlings face many dangers, but people can help protect them."),
 },
 "structure": {
  "NC": ("Overall structure", "article", "Describe the overall structure of paragraphs 3 and 4 of the article. What signal words show it?", None, "Problem and solution: lights and predators are the problem (\"can cause problems\"); people help by turning off lights and marking nests (\"People can help\")."),
  "MI": ("Multiple choice", "article", "Which structure does the author mainly use in paragraphs 3 and 4?", ["chronological order", "compare and contrast", "problem and solution", "description"], "problem and solution"),
  "TX": ("Multiple choice", "article", "Why does the author include the statistic \"1 in 1,000 hatchlings survives\" in the last paragraph?", ["To show that turtles live a long time", "To explain why every protected nest matters", "To describe what a nest looks like", "To tell when turtles hatch"], "To explain why every protected nest matters"),
 },
 "vocab": {
  "NC": ("Context clues", "article", "Use context to determine the meaning of instinct in paragraph 3 of the article. Which clues helped?", None, "A natural behavior an animal is born with. Paragraph 2 explains hatchlings crawl toward the brightest horizon without being taught."),
  "MI": ("Two-part (Part A / Part B)", "article", "Part A: What does predators mean in paragraph 2? Part B: Which sentence helps you understand it?", ["animals that hunt other animals", "people who visit the beach", "baby turtles", "bright lights"], "Part A: animals that hunt other animals. Part B: \"Ghost crabs and birds also hunt them.\""),
  "TX": ("Multiple choice", "story", "Read this sentence from the story: \"Marcus wrote the date and location on the clipboard.\" The Latin root loc in location means —", ["place", "time", "write", "see"], "place"),
 },
 "figlang": {
  "NC": ("Explain figurative language", "poem", "The poet calls the ocean \"a restless giant.\" Explain this metaphor and what it shows about the ocean.", None, "It compares the ocean to a huge, moving giant to show it is large, powerful and always moving."),
  "MI": ("Multiple choice", "story", "Jada says to look for tracks \"that look like a tractor drove out of the ocean.\" This simile helps the reader understand that the tracks are —", ["small and hard to see", "wide and deep", "made by a real tractor", "covered by water"], "wide and deep"),
  "TX": ("Multiple choice", "poem", "In the poem, the ocean \"breathes in, then breathes out.\" What does this personification describe?", ["waves moving in and out", "wind blowing", "turtles breathing", "the moon rising"], "waves moving in and out"),
 },
 "genre": {
  "NC": ("Poem, drama and prose", "poem", "Explain two differences between \"The Ocean at Night\" and \"Turtle Patrol.\" Use the words stanza, line or rhyme.", None, "The poem is written in lines and two stanzas with rhyme (out / about); the story is prose written in paragraphs with dialogue."),
  "MI": ("Constructed response", "story", "Is \"Turtle Patrol\" told in first-person or third-person point of view? How do you know, and how would it change if Marcus told it?", None, "Third person: the narrator uses he and Marcus. In first person we would hear Marcus's thoughts directly using I."),
  "TX": ("Multiple choice", "poem", "How is the poem organized?", ["in two stanzas of four lines each", "in one long paragraph", "as a list of facts", "as dialogue between characters"], "in two stanzas of four lines each"),
 },
 "compare": {
  "NC": ("Integrate two texts", "pair", "Use information from both \"Turtle Patrol\" and the article to explain why volunteers mark sea turtle nests.", None, "The article says volunteers mark nests so they are not disturbed; in the story Marcus puts stakes and tape around the nest so no one steps on it."),
  "MI": ("Constructed response", "pair", "How does the article help you understand why Marcus says, \"We kept your spot safe\"? Use one detail from each text.", None, "The article explains hatchlings face many dangers and few survive; the story shows Marcus protecting the nest all summer."),
  "TX": ("Multiple choice", "pair", "Which idea is found in BOTH the story and the article?", ["Hatchlings head toward the water at night.", "Turtles lay 1,000 eggs.", "Marcus is Jada's cousin.", "Ghost crabs build nests."], "Hatchlings head toward the water at night."),
 },
}

R[5] = {
 "evidence": {
  "NC": ("Quote accurately", "story", "What can you infer about why Priya \"didn't answer right away\"? Quote accurately from the text to support your inference.", None, "She is thinking about the problem instead of giving up: \"She was staring at the laptop screen\" and \"Now Priya wondered if he meant it.\""),
  "MI": ("Two-part (Part A / Part B)", "story", "Part A: What does Andre's last line, \"Information,\" show? Part B: Which sentence from earlier in the story does it connect to?", ["He is still discouraged.", "He now agrees that mistakes can teach you.", "He wants to quit robotics.", "He thinks the coach was wrong."], "Part A: He now agrees that mistakes can teach you. Part B: \"Mr. Haynes, their coach, had told them that every crash was information.\""),
  "TX": ("Multiple choice", "story", "Which sentence best shows that Priya uses evidence to solve the problem?", ["\"Again?\" groaned Priya.", "\"Every time it spins, it's after the second turn,\" she said slowly.", "Andre slumped in his chair.", "Andre grinned."], "\"Every time it spins, it's after the second turn,\" she said slowly."),
 },
 "theme": {
  "NC": ("Theme and summary", "story", "Determine a theme of \"Twelve Seconds,\" including how the characters respond to the challenge. Then summarize the story.", None, "Theme: Failures give you information that helps you improve. The robot keeps crashing; instead of quitting, Priya studies the pattern, they find the sensor problem, fix it and finish in eleven seconds."),
  "MI": ("Two-part (Part A / Part B)", "story", "Part A: Which statement best expresses a theme of the story? Part B: Which two details best support it?", ["Robots are hard to build.", "Studying your mistakes can lead to success.", "Competitions are stressful.", "Coaches always know best."], "Part A: Studying your mistakes can lead to success. Part B: Priya notices the robot always spins after the second turn; the fixed robot finishes in eleven seconds."),
  "TX": ("Short constructed response", "story", "What theme does the author develop through Priya and Andre's actions? Use evidence from the story to support your answer.", None, "Scored on a stated theme with evidence, for example: don't give up after failure; Priya studies the code and they test the sensor until Bolt succeeds."),
 },
 "character": {
  "NC": ("Compare characters", "story", "Compare and contrast how Priya and Andre respond to the robot's crash. Use specific details.", None, "Andre wants to drop out and slumps in his chair; Priya stays calm, studies the code and finds a pattern. Both work together on the fix."),
  "MI": ("Selected response + evidence", "story", "Which word best describes Priya? Quote a sentence that shows it.", ["impatient", "observant", "careless", "boastful"], "observant; \"Every time it spins, it's after the second turn.\""),
  "TX": ("Multiple choice", "story", "What conflict do the characters face?", ["They argue about who will drive the robot.", "Their robot cannot finish the course, and the competition is in four days.", "Their coach quits the team.", "They lose their laptop."], "Their robot cannot finish the course, and the competition is in four days."),
 },
 "mainidea": {
  "NC": ("Two main ideas", "article", "Determine two main ideas of \"Failing Forward\" and explain how key details support each.", None, "1) Engineers follow a design cycle that expects failure (define, prototype, test, improve). 2) Failure gives useful data (the Wright brothers tested about 200 wing shapes)."),
  "MI": ("Two-part (Part A / Part B)", "article", "Part A: What is the central idea of the article? Part B: Which detail best supports it?", ["Airplanes were invented in 1903.", "Engineers use failure as information to improve their designs.", "Wind tunnels are small.", "Prototypes are expensive."], "Part A: Engineers use failure as information to improve their designs. Part B: The Wright brothers' wind tunnel tests helped them design the 1903 Flyer."),
  "TX": ("Multiple choice", "article", "Which detail best supports the idea that failure gives engineers useful data?", ["People picture inventors with brilliant ideas.", "The Wright brothers tested about 200 wing shapes in a wind tunnel.", "The cycle may repeat dozens of times.", "A prototype is a simple early model."], "The Wright brothers tested about 200 wing shapes in a wind tunnel."),
 },
 "structure": {
  "NC": ("Compare structures", "pair", "Compare the overall structure of paragraph 2 of the article with the structure of the story.", None, "Paragraph 2 uses sequence (first, next, then, finally); the story is told in chronological order around a problem and solution."),
  "MI": ("Multi-select", "article", "Select all the signal words in paragraph 2 that show sequence.", ["First", "Next", "Then", "Because", "Finally"], "First; Next; Then; Finally"),
  "TX": ("Multiple choice", "article", "Why does the author begin the article by describing how people often picture inventors?", ["To introduce an idea the article will correct", "To describe the Wright brothers", "To list the steps of the design cycle", "To give the meaning of prototype"], "To introduce an idea the article will correct"),
 },
 "vocab": {
  "NC": ("Context clues", "article", "In paragraph 2 of \"Failing Forward,\" what does prototype mean? Explain how the author helps you understand it.", None, "A simple early model. The author defines it right after the comma: \"a simple early model.\""),
  "MI": ("Two-part (Part A / Part B)", "story", "Part A: What does wildly mean in \"The readings jumped wildly\"? Part B: Which phrase helps you understand it?", ["slowly and calmly", "in a sudden, uncontrolled way", "quietly", "correctly"], "Part A: in a sudden, uncontrolled way. Part B: \"whenever the room got brighter\" (the readings changed a lot)."),
  "TX": ("Multiple choice", "article", "The prefix proto- in prototype means —", ["first", "again", "against", "small"], "first"),
 },
 "figlang": {
  "NC": ("Interpret figurative language", "poem", "In \"Prototype,\" the speaker calls failures \"a map, a ladder, a key.\" Interpret this metaphor.", None, "Failures guide you (map), help you rise step by step (ladder) and open new possibilities (key)."),
  "MI": ("Multiple choice", "story", "The shoebox is \"taped around the sensor like a tiny tunnel.\" What does this simile help the reader understand?", ["The shoebox blocks extra light from reaching the sensor.", "The robot drives through a real tunnel.", "The tape is decorative.", "The sensor is very large."], "The shoebox blocks extra light from reaching the sensor."),
  "TX": ("Multiple choice", "poem", "The line \"every crumpled, soggy wreck / was whispering a clue\" uses personification to show that —", ["the wrecks were noisy", "each failure taught the speaker something", "the speaker was tired", "the boat was still floating"], "each failure taught the speaker something"),
 },
 "genre": {
  "NC": ("How parts fit together", "poem", "Explain how the three stanzas of \"Prototype\" fit together to build the poem's message.", None, "Stanza 1 lists failures, stanza 2 shows each failure gave a clue, stanza 3 states the message that failures lead to growth."),
  "MI": ("Constructed response", "story", "\"Twelve Seconds\" is told in third person but follows Priya's thoughts. How does this point of view affect how the reader understands the turning point?", None, "We hear Priya wonder whether the coach meant it, so we see her realize the crash is information before she speaks."),
  "TX": ("Multiple choice", "poem", "Which line from the poem shows a rhyme with \"sailed\"?", ["that dove, and twirled, and failed.", "was whispering a clue,", "a map, a ladder, a key,", "to the builder I will be."], "that dove, and twirled, and failed."),
 },
 "compare": {
  "NC": ("Integrate texts", "pair", "Integrate information from the story, the article and the poem to explain how all three show the idea that failure can lead to success.", None, "Story: Bolt's crashes lead to the sensor fix. Article: engineers test until things break, like the Wright brothers. Poem: each failed try was \"whispering a clue.\""),
  "MI": ("Constructed response", "pair", "How does Priya's team follow the engineering design cycle described in the article? Give two examples.", None, "They test the prototype (run Bolt), collect data (notice it spins after the second turn, test the sensor), and improve the design (add the shoebox), then test again."),
  "TX": ("Multiple choice", "pair", "How are the story and the article alike?", ["Both are set at a robotics competition.", "Both show that testing and learning from mistakes improves a design.", "Both describe the Wright brothers.", "Both are written as poems."], "Both show that testing and learning from mistakes improves a design."),
 },
}

# Writing, research, conventions and foundations: grade-specific prompts per state.
W = {
 3: dict(op="Should our school hold a seed swap in the spring?", inf="the different ways seeds travel", nar="a time you tried to grow or make something and it did not go as planned",
         nar_mi="Continue \"The Seed Swap\" by writing what happens next fall when Lila saves her sunflower seeds.",
         edit="lila and grandma rose plants seeds last spring", edit_ans="Lila and Grandma Rose planted seeds last spring.",
         runon="The coconut floated across the ocean it landed on a beach.", runon_ok="The coconut floated across the ocean. It landed on a beach.",
         rq="How do birds help spread seeds?", src_mi=["a poem about spring rain", "a science website about how animals spread seeds", "a recipe for sunflower bread", "a map of Maple Street"], src_mi_ans="a science website about how animals spread seeds",
         prim=["a farmer's journal from 1920 describing the seeds she saved", "an encyclopedia article about seeds", "a textbook chapter about plants", "a cartoon about a sunflower"], prim_ans="a farmer's journal from 1920 describing the seeds she saved",
         words="carefully, envelopes, waterproof", split="care / ful / ly; en / ve / lopes; wa / ter / proof"),
 4: dict(op="Should beach towns require outdoor lights to be turned off during sea turtle nesting season?", inf="why sea turtle hatchlings face danger and how people can help", nar="a time you helped protect or care for an animal or place",
         nar_mi="Retell the night the turtles hatched from the point of view of one hatchling.",
         edit="marcus and jada walks the beach at sunrise last summer", edit_ans="Marcus and Jada walked the beach at sunrise last summer.",
         runon="The hatchlings crawled toward the ocean they followed the moonlight.", runon_ok="The hatchlings crawled toward the ocean. They followed the moonlight.",
         rq="Why are bright lights dangerous to sea turtle hatchlings?", src_mi=["a story about a pirate ship", "a wildlife agency web page about sea turtle nesting", "a beach vacation brochure", "a poem about the moon"], src_mi_ans="a wildlife agency web page about sea turtle nesting",
         prim=["a volunteer's logbook of turtle nests found on Emerald Isle", "an encyclopedia entry about turtles", "a magazine summary of turtle research", "a cartoon about a turtle"], prim_ans="a volunteer's logbook of turtle nests found on Emerald Isle",
         words="volunteers, hatchlings, instinct", split="vol / un / teers; hatch / lings; in / stinct"),
 5: dict(op="Is failing an important part of learning?", inf="how the engineering design cycle helps engineers improve their designs", nar="a time you kept trying after something did not work",
         nar_mi="Write the scene of the regional robotics competition from Andre's point of view.",
         edit="priya and andre tested the sensor, it gave strange readings, so they builded a tunnel", edit_ans="Priya and Andre tested the sensor. It gave strange readings, so they built a tunnel.",
         runon="The glider did not lift the brothers built a wind tunnel.", runon_ok="The glider did not lift, so the brothers built a wind tunnel.",
         rq="How did the Wright brothers use testing to design the 1903 Flyer?", src_mi=["a novel about a talking airplane", "a museum website about the Wright brothers' wind tunnel experiments", "an advertisement for model planes", "a poem about birds"], src_mi_ans="a museum website about the Wright brothers' wind tunnel experiments",
         prim=["Wilbur Wright's 1901 notebook of wind tunnel measurements", "a biography of the Wright brothers written in 2015", "an encyclopedia article about flight", "a documentary narrator's summary"], prim_ans="Wilbur Wright's 1901 notebook of wind tunnel measurements",
         words="competition, prototype, measurements", split="com / pe / ti / tion; pro / to / type; mea / sure / ments"),
}


def writing_items(g):
    w = W[g]
    t = TEXTS[g]
    s, a = t["story"][0], t["article"][0]
    return {
     "opinion": {
      "NC": ("Writing task", "pair", f"{w['op']} Write an opinion piece. State your opinion, support it with reasons and facts from \"{s}\" and \"{a},\" use linking words, and end with a conclusion.", None, "Look for: clear opinion, logically ordered reasons supported by text facts, linking words and a concluding section."),
      "MI": ("Performance task", "pair", f"Your principal asks: {w['op']} Write an opinion essay that uses information from both \"{s}\" and \"{a}.\"", None, "Scored on purpose and organization, evidence and elaboration, and conventions."),
      "TX": ("Extended constructed response", "pair", f"{w['op']} Write an argumentative essay that states your position and supports it with evidence from \"{s}\" and \"{a}.\"", None, "Scored on development and organization of ideas and on conventions."),
     },
     "informative": {
      "NC": ("Writing task", "article", f"Write an informative piece that explains {w['inf']}. Group related information in paragraphs, use facts from \"{a},\" and include a conclusion.", None, "Look for: introduction, grouped facts, precise vocabulary, linking words, concluding statement."),
      "MI": ("Performance task", "article", f"Write an informational article for the school newsletter that explains {w['inf']}. Use details from \"{a}.\"", None, "Scored on purpose and organization, evidence and elaboration, and conventions."),
      "TX": ("Extended constructed response", "article", f"Write an informational essay that explains {w['inf']}. Use evidence from \"{a}.\"", None, "Scored on development and organization of ideas and on conventions."),
     },
     "narrative": {
      "NC": ("Writing task", None, f"Write a personal narrative about {w['nar']}. Use dialogue, description and transition words to show the order of events.", None, "Look for: a clear situation, dialogue and description, a logical sequence and a conclusion."),
      "MI": ("Performance task", "story", w["nar_mi"], None, "Scored on narrative focus, development with dialogue and description, and conventions."),
      "TX": ("TEKS classroom task", None, f"Compose a personal narrative about {w['nar']}. (Narrative writing is taught in the TEKS but is not a STAAR essay type.)", None, "Look for: focused structure, engaging details and edited conventions."),
     },
     "process": {
      "NC": ("Edit", None, f"Edit this sentence for capitalization, verb tense and punctuation: \"{w['edit']}\"", None, w["edit_ans"]),
      "MI": ("Multiple choice", None, f"Which is the best way to fix this run-on sentence? \"{w['runon']}\"", [w["runon_ok"], w["runon"].replace(" it ", ", it ").replace(" they ", ", they ").replace(" the brothers", ", the brothers"), w["runon"].lower(), w["runon"].replace(".", "!")], w["runon_ok"]),
      "TX": ("Revising and editing", None, f"A student wrote: \"{w['runon']}\" What is the best way to revise this sentence?", [w["runon_ok"], "Delete the last word", "Add a comma after the first word", "No change is needed"], w["runon_ok"]),
     },
     "research": {
      "NC": ("Research task", None, f"Research question: {w['rq']} Take notes from two sources in your own words, sort them into categories, and list your sources.", None, "Notes are paraphrased, sorted into categories, and both sources are listed."),
      "MI": ("Multiple choice", None, f"A student is researching: {w['rq']} Which source would be most useful?", w["src_mi"], w["src_mi_ans"]),
      "TX": ("Multiple choice", None, f"A student is researching: {w['rq']} Which is a primary source?", w["prim"], w["prim_ans"]),
     },
     "foundations": {
      "NC": ("Word analysis", None, f"Read these words from this grade's passages by breaking them into syllables: {w['words']}.", None, w["split"]),
      "MI": ("Fluency check", "story", f"Read the first three paragraphs of \"{s}\" aloud for one minute. The teacher records words correct per minute and rates expression.", None, f"Compare words correct per minute to grade {g} norms and note phrasing and expression."),
      "TX": ("Decoding", None, f"Divide each word into syllables, then read it: {w['words']}.", None, w["split"]),
     },
    }


def items_for(g):
    d = dict(R[g])
    d.update(writing_items(g))
    return d
