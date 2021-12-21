# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:39:08 2021

@author: User
"""

class fanatic:
    """tem uma lista de topicos sobre os quais sao fanáticos e so podem fazer posts e comentar
mensagens sobre assuntos sobre os quais sao fanaticos. Estes topicos sao definidos atraves
de hashtags (e.g., 7flatearth, 7cutecat, ...). Um fanatico tem sempre uma posicao em
relacao aos temas(s) sobre os quais e fanatico. Se o fanatico tem uma opiniao positiva sobre
um topico(s), so pode fazer comentarios positivos sobre o mesmo, se o post for honesto, ou
comentarios negativos, se o post for falso. Inversamente, se o fanatico tiver uma posicao negativa
sobre esse topico, so podera fazer comentarios negativos em mensagens honestas e comentarios positivos em mensagens falsas.
"""
    def __init__(self,userkind,userid):
        self.userkind = userkind
        self.userid = userid
        self.sequence_of_fanaticisms_love = []
        self.sequence_of_fanaticisms_hate = []
    
    def get_userkind(self):
        return self.userkind
    
    def get_userid(self):
        return self.userid
        

    def sequenceOfFanaticisms(self):
        sequence = input().split(" ")
        self.sequence_of_fanaticisms_love = []
        self.sequence_of_fanaticisms_hate = []
        for i in sequence:
            if i == "loves":
                previous = "loves"
                continue
            elif i == "hates":
                previous = "hates"
                continue

            if previous == "loves":
                if i not in self.sequence_of_fanaticisms_love:
                    self.sequence_of_fanaticisms_love.append(i)
                else:
                    return False
            else:
                if i not in self.sequence_of_fanaticisms_hate:
                    self.sequence_of_fanaticisms_hate.append(i)
                else:
                    return False        

        for i in self.sequence_of_fanaticisms_love:
            if i in self.sequence_of_fanaticisms_hate:
                return False
        return True

    def register(self):
        return {"userkind":self.userkind,"userid":self.userid,"loves":self.sequence_of_fanaticisms_love,"hates":self.sequence_of_fanaticisms_hate}