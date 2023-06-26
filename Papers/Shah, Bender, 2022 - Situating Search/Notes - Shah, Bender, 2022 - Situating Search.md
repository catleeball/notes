# Notes for 20%

## Takeaway thoughts / questions / todos

- for systems that challenge false presuppositions:
	- how do they establish what is true? how do they deal with subjective information?
		- review Kim et al 2021 "which linguist invented the lightbulb" about presupposition verification
		- seems very hard, especially for "generalist" applications; maybe more doable for a small specific domain
	- do any QA systems currently challenge false presuppositions? what has that experience been like for users? and approximately how accurate is it?
- are there any comparative studies evaluating 'view from nowhere' effect between search engines vs CA-based search?
	- how would you meaningfully measure / compare?
- are there Q&A systems that clarify user queries or lit about it?
	- seems easier for domain-specific Q&A

- read more about cisnormativity
	- its presence in media
	- its impact on people & communities
- find lit about disinformation harms wrt TGNB folks
	- specific to generative LMs is good, but also from IR and media is good perspective
- learn more about qualitative methodology & qual experiment design that could be relevant going forward


## Notes by section

### 3.1

> Kalervo P. Jarvelin (2018 winner \[Salton Award\]) emphasized how important it is to understand and model the context in which the information interactions take place, in order to serve the information seekers

> ChengXiang Zhai (2021 winner \[Salton Award\]) presented a view of search systems where the notion of ‘intelligence’ has been shifting from system-centered to user-centered.

Opinions same from CHIIR, RecSys, The Web Conference, and WSDM

### 4.2

going over information search strategies (ISS)

> These all involve cases of **browsing** and **sense-making**.

*4.2. Analysis subsection*

- Goal of ISS analysis: illustrate that model-based dialogue agents hinder users performing IR
	- system sounds too authoritative in Q&A
		- e.g. Google question box: “What is the ugliest language in India?” -> Kannada
	- "rather than answering the question, the system should challenge the presupposition"
		- (aside) refer to google paper "Which Linguist Invented the Lightbulb?"
	- "answering the question without challenging the presupposition implicitly accepts those presuppositions into the common ground, i.e., implicitly affirms the user's point of view"
		- (aside) in addition to the two citations in this paper, see "Using Language" (Clark, 1996) [link](https://doi.org/10.1017/CBO9780511620539) wrt concept of common ground
	- "But what is needed here is not a system that purports to answer questions and flags cases of ‘disagreement’ or ‘controversy’, while generating synthetic links to possible sources for ‘both sides’, but rather information exploration tools that help users to differentiate among information sources."
		- big agree
		- difficult to do, but also conversational agents for IR seem like a regression in this regard, plus the other issues outlined in the paper
		- see also footnote 10 in paper
	- See also 4.3 

**above bullet pts: possible disinformation harms from generative lang models**

- " by synthesizing results from multiple different sources and thus masking the range that is available, rather than providing a range of sources, the system cuts off the user's ability to explore that space."
	- Limits info available to trans & nonbinary & questioning people

### 4.3

- Paper poses question "How would \[dialogue-style\] search results be interpreted by ... people who struggle to express their information needs?"
	- "_people don't know what they don't know_" (todo: see ref Shah 2018 [link](https://doi.org/10.1145/3176349.3176389](https://doi.org/10.1145/3176349.3176389))
	- paper mentions language proficiency, information literacy as non-exclusive causes
	- todo: see CHIIR 2019 conference regarding "debate" about whether search engines should support "information-literate actions such as comparing, evaluating, and differentiating between information sources"

- many queer kids grow up in strict homes that restrict information about queer people
- people with a background with limited info about queer identities won't be able to search and learn more about identities they are unaware of or misinformed about
	- goes back to IR system needs to challenge presuppositions
	- todo: find lit about Q&A systems that clarify user queries maybe?

### 4.4 - Addressing bias in search results

todo: A lot of the references here look maybe useful

> As Benjamin [[9](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0009)] argues, this is because race itself is a technology which interacts with the design and use of other technologies to present whiteness as default and normal and the white gaze as dispassionate and allowing a ‘view from nowhere’ 

- todo: look over reference 9 
- consider similar to above where the "default" is cisnormative
	- todo: look up queer studies lit about cisnormativity and its influence / harms

> increasing the range and extent of harmful biases amplified by the system and in terms of decreasing users’ ability to recognize and refute those biases

- paper argues 'view from nowhere' is exacerbated by current CAs for IR
	- a bunch of refs on bias in LMs
		- [32](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0032), [11](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0011), [16](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0016); see [10](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0010) and [7](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0007) for overviews
	- people less likely to challenge info from an interlocutor
		- [1](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0001), [24](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0024)
		- people not refuting or recognizing bias from regular search engine results still a problem too though [54](https://dl.acm.org/doi/fullHtml/10.1145/3498366.3505816#BibPLXBIB0054), but argues that current state of CAs will worsen this
			- **question**: is there a way to evaluate if people are more or less likely to challenge a CA's results vs a traditional search engine? was this done in any of the above refs already?

author's argument for CAs worsening 'view from nowhere'

>Contrast \[traditional search engine query\] with posing the query as a question to a dialogue agent and receiving a single answer, possibly synthesized from multiple sources, and presented from a disembodied voice that seems to have both the supposed objectivity of not being a person (despite all the data it is working with coming from people) and access to “all the world's knowledge”. Where are the toe-holds that would allow a user to start to understand where the results are coming from, what biases the source data might contain, how those data were collected, and how modeling decisions might have amplified biases?

### 5.2 - A new vision

author states desiderata for ideal search system. most relevant seem like:

- transparency about sources & their rankings / presentation
- should support users in improving their information literacy

> the system should instead first focus on better understanding those contexts and tasks through a combination of context extraction techniques, dialogue with the user, and support for interaction.

question: is it possible to perform "dialogue with user" from a CA in a meaningful way that solves the other problems?
- assuming probably not, because that's just the entire field of library science
- followup Q: barring dialogue, how can an automated IR system help provide guidance to user in their search tasks that could improve their information literacy?
	- this would also be vulnerable to bias and 'view to nowhere', but maybe less so than current state of things?

> the system should foreground sources and avoid decontextualizing snippets of text (or ‘information’) ... preservation of context is crucial to combating the pernicious effects of pattern recognition over datasets expressing harmful social biases

- this would be cool but extremely hard
- this relies on understanding the user's background and intents (i.e. common ground)
	- raises question of how much background on a user, if any, is appropriate or ethical to collect in order to facilitate these interactions
	- also relies on accurate semantic understanding of the user's query, in addition to accounting for their background, the context of the question and intent, etc
