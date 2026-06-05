# Logger module with config support
class LoggerModule:
    def __init__(self, config):
        self.config = config
    def log(self, message):
        print(f'[LOG] {message}')
