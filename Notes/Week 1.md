# Week 1
# Machine Learning Introduction

## 1) The simplest idea: what is AI?

- At the highest level, AI is about making computers do tasks that seem intelligent. 
- That can mean recognizing images, understanding speech, making decisions, predicting outcomes, or generating text and images. 
- The slides show AI as an umbrella term that includes supervised learning, unsupervised learning, reinforcement learning, and other areas like perception, navigation, and data analysis.
- A beginner-friendly way to think about it:
    - Data = examples from the real world.
    - Model = the machine’s way of finding patterns.
    - Learning = improving the model from experience.
    - Prediction / action = using the learned model on new input.
- So instead of writing fixed rules for every situation, AI often tries to learn patterns from data. That is the central theme behind modern machine learning.

## 2) Why the slides start with news and hype

- The first part shows AI in the news, with excitement, fear, and market growth. 
- The message is: AI is not just theory anymore; it has become important in business, research, and everyday tools. 
- The slides also show that AI is often discussed in extreme ways: some people think it will transform everything, while others fear it too much. 
- The course wants you to understand AI carefully and technically, not just follow the hype.
- A simple practical example:
    - When ChatGPT answers a question, it is not “thinking” like a human person. It is producing output based on learned patterns. That is still very powerful, but it is different from human intelligence. The slides later mention that generative AI can also hallucinate information, meaning it can produce plausible but wrong answers.

## 3) The history in plain English

- The history section is important because it explains why AI developed the way it did.

### Early inspiration: the brain

- In the 1930s–1950s, AI research was influenced by neuroscience. Scientists studied neurons: they receive signals and send signals. 
- That inspired the idea that intelligence might be built from many simple units connected together.

### Cybernetics and information theory

- Norbert Wiener worked on cybernetics, which studies control and feedback in animals and machines.
- Claude Shannon created information theory, which formalized how information can be measured and transmitted. The slides say this became foundational for digital circuits and computation, and the entropy formula is used widely in AI.

### Alan Turing

- Turing appears as a foundational figure in computation theory and AI. The slides mention:
    - computation theory: what computers can and cannot do
    - the Turing test: can a computer convince a human that it is human?

### Dartmouth, 1956

- The Dartmouth Summer Research Project on Artificial Intelligence is presented as the founding event of AI, including the name “artificial intelligence” itself. 
- That is why 1956 is a famous starting point in AI history.

## 4) Why early AI was both exciting and disappointing

- The slides show that early AI had big dreams:
    - problem solving
    - neural networks
    - language
    - toy worlds like Blocks World
- Then came a reality check.

### Perceptron limitation

- The perceptron was an early neural-network-style model. It could solve some problems, but not all. The famous example in the slides is XOR, which a simple perceptron cannot represent. This showed that early neural networks had limits.

### AI winter

- Because of limitations in hardware, complexity, and knowledge representation, funding slowed down. The slides call this the first AI winter. In simple terms: people expected too much too soon, and progress did not match the hype.

## 5) The expert systems era

- In the 1980s, AI came back through expert systems. These systems used:
    - a knowledge base: facts and rules
    - an inference engine: a mechanism that applies rules to draw conclusions
- Think of it like a doctor’s checklist:
    - If fever and cough → maybe pneumonia or COVID-19.
    - If wheezing and shortness of breath → maybe asthma.
- This is useful, but it is limited because:
    - it depends on manually written rules,
    - it is hard to scale,
    - it is brittle when the real world becomes messy.

## 6) Why neural networks came back

- The slides highlight three major breakthroughs.

### 1. Hopfield networks

- These are associative memory systems. 
The idea is simple: if the network has learned a clean pattern, it can recover that pattern from a noisy version. A useful analogy is restoring a blurry digit image back to a clean digit.

### 2. Backpropagation

- This is one of the most important ideas in AI. The question is:
    - How do we change the parameters of a model so that its outputs become closer to the correct answers?
- The slides give a taxi pricing example. You observe ride duration and cost, and you want the model to learn the pricing rule. 
- Backpropagation is the method that helps a neural network adjust itself based on errors.
- Very simply:
    - make a prediction,
    - compare it with the true value,
    - measure the error,
    - send that error backward through the network,
    - update the parameters.

