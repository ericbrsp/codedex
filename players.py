players_data = [
    {"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
    {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 2},
    # Add more players as needed
]

names = [player["name"] for player in players_data]
print("Player Names:", names)

positions = [player["position"] for player in players_data]
print("Player Positions:", positions)


# Update player yards gained
for player in players_data:
    player["yards_gained"] += 50  # Example update, adding 50 yards to each player

average_statistics = sum(player["yards_gained"] for player in players_data) / len(players_data)
print("Estatística: ", average_statistics)
