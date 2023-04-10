# test-bice

## Docker

#### Setup

```
docker-compose build app
```

#### Run Ipython
```
docker-compose run app ipython
```

##### usage with [ipython](#ipython)
```
from app.utils import get_all_pokemon_no_evolution_chain
from app.utils import get_min_weight  # need the names from get_all_pokemon_no_evolution_chain
from app.utils import get_min_weight_no_evolution

names = get_all_pokemon_no_evolution_chain()

for name in names:
    print(name)

min_weight = get_min_weight(names)
print(min_weight)

min_weight = get_min_weight_no_evolution(names)
print(min_weight)
```

#### Run main

```
docker-compose run app python app
```

## jupyter notebook

check the functions and results with the notebook


### Mejoras

- poetry
- deploy as API