### 3. Convolutional networks

- Yann LeCun’s work showed that neural networks could recognize handwritten digits efficiently. This became very useful for tasks like zip code reading and check processing. The main idea is that convolution helps detect patterns like edges, shapes, and digit strokes.

## 7) Probabilistic models: another way AI thinks

- The slides also cover Bayesian networks and probabilistic graphical models. Here, instead of focusing on neural-style learning, the idea is:
    - represent variables and their dependencies as a graph,
    - use probabilities to reason under uncertainty.
- Example from the slides:
    - disease influences cough,
    - if we know the probabilities, we can compute the probability of disease given cough using Bayes’ rule.
- Beginner version:
    - If someone has a cough, that does not automatically mean they are sick. But cough makes illness more likely. Probability helps AI reason when it is not certain.

## 8) Modern AI: generative models

- Since around 2017, the slides say AI has been dominated by generative models—systems that can create text, images, and video. The technical foundations mentioned are attention and diffusion.

### Attention

- Attention helps the model decide which words matter most to each other in a sequence. 
- The slide’s example sentence about “the animal” and “it” shows that understanding pronouns requires linking words across the sentence. 
- Attention helps the model focus on the relevant earlier word.

### Diffusion

- Diffusion is described as: humans specify how to destroy content, and the AI learns how to reverse that process. 
- In practice, that means adding noise step by step, then learning how to denoise and reconstruct data. 
- That is the basic idea behind many image-generation systems.

## 9) Consumer AI: what you already know

- The slides give examples like chatbots, text-to-image systems, and text-to-video systems. These tools can:
    - answer questions,
    - adapt to styles,
    - perform creative tasks,
    - schedule calendars,
    - generate code,
    - do visual analytics,
    - solve math problems.
- But the slides also warn that these systems can hallucinate. So the skill you need is not only “using AI,” but also checking, verifying, and thinking critically.

## 10) AI in research and real-world applications

- This lecture also shows AI beyond chatbots:
    - Biology: protein structure prediction, where amino acid sequences determine 3D structure and function. The slides mention AlphaFold as a major success.
    - Physics: reconstructing temperature, pressure, and velocity fields from measurements.
    - Medicine: improving MRI-based blood flow measurements with physically accurate AI.
    - Gaming: generating visual game frames from user input rather than relying only on explicit world rules.
    - Finance: using market data to predict actions like buy or sell.
Autonomous driving: perception, mapping, planning, and control.
- This is important for you because it shows AI is not one single thing. It is a toolkit used in many domains.

## 11) What this course expects from you

- This part is very practical. The course uses:
    - Python 3
    - packages like numpy, scipy, matplotlib
    - coding exercises done from scratch rather than just using ready-made AI tools.
- That means your success depends on three foundations:
    - basic programming,
    - math,
    - patience with implementation.
- The slides also clearly say that if you are rusty, you should review:
    - probability and distributions,
    - linear algebra,
    - derivatives and calculus.

# Slide 1: 

- The word “Machine Learning” tells you:
    - You are going to learn how machines learn from data
    - Not just definitions, but how to build and understand models
- Machine Learning = Teaching a computer to learn patterns from data instead of manually programming rules.
- Real Life Example:
    - Instead of writing:
        - if email contains "win money" → spam
    - Machine Learning does:
        - Give 10,000 emails (spam + not spam)
        - The model learns patterns automatically
        - Then predicts for new emails

## What is the difference between programming and machine learning?

### Traditional Programming
- You write rules manually.
#### Example:
- If temperature < 0 → show “cold”
- If email has “win money” → spam
- So the flow is:
    - Input → Rules (written by you) → Output

### Machine Learning

- You don’t write rules directly.
- Instead, you give:
    - Data (examples)
    - Expected answers
- The machine learns the rules by itself.

#### Example:
- Give 10,000 emails (spam + not spam)
- Then predicts new emails
- Model learns patterns
- So the flow is:
    - Input + Output examples → Learning → Model → Output

