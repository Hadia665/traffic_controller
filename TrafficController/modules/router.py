from modules.search import bfs_traversal, uniformCostSearch, AStar,UnWeightedGraph, WeightedGraph
from modules.knowledgebase import getPriority, checkAutherization, approveReject
from modules.csp import solveCSP
from modules.ann import predictPriority
def routeRequest(data):
    """Handle simple route request"""
    path,hops=bfs_traversal(UnWeightedGraph,data["currentLocation"],data["destination"])
    return {"route": path, "hops": hops}
def policyCheck(data):
    """Handle policy check request"""
    priority=getPriority(data["vehicleType"],data["incidentSeverity"],data["timeSensitive"])
    result=approveReject(data["vehicleType"],data["requestCategory"],"SignalOverride",data["destination"])
    return {"priority":priority,"status":result}
def controlAllocation(data):
    """Handle control allocation request"""
    signals=solveCSP()
    result=approveReject(data["vehicleType"],data["requestCategory"],"SignalOverride",data["destination"])
    return {"signals":signals,"status":result}
def emergencyResponse(data):
    """Handle emergency response request"""
    priority=predictPriority(data["vehicleType"],data["incidentSeverity"],data["timeSensitive"],data["trafficDensity"])
    result=approveReject(data["vehicleType"],data["requestCategory"],"EmergencyRoute",data["destination"])
    signals=solveCSP()
    cost,path,_=AStar(WeightedGraph,data["currentLocation"],data["destination"])
    return {
        "priority":priority,
        "status":result,
        "signals":signals,
        "route":path,
        "cost":cost
    }
def integratedRequest(data):
    """Handle integrated city service request"""
    priority=predictPriority(data["vehicleType"],data["incidentSeverity"],data["timeSensitive"],data["trafficDensity"])
    result=approveReject(data["vehicleType"],data["requestCategory"],"EmergencyRoute",data["destination"])
    signals=solveCSP()
    cost,path,_=AStar(WeightedGraph,data["currentLocation"],data["destination"])
    return {
        "priority":priority,
        "status":result,
        "signals":signals,
        "route":path,
        "cost":cost
    }
def routeRequestWeighted(data):
    """Handle weighted route request - UCS"""
    cost,path,_=uniformCostSearch(WeightedGraph,data["currentLocation"],data["destination"])
    return {"route":path,"cost":cost}
def processRequest(data):
    """Main router - decides which pipeline to use"""
    category=data["requestCategory"]
    if category=="Route Request":
        return routeRequest(data)
    elif category=="Policy Check":
        return policyCheck(data)
    elif category=="Control Allocation Request":
        return controlAllocation(data)
    elif category=="Emergency Response Request":
        return emergencyResponse(data)
    elif category=="Integrated City Service Request":
        return integratedRequest(data)
    else:
        return {"error": "Invalid request category!"}