# Seting up the game

The purpose of this repository is to offer a server capable of generating random chess
positions where black and white are equals.

## Understanding

To generate random positions, a random generator creates an initial position from the BobyFisher variant. Then, a random number
of moves is performed (between 1 and 10). Finaly, an engine based on Stockfish plays the game aiming to reduce the
score difference between black and white until it reaches 0. In case no position is found within 40 moves, a new instance 
is started.

## Architecture

The pattern used here is the Model, View, Controller one. One server is being used to support the front and the back at the same time.

Several routes are accessible:

    - /isRunning: test whether the server is running
    - /display/showGame: display a board game with a random position
    - /v1/generateEqualGame: return a Fen string corresponding to an equal position between black and white

For the frontend, a solution based on Jinja and Fastapi was chosen. Deploying a full application using Angulare or else seemed execive to me
in this context. Moreover, existing libraries to display chess games were found easy to integrate in vanilla JS.
 

## Configuration

Adjust the `config.toml` file with the location of the Stockfish instance to use


## Run the application

Prepare the environment for the application by running the following command

```bash
pip install -r requeriments.txt
```

To deploy the application, run the following command in a terminal:

```bash
fastapi run app/main.py
```
 

## References

 - https://python-chess.readthedocs.io/en/latest/
 - https://fastapi.tiangolo.com/
 - https://www.chessboardjs.com/