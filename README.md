# Seting up the game

The purpose of this repository is to offer a server capable of generating random chess positions where black and white are equals.

## Understanding

To generate random positions, a random generator creates an initial position from the BobyFisher variant. Then, a random number of moves is performed (between 1 and 10). Finaly, an engine based on Stockfish plays the game aiming to reduce the score difference between black and white until it reaches 0. In case no position is found within 40 moves, a new instance is started.

## Architecture

The pattern used here is the Model, View, Controller one. One server is being used to support the front and the back at the same time.

Several routes are accessible:

- /isRunning: test whether the server is running
- /display/equalBoard: display a board game with a random position
- /v1/generateEqualGame: return a Fen string corresponding to an equal position between black and white

For the frontend, a solution based on Jinja and Fastapi was chosen. Deploying a full application using Angulare or else seemed execive to me
in this context. Moreover, existing libraries to display chess games were found easy to integrate in vanilla JS.

The `v1` is used in this case to prepare for later modifcations/improvement of the api without having to interupt the workflow of other users. 

The `isRunning` route is used to automatically check whether the api is running. It can be link to server monitoring services.

## Configuration

Adjust the `config.toml` file with the location of the Stockfish instance to use and install the needed libraries.


## Run the application

Prepare the environment for the application by running the following command

```bash
pip install -r requeriments.txt
```

To deploy the application, run the following command in a terminal:

```bash
fastapi run app/main.py
```

## Possible improvements

 - at the loading of the api, generate 5 to 10 positions and store them in a cache file. Each time a position is asked by a user, re-compute one position to add it to the cache afterwards. This would reduce the latency due to "long" computatitons

- possibility to add d-dos protection directly in the api or to delegate it to the firewall

- add testcases
    - integration tests for the Board object to ensure the different functions handle all possibilities
    - end to end test to check that the display works properly

## References

 - https://python-chess.readthedocs.io/en/latest/
 - https://fastapi.tiangolo.com/
 - https://www.chessboardjs.com/
 - https://tobiasahlin.com/spinkit/