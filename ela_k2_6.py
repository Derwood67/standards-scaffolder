"""ELA additions for grades K, 1, 2 and 6 (grade K is stored as 0).

FOCUS[key][grade]: the grade-level focus line for each ELA skill template in gen_data.ELA.
TEXTS[grade]: original story, article and poem on one topic (K-2 are read-aloud texts).
R[grade][key]: reading items. K-2 use {"ALL": item} (no state test before grade 3);
grade 6 uses {"NC": ..., "MI": ..., "TX": ...}.
item = (format, text_ref, prompt, choices_or_None, answer)
W[6]: writing variables for passages.writing_items. K-2 writing items come from k2_writing().
"""

FOCUS = {
 "evidence": {0: "With prompting and support, ask and answer questions about key details.", 1: "Ask and answer questions about key details in a text.", 2: "Ask and answer who, what, where, when, why and how questions.", 6: "Cite textual evidence to support analysis of what the text says and inferences drawn from it."},
 "theme": {0: "With support, retell familiar stories with key details.", 1: "Retell stories and show understanding of their central message or lesson.", 2: "Recount fables and folktales and determine the central message, lesson or moral.", 6: "Determine a theme and how it is conveyed through details; summarize without personal opinions."},
 "character": {0: "With support, identify characters, settings and major events.", 1: "Describe characters, settings and major events using key details.", 2: "Describe how characters respond to major events and challenges.", 6: "Describe how a plot unfolds in episodes and how characters respond or change."},
 "mainidea": {0: "With support, identify the main topic and retell key details.", 1: "Identify the main topic and retell key details.", 2: "Identify the main topic of a multi-paragraph text and the focus of specific paragraphs.", 6: "Determine a central idea, how it is conveyed through details, and summarize."},
 "structure": {0: "Name the front cover, back cover and title page; describe how two events or ideas connect.", 1: "Use text features such as headings to locate key facts.", 2: "Use text features to locate key facts efficiently and explain how images clarify a text.", 6: "Analyze how a sentence, paragraph or section fits into the overall structure and develops ideas."},
 "vocab": {0: "Ask and answer questions about unknown words; sort words into categories.", 1: "Use sentence-level context and common affixes as clues to word meaning.", 2: "Use context, prefixes and root words to determine meaning; use glossaries.", 6: "Use context, Greek and Latin affixes and roots, and reference materials to determine meaning."},
 "figlang": {0: "Recognize rhyme and act out shades of meaning with support.", 1: "Identify words and phrases that suggest feelings or appeal to the senses.", 2: "Describe how words and phrases supply rhythm and meaning in a story, poem or song.", 6: "Interpret figures of speech such as personification and simile and explain their effect on meaning and tone."},
 "genre": {0: "Recognize common types of texts such as storybooks and poems.", 1: "Explain differences between books that tell stories and books that give information.", 2: "Describe the overall structure of a story, including how the beginning introduces and the ending concludes it.", 6: "Explain how an author develops the point of view of the narrator or speaker; analyze how a stanza or scene fits the whole."},
 "compare": {0: "With support, compare the adventures of characters in familiar stories.", 1: "Compare the adventures and experiences of characters in stories.", 2: "Compare two versions of the same story or two texts on the same topic.", 6: "Compare texts in different forms or genres on similar themes and topics."},
 "opinion": {0: "Use drawing, dictating and writing to tell an opinion about a topic or book.", 1: "Write opinion pieces that name a topic, state an opinion, give a reason and provide closure.", 2: "Write opinion pieces with reasons, linking words and a concluding statement.", 6: "Write arguments that support claims with clear reasons and relevant evidence."},
 "informative": {0: "Use drawing, dictating and writing to name a topic and tell something about it.", 1: "Write informative texts that name a topic, supply facts and provide closure.", 2: "Introduce a topic, use facts and definitions, and provide a concluding statement.", 6: "Examine a topic and convey ideas through relevant facts, definitions, quotations and examples."},
 "narrative": {0: "Use drawing, dictating and writing to tell about a single event and react to it.", 1: "Narrate two or more sequenced events with details and time-order words.", 2: "Recount a well-elaborated event with details and an ending.", 6: "Write narratives with descriptive details, dialogue, pacing and well-structured event sequences."},
 "process": {0: "With guidance, add details to strengthen writing; print letters and use end punctuation.", 1: "With guidance, add details; capitalize dates and names; use end punctuation.", 2: "With guidance, revise and edit; use apostrophes and capitalize proper nouns.", 6: "Plan, revise, edit and rewrite; use pronouns correctly and vary sentence patterns."},
 "research": {0: "Take part in shared research and writing; recall information from experience.", 1: "Take part in shared research; gather information to answer a question.", 2: "Take part in shared research; recall or gather information to answer a question.", 6: "Conduct short research projects using several sources; quote or paraphrase and avoid plagiarism."},
 "foundations": {0: "Know letter-sound matches, read common high-frequency words, and read emergent-reader texts with purpose.", 1: "Decode one- and two-syllable words and read grade-level text with accuracy and fluency.", 2: "Decode two-syllable words with long vowels and common prefixes and suffixes; read with accuracy and expression."},
}

