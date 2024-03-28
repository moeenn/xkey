from pynput.keyboard import Key, Controller
import random
import time
from datetime import datetime


class Application:
    keyboard: Controller
    sleep_delay: int = 5

    def run(self) -> None:
        self.keyboard = Controller()

        while True:
            tab_times = random.randint(2, 6)
            print(self.now())
            self.switch_tabs(tab_times)
            time.sleep(self.sleep_delay)

    def switch_tabs(self, times=1):
        self.keyboard.press(Key.ctrl)
        for _ in range(times):
            self.keyboard.press(Key.tab)
            self.keyboard.release(Key.tab)

        self.keyboard.release(Key.ctrl)

    def now(self) -> str:
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
