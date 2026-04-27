import os
import streamlit as st
from modules.preprocessing import validateRequest
from modules.router import processRequest
from modules.finalResponse import generateResponse
st.set_page_config(
    page_title="Smart City Traffic AI",
    page_icon="logo.png",
    layout="wide"
)
if "page" not in st.session_state:
    st.session_state.page="welcome"
if st.session_state.page=="welcome":
    col1,col2=st.columns([1,5])
    with col1:
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        st.image(logo_path, width=90)
    with col2:
        st.markdown("""
            <h1 style='text-align: center;'>
            Smart City Traffic & Emergency Response AI
            </h1>
            <h4 style='text-align: center; color: gray;'>
            Intelligent Traffic Management for Modern Cities
            </h4>
            """, unsafe_allow_html=True)
    st.markdown("---")
    col1,col2,col3=st.columns([1,2,1])
    with col2:
        st.markdown("""
        ###  What This System Does:
        -  **Route Planning** for civilian drivers
        -  **Emergency Vehicle** priority routing  
        -  **Traffic Signal** coordination
        -  **Policy Validation** for traffic control
        """)
        st.markdown("---")
        if st.button(" Get Started", use_container_width=True):
            st.session_state.page = "form"
            st.rerun()
# Form Page
if st.session_state.page=="form":
    st.markdown("<h2 style='text-align: center;'> Submit Traffic Request</h2>", 
                unsafe_allow_html=True)
    st.markdown("---")
    col1,col2=st.columns(2)
    with col1:
        requestCategory=st.selectbox(
            "Request Category",["Route Request","Policy Check","Control Allocation Request","Emergency Response Request","Integrated City Service Request"])
        vehicleType=st.selectbox(
            "Vehicle Type",["Car", "Bus", "Motorcycle","Ambulance", "Fire Truck", "Police Car"])
        currentLocation=st.selectbox(
            "Current Location",["Police HQ","River Bridge","North Station","Traffic Control Center","Stadium","East Market","Fire Station","Central Junction","West Terminal","Airport Road","City Hospital","South Residential","Industrial Zone"])
        destination=st.selectbox(
            "Destination",["Police HQ", "River Bridge","North Station","Traffic Control Center","Stadium","East Market","Fire Station","Central Junction","West Terminal","Airport Road","City Hospital","South Residential","Industrial Zone"])
    with col2:
        if requestCategory in ["Emergency Response Request","Integrated City Service Request","Policy Check","Control Allocation Request"]:
            incidentSeverity=st.selectbox(
                "Incident Severity",
                ["None","Low","Medium","High"]
            )
            timeSensitive=st.checkbox("Time Sensitive?")
            trafficDensity=st.selectbox("Traffic Density",["Low","Medium","High"])
        else:
            incidentSeverity = "None"
            timeSensitive = False
            trafficDensity = "Low"
    st.markdown("---")
    if st.button(" Submit Request",use_container_width=True):
        isValid, result = validateRequest(requestCategory,vehicleType,currentLocation,destination,incidentSeverity,timeSensitive,trafficDensity)
        if not isValid:
            st.error(result)
        else:
            routerResult = processRequest(result)
            finalResult = generateResponse(requestCategory, routerResult)
            st.session_state.result=finalResult
            st.session_state.category=requestCategory
            st.session_state.page="results"
            st.rerun()
if st.session_state.page=="results":
    result=st.session_state.result
    category=st.session_state.category
    st.markdown("<h2 style='text-align: center;'> Request Results</h2>",unsafe_allow_html=True)
    st.markdown("---")
    st.success(result["message"])
    col1,col2=st.columns(2)
    with col1:
        if "route" in result and result["route"]:
            st.markdown("###  Route")
            route_str = " → ".join(result["route"])
            st.info(route_str)
        if "cost" in result and result["cost"]:
            st.markdown("###  Travel Cost")
            st.info(f"{result['cost']} units")
        if "hops" in result and result["hops"]:
            st.markdown("###  Total Hops")
            st.info(f"{result['hops']} hops")
    with col2:
        if "priority" in result:
            st.markdown("###  Priority Level")
            priority = result["priority"]
            if priority=="Critical":
                st.error(f" {priority}")
            elif priority=="High":
                st.warning(f" {priority}")
            elif priority=="Normal":
                st.success(f" {priority}")
            else:
                st.info(f" {priority}")
        if "status" in result:
            st.markdown("###  Policy Status")
            if result["status"] == "Approved":
                st.success(f" {result['status']}")
            else:
                st.error(f" {result['status']}")
        if "signals" in result and result["signals"]:
            st.markdown("###  Signal Plan")
            for signal, color in result["signals"].items():
                if color == "Green":
                    st.success(f"{signal} →  {color}")
                elif color == "Red":
                    st.error(f"{signal} →  {color}")
                else:
                    st.warning(f"{signal} →  {color}")
    
    st.markdown("---")
    # Back button
    if st.button(" New Request",use_container_width=True):
        st.session_state.page = "form"
        st.rerun()


