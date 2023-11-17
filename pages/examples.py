from streamlit_image_select import image_select
from PIL import Image
import streamlit as st
import time

def mockStream(text: str):
     return text
        
img = image_select(
    label="Select an image to see what Caution Clip can do",
    images=[
        Image.open("images/electrical.png"),
        Image.open("images/ladder.jpg"),
        Image.open("images/pi.jpg"),
         
    ]
)

if img == Image.open("images/electrical.png"):
    st.header("What kind of safety equipment is needed here?")
    st.write(mockStream("When dealing with electrical systems such as this, it is important to prioritize safety to protect against electric shock, short circuits, and other electrical hazards. Here are some safety equipment and precautions that should be considered:\n\n1. Insulated Tools: Use tools with insulated handles designed for electrical work to prevent electric shock.\n\n2. Rubber Insulating Gloves: Wear properly rated rubber insulating gloves to protect your hands from electric shock.\n\n3. Safety Glasses: Wear safety glasses to protect your eyes from potential sparks or debris.\n\n4. Voltage Detector: Use a non-contact voltage detector to ensure that the power is off before handling any components.\n\n5. Protective Clothing: If there is a risk of arc flash, you may need flame-resistant (FR) clothing.\n\n6. Lockout Devices: Implement lockout tagout procedures to ensure that the power supply is shut off and cannot be turned back on while maintenance is being conducted.\n\n7. Electrical Matting: Stand on an insulating mat when working on electrical equipment to reduce the risk of electric shock.\n\n8. Arc Flash Protection: If the system is part of a larger electrical distribution network with high fault currents, an arc flash analysis might be necessary to determine the appropriate level of arc flash protection"))

elif img == Image.open("images/ladder.jpg"):
     st.header("Is this ladder safe to use?")
     st.write(mockStream("""
No, as it is positioned on uneven ground, leaning to one side, and without any stabilizers. This setup increases the risk of the ladder tipping over, which could result in injury.
"""))
else:
     st.header("How can I reduce the heat?")
     st.write(mockStream("""Use a Case with Good Ventilation: A case with proper ventilation allows the hot air to escape and cooler air to flow in, which can help in cooling the Raspberry Pi.
                              
Heat Sinks: Attaching heat sinks to the main chips, namely the CPU, GPU, and USB/Ethernet controller, can help dissipate heat more effectively.

Active Cooling with a Fan: Incorporating a small fan into your setup can provide active airflow, greatly enhancing the cooling effect.
"""))