PREK = "PreK: Listen to stories and informational books read aloud and talk about them"

TEXTS = {
 0: {
  "topic": "Rain",
  "story": ("Puddle Day", """Rain fell all morning. Nia pressed her nose to the window.

"When can I go out?" she asked.

"When the rain stops," said Papa.

At last the sun came out. Nia put on her red boots. She found a big puddle. Splash! Splash! The water jumped up high.

Then Nia saw a worm in the puddle. She gently picked it up and set it in the grass. "Now you are safe," she said."""),
  "article": ("Where Does Rain Go?", """Rain falls from clouds.

Some rain soaks into the ground. Plants drink it with their roots.

Some rain runs into streams and ponds.

When the sun shines, puddles dry up. The water goes back up into the air. Later it falls again as rain."""),
  "poem": ("Rain Song", """Pitter, patter on the roof,
Drip, drop by the door,
Rain is tapping out a song,
Then it pours and pours!

Puddles shine like mirrors,
Clouds roll far away,
Sun peeks out and smiles at me,
Now it's time to play."""),
 },
 1: {
  "topic": "Bees",
  "story": ("Max and the Bee", """Max was eating a peach on the porch. A bee landed on the table. Max jumped up. "Go away!" he yelled, and he waved his arms.

"Stay still," said his sister, June. "Bees sting when they are scared."

Max held very still. The bee walked across the table. It sipped a drop of peach juice. Then it flew to the flowers by the fence.

"It just wanted a snack," said June.

Max smiled. "I guess we both like sweet things," he said."""),
  "article": ("Busy Bees", """Home Sweet Hive
Honeybees live together in a hive. One queen bee lays the eggs. Worker bees do the other jobs.

Flower Helpers
Worker bees fly from flower to flower to drink sweet nectar. As they fly, yellow pollen sticks to their legs. The pollen helps flowers make seeds.

Bee Dance
Back at the hive, bees turn nectar into honey. A bee can do a special dance to tell other bees where to find flowers."""),
  "poem": ("Buzz", """Buzz, buzz, in the sun,
Busy bee has work to be done.
Flower to flower, all day long,
Humming a happy honey song."""),
 },
 2: {
  "topic": "Ants",
  "story": ("The Picnic Parade", """Carlos and his grandpa spread a blanket under the oak tree. They had sandwiches, grapes and a big slice of watermelon.

After lunch, Carlos dropped a piece of watermelon in the grass. Soon a line of tiny black ants marched toward it.

"Grandpa, they're stealing our food!" Carlos said.

Grandpa knelt down. "Look closer," he said. "They are working together. One ant found the food. Now the others are following her trail."

Carlos watched for a long time. The ants carried tiny bits of watermelon back to a hole near the tree. Not one ant gave up.

On the way home, Carlos had an idea. "Tomorrow, let's bring a piece of watermelon just for them," he said.

Grandpa laughed. "Now you are a real ant scientist." """),
  "article": ("Ants Work Together", """A Big Family
Ants live in large groups called colonies. A colony can have thousands of ants. The queen lays eggs. Worker ants take care of the young, build tunnels and find food.

Following the Trail
When a worker ant finds food, it leaves a trail of scent on the way back to the nest. Other ants smell the trail with their antennae and follow it to the food.

Strong and Small
Ants are tiny, but they are strong. Many ants can lift things heavier than their own bodies. By working together, ants can move food much bigger than one ant."""),
  "poem": ("Ant Line", """One by one and two by two,
Marching where the grasses grew,
Tiny feet that never stop,
Carry crumbs up to the top.

Over pebbles, under leaves,
Past the roots of shady trees,
Little helpers, side by side,
Working hard with ant-sized pride."""),
 },
 6: {
  "topic": "Exploring the deep ocean",
  "story": ("Below the Surface", """Rosa had imagined the research ship would feel like a floating laboratory. Instead, on her first morning aboard the Seeker, it felt like a washing machine. The deck rolled under her feet, and her stomach rolled with it.

"You'll get your sea legs," said Dr. Hale, the chief scientist, handing her a cracker. "Everyone does. Eventually."

Rosa was the youngest person on the expedition, invited because her science fair project on ocean sound had won a state award. Now, staring at the gray water, she wondered whether the judges had made a mistake.

On the third day, the crew lowered the remotely operated vehicle, a yellow robot the size of a small car, into the water. Rosa sat in the control room beside the pilot, watching the screens. At 200 meters, the blue light faded to dusk. At 1,000 meters, the screens went black except for the glow of the robot's lamps.

Then something flickered at the edge of the light: a ribbon of blue sparks drifting past like a slow firework.

"Bioluminescence," whispered the pilot. "Something down there makes its own light."

Rosa forgot about her stomach. For two hours she logged every flash, noting the depth and the time. When the robot surfaced, Dr. Hale read her notes and raised an eyebrow.

"These are careful observations," she said. "Most people just stare."

That night, Rosa stood at the rail. The ship still rolled, but she rocked with it now, the way the ocean seemed to ask her to. Somewhere beneath her, in the dark, the sparks were still drifting. She had a feeling she would spend her life trying to understand them."""),
  "article": ("Mapping the Deep", """More than 70 percent of Earth's surface is covered by ocean, yet scientists have more detailed maps of the surface of Mars than of much of the seafloor. Why is the bottom of our own planet so hard to see?

The answer is water. Light fades quickly as it travels down through the ocean, and below about 1,000 meters no sunlight reaches at all. The cameras and satellites that map land cannot see through that much water.

Instead, scientists map the seafloor with sound. A ship sends pulses of sound toward the bottom and measures how long the echoes take to return. Because sound travels through seawater at a known speed, about 1,500 meters per second, the time tells how deep the water is. Modern ships use multibeam sonar, which sends out a fan of sound beams to map a wide strip of seafloor at once.

The work is slow. A ship can map only the strip beneath its path, and the ocean is enormous. An international project called Seabed 2030 is working to map the entire ocean floor in detail by the year 2030. When the project began in 2017, only about 6 percent of the seafloor had been mapped in high detail. By 2024, the total had reached about a quarter.

Better maps matter. They help ships navigate safely, show where undersea cables can be laid, and reveal underwater mountains and canyons where sea life gathers. They also help scientists predict how tsunamis will travel. Every new strip of map is a step toward knowing our planet's last unexplored frontier."""),
  "poem": ("The Deep", """I am the deep, the patient dark,
the room no sun has entered.
I keep my secrets folded small
in canyons, cold and centered.

You send your songs of sound to me;
I hum them back, unhurried.
You count the seconds of my voice
and draw me, slow, unworried.

But some things I will not explain:
the sparks that drift like embers,
the lanterns carried by the fish,
the dark that still remembers."""),
 },
}

