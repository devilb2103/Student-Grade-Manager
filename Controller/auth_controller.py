auth_Creds = {"admin": "1234"}

async def VerifyRequest(user, pswd):
    if not((user in auth_Creds) and (auth_Creds[user] == pswd)):
        return {
            "status" : 401,
            "message" : "401 Unauthorized"
            }
    else:
        return {
            "status" : 200,
            "message" : "Access allowed"
            }