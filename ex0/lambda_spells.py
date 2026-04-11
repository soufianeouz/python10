def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]
    
    avg_power = sum(map(lambda x: x["power"], mages)) / len(mages)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": round(avg_power, 2)
    }



def main():
    print("\nTesting artifact sorter...")

    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "magic"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"}
    ]

    sorted_artifacts = artifact_sorter(artifacts)

    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")

    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)

    print(" ".join(transformed))


if __name__ == "__main__":
    main()