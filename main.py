import pyxel as px
import random
import time
from constant import Const

class TapNumbers:
    def __init__(self):
        px.init(Const.WINDOW_WIDTH, Const.WINDOW_HEIGHT, title=Const.GAME_TITLE)
        self.__reset()
        px.mouse(True)
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.MOUSE_BUTTON_LEFT):
            if self.game_over:  # ゲームオーバー時はクリックでゲームリスタート
                self.__reset()
                return
            index = px.mouse_y // Const.CELL_SIZE * Const.GRID_SIZE + px.mouse_x // Const.CELL_SIZE # 行index * グリッド数 + 列index
            if index < len(self.numbers) and self.numbers[index] == self.current_number:
                self.numbers[index] = None
                self.current_number += 1
                if self.current_number > Const.GRID_SIZE ** 2:
                    self.game_over = True
                    self.end_time = time.time()

    def draw(self):
        px.cls(0)
        for i, num in enumerate(self.numbers):
            if num is not None:
                x,y = i % Const.GRID_SIZE * Const.CELL_SIZE, i // Const.GRID_SIZE * Const.CELL_SIZE
                px.rect(x, y, Const.CELL_SIZE, Const.CELL_SIZE, 5)
                px.text(x + Const.CELL_SIZE // 2 - 2, y + Const.CELL_SIZE // 2 - 2, str(num), 7)
        if self.game_over:
            px.text(50, Const.WINDOW_HEIGHT / 2 - 10, "GAME CLEAR!", px.frame_count % 16)
            px.text(50, Const.WINDOW_HEIGHT / 2, f"Time: {self.end_time - self.start_time:.2f}s", 7)
            px.text(50, Const.WINDOW_HEIGHT / 2 + 10, "TAP TO RETRY", 7)

    def __reset(self):
        self.numbers = list(range(1, Const.GRID_SIZE ** 2 + 1))
        random.shuffle(self.numbers)
        self.current_number = 1
        self.start_time = time.time()
        self.game_over = False

TapNumbers()