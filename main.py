from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

print("Testing against Quincy...")
play(player, quincy, 100, verbose=True)

print("\nTesting against Abbey...")
play(player, abbey, 100, verbose=True)

print("\nTesting against Kris...")
play(player, kris, 100, verbose=True)

print("\nTesting against Mrugesh...")
play(player, mrugesh, 100, verbose=True)
