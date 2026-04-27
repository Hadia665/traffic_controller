def generateResponse(category, result):
    """Generates final human readable response based on request category and result"""
    if category=="Route Request":
        return {
            "message":"Route Successfully Generated!",
            "route": result["route"],
            "hops": result["hops"]
        }
    elif category=="Policy Check":
        return {
            "message":f"Policy Check: {result['status']}",
            "priority":result["priority"],
            "status":result["status"]
        }
    elif category=="Control Allocation Request":
        return {
            "message":"Signal Control Plan Generated!",
            "signals":result["signals"],
            "status":result["status"]
        }
    elif category == "Emergency Response Request":
        return {
            "message":"Emergency Response Plan Ready!",
            "priority":result["priority"],
            "status":result["status"],
            "route":result["route"],
            "cost":result["cost"],
            "signals":result["signals"]
        }
    elif category=="Integrated City Service Request":
        return {
            "message":"Integrated City Service Response Ready!",
            "priority": result["priority"],
            "status": result["status"],
            "route": result["route"],
            "cost": result["cost"],
            "signals": result["signals"]
        }