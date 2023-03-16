import streamlit as st
def findResistance(a, b, c, d):
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
	
	if a in color_digit and b in color_digit and c in multiplier and d in tolerance:
		xx = st.write_color_digit.get(a)
		yy = st.write_color_digit.get(b)
		zz = st.write_multiplier.get(c)
		aa = st.write_tolerance.get(d)
		print("Resistance = "+xx + yy+\
				" x "+zz+" ohms "+aa)
	else:
		print("Invalid Colors")
	a=st.color_digit("1st Band of Color") 
	b=st.color_digit("2nd Band of Color") 
	c=st.multiplier("3rd Band of Color")
	d=st.tolerance("4th Band of Color") 
	findResistance(a, b, c, d)