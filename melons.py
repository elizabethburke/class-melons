"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""       
        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5

        if qty >= 3:
            total = total*0.75

        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5

        total = self.price * qty
        if qty >= 5:
            return total * .5
        else:
            return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5

        return total

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5
        return total

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5
        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5
        return total

class HornedMelonOrder(object):
    species = "HornedMelon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5
        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5
        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if self.species in ['Casaba','Ogen']:
            self.price = self.price + 1        
        
        if self.shape == "square":
            self.price = self.price * 2

        total = self.price * qty

        if self.imported == True:
            total = total * 1.5
        return total