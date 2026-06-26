def descendentes(a):
    return [ nm for nm, _ in a[1] ] + \
           [ nm for f in a[1] for nm in descendentes(f) ]

arv = ( "Maria", [ ("Joana", [ ("Lucio", []),
                               ("Jõao", [])
                             ]
                   ),
                   ("Pedro",[]),
                   ("Patricia", [ ("Marina", [ ("Marcelo", []),
                                               ("Tomás", [])
                                             ]
                                  )
                                ]
                   ),
                   ("Marcos",[])
                 ]
      )

descendentes(arv)