A = "ALL"
R = {
 0: {
  "evidence": {A: ("Listen and answer", "story", "Why does Nia put the worm in the grass?", ["to keep it safe", "to feed it", "to play with it"], "to keep it safe")},
  "theme": {A: ("Retell", "story", "Retell \"Puddle Day.\" What happened first, next and last?", None, "First it rained and Nia waited. Next she splashed in a puddle. Last she saved a worm.")},
  "character": {A: ("Story parts", "story", "Who are the characters in \"Puddle Day\"? Where does the story happen?", None, "Nia and Papa; at home and outside by a puddle.")},
  "mainidea": {A: ("Main topic", "article", "What is \"Where Does Rain Go?\" mostly about?", ["where rain goes", "red boots", "worms"], "where rain goes")},
  "structure": {A: ("Connect ideas", "article", "What happens to a puddle when the sun shines?", ["It dries up.", "It gets bigger.", "It turns to ice."], "It dries up.")},
  "vocab": {A: ("Word meaning", "story", "Nia \"gently\" picked up the worm. What does gently mean?", ["softly and carefully", "fast and hard", "with a shout"], "softly and carefully")},
  "figlang": {A: ("Rhyme", "poem", "Which two words from \"Rain Song\" rhyme?", ["away / play", "roof / door", "song / sun"], "away / play")},
  "genre": {A: ("Kinds of texts", "poem", "Is \"Rain Song\" a storybook or a poem? How do you know?", None, "A poem. It has short lines, rhyming words and a beat.")},
  "compare": {A: ("Compare texts", "pair", "What happens to puddles in the story? What happens to puddles in the article?", None, "In the story Nia splashes in a puddle. In the article the sun dries puddles up.")},
 },
 1: {
  "evidence": {A: ("Key details", "story", "Why does June tell Max to stay still?", ["Bees sting when they are scared.", "She wants his peach.", "The bee is asleep."], "Bees sting when they are scared.")},
  "theme": {A: ("Lesson", "story", "What lesson does Max learn in \"Max and the Bee\"?", None, "Stay calm around bees. The bee only wanted a snack and was not trying to hurt him.")},
  "character": {A: ("Describe a character", "story", "How does Max feel at the beginning of the story? How does he feel at the end?", None, "Scared at the beginning; calm and happy at the end.")},
  "mainidea": {A: ("Main topic", "article", "What is the main topic of \"Busy Bees\"?", ["how honeybees live and work", "how to eat a peach", "how to plant a garden"], "how honeybees live and work")},
  "structure": {A: ("Headings", "article", "Which heading would you read to learn how bees help flowers?", ["Home Sweet Hive", "Flower Helpers", "Bee Dance"], "Flower Helpers")},
  "vocab": {A: ("Context clues", "article", "What is nectar? Which words in the article help you know?", None, "A sweet drink in flowers. The article says bees \"drink sweet nectar\" from flowers.")},
  "figlang": {A: ("Sense words", "poem", "Which words in \"Buzz\" help you hear the bee?", None, "\"Buzz, buzz\" and \"Humming\"")},
  "genre": {A: ("Story or information", "pair", "Which text tells a story and which gives information? How can you tell?", None, "\"Max and the Bee\" tells a story with characters. \"Busy Bees\" gives facts about real bees and has headings.")},
  "compare": {A: ("Compare texts", "pair", "What does the bee in the story do that the article says bees do?", None, "It drinks something sweet and flies to the flowers.")},
 },
 2: {
  "evidence": {A: ("Ask and answer", "story", "Why do the ants march toward the watermelon? Use a detail from the story.", None, "One ant found the food and the others followed her trail: \"Now the others are following her trail.\"")},
  "theme": {A: ("Central message", "story", "What is the central message of \"The Picnic Parade\"?", ["Working together helps get a big job done.", "Picnics are fun.", "Watermelon is sweet.", "Ants are scary."], "Working together helps get a big job done.")},
  "character": {A: ("Character response", "story", "How does Carlos change from the beginning to the end of the story?", None, "At first he thinks the ants are stealing. At the end he is curious and wants to share food with them.")},
  "mainidea": {A: ("Focus of a section", "article", "What is the section \"Following the Trail\" mostly about?", ["how ants use scent to lead other ants to food", "how big a colony is", "what the queen does", "how strong ants are"], "how ants use scent to lead other ants to food")},
  "structure": {A: ("Text features", "article", "Which heading tells where to read about ant colonies?", ["A Big Family", "Following the Trail", "Strong and Small"], "A Big Family")},
  "vocab": {A: ("Word meaning", "article", "In \"Ants Work Together,\" what are colonies?", ["large groups of ants that live together", "tunnels under the ground", "pieces of food"], "large groups of ants that live together")},
  "figlang": {A: ("Rhythm and rhyme", "poem", "Which lines of \"Ant Line\" sound like marching? Why?", None, "\"One by one and two by two, / Marching where the grasses grew.\" The steady beat and rhyme sound like feet marching.")},
  "genre": {A: ("Story structure", "story", "How does the beginning of \"The Picnic Parade\" start the story, and how does the ending finish it?", None, "The beginning sets up the picnic. The ending shows what Carlos learned: he plans to bring watermelon for the ants.")},
  "compare": {A: ("Two texts, one topic", "pair", "How does \"Ants Work Together\" help explain what Carlos sees?", None, "The article says ants leave a scent trail for other ants to follow. That is why the ants march in a line to the watermelon.")},
 },
 6: {
  "evidence": {
   "NC": ("Text evidence", "story", "What can the reader infer about Rosa from how she responds to the bioluminescence? Cite two pieces of evidence.", None, "She is curious and careful. \"Rosa forgot about her stomach\" and \"For two hours she logged every flash, noting the depth and the time.\""),
   "MI": ("Two-part (Part A / Part B)", "story", "Part A: What does Dr. Hale's comment \"Most people just stare\" suggest? Part B: Which detail best supports your answer?", ["Rosa's work is unusually thorough.", "Rosa should not have been on the ship.", "Dr. Hale is annoyed with Rosa.", "The robot's cameras were broken."], "Part A: Rosa's work is unusually thorough. Part B: \"For two hours she logged every flash, noting the depth and the time.\""),
   "TX": ("Multiple choice", "story", "Which sentence best supports the idea that Rosa doubts herself at first?", ["Now, staring at the gray water, she wondered whether the judges had made a mistake.", "Rosa sat in the control room beside the pilot, watching the screens.", "Rosa forgot about her stomach.", "That night, Rosa stood at the rail."], "Now, staring at the gray water, she wondered whether the judges had made a mistake."),
  },
  "theme": {
   "NC": ("Theme", "story", "What is a theme of \"Below the Surface\"? Explain how the author develops it over the course of the story.", None, "Example: Curiosity can carry a person past doubt and discomfort. Rosa starts seasick and unsure, is drawn in by the bioluminescence, and ends steady and imagining a life of study."),
   "MI": ("Two-part (Part A / Part B)", "story", "Part A: Which statement best expresses a theme of the story? Part B: Which detail best supports it?", ["Curiosity can help a person push past doubt and discomfort.", "Robots are better explorers than people.", "Science fairs are not important.", "The ocean is too dangerous to explore."], "Part A: Curiosity can help a person push past doubt and discomfort. Part B: \"Rosa forgot about her stomach.\""),
   "TX": ("Short constructed response", "story", "How does Rosa's time in the control room change her? Support your answer with evidence from the story.", None, "Scored on a clear idea with evidence, for example: she goes from doubting herself to feeling confident and purposeful; she \"rocked with it now\" and plans to spend her life studying the sparks."),
  },
  "character": {
   "NC": ("Plot and character", "story", "How does the rolling ship affect Rosa at the beginning and at the end of the story? What does the change show?", None, "At first the deck makes her sick. At the end \"she rocked with it now,\" which shows she has adjusted and found her place."),
   "MI": ("Selected response + evidence", "story", "Which word best describes Rosa at the end of the story? Then quote the sentence that shows it.", ["uncertain", "determined", "bored", "frightened"], "determined; \"She had a feeling she would spend her life trying to understand them.\""),
   "TX": ("Multiple choice", "story", "Why does the author include Dr. Hale handing Rosa a cracker?", ["To show that Rosa is seasick and new to life at sea", "To show that the ship has run out of food", "To show that Dr. Hale is unfriendly", "To explain how the robot works"], "To show that Rosa is seasick and new to life at sea"),
  },
  "mainidea": {
   "NC": ("Central idea and summary", "article", "Determine the central idea of \"Mapping the Deep\" and write an objective summary of how the author develops it.", None, "Central idea: mapping the seafloor is hard but important. The author explains why light cannot be used, how sonar measures depth, the slow progress of Seabed 2030, and why maps matter."),
   "MI": ("Two-part (Part A / Part B)", "article", "Part A: What is the central idea of the article? Part B: Which sentence best supports it?", ["Scientists use sound to slowly map the hard-to-see seafloor, and the maps are important.", "Mars is easier to visit than the ocean.", "Light travels faster than sound.", "Ships are dangerous in storms."], "Part A: Scientists use sound to slowly map the hard-to-see seafloor, and the maps are important. Part B: \"Instead, scientists map the seafloor with sound.\""),
   "TX": ("Multiple choice", "article", "Which is the best summary of the third paragraph of \"Mapping the Deep\"?", ["Ships find depth by timing sound echoes, and multibeam sonar maps wide strips at once.", "Sound travels at 1,500 meters per second.", "Satellites map the land.", "Ships carry robots."], "Ships find depth by timing sound echoes, and multibeam sonar maps wide strips at once."),
  },
  "structure": {
   "NC": ("Text structure", "article", "How does the first paragraph of \"Mapping the Deep\" prepare the reader for the rest of the article?", None, "It raises a question (why is the seafloor so hard to see?) that the rest of the article answers."),
   "MI": ("Multi-select", "article", "Select all the reasons the author gives for why seafloor maps matter.", ["They help ships navigate safely.", "They show where undersea cables can be laid.", "They help predict how tsunamis travel.", "They make satellites more powerful.", "They stop undersea earthquakes."], "They help ships navigate safely; they show where undersea cables can be laid; they help predict how tsunamis travel."),
   "TX": ("Multiple choice", "article", "The author organizes the second and third paragraphs of \"Mapping the Deep\" mainly by —", ["presenting a problem and then a solution", "comparing two scientists", "telling events in time order", "listing the causes of tsunamis"], "presenting a problem and then a solution"),
  },
  "vocab": {
   "NC": ("Affixes and roots", "article", "In \"Mapping the Deep,\" the word multibeam begins with the prefix multi-. Use the prefix and context to explain what multibeam sonar is.", None, "Multi- means many, so multibeam sonar sends out many sound beams at once, \"a fan of sound beams.\""),
   "MI": ("Two-part (Part A / Part B)", "article", "Part A: What does frontier mean in the last sentence of the article? Part B: Which words help you know?", ["an area not yet explored", "a kind of ship", "a guarded border", "a deep canyon"], "Part A: an area not yet explored. Part B: \"last unexplored\""),
   "TX": ("Multiple choice", "story", "Based on the story, bioluminescence means —", ["light that a living thing makes itself", "a kind of firework", "light from a robot's lamp", "moonlight on the water"], "light that a living thing makes itself"),
  },
  "figlang": {
   "NC": ("Figurative language", "poem", "In \"The Deep,\" the speaker says, \"I hum them back, unhurried.\" What is being described, and what is the effect of the personification?", None, "Sonar echoes returning to the ship. Personification makes the ocean seem alive, patient and mysterious."),
   "MI": ("Multiple choice", "poem", "Which line from \"The Deep\" contains a simile?", ["the sparks that drift like embers", "I am the deep, the patient dark", "You send your songs of sound to me", "in canyons, cold and centered"], "the sparks that drift like embers"),
   "TX": ("Multiple choice", "poem", "The phrase \"the room no sun has entered\" suggests that the deep ocean is —", ["completely dark", "very small", "warm", "crowded"], "completely dark"),
  },
  "genre": {
   "NC": ("Point of view", "poem", "Who is the speaker of \"The Deep,\" and how is that point of view different from the voice of \"Mapping the Deep\"?", None, "The ocean itself speaks in first person. The article uses an objective, informational third-person voice."),
   "MI": ("Constructed response", "poem", "How does the final stanza of \"The Deep\" contribute to the poem's meaning?", None, "It shifts from what people can measure to what the ocean keeps secret (the sparks and lanterns), stressing that some things remain unknown."),
   "TX": ("Multiple choice", "poem", "Which describes the rhyme pattern in each stanza of \"The Deep\"?", ["The second and fourth lines rhyme.", "Every line rhymes.", "The first and third lines rhyme.", "There is no rhyme."], "The second and fourth lines rhyme."),
  },
  "compare": {
   "NC": ("Compare texts", "pair", "Compare how \"Below the Surface\" and \"Mapping the Deep\" present the deep ocean.", None, "The story shows one person's sense of wonder (the bioluminescence); the article gives facts about light, sound and mapping. Both show the deep ocean as dark and hard to explore."),
   "MI": ("Constructed response", "pair", "Explain how the information about light in \"Mapping the Deep\" helps the reader understand the control-room scene in \"Below the Surface.\"", None, "The article says no sunlight reaches below about 1,000 meters. In the story, the screens go black at 1,000 meters except for the robot's lamps."),
   "TX": ("Multiple choice", "pair", "Which idea appears in both \"Below the Surface\" and \"Mapping the Deep\"?", ["The deep ocean is dark and still holds much that is unknown.", "Robots are expensive.", "Seasickness is common.", "Seabed 2030 will finish early."], "The deep ocean is dark and still holds much that is unknown."),
  },
 },
}

