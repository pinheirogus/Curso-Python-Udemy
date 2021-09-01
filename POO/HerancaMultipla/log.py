class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as file1:
            file1.write(msg)
            file1.write('\n')

    def log_info(self, msg):
        self.write(f'Info: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')