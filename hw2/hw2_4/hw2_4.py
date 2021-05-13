from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPlaptop(Laptop):
    def __init__(self, screen_name, keyboard_name, touchpad_name, webcam_name, port_name, dynamics_name):
        self.screen_name = screen_name
        self.keyboard_name = keyboard_name
        self.touchpad_name = touchpad_name
        self.webcam_name = webcam_name
        self.port_name = port_name
        self.dynamics_name = dynamics_name

    def screen(self):
        print(f'Screen: {self.screen_name}')

    def keyboard(self):
        print(f'Keyboard language: {self.keyboard_name}')

    def touchpad(self):
        print(f'Touchpad: {self.touchpad_name}')

    def webcam(self):
        print(f'Webcam: {self.webcam_name}')

    def ports(self):
        print(f'Ports: {self.port_name}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamics_name}')


if __name__ == "main":
    Envy = HPlaptop('15.6" (1920x1080) Full HD Multitouch', 'EN', 'Touchpad with the fingerprint scanner',
                    'HPTrueVision 720p',
                    '2 x USB 3.1 Type-A Gen 1/1 x USB 3.1 Type-C Gen 2 (Power Delivery&DisplayPort)/HDMI',
                    'Bang&Olufsen, 3 speakers, HP Audio boost technology')
    Envy.screen()
    Envy.keyboard()
    Envy.touchpad()
    Envy.webcam()
    Envy.ports()
    Envy.dynamics()