W6 = dict(op="Should governments spend more on exploring the ocean than on exploring space?", inf="how scientists map the seafloor and why the maps matter",
          nar="a time you discovered something that changed how you saw a place",
          nar_mi="Rewrite the control-room scene in \"Below the Surface\" from the pilot's point of view.",
          edit="rosa and her mentor dr. hale has watched the screens for hours, they seen blue sparks", edit_ans="Rosa and her mentor, Dr. Hale, had watched the screens for hours. They saw blue sparks.",
          runon="The robot dove below 1,000 meters the screens went black.", runon_ok="The robot dove below 1,000 meters, and the screens went black.",
          rq="How do scientists study animals that make their own light in the deep ocean?",
          src_mi=["a science fiction novel about sea monsters", "a government ocean research agency's page about deep-sea exploration", "an advertisement for scuba gear", "a poem about waves"], src_mi_ans="a government ocean research agency's page about deep-sea exploration",
          prim=["a scientist's dive log recorded aboard a research ship", "an encyclopedia article about the ocean", "a textbook chapter on marine life", "a blog post summarizing a documentary"], prim_ans="a scientist's dive log recorded aboard a research ship",
          words="bioluminescence, expedition, observations", split="bi / o / lu / mi / nes / cence; ex / pe / di / tion; ob / ser / va / tions")


