signals={
    "S1": "Central Junction",
    "S2": "North Station",
    "S3":"East Market",
    "S4":"River Bridge",
    "S5":"City Hospital"
}
domain={s:["Green","Yellow","Red"] for s in signals}
conflicts=[
    ("S1","S2"),
    ("S1","S3"),
    ("S2","S4"),
    ("S3","S5")
]
def isConsistent(signal,color,assignment):
    """Check if assigning color to signal causes any conflict with neighbors"""
    for (s1,s2) in conflicts:
        if s1==signal and s2 in assignment:
            if assignment[s2]==color:
                return False
        if s2==signal and s1 in assignment:
            if assignment[s1]==color:
                return False
    return True
def backTracking(assignment):
    """Backtracking with MRV and LCV"""
    if len(assignment)==len(signals):
        return assignment
    signal=MRV(assignment)
    for color in LCV(signal,assignment):
        if isConsistent(signal,color,assignment):
            assignment[signal]=color
            result=backTracking(assignment)
            if result:
                return result
            del assignment[signal]
    return None
def solveCSP():
    """Solves CSP and return signal assignments"""
    result=backTracking({})
    return result
def MRV(assignemnt):
    """Select unassigned signals with Minimum Remaining Value"""
    unassigned=[s for s in signals if s not in assignemnt]
    return min(unassigned,key=lambda s:len([color for color in domain[s]
                                            if isConsistent(s,color,assignemnt)
                                            ]))
def LCV(signal,assignment):
    """Orders color by Leasr Contraining Value First"""
    def countConflict(color):
        count=0
        for (s1,s2) in conflicts:
            if s1==signal:
                neighbor=s2
            elif s2 ==signal:
                neighbor=s1
            else:
                continue
            if neighbor not in assignment:
                if not isConsistent(neighbor,color,{**assignment,signal:color}):
                    count+=1
        return count
    return sorted(domain[signal],key=countConflict)