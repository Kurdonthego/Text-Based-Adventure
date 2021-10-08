from tabulate import tabulate

# defining the layout of the space ship
# EnemyTile is where the user must fight attackers
# SuppliesTile is where food, weapons, and first aid are stored
# EscapePod is the end of the game
# BoringTile is where nothing occurs
# StartTile is where the game begins
ship_map = [
     ["EnemyTile", "SuppliesTile", "BoringTile"],
     ["BoringTile", "BoringTile", "BoringTile"],
     ["EnemyTile", "StartTile", "EnemyTile"],
     ["EscapePod", "BoringTile", "BoringTile"]
 ]
ship_map[0][0] = "BoringTile"
ship_map[3][0] = "BoringTile"
ship_map[2][1] = "EscapePod"

print(tabulate(ship_map, tablefmt="plain"))