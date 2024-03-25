from pynput.keyboard import Key, Controller
import random
import time


class Application:
    keyboard: Controller
    sleep_delay: int = 5

    def run(self) -> None:
        self.keyboard = Controller()

        while True:
            time.sleep(self.sleep_delay)
            tab_times = random.randint(2, 6)
            self.switch_tabs(tab_times)

    def switch_tabs(self, times=1):
        self.keyboard.press(Key.ctrl)
        for _ in range(times):
            self.keyboard.press(Key.tab)
            self.keyboard.release(Key.tab)

        self.keyboard.release(Key.ctrl)