### Key Difference (VERY IMPORTANT)
- Programming = explicit rules
- Machine Learning = learned patterns from data

## 2) Why is “learning from data” useful?

- Because real-world problems are too complex to write rules for.

#### Example 1: Image recognition

- Can you write rules like:
    - “If pixel 1 = this, pixel 2 = that → it's a cat”?
    - ❌ Impossible.
- But ML can:
    - Look at thousands of cat images
    - Learn patterns automatically

#### Example 2: Speech recognition

- Human speech varies:
    - Accent
    - Speed
    - Noise
- Writing rules = ❌ impossible
- Learning from data = ✅ works

#### Example 3: Fraud detection

- Fraud changes constantly.
    - Rules become outdated ❌
    - ML adapts from new data ✅
    - Core idea
- Learning from data allows systems to:
    - Handle complexity
    - Adapt over time
    - Work in real-world messy situations

#### Final Simple Summary

- Programming → You teach the computer what to do
- Machine Learning → You let the computer figure out how to do it

# Slide 2
# Slide 3
# Slide 4
# Slide 5
# Slide 6
# Slide 7
# Slide 8
# Slide 9
# Slide 10
# Slide 11
- Early AI inspired by neuroscience
- Focus on neurons (brain cells)
- Key ideas:
    - neurons receive signals
    - neurons send signals
- Simple explanation
    - Early scientists tried to understand:
        - “How does the human brain work?”
    - Then they thought:
        - “Can we build machines that work like the brain?”

### 1) What is a neuron? (very simple)

-   In your brain:
    - A neuron receives signals from other neurons
    - Processes the information
    - Sends a signal forward

- Simple analogy
    - Think of a neuron like a switch:
        - Inputs come in
        - It decides something
        - Sends output

### 2) Why is this important for AI?

- Because this idea led to:
    - Artificial Neural Networks which are used in:
        - image recognition
        - speech recognition
        - chatbots

### 3) Real-world connection

- When you use: 
    - YouTube recommendations
    - Instagram feed
    - ChatGPT
- Behind the scenes → neural networks inspired by the brain

### 4) Key insight (VERY IMPORTANT)

- AI did NOT start with computers alone
- It started with:
    - biology (brain)
    - neuroscience

### 5) Beginner mental model

- Think like this:
    - Brain neuron → inspiration
    - Artificial neuron → implementation

### One-line takeaway (Slide 11)
- Early AI was inspired by how neurons in the human brain receive and send signals.

# Slide 12

# Slide 13
What’s on the slide?
Mentions Norbert Wiener
Concept: Cybernetics
Definition:
👉 “control and communication in the animal and the machine”
Focus on:
feedback
recursive systems
🧠 Simple explanation

👉 Cybernetics = systems that observe → act → adjust based on feedback

🔁 What is “feedback”?

Feedback means:
👉 The system checks its output and corrects itself

🔹 Simple real-life example

Think of a thermostat (room temperature controller):

You set temperature = 22°C
Room is 18°C → heater turns ON
Room reaches 22°C → heater turns OFF

👉 System continuously:

observes
compares
adjusts

This is feedback control

🤖 Why is this important for AI?

Because AI systems also:

take input
produce output
adjust based on error

👉 This is the base idea behind:

learning
optimization
backpropagation (later topic)
🔁 “Recursive system” (don’t worry, simple meaning)

👉 A system that:

repeats a process
uses its previous output as input
Example:
YouTube recommendations:
you watch → system updates → recommends → you watch again → system updates again

👉 Continuous loop

🧠 Key insight (Slide 13)

👉 Intelligence is not just thinking—it is:

reacting
correcting
adapting
One-line takeaway

👉 Cybernetics introduced the idea that intelligent systems use feedback to continuously improve their behavior.

# Slide 14

What’s on the slide?
Mentions Claude Shannon
Concept: Information Theory
Definition:
👉 “quantification and transmission of information”
Introduces:
👉 Entropy formula
🧠 Simple explanation

👉 Information Theory = how we measure and handle information mathematically

📦 What is “information”?

Think:

a message
data
signal

Example:

text message
image
audio
📊 What is “quantification”?

