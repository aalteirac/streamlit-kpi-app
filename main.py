import streamlit as st
from streamlit_kpi import streamlit_kpi


st.set_page_config(layout="wide")

with st.expander('Settings'):
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        title=st.text_input('Title:','Monthly<br>Sales')
        valueText=st.text_input('Text Value:','Bryan is winning 10k')
        unit=st.text_input('Value Unit:','Mb')
        backgroundColor=st.text_input('Background Color (str/hex):','#f3f3f3')  
    with col2:    
        showProg=st.checkbox('Show Progress bar',True)
        progress=st.slider('Progress %',0,100,64)
        st.slider('Numeric value',10,1000,200,10,key='sd')
        progressColor=st.text_input('Progress Color (str/hex):','green')  
    with col3:    
        animate=st.checkbox('Activate Animation',True)
        animationDur=st.slider('Animation Duration',1000,5000,1000,step=500)
        height=st.slider('Widget Height',100,1000,210,10) 
        textAlign=st.selectbox('General Text Align)',['left','center','right'],key='alig')
    with col4:
        showIcon=st.checkbox('Show Icon',True)
        iconTop=st.slider('Icon Top Position',0,100,35)    
        iconLeft=st.slider('Icon Left Position',0,100,79) 
        iconType=st.selectbox('Icon Samples (all font awesome)',['fa-regular fa-thumbs-up','fa-regular fa-thumbs-down','fa-solid fa-thumbs-up','fa-solid fa-thumbs-down','fa-ethernet','fa-mobile','fa-globe', 'fa-network-wired','fa-server','fa-ethernet','fa-satellite-dish','fa-wifi','fa-money-bill'],key='ico')
    with col5:
        iconOpacity=st.slider('Icon Opacity',0,100,40)  
        iconColor=st.text_input('Icon Color (str/hex):','black')  
        titleColor=st.text_input('Title Color (str/hex):','black') 
        valueColor=st.text_input('Value Color (str/hex):','black')   
if st.session_state.get('sd') is None:
    nb=2000
else:
    nb=st.session_state.get('sd')
if title =='':
    title="Text Long long long"

col1,col2,col3,col4=st.columns(4)
with col1:
    streamlit_kpi(key="zero",height=height,title=title,value=nb+0.5678,icon=iconType,progressValue=progress,unit=unit,animate=animate,animateDuration=animationDur,
                    showProgress=showProg,iconTop=iconTop,showIcon=showIcon,
                    iconLeft=iconLeft,iconOpacity=iconOpacity,iconColor=iconColor,
                    backgroundColor=backgroundColor,titleColor=titleColor,valueColor=valueColor,
                    progressColor=progressColor,textAlign=textAlign
                    )
with col2:
    streamlit_kpi(key="one",height=height,title=title,value=nb,icon=iconType,progressValue=progress,unit=unit,animate=animate,animateDuration=animationDur,
                showProgress=showProg,iconTop=iconTop,showIcon=showIcon,
                iconLeft=iconLeft,iconOpacity=iconOpacity,iconColor=iconColor,
                backgroundColor=backgroundColor,titleColor=titleColor,valueColor=valueColor,
                progressColor=progressColor,textAlign=textAlign
                )
with col3:
    streamlit_kpi(key="zerob",height=height,title=title,value=nb+0.5678,icon=iconType,progressValue=progress,unit=unit,animate=animate,animateDuration=animationDur,
                    showProgress=showProg,iconTop=iconTop,showIcon=showIcon,
                    iconLeft=iconLeft,iconOpacity=iconOpacity,iconColor=iconColor,
                    backgroundColor=backgroundColor,titleColor=titleColor,valueColor=valueColor,
                    progressColor=progressColor,textAlign=textAlign
                    )
with col4:
    streamlit_kpi(key="oneb",height=height,title=title,value=nb,icon=iconType,progressValue=progress,unit=unit,animate=animate,animateDuration=animationDur,
                showProgress=showProg,iconTop=iconTop,showIcon=showIcon,
                iconLeft=iconLeft,iconOpacity=iconOpacity,iconColor=iconColor,
                backgroundColor=backgroundColor,titleColor=titleColor,valueColor=valueColor,
                progressColor=progressColor,textAlign=textAlign
                )     
streamlit_kpi(key="three",height=height*2,title=title,value=valueText,icon=iconType,progressValue=progress,unit=unit,animate=animate,animateDuration=animationDur,
                showProgress=showProg,iconTop=iconTop,showIcon=showIcon,
                iconLeft=iconLeft,iconOpacity=iconOpacity,iconColor=iconColor,
                backgroundColor=backgroundColor,titleColor=titleColor,valueColor=valueColor,
                progressColor=progressColor,textAlign=textAlign
                )