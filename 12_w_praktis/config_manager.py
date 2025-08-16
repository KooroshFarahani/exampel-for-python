import json

def config_W():
    data ={"username":"Ali" , "theme": "dark", "language": "fa"  }
    with open("config.json",'w')as file :
        json.dump(data,file)

def config_R():
    with open("config.json" ,'r')as file:
        loaded_data=json.load(file)
        print(loaded_data)



config_W()
config_R()