validateVehicle=["Ambulance","Fire Truck","Police Car","Car","Bus","Motorcycle"]
validateLocation=["Police HQ","River Bridge","North Station","Traffic Control Center", "Stadium", "East Market","Fire Station","Central Junction","West Terminal","Airport Road","City Hospital","South Residential","Industrial Zone"]
validCategory=["Route Request","Policy Check","Control Allocation Request","Emergency Response Request","Integrated City Service Request"]
validSeverity=["High","Medium","Low","None"]
validTraffic=["High","Medium","Low"]
def validateRequest(requestCategory,vehicleType,currentLocation,destination,incidentSeverity="None",timeSensitive=False,trafficDensity="Low"):
    """Validates all input fields"""
    if requestCategory not in validCategory:
        return False,"Invalid request category!"
    if vehicleType not in validateVehicle:
        return False,"Invalid vehicle type!"
    if currentLocation not in validateLocation:
        return False,"Invalid current location!"
    if destination not in validateLocation:
        return False,"Invalid destination!"
    if currentLocation==destination:
        return False,"Current location and destination cannot be same!"
    if incidentSeverity not in validSeverity:
        return False,"Invalid incident severity!"
    if trafficDensity not in validTraffic:
        return False,"Invalid traffic density!"
    cleanData = {
        "requestCategory": requestCategory,
        "vehicleType": vehicleType,
        "currentLocation": currentLocation,
        "destination": destination,
        "incidentSeverity": incidentSeverity,
        "timeSensitive": timeSensitive,
        "trafficDensity": trafficDensity
    }
    return True, cleanData
