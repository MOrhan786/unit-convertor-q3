#Project 01: Unit Convertor
# Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st  


def convert_units(value, unit_from, unit_to):
    
    conversions = {
        # Length conversions
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "meters_miles": 0.000621371,  # 1 meter = 0.000621371 miles
        "miles_meters": 1609.34,  # 1 mile = 1609.34 meters
        "inches_centimeters": 2.54,  # 1 inch = 2.54 centimeters
        "centimeters_inches": 0.393701,  # 1 centimeter = 0.393701 inches
        
        # Weight conversions
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
        "pounds_kilograms": 0.453592,  # 1 pound = 0.453592 kilograms
        "kilograms_pounds": 2.20462,  # 1 kilogram = 2.20462 pounds
        "ounces_grams": 28.3495,  # 1 ounce = 28.3495 grams
        "grams_ounces": 0.035274,  # 1 gram = 0.035274 ounces
        
        # Volume conversions
        "liters_milliliters": 1000,  # 1 liter = 1000 milliliters
        "milliliters_liters": 0.001,  # 1 milliliter = 0.001 liters
        "gallons_liters": 3.78541,  # 1 gallon = 3.78541 liters
        "liters_gallons": 0.264172,  # 1 liter = 0.264172 gallons
        
        # Temperature conversions
        "celsius_fahrenheit": lambda x: (x * 9/5) + 32,  # Celsius to Fahrenheit
        "fahrenheit_celsius": lambda x: (x - 32) * 5/9,  # Fahrenheit to Celsius
        "celsius_kelvin": lambda x: x + 273.15,  # Celsius to Kelvin
        "kelvin_celsius": lambda x: x - 273.15,  # Kelvin to Celsius
    }

    key = f"{unit_from}_{unit_to}"  
    if key in conversions:
        conversion = conversions[key]
        
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  # Otherwise, multiply by the conversion factor
    else:
        return "Conversion not supported"  # Return message if conversion is not defined





# Set page configuration
st.set_page_config(page_title="Ultimate Unit Converter", page_icon="📏")

# Styled title with green color
st.markdown("<h1 style='color: orange;'> 🎗Ultimate Unit Converter</h1>", unsafe_allow_html=True)

#st.title("📏 Ultimate Unit Converter")  
st.markdown("**Convert between various units of length, weight, volume, and temperature with ease!**")

# User input: numerical value to convert
value = st.number_input("Enter value:", min_value=0.0, step=0.1)


unit_from = st.selectbox(
    "Convert from:",
    ["meters", "kilometers", "miles", "inches", "centimeters",  # Length
     "grams", "kilograms", "pounds", "ounces",  # Weight
     "liters", "milliliters", "gallons",  # Volume
     "celsius", "fahrenheit", "kelvin"]  # Temperature
)


unit_to = st.selectbox(
    "Convert to:",
    ["meters", "kilometers", "miles", "inches", "centimeters",  # Length
     "grams", "kilograms", "pounds", "ounces",  # Weight
     "liters", "milliliters", "gallons",  # Volume
     "celsius", "fahrenheit", "kelvin"]  # Temperature
)

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  
    if result == "Conversion not supported":
        st.error("⚠️ Conversion not supported. Please select compatible units.")
    else:
        st.success(f"✅ **Converted Value:** {result:.4f}") 


st.markdown("---")
st.markdown("_Made with ❤️ by Mrs Asif_")