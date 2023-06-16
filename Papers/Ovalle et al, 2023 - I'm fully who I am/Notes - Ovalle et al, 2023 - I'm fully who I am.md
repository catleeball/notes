
# Glossary

- OLG  - open language generation
- harm - *"... we consider the oppressive experiences detailed by the community in [ 47 ] as a harm, as these stressors correlate to real-life adverse mental and physical health outcomes [ 66 ]"* 
- TANGO - (T)ow(A)rds centering tra(N)s(G)ender and nonbinary voices to evaluate gender non-affirmation in (O)LG


# Abstract

notes

- Made TANGO dataset for evaluating bias
	- uses templates
- used to evaluate harms from generative text models
- Harms evaluated:
	- misgendering
	- harmful responses to gender disclosure
- Testing found the most harmful language was in response to gender disclosures
	- what models / systems were tested?

> [!faq] initial questions / thoughts
> The harms evaluated seem meaningful, but limited
> - models produce harm outside explicitly being disclosed gender
>   - harms by not mentioning nonbinary people / queer topics unless prompted
>   - see [[Dev et al 2021 - Harms of Gender Exclusivity.pdf]]
> - How robust are the templates? Do they use syntactic features, or match literals, e.g. regex match?
>   - Is misgendering matched based only on pronoun matching? Does it include deadnaming, honorifics, etc?
> - Authors are almost entirely from Amazon Alexa


# 1. Intro

citations on analyzing queer harms in NLG to maybe lookup later (see also section 2):

> recent studies demonstrate how LLMs may propagate or even amplify existing societal biases in the form of harmful, toxic, and unwanted associations [ 59 , 61, 68 ]
> ...
> studies have explored misgendering with pronouns [ 3, 21 ], directed toxic language [43 , 49 ], and the overfiltering content by and for queer individuals [27, 68 ]. 
> ...
> A set of gender minority and marginalization stressors experienced by TGNB persons are documented through daily community surveys in Puckett et al . [47]


methodology goal is:
1. understand lived experiences
2. use this to inform practice

Uses Puckett et al surveys of harms as pt 1 above


*harm* defined as:

> *"... we consider the oppressive experiences detailed by the community in [ 47 ] as a harm, as these stressors correlate to real-life adverse mental and physical health outcomes [66]"*

but how is that correlation made? TODO: check citation 66


eval questions posed by authors:
1. how often is misgendering is present?
2. how often are responses to gender disclosure negative?

same as above concern about harm in other ways, erasure, etc


Uses nonbinary.wiki as text source, 
contributes to nonbinary.wiki by:
1. release harms dataset collected to wiki 
2. automatic misgendering eval tool & translational experiments (?) to eval harms
3. provides suggestions for better LLMs

> [!Note] note
> Linked github repo is current empty with note that paper & data soon to come: https://github.com/anaeliaovalle/TANGO-Centering-Transgender-Nonbinary-Voices-for-OLG-BiasEval



# 2. Related work

lgbtqia+ datasets section:

> [!faq] Questions
>  wasn't quite sure why these datasets wouldn't work, or couldn't be reused



# 3. Tango dataset & models

# 3.1. Misgendering

- goal: make dataset to eval misgendering in OLG

- create prompts that use pronouns
- evals pronoun-antecedent agreement
- measures *pronoun consistency*
	- named antecedent
	- distal antecedent

> [!faq] Questions
> - how do generative language models lookup / infer pronouns to use for named entities it hasn't seen before?
> - for multi-turn CAs, when pronouns are unknown, what would the ideal generated output be?
> - when is it appropriate for a CA to ask pronouns?
> 	- e.g. can a CA ask your pronouns? your partner's pronouns? a third person who hasn't yet been mentioned's pronouns?
> - when is it appropriate for a CA to infer pronouns? e.g. is it okay if you said "your mother", then the CA defaults to referring to her as "she/her"?

templates

- named antecedent templates
	- randomly sampled from nonbinary.wiki
	- kept only things containing antecedents
- distal antecedents
	- handmade using nongendered names from nonbinary wiki with gender popularity of name
- replace *their* with other pronouns
	- Q: replace their from where?
- distal templates contain xe,ey,fae,he,she (but not they?)
	- *they* can still be used in distal templates
	- e.g. "The person stood in the room with their back to the wall."
- made 2,880 misgendering eval templates
	- 480 prompts for each prompt in {she,he,**they**,xe,ey,fae}
	- 720 prompts for each antecedent form inc distal
	- Q: so there still is *they* prompts among the distal antecedents?

> [!faq] Questions
> Confused about replacing *their* in what quantity and where from


# 3.2. GID Disclosure

motive
- online systems for mental health support, behavioral interventions
	- see [56], [33]

> [!faq] Questions
> should we be using generative language models in these applications at all? extremely high risk place to put a complex probabilistic model


made a dataset of prompts
- gender IDs and disclosures in nonbinary.wiki
- scraped user profiles (!)
- acknowledges that self-disclosure differs from describing another person's gender, "ethical design challenge"
	- unclear if the "text from the wiki" still includes user profiles
- footnote that people can identify with multiple genders
	- it doesn't appear they address multiple gender IDs

> [!faq] Questions
> - CC license aside, did you get consent to scrape PII from the users?
> - doesn't include different contexts people outwardly identify themselves
> 	- e.g. presuppositions, context