def k2_writing(g):
    t = TEXTS[g]
    a = t["article"][0]
    P = {
     0: dict(op="Draw and tell: Is a rainy day a good day? Tell why.", inf=f"Draw and write about where rain goes. Use what you learned from \"{a}.\"",
             nar="Draw and tell about a time you played outside after it rained.", edit="nia has red boots", edit_ans="Nia has red boots.",
             rq="As a class, ask: Where do worms go when it rains? Draw one thing you learned.", rq_ans="Drawings show one fact from shared reading or a class observation.",
             words="sun, red, up, can, the", wans="Child blends short-vowel words (sun, red, up, can) and reads the as a high-frequency word."),
     1: dict(op="Are bees helpful? Write your opinion and one reason.", inf=f"Write two facts about honeybees from \"{a}.\" End with a closing sentence.",
             nar="Write about a time you saw an insect. Tell what happened first, next and last.", edit="max and june sat on the porch on june 5", edit_ans="Max and June sat on the porch on June 5.",
             rq=f"Shared research: What do bees eat? Find the answer in \"{a}\" and one other book.", rq_ans="Bees drink nectar from flowers (and turn it into honey).",
             words="peach, still, honey, flower", wans="peach (one syllable, ea team); still; hon / ey; flow / er"),
     2: dict(op="Should our class keep an ant farm? Write your opinion, two reasons and an ending.", inf=f"Explain how ants work together. Use facts from \"{a}\" and end with a closing sentence.",
             nar="Write about a day you watched something closely in nature. Use details and an ending.", edit="carlos and his grandpa didnt see the ants at first", edit_ans="Carlos and his grandpa didn't see the ants at first.",
             rq=f"How do ants find food? Use \"{a}\" and one other source. Write two facts.", rq_ans="Ants leave scent trails; other ants smell the trail with their antennae and follow it.",
             words="picnic, watermelon, scientist", wans="pic / nic; wa / ter / mel / on; sci / en / tist"),
    }[g]
    fmt = "Drawing, dictating or writing" if g == 0 else "Writing task"
    return {
     "opinion": {A: (fmt, "pair" if g else None, P["op"], None, "Look for: a clear opinion and a reason" + (" and an ending." if g else " (drawn, told or written)."))},
     "informative": {A: (fmt, "article", P["inf"], None, "Look for: the topic, facts from the text, and (grades 1-2) a closing sentence.")},
     "narrative": {A: (fmt, None, P["nar"], None, "Look for: events in order with details and time-order words, and a reaction or ending.")},
     "process": {A: ("Fix the sentence", None, f"Fix the capital letters and punctuation: \"{P['edit']}\"", None, P["edit_ans"])},
     "research": {A: ("Shared research", "article", P["rq"], None, P["rq_ans"])},
     "foundations": {A: ("Read aloud", None, f"Read these words: {P['words']}.", None, P["wans"])},
    }
