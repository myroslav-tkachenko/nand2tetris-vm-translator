class Parser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.input_file = open(self.file_name)
        self.current_command = None
        self.next_command = self.input_file.readline()

    def __del__(self, *args):
        self.input_file.close()

    def advance(self):
        if not self.has_more_commands():
            return

        while True and self.has_more_commands():
            self.current_command = self.next_command.split(
                '//')[0].strip()
            self.next_command = self.input_file.readline()

            if self.current_command:
                break

    def has_more_commands(self):
        return bool(self.next_command)

    def command_type(self):
        try:
            prefix = self.current_command.split(' ')[0]
        except:
            return None

        return prefix
