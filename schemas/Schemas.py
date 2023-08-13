def userEntity(item)->dict:
    return {
        "id":str(item["_id"]),
        "name":str(item["Username"]),
        "password":str(item["Password"]),
        "email":str(item["Email"]),
        "Tel":str(item["Tel"]),
        "Created_time":str(item["Created_time"]),
        "Updated_time":str(item["Updated_time"]),
        "Last_login":str(item["Last_login"]),
  }
    
def usersEntity(entity)->list:
    return [userEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i =='_id' },**{i:a[i] for i in a if i !='_id'}}

def serializeList(entity) ->list:
    return [serializeDict(a) for a in entity]