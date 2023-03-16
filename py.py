import streamlit as st
from PIL import Image
st.title("PHYSICS")
tab1,tab2,tab3,tab4,tab5 = st.tabs(['RESISTOR COLOR CODE CALCULATOR','NUMBER CONVERSION','OHMS LAW','PARALLEL AND SERIES ','Constants'])
with tab1:
 st.title("RESISTOR COLOR CODE CALCULATOR")
#color_digit = {'black': '0','brown': '1','red': '2','orange': '3','yellow': '4','green' : '5','blue' : '6','violet' : '7','grey' : '8','white': '9'}
#multiplier = {'black': '1','brown': '10','red': '100','orange': '1k','yellow': '10k','green' : '100k','blue' : '1M','violet' : '10M','grey' : '100M','white': '1G'}
#tolerance = {'brown': '+/- 1 %','red' : '+/- 2 %','green': "+/- 0.5 %",'blue': '+/- 0.25 %','violet' : '+/- 0.1 %','gold': '+/- 5 %','silver' : '+/- 10 %','none': '+/-20 %'}
img=Image.open("ohms.png")
st.image(img)	
first=st.selectbox("1st Band of Color",('Black','Brown','Red','Orange','Yellow','Green','Blue','Grey','White'))
if first=='Black':
 first=0
if first=='Brown':
 first=1
if first=='Red':
 first=2
if first=='Orange':
 first=3
if first=='Yellow':
 first=4
if first=='Green':
 first=5
if first=='Blue':
 first=6 
if first=='Violet':
 first=7
if first=='Grey':
 first=8 
if first=='White':
 first=9
second=st.selectbox("2nd Band of Color",('Black','Brown','Red','Orange','Yellow','Green','Blue','Grey','White'))
if second=='Black':
 second=0
if second=='Brown':
 second=1
if second=='Red':
 second=2
if second=='Orange':
 second=3
if second=='Yellow':
 second=4
if second=='Green':
 second=5
if second=='Blue':
 second=6
if second=='Violet':
 second=7
if second=='Grey':
 second=8
if second=='White':
 second=9
third=st.selectbox("3rd Band of Color",('Black','Brown','Red','Orange','Yellow','Green','Blue','Grey','White'))
if third=='Black':
 third=1
if third=='Brown':
 third=10
if third=='Red':
 third=100
if third=='Orange':
 third=1000
if third=='Yellow':
 third=10000
if third=='Green':
 third=100000
if third=='Blue':
 third=1000000
if third=='Violet':
 third=10000000
if third=='Grey':
 third=100000000
if third=='White':
 third=1000000000
fourth=st.selectbox("4th Band of Color",('Brown','Red','Green','Blue','Violet','Gold','Silver'))
if fourth=='Brown':
 fourth= 1 
if fourth=='Red':
 fourth= 2
if fourth=='Green':
 fourth= 0.5
if fourth=='Blue':
 fourth= 0.25
if fourth=='Violet':
 fourth= 0.1
if fourth=='Gold':
 fourth= 5
if fourth=='Silver':
 fourth= 10 
if fourth=='None':
 fourth= 20
v = first*second*(third)
st.write("Resistance Value ", v ,"±",fourth ,"%","ohms")  

#with tab2:
 
#with tab3:
  
#with tab4:
   
with tab5:
	st.title("CONSTANTS")
