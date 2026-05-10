# 🏋️ AI Gym Coach

> **Your intelligent, real-time fitness companion powered by computer vision and generative AI.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Landing%20Page-00C9FF?style=for-the-badge&logo=vercel&logoColor=white)](https://landing-page-ai-gym-coach.vercel.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.54-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose%20Detection-0097A7?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)

---

## 🌐 Live Demo

🔗 **Landing Page:** [https://landing-page-ai-gym-coach.vercel.app/](https://landing-page-ai-gym-coach.vercel.app/)

---

## 📖 About the Project

**AI Gym Coach** is a full-stack AI-powered fitness application that uses your device's camera to track your workouts in real time. It detects body pose landmarks through computer vision, counts exercise repetitions, and delivers voice-based coaching feedback — all without needing any wearable hardware.

The application blends **MediaPipe's human pose estimation**, **Groq's blazing-fast LLM inference**, and **Google Text-to-Speech** to create a personalized coaching experience that motivates, guides, and adapts to the user's performance during each session. Workout history is persisted using a local SQLite database, enabling users to track their long-term progress.

Whether you're doing squats, push-ups, or curls — AI Gym Coach sees your form, counts your reps, and talks you through it.

---

## ✨ Key Features

- 📸 **Real-Time Pose Detection** — Tracks 33 body landmarks at up to 30 FPS via your webcam using MediaPipe Pose.
- 🔢 **Automatic Rep Counting** — Intelligently counts repetitions using joint angle analysis across multiple exercises.
- 🗣️ **AI Voice Coaching** — Generates personalized motivational feedback using Groq (LLaMA) and reads it aloud via gTTS.
- 📊 **Workout History & Analytics** — Stores sessions in SQLite; view aggregated stats with pandas-powered data tables.
- 🔐 **User Authentication** — Secure login and registration with per-user exercise history tracking.
- 🎨 **Custom UI** — Dark-themed, branded interface built with custom CSS injected into Streamlit.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) + Custom CSS |
| **Real-Time Video** | [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc) |
| **Pose Estimation** | [MediaPipe](https://mediapipe.dev/) (Pose Landmarker) |
| **Computer Vision** | [OpenCV](https://opencv.org/) (Headless) |
| **AI Coaching (LLM)** | [Groq API](https://groq.com/) — LLaMA 3 |
| **Text-to-Speech** | [gTTS](https://pypi.org/project/gTTS/) (Google Text-to-Speech) |
| **Data Processing** | [Pandas](https://pandas.pydata.org/) |
| **Database** | SQLite3 (via Python's built-in `sqlite3`) |
| **Config Management** | [python-dotenv](https://pypi.org/project/python-dotenv/) |
| **Language** | Python 3.10+ |
| **Landing Page** | HTML5, CSS3, deployed on [Vercel](https://vercel.com/) |

---

## 🗂️ Project Structure

```
AI Gym Coach/
├── main.py                  # Streamlit app entry point & routing
├── requirements.txt         # Python dependencies
├── packages.txt             # System-level packages (for Streamlit Cloud)
├── runtime.txt              # Python version specification
├── static/
│   ├── style.css            # Custom UI styling
│   └── AdobeClean.otf       # Custom font
├── services/
│   ├── auth/                # User authentication logic
│   ├── coaching/            # AI voice coaching pipeline
│   ├── config/              # App configuration
│   ├── persistence/         # SQLite database layer
│   ├── state/               # Streamlit session state management
│   ├── tracking/            # Rep counting & metrics
│   ├── ui/                  # Reusable UI components
│   └── vision/              # Pose detection & video processing
├── detectors/               # Exercise-specific angle detectors
├── core/                    # Shared models & utilities
└── ml_models/               # ML model assets
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A webcam
- A [Groq API Key](https://console.groq.com/)

### Installation

```bash
# Clone the repository
git clone https://github.com/Ehsaan08/AI-GYM-COACH-.git
cd AI-GYM-COACH-

# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Run the App

```bash
streamlit run main.py
```

---

## 📦 Dependencies

```
streamlit==1.54.0
streamlit-webrtc==0.64.5
mediapipe==0.10.14
opencv-python-headless==4.10.0.84
pandas==2.2.3
groq>=0.12.0
gtts==2.5.3
python-dotenv==1.2.2
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues, suggest features, or submit pull requests.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with ❤️ using Python, MediaPipe & Groq AI
</p>
