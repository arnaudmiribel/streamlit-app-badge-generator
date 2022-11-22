from itertools import cycle, islice
from pathlib import Path
import streamlit as st
from htbuilder import a, img
from shieldit import CSS_DEFAULT_COLORS, SHIELD_DEFAULT_COLORS, ShieldBadge

st.set_page_config(
    page_title="Badge generator",
    page_icon="🛡️",)


st.title("🛡️ Badge generator")

"""
This app helps you finding the ideal **custom** [Shields badge](https://shields.io/) you are looking for!
"""

##################################################################################
# Functions
@st.experimental_singleton
def get_simple_icons():
    return Path("simple_icons.txt").read_text().splitlines()

def display_badge(badge: ShieldBadge):
    badge_html = str(a(href=badge.link, title="Badge")(img(src=badge.link)))
    st.write(badge_html, unsafe_allow_html=True)
     

##################################################################################
# Inputs Section
st.subheader("Step 1: Give your inputs")

left, right = st.columns(2)
label = left.text_input("Left", "left")
message = right.text_input("Right", "right")

# Badge style
with st.expander("Advanced options"):
    style = st.selectbox(
         "Choose style", ("plastic", "flat", "flat-square", "for-the-badge")
        )
        
    # Set background color for the left part
    label_color = st.selectbox("Left Label Color", options=("default", "custom_left"))
    if label_color == "default":
        label_color = "#565656"
        
    if label_color == "custom_left":
        label_color = st.color_picker(
            "Pick a color", key=label_color
        )

    # Set background color for the right part
    r_label_color = st.selectbox("Right Label Color", options=("default", "custom_right"))
    st.info("This effect can only be applied under 'Option 2' tab")
    if r_label_color == "default":
        r_label_color = "#565656"
        
    if r_label_color == "custom_right":
        r_label_color = st.color_picker(
            "Pick a color", key=r_label_color
        )    
    
    # Simple-icons support
    simple_icons = [""] + get_simple_icons()
    logo = st.selectbox("Logo", options=(simple_icons))

    # Icons color support
    logo_color = st.selectbox("Logo Color", options=("default", "choose_color"))
    if logo_color == "default":
        logo_color = "#fff"
    
    if logo_color == "choose_color":
        logo_color = st.color_picker(
            "Pick a color", key=logo_color
        )

##################################################################################
# Badge Results Section
st.write("")
st.write("")
st.subheader("Step 2: Choose your favorite badge!")
st.caption("Just right-click on your favorite badge and copy its link!")
st.write("")

tab1, tab2 = st.tabs(["Option 1", "Option 2"])

with tab1:
    st.subheader("Customize many badges at once")
    st.write("")
    st.info("Social badge style remains the same for all, try it out in the next tab please.")
        
    colors = SHIELD_DEFAULT_COLORS + CSS_DEFAULT_COLORS
    colors_cycle = islice(cycle(colors), len(colors))
    num_columns = 5

    for row in range(len(colors) // num_columns):
        columns = cycle(st.columns(num_columns))
        for column in range(num_columns):
            with next(columns):
                badge = ShieldBadge(
                    label=label,
                    message=message,
                    color=next(colors_cycle),
                    style=style,
                    logo=logo,
                    label_color=label_color,
                    logo_color=logo_color,
                    )
                display_badge(badge)


with tab2:
    st.subheader("Apply all the custom options on one badge")
    st.write("")
    style_1 = st.selectbox(
         "Select style", ("plastic", "flat", "flat-square", "for-the-badge", "social")
        )

    badge_1 = ShieldBadge(
        label=label,
        message=message,
        color=r_label_color,
        style=style_1,
        logo=logo,
        label_color=label_color,
        logo_color=logo_color,
        )
    display_badge(badge_1)
