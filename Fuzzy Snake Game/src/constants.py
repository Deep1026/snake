# import different controllers
from snake_controllers.FuzzyRulesController import FuzzyRulesController
from snake_controllers.ManualController import ManualController
from snake_controllers.FuzzyRulesForBricksController import FuzzyRulesForBricksController

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
SNAKE_MOVES_FILE = "snake_moves.txt"
MANUAL = 0
FUZZY = 1
FUZZY_WITH_BRICKS = 2

move_direction_text_dict = { UP: "UP", DOWN: "DOWN", LEFT: "LEFT", RIGHT: "RIGHT"}
controller_name_mapping = { MANUAL: ManualController, FUZZY: FuzzyRulesController, FUZZY_WITH_BRICKS: FuzzyRulesForBricksController}
MAX_VAL = 99999
STEP_SIZE = 44

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)