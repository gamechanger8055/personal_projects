"""
facade pattern is a structural pattern that a simplified interface to a complex subsystem, making it easier to use.
used when we need to hide system complexity with user.

Example: A home theater remote control that hides the complexity of interacting with multiple devices
 like TVs, DVD players, and sound systems behind a single interface.
"""

#Home theatre system

class HomeTheatreFacade:
    def __init__(self, tv, dvd_player, sound_system, lights):
        self.tv = tv
        self.dvd_player = dvd_player
        self.sound_system = sound_system
        self.lights = lights

    def watch_movie(self, movie):
        self.lights.dim()
        self.sound_system.turn_on()
        self.sound_system.set_volume(8)
        self.dvd_player.turn_on()
        self.dvd_player.play(movie)
        self.tv.turn_on()

    def end_movie(self):
        self.lights.brighten()
        self.sound_system.turn_off()
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.tv.turn_off()

# Client code
tv = TV()
dvd_player = DVDPlayer()
sound_system = SoundSystem()
lights = Lights()

home_theater = HomeTheatreFacade(tv, dvd_player, sound_system, lights)
home_theater.watch_movie("Inception")
home_theater.end_movie()