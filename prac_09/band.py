class Band:
    """Band class representing a musical band with musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a musician to the band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument (or needing one)."""
        return "\n".join(musician.play() for musician in self.musicians)
