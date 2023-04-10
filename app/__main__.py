from utils import get_all_pokemon_no_evolution_chain
from utils import get_min_weight
from utils import get_min_weight_no_evolution


def handle_input():
    no_evolution = []
    min_weight = None
    while True:
        choice = input(
            """
            Enter:
            - 1 to get all the pokemons with no evolution
            - 2 to get the min weight pokemon with no evolution
            - 3 exit
            """
        )

        if "1" == choice:
            if not no_evolution:
                no_evolution = get_all_pokemon_no_evolution_chain()

            for pokemon in no_evolution:
                print(pokemon)

        elif "2" == choice:

            if not min_weight and no_evolution:
                min_weight = get_min_weight(no_evolution)
            elif not min_weight and not no_evolution:
                min_weight = get_min_weight_no_evolution()
            print(min_weight)

        elif "3" == choice:
            break

        else:
            print("input no reconocido")


if __name__ == "__main__":
   handle_input()
