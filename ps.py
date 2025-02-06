import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Prediscan Medtech",
    page_icon="👀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Introduction
st.title("Prediscan Medtech Details for Retinal Vessels Caliber and Diseases Diagnosis")
st.markdown("""
Detailed information on quantifiable parameters, threshold values, and recommendations for additional tests.
""")

# Navigation Sidebar
st.sidebar.title("Navigation")
options = [
    "Diabetic Retinopathy",
    "Glaucoma",
    "Age-Related Macular Degeneration",
    "Hypertensive Retinopathy",
    "Retinopathy of Prematurity",
    "Central Serous Chorioretinopathy"
]
selected_option = st.sidebar.selectbox("Select a Disease", options)

# Content for each disease
if selected_option == "Diabetic Retinopathy":
    st.header("Diabetic Retinopathy")
    st.subheader("Visual Features to Consider")
    st.write("- Microaneurysms")
    st.write("- Hemorrhages")
    st.write("- Hard Exudates")
    st.write("- Cotton Wool Spots")
    st.write("- Neovascularization")
    st.write("- Venous Beading")
    
    st.subheader("Threshold Values and Abnormalities")
    st.table([
        ["Feature", "Normal Threshold", "Abnormal Threshold", "Mathematical Formula/Logic"],
        ["Microaneurysms", "No microaneurysms in any field", "≥ 5 in one field", "Count microaneurysms in each field; if > 5 in any field, classify as abnormal."],
        ["Hemorrhages", "None", "> 5 dot/blot hemorrhages in one field", "Classify and count hemorrhages; if > 5 in any field, classify as abnormal."],
        ["Hard Exudates", "None", "Within 500 µm of fovea", "Measure distance from fovea; if within 500 µm, classify as abnormal."],
        ["Cotton Wool Spots", "None", "Presence of any", "Count and document location."],
        ["Neovascularization", "Absent", "Present", "Identify abnormal vessel growth near disc or elsewhere."],
        ["Venous Beading", "Smooth vessels", "Irregular venous structure", "Assess tortuosity visually."]
    ])
    
    st.subheader("Additional Tests")
    st.write("- **Optical Coherence Tomography (OCT):** Suspected macular edema or subretinal fluid")
    st.write("- **Fluorescein Angiography (FA):** Suspected neovascularization or vascular leakage")
    st.write("- **OCT Angiography (OCTA):** Suspected diabetic macular ischemia")

elif selected_option == "Glaucoma":
    st.header("Glaucoma")
    st.subheader("Visual Features to Consider")
    st.write("- Cup-to-Disc Ratio")
    st.write("- Neuroretinal Rim Width")
    st.write("- Retinal Nerve Fiber Layer Defects")
    st.write("- Optic Disc Hemorrhages")
    st.write("- Parapapillary Atrophy")
    
    st.subheader("Threshold Values and Abnormalities")
    st.table([
        ["Feature", "Normal Threshold", "Abnormal Threshold", "Mathematical Formula/Logic"],
        ["Cup-to-Disc Ratio (Vertical)", "< 0.3", "> 0.6", "Calculate vertical CDR = Vertical Cup Diameter / Vertical Disc Diameter."],
        ["Neuroretinal Rim Width", "Follows ISNT Rule", "Violation of ISNT Rule", "Measure width in inferior, superior, nasal, temporal quadrants."],
        ["Retinal Nerve Fiber Layer Defects", "Uniform thickness", "Wedge-shaped defects", "Identify wedge-shaped defects visually."],
        ["Optic Disc Hemorrhages", "Absent", "Present", "Identify and document location."],
        ["Parapapillary Atrophy", "Minimal", "Extensive", "Measure area of atrophy around disc."]
    ])
    
    st.subheader("Additional Tests")
    st.write("- **Optical Coherence Tomography (OCT):** Detected abnormalities in cup-to-disc ratio or neuroretinal rim width")
    st.write("- **Visual Field Testing (Perimetry):** Structural changes in the optic disc or RNFL with unclear functional loss")
    st.write("- **OCT Angiography (OCTA):** Assessment of vascular changes in the optic nerve head, particularly in normal-tension glaucoma")
    
    st.subheader("Logics and Checks")
    st.write("- Both eyes should have elevated CDR for a definitive diagnosis.")
    st.write("- Asymmetry in CDR between eyes > 0.2 is suspicious.")
    st.write("- Progressive thinning of the neuroretinal rim over time confirms glaucoma.")

