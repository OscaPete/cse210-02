# Instead of "import conductor", used "import thrower" ~AB
from Gameplay.conductor import thrower

game = thrower()  # changed to "thrower()" instead of "conductor()"
game.start()
