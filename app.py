import streamlit as st
import streamlit.components.v1 as components
from ultralytics import YOLO
from collections import Counter
from PIL import Image, UnidentifiedImageError
from component_database import component_database as db
import html

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="E-Waste Intelligence",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ANIMATED ECO-TECH DESIGN
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --green: #66ffad;
    --cyan: #65e8ff;
    --dark: #07120f;
    --panel: rgba(255,255,255,0.045);
    --muted: #a4b9b0;
}

.stApp {
    background:
        radial-gradient(ellipse at 15% 0%, #123b2b 0%, transparent 38%),
        radial-gradient(ellipse at 95% 35%, #102c32 0%, transparent 35%),
        #07120f;
    color: #edfdf5;
    font-family: 'DM Sans', sans-serif;
}

html {
    scroll-behavior: smooth;
}

[data-testid="stHeader"] {
    background: rgba(7,18,15,0.85);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1, h2, h3, h4 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #effff6 !important;
}

p, li, label {
    color: #d0e5db;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 4rem 2rem 3rem;
    border: 1px solid rgba(102,255,173,0.20);
    border-radius: 28px;
    background: linear-gradient(130deg,
        rgba(29,91,60,0.42),
        rgba(10,30,28,0.78) 55%,
        rgba(18,58,68,0.38));
    animation: fadeUp 0.9s ease both;
}

.hero:before {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: rgba(102,255,173,0.10);
    filter: blur(65px);
    top: -120px;
    right: -70px;
    animation: floatGlow 7s ease-in-out infinite alternate;
}

.eyebrow {
    display: inline-block;
    padding: 8px 13px;
    border: 1px solid rgba(102,255,173,0.30);
    border-radius: 50px;
    color: var(--green);
    background: rgba(102,255,173,0.07);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.6rem, 6vw, 5.2rem);
    line-height: 1.04;
    letter-spacing: -0.055em;
    font-weight: 700;
    margin: 1.2rem 0;
    color: white;
}

.gradient-text {
    background: linear-gradient(90deg, #66ffad, #65e8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-copy {
    max-width: 680px;
    font-size: 1.08rem;
    line-height: 1.8;
    color: #bad1c5;
}

.hero-bottom {
    margin-top: 1.8rem;
    color: var(--green);
    font-size: 0.88rem;
    letter-spacing: 0.03em;
}

.section-kicker {
    color: var(--green);
    font-size: 0.76rem;
    letter-spacing: 0.16em;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.8rem, 3vw, 2.8rem);
    line-height: 1.15;
    letter-spacing: -0.04em;
    margin-bottom: 0.5rem;
}

.section-copy {
    color: var(--muted);
    line-height: 1.75;
}

.feature-card {
    height: 100%;
    padding: 1.4rem;
    border-radius: 20px;
    border: 1px solid rgba(150,255,200,0.14);
    background: var(--panel);
    transition: transform 0.25s ease,
                border-color 0.25s ease,
                background 0.25s ease;
    animation: fadeUp 0.8s ease both;
}

.feature-card:hover {
    transform: translateY(-6px);
    border-color: rgba(102,255,173,0.48);
    background: rgba(102,255,173,0.07);
}

.feature-icon {
    font-size: 2rem;
    margin-bottom: 0.7rem;
}

.feature-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: #f0fff7;
}

.feature-copy {
    color: #a9c2b6;
    font-size: 0.93rem;
    line-height: 1.7;
}

.panel {
    border: 1px solid rgba(150,255,200,0.15);
    background: rgba(255,255,255,0.035);
    border-radius: 22px;
    padding: 1.4rem;
}

.metric-card {
    border: 1px solid rgba(102,255,173,0.20);
    background: linear-gradient(145deg,
        rgba(102,255,173,0.08),
        rgba(101,232,255,0.025));
    border-radius: 18px;
    padding: 1.2rem;
    margin-bottom: 0.6rem;
    transition: transform 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-3px);
}