elif selected_option == "Age-Related Macular Degeneration":
    st.header("Age-Related Macular Degeneration (AMD)")
    st.subheader("Visual Features to Consider")
    st.write("- Drusen")
    st.write("- Geographic Atrophy")
    
    st.subheader("Threshold Values and Abnormalities")
    st.table([
        ["Feature", "Normal Threshold", "Abnormal Threshold", "Mathematical Formula/Logic"],
        ["Drusen Size", "Small (< 63 µm)", "Intermediate (63–124 µm), Large (> 125 µm)", "Measure drusen diameter."],
        ["Geographic Atrophy", "Absent", "Present", "Measure area of RPE loss."]
    ])
    
    st.subheader("Additional Tests")
    st.write("- **Optical Coherence Tomography (OCT):** Large drusen (>125 µm) or geographic atrophy")
    st.write("- **Fluorescein Angiography (FA):** Suspected choroidal neovascularization")
    st.write("- **OCT Angiography (OCTA):** Non-invasive visualization of CNV and macular perfusion")
    
    st.subheader("Logics and Checks")
    st.write("- Early AMD: Presence of medium drusen.")
    st.write("- Intermediate AMD: Presence of large drusen or pigmentary changes.")
    st.write("- Advanced AMD: Presence of geographic atrophy or choroidal neovascularization.")

elif selected_option == "Hypertensive Retinopathy":
    st.header("Hypertensive Retinopathy")
    st.subheader("Visual Features to Consider")
    st.write("- Arteriolar Narrowing")
    st.write("- Arteriovenous Nicking")
    st.write("- Flame-Shaped Hemorrhages")
    st.write("- Cotton Wool Spots")
    st.write("- Macular Star")
    
    st.subheader("Threshold Values and Abnormalities")
    st.table([
        ["Feature", "Normal Threshold", "Abnormal Threshold", "Mathematical Formula/Logic"],
        ["Arteriolar Narrowing", "AVR: 0.6–0.8", "AVR: < 0.6", "Calculate AVR = Arteriolar Diameter / Venular Diameter."],
        ["Arteriovenous Nicking", "Absent", "Present", "Identify compression of veins by arteries."],
        ["Flame-Shaped Hemorrhages", "None", "Presence", "Identify and count hemorrhages."],
        ["Cotton Wool Spots", "None", "Presence", "Identify and count cotton wool spots."],
        ["Macular Star", "Absent", "Present", "Identify star-like pattern of exudates."]
    ])
    
    st.subheader("Additional Tests")
    st.write("- **Monitor systemic blood pressure.**")
    st.write("- **Evaluate for systemic complications of hypertension.**")
    
    st.subheader("Logics and Checks")
    st.write("- Grade hypertensive retinopathy based on the Keith-Wagener-Barker classification.")

elif selected_option == "Retinopathy of Prematurity":
    st.header("Retinopathy of Prematurity (ROP)")
    st.subheader("Visual Features to Consider")
    st.write("- Vascular Ridge")
    st.write("- Plus Disease")
    
    st.subheader("Threshold Values and Abnormalities")
    st.table([
        ["Feature", "Normal Threshold", "Abnormal Threshold", "Mathematical Formula/Logic"],
        ["Vascular Ridge", "Normal vascularization", "Presence of ridge", "Identify avascular zones and ridge formation."],
        ["Plus Disease", "No tortuosity", "Tortuosity score > 2", "Use standardized images to grade tortuosity and dilation."]
    ])
    
    st.subheader("Additional Tests")
    st.write("- **Perform RetCam imaging for detailed visualization.**")
    st.write("- **Conduct serial examinations to monitor progression.**")
    
    st.subheader("Logics and Checks")
    st.write("- Both eyes are typically affected.")
    st.write("- Treatment threshold: Zone I or posterior Zone II with plus disease.")

elif selected_option == "Central Serous Chorioretinopathy":
    st.header("Central Serous Chorioretinopathy (CSCR)")
    st.subheader("Visual Features to Consider")
    st.write("- Pigment Epithelial Detachment")
    
    st.subheader("Threshold Values and Abnormalities")
    st.table([
        ["Feature", "Normal Threshold", "Abnormal Threshold", "Mathematical Formula/Logic"],
        ["Pigment Epithelial Detachment", "Absent", "Present", "Measure elevation of RPE."]
    ])
    
    st.subheader("Additional Tests")
    st.write("- **Perform Optical Coherence Tomography (OCT) to quantify subretinal fluid.**")
    st.write("- **Conduct Fluorescein Angiography (FA) to identify leakage points.**")
    
    st.subheader("Logics and Checks")
    st.write("- Unilateral presentation is common.")
    st.write("- Chronic cases may lead to permanent vision loss.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed by Prediscan Medtech Private Limited")
st.sidebar.write("Sources:")
st.sidebar.write("- American Academy of Ophthalmology (AAO)")
st.sidebar.write("- World Health Organization (WHO)")
st.sidebar.write("- Indian Council of Medical Research (ICMR)")
st.sidebar.write("- National Programme for Control of Blindness (NPCB)")
st.sidebar.write("- Indian Journal of Ophthalmology (IJO)")
