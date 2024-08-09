import streamlit as st

st.title('Title -> Helloo')
st.header('Header -> Hi')
st.subheader('Subheader ->Welcome')
st.text('Text ->Happy')

st.markdown('#bye')

st.success('Success!')
st.info('Information!')
st.warning('Warning!')
st.error('Error!')
st.exception(ZeroDivisionError('Div not possible'))


st.subheader('Help')
st.help(ZeroDivisionError)

st.subheader('Write')
st.write('range(1,10)')
st.write(range(1,10))
st.write(1*2*3)

st.subheader('Code')
st.code('x =10\n'
        'for i in range(x):\n'
        '\tprint(i)')


st.subheader('Checkbox')
st.checkbox('Male')
if(st.checkbox('Adult')):
    st.write("You are an Adult!")

st.subheader('RadioButton')
radiobutton = st.radio('Select:',('Male','Female','Other'))
if(radiobutton =='Male'):
    st.write("You're a Male")
elif(radiobutton =='Female'):
    st.write("You're a Female")
elif(radiobutton =='Other'):
    st.write("You're a Other")


st.subheader('Select Box')
selectBox = st.selectbox("Data Science :",['Data Analysis','Web Scrapping','Machine Learning','Deep Learning','Natural Language Processing','Computer Vision','Image Processing'])

st.write("You've selected : ", selectBox)

st.subheader('MultiSelect Box')
multiSelectBox = st.multiselect("Data Science :",['Data Analysis','Web Scrapping','Machine Learning','Deep Learning','Natural Language Processing','Computer Vision','Image Processing'])

st.write("You've selected : ", len(multiSelectBox), 'courses')

st.subheader("Button")
if(st.button('Click me')):
    st.write('Thanks for clicking me')



st.subheader("Slider")
vol = st.slider('Select the volume',0,100,step = 1)
st.write('Volume is :',vol)


st.subheader("Text Input")
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')

st.subheader("Text Area")
st.text_area('Write something interesting about yourself')



st.subheader("Input Number")
st.number_input('Select your age ',18,110)

st.subheader("Input Date")
st.date_input('Date')

st.subheader("Input Time")
st.time_input('Time')
