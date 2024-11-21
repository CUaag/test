import arcade

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Drag and Drop Cards"
CARD_SCALE = 0.6
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

class Card(arcade.Sprite):
    def __init__(self, suit, value, scale=1):
        self.suit = suit
        self.value = value
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.card_list = None
        self.held_cards = None
        self.held_cards_original_position = None
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.card_list = arcade.SpriteList()
        self.held_cards = []
        self.held_cards_original_position = []
        for card_suit in CARD_SUITS:
            for card_value in CARD_VALUES:
                card = Card(card_suit, card_value, CARD_SCALE)
                card.position = START_X, BOTTOM_Y
                self.card_list.append(card)

    def pull_to_top(self, card):
        self.card_list.remove(card)
        self.card_list.append(card)

    def on_draw(self):
        self.clear()
        self.card_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        cards = arcade.get_sprites_at_point((x, y), self.card_list)
        if len(cards) > 0:
            primary_card = cards[-1]
            self.held_cards = [primary_card]
            self.held_cards_original_position = [self.held_cards[0].position]
            self.pull_to_top(self.held_cards[0])

    def on_mouse_release(self, x, y, button, modifiers):
        if len(self.held_cards) == 0:
            return
        self.held_cards = []

    def on_mouse_motion(self, x, y, dx, dy):
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
