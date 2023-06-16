Post-reading thoughts:

- figure out how to model gender in an LM
	- could theoretically be most accurate
	- toilsome to implement for each language
		- relies on language having stable consensus over syntax, orthography, etc
	- syntax modeling may be inflexible to changes / reinforces mistakes
	- prescriptive
- model with more nonbinary language
	- would need to find corpora;
	- this study showed things still inaccurate after fine-tuning with nonbinary.wiki data, not clear that adding more data would help (although trends in CL suggest it might)
- make nonbinary language corpora by substituting pronouns & agreement in existing works, use that to create model / fine-tune
	- artificial; might not reflect actual spoken language
	- can be automated for time savings, but would rely on accuracy of POS taggers and whatever automaton not being buggy
		- should still have humans review
	- could be hand-processed to maybe somewhat increase authenticity of language
		- laborious
		- not guaranteed to be as natural as actual texts using nonbinary language



# * * * Paper reading * * *

pdf: [[Dev et al 2021 - Harms of Gender Exclusivity.pdf]]
url: https://aclanthology.org/2021.emnlp-main.150.pdf


## abstract

why doesn't the content warning line show up in the abstract when zotero imports this paper?

## 2. Gender, Language, and Bias

section 2.1 specifically could work well as a primer for a cis person wanting to learn about trans and nonbinary people

<mark style="background: #FFFF00;">TODO</mark>: lookup references:
- (Rajunov and Duane, 2019)
	- see [[Micah Rajunov, Scott Duane - Nonbinary_ Memoirs of Gender and Identity (2019, Columbia University Press) - libgen.li.pdf]]
- (Cao and Daumé III, 2020)
	- https://aclanthology.org/2020.acl-main.418/
- (Barocas et al., 2017)  on representational and allocational harms
	- https://fairmlbook.org

- notes that {gender id, gender presentation, sex} overlap and manifest differently
- notes that paper is english-specific and specific to gender in western culture

- referential gender
	- pronouns
	- names
- lexical gender
	- non-referential gender
	- e.g. "mother", "Mr.", etc

## 3 Harms

examine specific NLP tasks, understand harms

- misgendering
- erasure
	- cyclic
		- as papers & tech published assuming binary gender, it begets more research built with the assumption of binary gender


## 3.1 Survey on Harms

survey sample:
- nonbinary people
- familiar with ai
- English fluency

acknowledges this is a skewed audience wrt socioeconomics, ethnicity
- see also 3.1.1 on actual demographics of population

survey:
- anonymous
- all Qs optional
- not paid


## 3.1.1. Survey Demographics

19 participants:
- 17 white
- 84% use they/them (assuming this may be in combination w others)
- mostly from US, or otherwise mostly Canada & West Europe


## 3.1.2. Harms in Language Tasks

- Allocational harms, Representational harms
	- NER, coref resolution, MT

survey tasks use AllenNLP demos

non-leading questions about alloc & rep harms that the given task could pose to nonbinary people
- Q: is there a way to assert a question isn't leading?

\>84% can think of bad consequences in current tech wrt nonbinary gender


## 4.2. Text representation Skews

Representational erasure in GloVe
- neopronouns don't have meaningful neighbors; trad pronouns do

Biased associations in GloVe
- binary gender
	- problematic adjective association
- nonbinary
	- sentiment bias for words like "transman", "nonbinary"
	- associations vastly different than w binary associations
	- slurs & derogatory terms present among neighbors

Representational erasure in BERT
- neopronouns infrequent, poor embeddings
- sometimes recognizes singular they ( they(s) / they(p) ), but not often or accurately

trained bert with some masked pronoun sentences
- sentences from non-binary wiki
- manually annotated
- improved accuracy, but not enough to consistently distinguish they(s) / they(p)

bert & misgendering
- misgenders frequently, reinforces erasure
- proposed eval framework
	- use 919 ~unisex names from public record to minimize gender correlation


## 5. conclusion

- recap
- paper catalogues harms
- discrete gender buckets inevitably leads to marginalization

open question
- how to define and model gender in lang representations & tasks
- *if* we should define and model gender in lang representations


-----

# * * * Video Watching * * *

url: https://aclanthology.org/2021.emnlp-main.150.mp4

tech failing example
- coref resolution failing with sing they

## Misgendering
- can be forced to self-misgender in forms and reporting due to required binary input

## Erasure
- Research assumptions of binary lead to erasure
- Outputs for eval and comparison continue only producing binary lang
- cyclic

## Survey on harms

examine representational harms and allocational harms across categories of tech:
- NER
- Coref res
- MT

## Challenges

evaluate where biases encoded

## skewed data example: wikipedia text:

- he 15 M
- she 4.8 M
- they 4.9 M
- ze 7.4 thou
- xe 4.5 thou

neopronoun counts have false positives too 

nearest neighbors inaccurate for neopronouns

leads to models like bert not understanding they

## tasks for misgenedering by bert

$name went to hospital for $pronoun appointment. $redacted was feeling sick

not only unable to predict to pronouns generally, misgenders

## How (and if) to model gender

need this to make fair systems that

## prev attempts

third option "other"

"they" doesn't work as a third bucket, still misgenders, erases identities

task-based approach?

human-in loop model building?


