import streamlit as st
from random import randint
import pandas as pd


class Die:
    """A simple die class."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


st.title("Dice Rolling Simulation")

# Sidebar controls
st.sidebar.header("Simulation Settings")


num_dice = st.sidebar.slider("Number of dice", 1, 5, 1)
num_rolls = st.sidebar.slider("Number of rolls", 100, 10000, 1000, step=100)

show_data = st.sidebar.checkbox("Show frequency table", value=True)

# Button to run simulation
if st.button("Roll Dice"):

    dice = [Die() for x in range(num_dice)] # 生成若干骰子

    results = []

    for roll_num in range(num_rolls):
        result = sum(die.roll() for die in dice)
        results.append(result)

    frequencies = []

    min_result = num_dice
    max_result = num_dice * 6
    poss_results = range(min_result, max_result + 1)

    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    # Create DataFrame for display and plotting
    df = pd.DataFrame({
        "Result": list(poss_results),
        "Frequency": frequencies
    })

    if show_data:
        st.subheader("Frequency Table")
        st.dataframe(df)

    st.subheader("Bar Chart of Dice Results")

    chart_data = df.set_index("Result")
    st.bar_chart(chart_data)


else:
    st.info("Click the button to roll the dice.")
