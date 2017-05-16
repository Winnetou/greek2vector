import numpy as np

consonants=list('βγδκτπμνσςλῥρζξψθφχ')
vowels = list('')
short_vowels = list("εο")  #
long_vowels = list("ηω")
consonant_clusters = list("ζξψ")
liquids = list("λῥρ")
nasals = list("μνσς")
tenuis_stops = list("κτπ")
voiced_stops = list("βγδ")
aspirated_stops = list("θφχ")

# below: a big dict, where we map


numeral_vals = {

"α": 0.010,
"ᾳ":0.01,

"ἁ":0.01,
"ἀ":"",
"ᾀ":"",
"ᾁ":"",

"ὰ":"",
"ᾲ":"",
"ά":"",
"ᾴ":"",
"ᾶ":"",
"ᾷ":"",


"ἅ":"",
"ᾅ":"",

"ἂ":"",
"ᾄ":"",


"ἆ":"",
"ἇ":"",
"ᾇ":"",

"β":0.1,
"γ":0.2,
"δ":0.3,

"ε":0.4,
"ἑ":0.4,
"ἐ":0.4,

"ὲ":0.4,
"έ":0.4,

"ἒ":0.4,
"ἓ":0.4,
"ἔ":0.4,
"ἕ":0.4,

"ζ":0.5,

"η":0.6,
"ῃ":"",

"ἡ":"",
"ἠ":"",
"ὴ":"",
"ή":"",
"ῆ":"",

"ἤ":"",
"ἥ":"",
"ἢ":"",
"ἣ":"",
"ἦ":"",
"ἧ":"",

"θ":0.7,

"ι":0.8,
"ἰ":"",
"ἱ":"",

"ὶ":"",
"ί":"",
"ῖ":"",

"ἲ":"",
"ἴ":"",
"ἳ":"",
"ἵ":"",
"ἶ":"",
"ἷ":0.8,

"κ":0.9,
"λ":0.10,
"μ":0.11,
"ν":0.12,
"ξ":0.13,

"ο":0.14,

"ὀ":"",
"ὁ":"",

"ὸ":"",
"ό":"",

"ὄ":"",
"ὅ":"",
"ὃ":"",
"ὂ":"",

"π":0.15,

"ῥ":"",
"ρ":"",

"σ":"",
"ς":"",
"τ":"",

"υ":"",
"ὑ":"",
"ὐ":"",
"ὺ":"",
"ύ":"",
"ῦ":"",

"ὒ":"",
"ὔ":"",
"ὕ":"",
"ὓ":"",
"ὖ":"",
"ὗ":"",

"ϋ":"",

"χ":"",
"ψ":"",
"φ":"",

"ω":"",

"ὡ":"",
"ὠ":"",

"ὼ":"",
"ώ":"",
"ῶ":"",

"ὢ":"",
"ὤ":"",
"ὥ":"",
"ὣ":"",

"ὦ":"",
"ὧ":"",

"ῳ":"",

}


def _letters_vector(letter):
    return 0

def vectorize_word(word):
    """

    :param word:
    :return:
    """
    # the vector we return includes:
    # position of the letter in the word. as a number
    # position of the letter in the word from the end -  as a number

    # if the letter is a consonant or a vowel
    # if it is accented
    # type of accent - acutus, gravis, circumflex

    # for every letter, we also record the previous and the next letter,
    #  default to 0 if the previous or the next
    # is whitespace.
    for position, letter in enumerate(word):
        previous_letter, next_letter = 0, 0
        if position == 0:
            # no previous
            previous_letter = 0
        else:
            previous_letter = _letters_vector(word[position-1])

        if position == len(word)-1:
            # it is the last letter
            next_letter = 0
        else:
            next_letter = _letters_vector(word[position+1])
        {}