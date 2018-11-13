class Command:

    def __init__(self, command):
        command_params = command.split()
        self.command_type = command_params[0]
        if (len(command_params) > 1):
            self.first_param = int(command_params[1])
        if (len(command_params) > 2):
            self.second_param = int(command_params[2])

    def execute_command(self, current_list):
        if self.command_type == 'insert':
            current_list.insert(self.first_param, self.second_param)
        elif self.command_type == 'remove':
            current_list.remove(self.first_param)
        elif self.command_type == 'print':
            print(current_list)
        elif self.command_type == 'append':
            current_list.append(self.first_param)
        elif self.command_type == 'sort':
            current_list.sort()
        elif self.command_type == 'pop':
            current_list.pop()
        else :
            current_list.reverse()


if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        command = Command(input())
        command.execute_command(my_list)
        
