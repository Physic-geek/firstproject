import streamlit as st
st.title("RESISTOR COLOR CODE CALCULATOR")
color_digit = {'black': '0',
				'brown': '1',
				'red': '2',
				'orange': '3',
				'yellow': '4',
				'green' : '5',
				'blue' : '6',
				'violet' : '7',
				'grey' : '8',
				'white': '9'}
multiplier = {'black': '1',
				'brown': '10',
				'red': '100',
				'orange': '1k',
				'yellow': '10k',
				'green' : '100k',
				'blue' : '1M',
				'violet' : '10M',
				'grey' : '100M',
				'white': '1G'}
tolerance = {'brown': '+/- 1 %',
				'red' : '+/- 2 %',
				'green': "+/- 0.5 %",
				'blue': '+/- 0.25 %',
				'violet' : '+/- 0.1 %',
				'gold': '+/- 5 %',
				'silver' : '+/- 10 %',
				'none': '+/-20 %'}
	
first=st.write("1st Band of Color")
a=st.checkbox("BLACK 0")
b=st.checkbox("BROWN 1")
c=st.checkbox("RED 2")
d=st.checkbox("ORANGE 3")
e=st.checkbox("YELLOW 4")
f=st.checkbox("GREEN 5")
g=st.checkbox("BLUE 6")
h=st.checkbox("VIOLET 7")
i=st.checkbox("GOLD 8")
j=st.checkbox("GREY 9")
second=st.write("2nd Band of Color")
a1=st.checkbox("BLACK  0")
b1=st.checkbox("BROWN  1")
c1=st.checkbox("RED  2")
d1=st.checkbox("ORANGE  3")
e1=st.checkbox("YELLOW  4")
f1=st.checkbox("GREEN  5")
g1=st.checkbox("BLUE  6")
h1=st.checkbox("VIOLET  7")
i1=st.checkbox("GOLD  8")
j1=st.checkbox("GREY  9")
third=st.write("Multiplier (3rd Band of Color)")
a2=st.checkbox("BLACK 1")
b2=st.checkbox("BROWN 10")
c2=st.checkbox("RED 100")
d2=st.checkbox("ORANGE 1K")
e2=st.checkbox("YELLOW 10k")
f2=st.checkbox("GREEN 100K")
g2=st.checkbox("BLUE 1M")
h2=st.checkbox("VIOLET 10M")
i2=st.checkbox("GOLD 100M")
j2=st.checkbox("GREY 1G")
fourth=st.write("Tolerance(4th Band of Color)")
a3=st.checkbox("BLACK")
b3=st.checkbox("BROWN")
c3=st.checkbox("RED")
d3=st.checkbox("ORANGE")
e3=st.checkbox("YELLOW")
f3=st.checkbox("GREEN")
g3=st.checkbox("BLUE")
h3=st.checkbox("VIOLET")
i3=st.checkbox("GOLD")
j3=st.checkbox("GREY")



v=first*second*(third)+fourth
st.write("Resistance Value ",v,"ohms")