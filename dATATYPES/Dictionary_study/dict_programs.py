sampledict = {
    "class":{
        "student":{
            "name":"Mike",
            "course":{
                "python":2023,
                "angular":2022,

            "marks":{
                "physics":70,
                 "history":80
                }

        }
    }
}
}
#print(sampledict["class"]["student"]["marks"]['physics'])
print(sampledict["class"]["student"]["name"])
print(sampledict["class"]["student"]["course"]["marks"]["physics"])

sampledict = {
     "dict1":{"name":"chithra","age":12 ,"course":"python"},
     'dict2': {'place':"abc","qualification":"b-tech"},
     'dict3':{'job':'pythondev','sal':25000}
}
sampledict["dict2"]["qualification"]="bca"
print(sampledict)