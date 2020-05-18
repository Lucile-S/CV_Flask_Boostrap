"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = "<p> Je suis apprentie Développeuse Data IA à l’école  IA Microsoft powered by Simplon et j’aspire à travailler dans le domaine de la santé. Très curieuse avec l'envie de toujours apprendre, j’ai étudié à la fois l’infiniment grand, l’astrophysique, avant de passer à l’infiniment petit, la science des protéines.  J'ai une expérience de 6 ans en tant que chercheuse dans différents laboratoires. Je conserve de mes activités de recherche une autonomie, une rigueur et une capacité d'analyse, ainsi que le goût de la programmation et de l’analyse de données. À présent, je veux mettre mes nouvelles compétences et mon expérience à la disposition d’une équipe pour exploiter la puissance des données et de l’IA au profit des enjeux de demain.  </p>"


languages = [
        ['Français', ' (Natif)'],
        ['Anglais', ' (Intermédiaire)']
        ]

education = [
        ['Formation Simplon "Développeur Data IA" ', 'Ecole IA Microsoft - Issy les Moulineaux ', 'Mars 2020 - Auj.'],
        ['Doctorat en Biochimie Structurale', 'Univ. Pierre et Marie Curie - Paris ', '2016'],
        ['Master 2 Physique spécialité Biophysique ', 'Univ. Pierre et Marie Curie', '2013'],
        ['Master 2 Physique spécialité Astronomie et Astrophysique', 'Univ. Pierre et Marie Curie', '2012'],
        ['Licence Physique et Chimie ', 'Univ. du Littoral Cote d’opale, Dunkerque ', '2010'],
        ]

interests = ['Sport, Cuisine, Patisserie, MOOC']

moocs = [
        ['Spark and Python for Big Data with PySpark'],
        [' Probability and Statistics in Data Science using Python'],
        ['Python for Data Science and Machine Learning Bootcamp '],
        ['Data Science in Stratified Healthcare and Precision Medicine '],
        ]

"""
Experience
----------
This should be a list of lists. Each sublist corresponds to a particular job
and is of the form:
    ['Title', 'Date range', 'Company name and location', 'Description of role']

The 'Description of role' field does not get escaped by the templating engine,
so you can put raw HTML in it if you like.
"""
experience = [
       [' Chercheuse en Science des protéines ',
            'Mars 2017 - Oct. 2019',
            'CNRS/Univ. de Montpellier, Centre de Biochimie Structural',
            '<p></p> Analyse de données expérimentales : automatisation de la collecte, du nettoyage, du traitement des données et de la visualisation des résultats par des scripts Python </p> Production, purification, préparation et caractérisation expérimentale (Résonance Magnétique Nucléaire) et bioinformatique d’une protéine dans le but de mieux comprendre son fonctionnement </p>'
        ],
        ['Chercheuse Doctorante',
            'Oct. 2013 - 0ct. 2016',
            'Univ. Pierre et Marie Curie, Laboratoire des BioMolécules, Paris',
            '<p>Production et purification de protéines membranaires et leur études structurales et biophysiques </p><p>Enseignement TD et TP de chimie analytique, niveau Licence 1 et 2  </p>'
        ],
        ['Chercheuse Stagiaire ',
            '2011 et 2012',
            'Univ. Pierre et Marie Curie - Institut d’Astrophysique de Paris ',
            '<p>Exploration (data mining) d’une grande quantité de données photométriques </p></p>Croisement de catalogues de données (avec Python) pour la recherche de planètes en transit autour d’étoiles  </p> </p>Traitement et analyse d’images astronomiques (avec Python et IDL) </p>'
        ]
    ]

"""
Projects
--------
The project_intro field is for a short introduction to your work.
Project are a list of lists, where each sublist refers to a specific project,
and is of the form:
    ['Title', 'Description', 'Link to project webpage']
"""
# project_intro = ''
skills = [
        ['Programmation ',
            'Python (avancé), R et MySQL (débutant)'
        ],
        ['Machine Learning ',
            'Scikit-Learn,  PySpark,  Keras '
        ],
        ['Tâches sur les données',
            'Visualisation, Manipulation, Nettoyage, Analyse exploratrice, Modèle prédictif '
        ],
        ['Outils Web & Applications ',
            'Selenium, BeautifulSoup, Docker, Git, Streamlit, Flask, Shiny'

        ],
        ['OS',
            'Linux/Unix, Windows, Mac',
        ],
        ['Bureautique',
         'LaTeX', 'Microsoft Office', 'Open Office'
           
        ]
    ]



"""
default_data
------------
This dictionary puts everything together. It will be read by the Flask app when
it is instantiated.
"""
data = {
    'site_title' : 'Responsive Resume/CV Template for Developers',
    'name' : 'Lucile S',
    'tagline' : 'Data Scientist Junior',
    'email' : ' xxe@website.com',
    'phone' : ' xxxxxxxxx',
    'researchgate' : ' researchgate',
    'linkedin' : ' linkedin.com/in/xxxxx',
    'github' : ' github.com/username',
    'twitter' : ' kaggle',
    'languages' : languages,
    'education' : education,
    'interests' : interests,
    'moocs' : moocs,
    'summary' : summary,
    'experience' : experience,
    'skills' : skills
    }
