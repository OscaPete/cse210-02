# Instead of "import conductor", used "import thrower" ~AB
from gameplay.conductor import thrower

game = thrower()  # changed to "thrower()" instead of "conductor()"
game.start()
