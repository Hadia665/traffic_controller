emergencyVehicle=["Ambulance","Fire Truck","Police Cars"]
civilianVehicle=["Car","Bus","Motorcycle"]
hospitals=["City Hospital"]
signalZones=["Central Junction","North Station","East Market","West Terminal",]
def getPriority(vehicletype,incidentSeverity,timesensitive):
    """ Determines priority on the basis of vehicle,incident severity,and time sensitivity"""
    if vehicletype in emergencyVehicle:
        if incidentSeverity=="High":
            return "Critical"
        elif timesensitive==True:
            return "High"
        else:
            return "High"
    elif vehicletype in civilianVehicle:
        return "Normal"
    else:
        return "Normal"
def signalOverride(vehicletype,signal):
    if signal in signalZones:
        if vehicletype in emergencyVehicle:
            return True
        elif vehicletype in civilianVehicle:
            return False
        else:
            return False
    else:
        return False
def emergencyCoridor(vehicle,destination):
    if vehicle == "Ambulance" and destination in hospitals:
        return True
    else:
        return False
def checkAutherization(vehicle,action,destination):
    """Check if Vehicle is authorized to perform a specific action"""    
    if action=="SignalOverride":
        return signalOverride(vehicle,destination)
    elif action == "EmergencyRoute":
        return emergencyCoridor(vehicle,destination)
    else:
        return False
def approveReject(vehicle ,RequestType,action,destination):
    """Approves or Request based on rules and authorization"""   
    if RequestType=="Route Request":
        return "Approved"
    elif RequestType=="Policy Check":
        if checkAutherization(vehicle,action,destination):
            return "Approved"
        else:
            return "Rejected"
    elif RequestType=="Emergency Response Request":
        if checkAutherization(vehicle,action,destination):
            return "Approved"
        else:
            return "Rejected"
    else:
        return "Rejected"

