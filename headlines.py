import streamlit as st
import os
import google.generativeai as genai

def get_gemini_response(platform, gen, description):

  prompt = f"Platform: {platform}\nContent Type: {gen}\nDescription: {description}"
  response = model.generate_content(prompt)
  return response.text

# Configure genai (assuming you have set the GOOGLE_API_KEY environment variable)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("HEADLINES AI")

platform = st.selectbox("Choose Platform", ["YouTube", "Medium", "Reddit", "Indie Hackers", "Blog"])
platform = platform.lower()  #Convert to lowercase for consistency

content_type_options = {
    "youtube": ["Video Ideas", "Headlines", "Description", "Hashtags"],  #Key changed to lowercase
    "medium": ["Headlines", "CTAs"],
    "reddit": ["Headlines", "CTAs"],
    "indie hackers": ["Headlines", "CTAs"],
    "blog": ["Headlines", "CTAs"],
}

gen = st.selectbox("Select Content Type", content_type_options[platform])
gen = gen.lower()  # Convert to lowercase for consistency

description = st.text_area("What is your content about?\n(Describe in 2-3 lines with main highlights to get the best outputs)", height=100)

if st.button("Generate Content"):
  response = get_gemini_response(platform, gen, description)
  st.write("Generated Content:")
  st.success(response)
