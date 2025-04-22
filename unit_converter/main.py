import streamlit as st
st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Unit converter")

def length_unit_converter():
    def lengthLogic():
        st.write('w8 converting')
    
    st.write("you are in length converter")
    st.selectbox("Units",options=["kilometres","metres",'centimetres','millimetres','inches','Yard',"Mile"])
    st.number_input("Enter the length ", on_change=lengthLogic)



def area_unit_converter():
    st.write("you are in area converter")

def time_unit_converter():
    st.write("you are in time converter")

def volume_unit_converter():
    st.write("you are in volume converter")

def weight_unit_converter():
    st.write("you are in weight converter")

def temperature_unit_converter():
    st.write("you are in temperature converter")





col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1.1,1,1])
with col1:
    length = st.checkbox("length")
with col2:
    area = st.checkbox("area")
with col3:
    volume = st.checkbox("volume")
with col4:
    temperature = st.checkbox("temperature")
with col5:
    time = st.checkbox("time")
with col6:
    weight = st.checkbox("weight")
                
if length:   
    st.subheader("Length Unit Converter")
    from_coloumn,to_coloumn = st.columns(2)
    with from_coloumn:
        units = {
            "kilometres":1000,
            "metres":1.00,
            'centimetres':0.01,
            'millimetres':0.001,
            'inches':0.0254,
            'Yard':0.9144,
            "Mile":1609.34
        }
        convert_from_unit = st.selectbox("From Units",options=units.keys())
        number = st.number_input("Enter the Number ",key="length_input")
        number_in_m = number*units[convert_from_unit]
    with to_coloumn:
        convert_to_unit = st.selectbox("To Units",options=units.keys())
        #logic....
        result = number_in_m/units[convert_to_unit]
        st.number_input(label="",value=result,disabled=True,key="length_output")



if area:
    st.subheader("Area Unit Converter")
    from_coloumn,to_coloumn = st.columns(2)
    with from_coloumn:
        units = {
            "kilometres_sq":1000000,
            "metres_sq":1,
            'centimetres_sq':0.0001,
            'millimetres_sq':0.000001,
            "foot_sq": 0.092903,
            'Yard_sq':0.836127,
            "acre" :4046.86,
            "hectacre":10000
        }
        convert_from_unit = st.selectbox("From Units",options=units.keys())
        number = st.number_input("Enter the Number ",key="area_input")
        number_in_m2 = number*units[convert_from_unit]
    with to_coloumn:
        convert_to_unit = st.selectbox("To Units",options=units.keys())
        #logic....
        result = number_in_m2/units[convert_to_unit]
        st.number_input(label="",value=result,disabled=True,key="area_output")






if volume:
    st.subheader("Volume Unit Converter")
    from_coloumn,to_coloumn = st.columns(2)
    with from_coloumn:
        units = {
            "m_cub":1000,
            "litre":1,
            'millitres':0.001,
            "gallon(US)": 3.78541,
            "gallon(UK)": 4.54609,
            'foot_cub':28.3168,
            "inch_cub" :0.0163871
        }
        convert_from_unit = st.selectbox("From Units",options=units.keys())
        number = st.number_input("Enter the Number ",key="volume_input")
        number_in_l = number*units[convert_from_unit]
    with to_coloumn:
        convert_to_unit = st.selectbox("To Units",options=units.keys())
        #logic....
        result = number_in_l/units[convert_to_unit]
        st.number_input(label="",value=result,disabled=True,key="volume_output")








if temperature:
    st.subheader("Temperature Unit Converter")
    from_coloumn, to_coloumn = st.columns(2)

    with from_coloumn:
        # Define the conversion dictionary FIRST
        units = {
            "centigrade": {
                "centigrade": lambda x: x,
                "fahrenheit": lambda x: (x * 1.8) + 32,
                "kelvin": lambda x: x + 273.15
            },
            "fahrenheit": {
                "fahrenheit": lambda x: x,
                "centigrade": lambda x: (x - 32) / 1.8,
                "kelvin": lambda x: (x - 32) * 5/9 + 273.15
            },
            "kelvin": {
                "kelvin": lambda x: x,
                "centigrade": lambda x: x - 273.15,
                "fahrenheit": lambda x: (x - 273.15) * 1.8 + 32
            }
        }

        # Now, `units` exists, so `convert_from_unit` can access `units.keys()`
        convert_from_unit = st.selectbox("From Units", options=units.keys(), key="from_unit")

        # User enters the number
        number = st.number_input("Enter the Number", key="temp_input")

    with to_coloumn:
        convert_to_unit = st.selectbox("To Units", options=units.keys(), key="to_unit")

        # Perform conversion using lambda functions
        result = units[convert_from_unit][convert_to_unit](number)

        # Use text_input instead of number_input for output
        st.text_input("Converted Value", value=result, disabled=True, key="temp_output")












if time:
    st.subheader("Time Unit Converter")
    from_coloumn,to_coloumn = st.columns(2)
    with from_coloumn:
        units = {
            "days":86400,   
            "hours":3600,
            'minutes':60,
            "seconds": 1,
            "milliseconds": 0.001,
            'microseconds':0.0000001
        }
        convert_from_unit = st.selectbox("From Units",options=units.keys())
        number = st.number_input("Enter the Number ",key="ime_input")
        number_in_s = number*units[convert_from_unit]
    with to_coloumn:
        convert_to_unit = st.selectbox("To Units",options=units.keys())
        #logic....
        result = number_in_s/units[convert_to_unit]
        st.number_input(label="",value=result,disabled=True,key="ime_output")









if weight:
    st.subheader("Weight Unit Converter")
    from_coloumn,to_coloumn = st.columns(2)
    with from_coloumn:
        units = {
            "ton":1000,
            "kilogram":1,
            'gram':0.001,
            "milligram": 0.000001,
            "pound(lb)": 0.453592,
            'ounce(oz)':0.0283495
        }
        convert_from_unit = st.selectbox("From Units",options=units.keys())
        number = st.number_input("Enter the Number ",key="weight_input")
        number_in_kg = number*units[convert_from_unit]
    with to_coloumn:
        convert_to_unit = st.selectbox("To Units",options=units.keys())
        #logic....
        result = number_in_kg/units[convert_to_unit]
        st.number_input(label="",value=result,disabled=True,key="weight_output")

        




