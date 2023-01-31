

def write_file(data):
    with open('log.txt', 'a', encoding='utf=8') as file:
        file.write(str(data)) 

          
def read_file():
    with open('log.txt','r', encoding='utf=8') as file:
        return file.readlines()