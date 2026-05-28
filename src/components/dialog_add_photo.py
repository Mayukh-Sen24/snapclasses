import streamlit as st
from src.database.config import supabase
from PIL import Image
from src.database.db import enroll_Student_to_subject

@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write('Add classroom photos to add for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state['photo_tab'] = 'camera'

    t1,t2=st.columns(2)

    with t1:
        type_camera='primary' if st.session_state.photo_tab=='camera' else 'tertiary'
        if st.button('Camera',type=type_camera,width='stretch'):
            st.session_state.photo_tab='camera' 

    with t2:
        type_upload='primary' if st.session_state.photo_tab=='upload' else 'tertiary'
        if st.button('Upload',type=type_upload,width='stretch'):
            st.session_state.photo_tab='upload'         

    if st.session_state.photo_tab == 'camera':
        cam_photo=st.camera_input("Take a photo",key='dialog_cam')        
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast("Photo added successfully",icon="✅")
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        upload_photo=st.file_uploader("Upload a photo",type=['jpg','jpeg','png'],key='dialog_upload',accept_multiple_files=True)
        if upload_photo:
            for photo in upload_photo:
                st.session_state.attendance_images.append(Image.open(photo))
            st.toast("Photos added successfully",icon="✅")
            st.rerun()

    st.divider()
    if st.button('Done',type='primary',width='stretch'):
        st.rerun()


        