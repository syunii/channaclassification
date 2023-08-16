import streamlit as st

def dialog_close_button_clicked():
    st.write("###  Dialog close callback results:")
    st.write("#### No preferences saved!")
    dialog.close()

dialog = st.dialog(
    "first_dialog_with_help", title="Introduce yourself",
    on_close_button_clicked=dialog_close_button_clicked, can_be_closed=True)

def dialog_form_submit_button_clicked():
    st.write("### Dialog form submit button clicked results:")
    st.write(f"#### Hey {st.session_state.first_name} {st.session_state.last_name}!")
    st.write(f"#### Your preferences are saved")
    dialog.close()


with dialog:
    st.text_input("First name", key="first_name")
    st.text_input("Last name", key="last_name")
    st.checkbox("I accept cookies", key="cookies")
    st.form_submit_button("OK", on_click=dialog_form_submit_button_clicked)


if st.button("Open dialog", key="first_dialog_button"):
    dialog.open()