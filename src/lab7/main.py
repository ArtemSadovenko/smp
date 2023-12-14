from UserService import UserService
from JSONplaceholder import JSONPlaceholderAPI

def main():
    api = JSONPlaceholderAPI()
    print(api.get_posts())
    
    usrServ = UserService()
    usrServ.start()

if __name__ == '__main__':
    
    main()