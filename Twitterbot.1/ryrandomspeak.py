import random

x=0
while x < 10:

    nouns = (
        "This",
		"My",
		"That",
		"Kath's",
		"Your",
		"Riley's",
		"Some",
		"Her friend's",
		"Someone you know's",
		"The",
	)
    verbs = (
        "pissed",
		"destroyed",
		"ruined",
		"shat",
		"chewed on",
		"totally fucked-up",
		"didn't help","puked on",
		"made a foul mess of",
		"got fur on",
	) 
    moniker = (
        "bastard",
		"cat",
		"kitten",
		"dipshit",
		"monster",
		"a-hole",
		"bit of fluff",
		"wide-eyed shitbag",
		"furry fuckwad",
		"silly sack o' turds",
    )
    adj = ("adorable",
		"clueless",
		"fucking",
		"reprehensible",
		"stupid",
		"hopeless",
		"stinking",
		"furry",
		"psychotic",
		"monsterous",
	)
    ob = (
        "my carpet.",
        "my chances for love.",
        "most of my life.",
        "my best T-shirt.",
        "Kathy's shoes.",
        "everything outside her litter box!!",
        "Gwen's bed.","the kitchen counter!",
		"my parent's luggage.",
		"my face.",
    )
    
    sentence = '{0} {1} {2} {3} {4}'.format(
        *[
            parts[random.randrange(0,len(parts))] 
            for parts in (nouns,adj,moniker,verbs,ob)
        ]
    )
    #sentence = nouns[num1] + ' ' + adj[num2] + ' ' + moniker[num3] + ' ' + verbs[num4] + ' ' + ob[num5]
    print(sentence)
    x = x + 1  


