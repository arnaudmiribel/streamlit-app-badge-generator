from itertools import cycle, islice

import streamlit as st
from htbuilder import a, img

from shieldit import CSS_DEFAULT_COLORS, SHIELD_DEFAULT_COLORS, ShieldBadge

# from pathlib import Path


st.title("🛡️ Badge generator")

"""
This app helps you finding the ideal **custom** [Shields badge](https://shields.io/) you are looking for!
"""


# @st.experimental_singleton
# def get_simple_icons():
#     return Path("simple-icons.txt").read_text().splitlines()


# simple_icons = [""] + get_simple_icons()

st.subheader("Step 1: Give your inputs")
middle = st.columns(7)[3]
middle.image("https://img.shields.io/badge/Left-Right-red")
left, right = st.columns(2)
label = left.text_input("Left", "")
message = right.text_input("Right", "🪢 Featured extra")
# color = st.selectbox("Choose color", ("Show me a bunch!", "green", "yellow", "custom"))

# with st.expander("Advanced options"):
#     style = st.selectbox(
#         "Choose style", ("plastic", "flat", "flat-square", "for-the-badge", "social")
#     )
#     label_color = st.selectbox("Color", options=("#565656", "custom"))
#     if label_color == "custom":
#         _, indented_container = st.columns((1, 35))
#         label_color = indented_container.color_picker(
#             "↳ Pick a custom color", key=label_color
#         )
#     logo = st.selectbox("Logo", options=simple_icons)


def display_badge(badge: ShieldBadge):
    badge_html = str(a(href=badge.link, title="Badge")(img(src=badge.link)))
    st.write(badge_html, unsafe_allow_html=True)


st.write("")
st.write("")


st.subheader("Step 2: Choose your favorite badge!")
st.caption("Just right-click on your favorite badge and copy its link!")

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
                # style=style,
                # logo=logo,
                # label_color=label_color,
            )
            display_badge(badge)
