import os

import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer

from services.auth.login_wall import render_login_wall
from services.config.workout_config import EXERCISE_OPTIONS
from services.persistence.exercise_repository import init_db
from services.state.session_defaults import initial_session_defaults
from services.ui.style_loader import inject_local_font, inject_webrtc_styles, load_css
from services.vision.exercise_video_processor import VideoProcessorClass


def main():

    st.set_page_config(
        page_icon="🏋️",
        page_title="AI Gym Coach",
        initial_sidebar_state="expanded",
        layout="centered",
    )

    load_css(os.path.join(os.getcwd(), "static", "style.css"))
    inject_local_font(
        os.path.join(os.getcwd(), "static", "AdobeClean.otf"), "AdobeClean"
    )

    init_db()

    if not render_login_wall():
        return

    initial_session_defaults()

    workout_started = st.session_state.get("workout_started", False)

    with st.sidebar:
        st.title("🏋️ AI GYM COACH")

        if st.session_state.username:
            st.caption(f"👤Login as {st.session_state.username}")

        st.divider()

        st.subheader("Workout Plan")

        if not workout_started:
            st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")

            st.number_input("Sets", min_value=1, max_value=50, key="plan_sets", step=1)

            st.number_input(
                "Reps per set", min_value=1, max_value=50, key="plan_reps", step=1
            )

            st.markdown("")

            start_session_button = st.button(
                "Start Workout", width="stretch", key="start_session_button"
            )

            if start_session_button:
                st.session_state["workout_started"] = True

                st.rerun()
        else:
            exercise = st.session_state.get("plan_exercise")
            sets = st.session_state.get("plan_sets")
            reps = st.session_state.get("plan_reps")

            st.info(f"**{exercise}** -- {sets} Sets / {reps} Reps")

            end_session_button = st.button(
                "End Workout", key="end_session_button", width="stretch"
            )

            if end_session_button:
                st.session_state["workout_started"] = False
                st.rerun()

        if workout_started:
            st.divider()

            exercise = st.session_state.get("plan_exercise")
            total_reps = st.session_state.get("reps")
            current_set_reps = st.session_state.get("current_set_reps")
            reps_per_set = st.session_state.get("plan_reps")
            sets_completed = st.session_state.get("sets_completed")
            target_sets = st.session_state.get("plan_sets")

            st.subheader("Progress")

            st.metric("Total Reps", f"{total_reps}")
            st.metric("Current Set Reps", f"{current_set_reps} / {reps_per_set}")
            st.metric("Sets Completed", f"{sets_completed} / {target_sets}")

            st.divider()

            if exercise == "Squats":
                st.subheader("Squat Metric")
                st.metric("Knee Angle", f"{st.session_state.knee_angle}°")
                st.metric("Back Angle", f"{st.session_state.back_angle}°")
                st.metric("Depth Status", f"{st.session_state.depth_status}")

            elif exercise == "Push-ups":
                st.subheader("Push-ups Metric")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Body Alignment", f"{st.session_state.body_alignment}")
                st.metric("Hip position", f"{st.session_state.hip_status}")

            elif exercise == "Biceps Curls (Dumbbell)":
                st.subheader("Curl Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Shoulder Stability", f"{st.session_state.shoulder_status}")
                st.metric("Swing Detection", f"{st.session_state.swing_status}")

            elif exercise == "Shoulder Press":
                st.subheader("Shoulder Press Metric")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Arm Extension", f"{st.session_state.extension_status}")
                st.metric("Back Arch", f"{st.session_state.back_arch_status}")

            elif exercise == "Lunges":
                st.subheader("Lunges Metric")
                st.metric("Front Knee Angle", f"{st.session_state.front_knee_angle}°")
                st.metric("Torso Angle", f"{st.session_state.torso_angle}°")
                st.metric("Balance Status", f"{st.session_state.balance_status}")

    st.title("AI GYM COACH")
    st.markdown("#### Real-time pose detection with proactive AI voice coaching")

    if not workout_started:
        st.markdown(
            """
        <div style="
            border: 10px dashed #444;
            border-radius: 0px;
            padding: 40px 32px;
            text-align: center;
            color: #888;
            margin-top: 32px;
        ">
            <h2 style="color: #ccc; margin-bottom: 8px;">👈Set your workout plan </h2>
            <p style="font-size: 1.05rem;">
                Choose your exercise, sets and reps in the sidebar, <br>
                then click <strong>Start Workout</strong> to activate the camera and AI coach
            </p>
        </div>      
        """,
            unsafe_allow_html=True,
        )

    else:
        context = webrtc_streamer(
            key="exercise-analysis",
            mode=WebRtcMode.SENDRECV,
            video_processor_factory=VideoProcessorClass,
            rtc_configuration={
                "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
            },
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )

        inject_webrtc_styles()

    st.markdown("#### Workout History")


if __name__ == "__main__":
    main()
