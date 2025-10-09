class Allergies:
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        allergies = dict(
            eggs=1,
            peanuts=2,
            shellfish=4,
            strawberries=8,
            tomatoes=16,
            chocolate=32,
            pollen=64,
            cats=128
        )
        return [
            allergy for allergy, val in allergies.items()
            if val & self.score
        ]
