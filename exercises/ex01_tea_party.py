"""Help me plan a cozy tea party!"""

__author__: str = "730555924"


def main_planner(guests: int) -> None:
    """List of all things for the tea party"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Information on number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Information on number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Information on cost of tea party goods"""
    return float(treat_count * 0.75 + tea_count * 0.5)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
