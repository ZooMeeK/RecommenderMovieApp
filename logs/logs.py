import datetime


class Logs:
    
    
    def __init__(self):
        self.filename = 'data/logs/{}.txt'.format(datetime.datetime.now().strftime("%Y-%m-%d"))
    
    
    def write_logs(self, message):
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open(self.filename, 'a') as f:
            f.write('{} \t {} \n'.format(date, message))
    