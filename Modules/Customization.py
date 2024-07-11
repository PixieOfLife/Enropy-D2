
class custom_emojis:

    #? Logic For Online/Offline
    async def status(Status: bool=False):
        if Status == True:
            return ("<:d2online:1260989485798264883> ONLINE")
        else:
            return ("<:d2offline:1260989574394675284>  OFFLINE")