👉 Measuring information in numbers

Instead of saying:

“this message is complex”

We say:
👉 “this message has X amount of information”

🔥 What is “entropy”? (very important)

Don’t worry about formula yet.

👉 Entropy = uncertainty

🔹 Simple examples
Case 1: No uncertainty
You already know the answer

👉 Entropy = LOW

Case 2: High uncertainty
Many possible answers

👉 Entropy = HIGH

🎲 Example

Flip a coin:

If coin is always HEAD → no uncertainty → low entropy
If coin is fair → unpredictable → high entropy
🤖 Why is this important for AI?

Because AI deals with:

uncertainty
probabilities
predictions

Examples:

spam detection → not 100% sure
image recognition → probability of “cat”

👉 Entropy helps measure:

how uncertain the model is
how much information is in data
🔗 Connection to modern AI

Entropy is used in:

loss functions (training models)
decision trees
probabilistic models

👉 You will see this again later (VERY IMPORTANT)

🧠 Key insight (Slide 14)

👉 Intelligence requires handling uncertainty, not just fixed rules

One-line takeaway

👉 Information theory provides a mathematical way to measure uncertainty and information, which is fundamental for AI systems.

Together, they give you two core ideas:

Slide 13 → Control & Feedback

👉 Systems learn by correcting themselves

Slide 14 → Information & Uncertainty

👉 Systems deal with uncertainty using math

🧠 Final Big Picture

👉 AI =

feedback (learning) +
uncertainty handling (probability & information)

# Slide 15

What’s on the slide?
Field: Computation theory
Focus:
what computers can and cannot do
formal languages, computability, complexity
Mentions:
“Intelligent Machinery” (1948)
idea of learning via reward and punishment
🧠 Simple explanation

👉 This slide is about:

“What does it mean for a machine to think or compute?”

1) What is computation theory?

👉 It studies:

What problems computers can solve
What problems they cannot solve
How efficient solutions are
Simple analogy

Think of a calculator:

Can it solve 2 + 2? ✔️
Can it understand emotions? ❌

👉 Computation theory defines these limits

2) Turing’s big idea

Alan Turing asked:

👉 “Can machines be intelligent like humans?”

This was a revolutionary question at that time.

3) Learning via reward & punishment

This is VERY important.

👉 Idea:

If the machine does something correct → reward
If wrong → punish
Real-life analogy

Think of training a dog 🐕

Sit correctly → give treat ✔️
Wrong behavior → no reward ❌

👉 The dog learns over time

AI connection

This idea later becomes:
👉 Reinforcement Learning

Used in:

game AI (chess, AlphaGo)
robotics
decision-making systems
🧠 Key insight (Slide 15)

👉 Intelligence can come from learning through feedback, not just fixed rules

One-line takeaway

👉 Turing introduced the idea that machines can learn and that there are limits to what computers can do.

# Slides 16

What’s on the slide?
Paper: “Computing Machinery and Intelligence” (1950)
Concept: Turing Test
Question:
👉 Can a computer trick a human into thinking it is human?
🧠 Simple explanation

👉 The Turing Test is a way to check:

“Is a machine intelligent?”

1) How the Turing Test works

There are 3 participants:

A → Machine
B → Human
C → Judge (another human)

👉 The judge communicates (usually via text)

Goal:

👉 If the judge cannot tell who is the machine…

➡️ The machine is considered “intelligent”

2) Simple example

You chat with:

Person 1
Person 2

One is human, one is AI.

If you cannot distinguish them:

👉 AI passes the test

3) Why this is important

Before this:

Intelligence was abstract

Turing made it testable

4) Hidden insight (VERY IMPORTANT)

👉 AI does NOT need to “think like humans” internally

It only needs to:
👉 behave like a human externally

5) Modern connection

Chatbots like:

ChatGPT
virtual assistants

👉 Try to behave in a human-like way

(Some partially pass the Turing test in limited settings)

🧠 Key insight (Slide 16)

👉 Intelligence can be judged by behavior, not internal structure

One-line takeaway

👉 The Turing Test defines intelligence based on whether a machine can imitate human behavior convincingly.

