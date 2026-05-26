
import time
import streamlit as st
from src.pipelines.voice_pipeline import get_voice_embedding
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.database.db import get_all_students
from src.pipelines.face_pipeline import get_face_embedding, predict_attendance,train_classifier
from src.database.db import create_student
from PIL import Image
import numpy as np

def student_dashboard():
    st.header("Dashboard here")
    

def student_screen():


    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return


    c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
       if st.button("Go back to home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()
        
    st.header('Login using FaceID',text_alignment='center')
    st.space
    st.space

    photo_source=st.camera_input("Position your face in the center")
    if photo_source:
      img=np.array(Image.open(photo_source))

      with st.spinner('AI is scanning'):
          detected,all_ids,num_faces=predict_attendance(img)

          if num_faces==0:
              st.warning("No face detected, please try again")
          elif num_faces>1:
              st.warning("Multiple faces detected, please make sure only your face is visible and try again")
          else:
             if detected:
                    student_id=list(detected.keys())[0]
                    all_students=get_all_students()
                    student=next((s for s in all_students if s['student_id']==student_id),None)

                    if student:
                        st.session_state.is_logged_in=True
                        st.session_state.user_role='student'
                        st.session_state.student_data=student
                        st.toast(f"Welcome {student['name']}! You have successfully logged in.",icon="✅")
                        time.sleep(2)
                        st.rerun()
             else:
                    st.info('Face not recognized, please try again or contact support if the issue persists.')
                    show_registration=True
                    if show_registration:
                        with st.container(border=True):
                            st.header('Register new profile')
                            new_name=st.text_input('Enter your name',placeholder='Your name')

                            st.subheader('Optional:Voice Enrollment')
                            st.info("Enroll your voice only attendance")

                            audio_data=None

                            try:
                                audio_data=st.audio_input('Record a phrase like I am present, My name is Mayukh')
                            except Exception as e:
                                st.error("Audio data failed")

                            if st.button('Create Account',type='primary'):
                                if new_name:
                                    with st.spinner('Creating profile'):
                                        img=np.array(Image.open(photo_source))
                                        encodings=get_face_embedding(img)
                                        if encodings:
                                            face_emb=encodings[0].tolist()

                                            voice_emb=None
                                            if audio_data:
                                                voice_emb=get_voice_embedding(audio_data.read())

                                            response_data= create_student(new_name,face_embedding=face_emb,voice_embedding=voice_emb)    
                                            if response_data:
                                                train_classifier()
                                                st.session_state.is_logged_in=True
                                                st.session_state.user_role='student'
                                                st.session_state.student_data=response_data[0]
                                                st.toast(f'Profile created for {new_name}')
                                                time.sleep(2)
                                                st.rerun()
                                        else:
                                            st.error('Face encoding failed, please try again with a clearer photo')        
                                else:
                                    st.warning('Please enter your name to create a profile')
                                    


    footer_dashboard()
    