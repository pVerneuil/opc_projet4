from PyInquirer import prompt, Separator, Token, style_from_dict

style = style_from_dict({
    Token.Separator: '#673ab7 bold underline',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

main_menu = [
    {
        'type': 'list',
        'name': 'main_menu',
        'message': '=== Menu Principal ===',
        'choices': [
            Separator('= Tournois ='),
            'Créer un tournois',
            'Charger un tournois',
            Separator('= Joueurs ='),
            'Consulter les joueurs',
            'Ajouté un joueur',
            'Modifier le classement',
            Separator('= Rapports ='),
            'Liste de tout les joueurs',
            "Liste des joueurs d'un tournois",
            'Liste des tounois',
            Separator(),
            'Quitter'
        ]
    },
]