.metric-label {
    color: #9eb9ac;
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.metric-number {
    color: var(--green);
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    line-height: 1.3;
}

.component-card {
    border: 1px solid rgba(102,255,173,0.16);
    background: rgba(255,255,255,0.035);
    border-radius: 16px;
    padding: 1.1rem;
    margin: 0.5rem 0;
    animation: fadeUp 0.5s ease both;
}

.pill {
    display: inline-block;
    padding: 5px 10px;
    background: rgba(102,255,173,0.10);
    border: 1px solid rgba(102,255,173,0.18);
    color: var(--green);
    border-radius: 30px;
    font-size: 0.78rem;
    font-weight: 700;
}

.stButton > button {
    border-radius: 12px;
    border: 1px solid rgba(102,255,173,0.35);
    background: linear-gradient(90deg, #66ffad, #65e8ff);
    color: #07120f;
    font-weight: 700;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(102,255,173,0.16);
    color: #07120f;
}

[data-testid="stFileUploader"] {
    border: 1px dashed rgba(102,255,173,0.45);
    border-radius: 18px;
    padding: 1rem;
    background: rgba(102,255,173,0.035);
}

[data-testid="stExpander"] {
    border: 1px solid rgba(102,255,173,0.17);
    border-radius: 14px;
    background: rgba(255,255,255,0.025);
}

hr {
    border-color: rgba(150,255,200,0.14);
    margin-top: 2rem;
    margin-bottom: 2rem;
}

.footer {
    text-align: center;
    padding: 2rem 0 0.5rem;
    color: #819b8e;
    font-size: 0.85rem;
    line-height: 1.8;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(22px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes floatGlow {
    from { transform: translate(0, 0) scale(1); }
    to   { transform: translate(-35px, 35px) scale(1.2); }
}

@media (max-width: 700px) {
    .hero { padding: 2.3rem 1.2rem; }
    .hero-title { font-size: 2.6rem; }
    .block-container { padding-left: 1rem; padding-right: 1rem; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPERS
# =========================================================
ICONS = {
    "ic": "🧠",
    "capacitor": "🔋",
    "resistor": "🟫",
    "diode": "💡",
    "led": "💡",
    "connector": "🔌",
    "switch/button": "🔘",
    "header": "📌",
    "crystal": "💎",
    "debug/tp": "🔍",
    "inductor": "🌀"
}


def normalize_name(name):
    return " ".join(str(name).strip().lower().split())


def get_component_details(name):
    target = normalize_name(name)

    for key, details in db.items():
        if normalize_name(key) == target:
            return details

    return None


@st.cache_resource
def load_model():
    return YOLO("runs/detect/train/weights/best.pt")


def section_heading(kicker, title, copy):
    st.markdown(
        f"""
        <div class="section-kicker">{html.escape(kicker)}</div>
        <div class="section-title">{html.escape(title)}</div>
        <div class="section-copy">{html.escape(copy)}</div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="hero" id="top">
    <div class="eyebrow">♻️ AI for a greener tomorrow</div>
    <div class="hero-title">
        Give electronic waste<br>
        <span class="gradient-text">a second look.</span>
    </div>
    <div class="hero-copy">
        An AI-powered PCB analysis experience that detects electronic
        components, explores their typical materials, and guides users
        toward responsible e-waste recycling.
    </div>
    <div class="hero-bottom">
        ● COMPUTER VISION &nbsp; / &nbsp; MATERIAL INSIGHTS
        &nbsp; / &nbsp; RESPONSIBLE RECYCLING
    </div>
</div>
""", unsafe_allow_html=True)

# Simple anchor navigation
st.markdown("""
<div style="padding: 1.3rem 0; color:#a4b9b0;">
    <a href="#how-it-works" style="color:#66ffad;text-decoration:none;">How it works</a>
    &nbsp;&nbsp;·&nbsp;&nbsp;
    <a href="#analyzer" style="color:#66ffad;text-decoration:none;">Analyze a PCB</a>
    &nbsp;&nbsp;·&nbsp;&nbsp;
    <a href="#impact" style="color:#66ffad;text-decoration:none;">Why recycling matters</a>
</div>
""", unsafe_allow_html=True)


# =========================================================
# HOW IT WORKS
# =========================================================
st.markdown('<div id="how-it-works"></div>', unsafe_allow_html=True)
section_heading(
    "The workflow",
    "From image to insight.",
    "A simple workflow to explore a circuit board without claiming more "
    "than the AI can actually determine."
)

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📷</div>
        <div class="feature-title">01 — Upload</div>
        <div class="feature-copy">
            Upload a clear photo of a printed circuit board to begin
            the visual inspection.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">02 — Detect</div>
        <div class="feature-copy">
            A YOLO computer-vision model predicts component classes
            and draws bounding boxes around detections.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">♻️</div>
        <div class="feature-title">03 — Understand</div>
        <div class="feature-copy">
            Explore typical component functions, materials, and
            responsible recycling guidance from the database.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ANALYZER
# =========================================================
st.markdown('<div id="analyzer"></div>', unsafe_allow_html=True)
st.divider()

section_heading(
    "AI laboratory",
    "Analyze your circuit board.",
    "Upload an image and let the model examine the visible components."
)

with st.sidebar:
    st.markdown("## ⚙️ Analysis settings")
    conf = st.slider(
        "Minimum detection confidence",
        min_value=0.10,
        max_value=0.90,
        value=0.50,
        step=0.05
    )
    st.caption(
        "Higher values filter out more low-confidence predictions, "
        "but may also miss real components."
    )

    st.divider()
    st.markdown("### 🧪 Model")
    st.caption("YOLO PCB component detector")
    st.caption("Model: yolov8s_pcb_best.pt")

uploaded_file = st.file_uploader(
    "Choose a PCB image",
    type=["jpg", "jpeg", "png"],
    help="Use a clear, well-lit image with the board filling most of the frame."
)

if uploaded_file is None:
    st.markdown("""
    <div class="panel">
        <div class="feature-icon">🖼️</div>
        <h3>Ready when you are</h3>
        <p style="color:#a4b9b0;line-height:1.8;">
            Your uploaded image and its analysis will appear here.
            For best results, photograph the board clearly and avoid blur,
            glare, or very small components.
        </p>
        <span class="pill">JPG · JPEG · PNG</span>
    </div>
    """, unsafe_allow_html=True)

else:
    try:
        image = Image.open(uploaded_file).convert("RGB")
    except (UnidentifiedImageError, OSError, ValueError):
        st.error("The uploaded file is not a valid image. Please try another JPG or PNG.")
        st.stop()

    with st.expander("Preview uploaded image"):
        st.image(image, caption="Original PCB image", width="stretch")

    try:
        model = load_model()
        with st.spinner("🔬 Scanning the circuit board..."):
            result = model.predict(
                source=image,
                conf=conf,
                save=False,
                verbose=False
            )[0]
    except Exception as error:
        st.error("The model could not analyze this image.")
        st.caption(f"Technical details: {error}")
        st.stop()

    counts = Counter()
    confidence_values = {}

    if result.boxes is not None and len(result.boxes) > 0:
        for box in result.boxes:
            class_id = int(box.cls[0].item())
            score = float(box.conf[0].item())
            name = model.names[class_id]
            counts[name] += 1
            confidence_values.setdefault(name, []).append(score)

    st.markdown("### ✨ Your analysis")

    left, right = st.columns([1.25, 0.75], gap="large")

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("#### Detection preview")

        # Ultralytics plot() returns BGR pixels; convert them to RGB.
        annotated = Image.fromarray(result.plot()[:, :, ::-1])

        st.image(
            annotated,
            caption="AI-predicted component labels",
            width="stretch"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        total = sum(counts.values())
        unique = len(counts)

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total detections</div>
            <div class="metric-number">{total}</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Predicted component types</div>
            <div class="metric-number">{unique}</div>
        </div>
        """, unsafe_allow_html=True)

        if counts:
            st.markdown("#### Component breakdown")
            for name, count in counts.most_common():
                icon = ICONS.get(normalize_name(name), "🔹")
                st.markdown(
                    f'<div class="component-card">'
                    f'<span style="font-size:1.25rem;">{icon}</span> '
                    f'<strong>{html.escape(name)}</strong>'
                    f'<span style="float:right;color:#66ffad;font-weight:700;">'
                    f'× {count}</span></div>',
                    unsafe_allow_html=True
                )
        else:
            st.warning(
                "No components were detected at this confidence level. "
                "Try a clearer image or lower the confidence setting."
            )

    # -----------------------------------------------------
    # MATERIAL ANALYSIS
    # -----------------------------------------------------
    if counts:
        st.divider()
        section_heading(
            "Component library",
            "Material & recycling insights.",
            "These are typical properties of the predicted component types, "
            "not laboratory measurements of this particular board."
        )

        for index, (name, count) in enumerate(counts.most_common()):
            icon = ICONS.get(normalize_name(name), "🔹")
            details = get_component_details(name)
            scores = confidence_values.get(name, [])
            average_confidence = (
                sum(scores) / len(scores) if scores else None
            )

            with st.expander(
                f"{icon}  {name}  ·  {count} detected",
                expanded=(index == 0)
            ):
                if average_confidence is not None:
                    st.caption(
                        f"Average model confidence for this class: "
                        f"{average_confidence:.0%}"
                    )

                if details:
                    a, b = st.columns(2, gap="medium")

                    with a:
                        st.markdown("**⚙️ Function**")
                        st.write(details.get(
                            "function", "Information unavailable."
                        ))

                    with b:
                        st.markdown("**🧱 Typical materials**")
                        st.write(details.get(
                            "materials", "Information unavailable."
                        ))

                    st.markdown("**♻️ Recycling guidance**")
                    st.write(details.get(
                        "recycling",
                        "Consult an authorized e-waste recycler."
                    ))
                else:
                    st.info(
                        f"No matching entry for **{name}** was found in "
                        "`component_database.py`. Add this class to the "
                        "database to show its material information."
                    )

    st.caption(
        "AI predictions can be incorrect. A higher confidence score does not "
        "guarantee that a label is correct. Images cannot confirm exact material "
        "composition, quantities, or recoverable value."
    )


# =========================================================
# SUSTAINABILITY SECTION
# =========================================================
st.markdown('<div id="impact"></div>', unsafe_allow_html=True)
st.divider()

section_heading(
    "Beyond detection",
    "Make electronics part of the circular economy.",
    "Responsible e-waste management helps keep valuable resources in use "
    "and prevents unsafe disposal."
)

i1, i2, i3 = st.columns(3, gap="medium")

with i1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔎</div>
        <div class="feature-title">Recognize</div>
        <div class="feature-copy">
            Use computer vision to help identify visible electronic
            component categories.
        </div>
    </div>
    """, unsafe_allow_html=True)

with i2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌱</div>
        <div class="feature-title">Understand</div>
        <div class="feature-copy">
            Learn about common component functions and typical materials
            through a reference database.
        </div>
    </div>
    """, unsafe_allow_html=True)

with i3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">♻️</div>
        <div class="feature-title">Recycle responsibly</div>
        <div class="feature-copy">
            Choose an authorized e-waste recycler instead of unsafe
            dismantling or disposal.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <div style="font-size:1.5rem;">♻️</div>
    <strong style="color:#66ffad;">E-Waste Intelligence</strong><br>
    AI-assisted PCB component detection & material insights<br>
    <span style="font-size:0.78rem;">
        Built for awareness, reuse, and responsible recycling.
        Predictions are estimates, not material certification.
    </span>
</div>
""", unsafe_allow_html=True)