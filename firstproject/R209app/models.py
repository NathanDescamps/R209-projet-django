from django.db import models

class tableaux(models.Model):

    titre = models.CharField(max_length=100)

    peintre = models.CharField(max_length = 100)
    date_parution = models.DateField(blank=True, null = True)

    mouvement_artistique = models.CharField(max_length = 100)

    idee = models.TextField(null = True, blank = True)


    def __str__(self):
        chaine = f"{self.titre} est une oeuvre qui a été peinte par {self.peintre} paru en {self.date_parution} elle fait partie du mouvement {self.idee}."
        return chaine

    def dico(self):
        return {"titre":self.titre, "peintre":self.peintre, "date_parution":self.date_parution, "mouvement_artistique":self.mouvement_artistique, "idee":self.idee}

