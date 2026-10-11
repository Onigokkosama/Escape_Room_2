

from world_loader import WorldLoader
from game_state import GameState
from command_handler import CommandHandler
from event_manager import EventManager
from renderer import Renderer

class GameEngine:
    def __init__(self):
        self.state = GameState()
        self.world = WorldLoader().load_world("data/world.json")
        self.renderer = Renderer(self.state)
        self.commands = CommandHandler(self.state, self.world)
        self.events = EventManager(self.state, self.world)

    def start_game(self):
        # scelta lingua iniziale
        self.state.language = self.renderer.select_language()
        # game loop semplificato
        while not self.state.quit:
            self.renderer.show_room(self.state.current_room)
            cmd = self.renderer.get_input()
            self.commands.handle(cmd)
            self.events.check_events(trigger="on_command")
