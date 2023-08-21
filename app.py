import streamlit as st
import replicate
import time

# Configure Streamlit Page
page_icon = "https://spng.pngfind.com/pngs/s/67-672131_attentive-cat-silhouette-cat-with-long-tail-silhouette.png"
st.set_page_config(page_title="Mischa Cat Generator", page_icon=page_icon)

# Read Custom CSS
with open("assets/css/style.css", "r") as f:
    css_text = f.read()
custom_css = f"<style>{css_text}</style>"
st.markdown(custom_css, unsafe_allow_html=True)

# Heading
st.header("'Mischa' Cat Generator")
powered_by = """
<div style="display: flex; align-items: center; margin-bottom:0px">
    <span style="font-size: 12px; margin-right: 4px; font-style: italic;">Powered by:</span>
    <img src="https://www.sequoiacap.com/wp-content/uploads/sites/6/2022/06/replicate-logo-black-transparent.svg" alt="OpenAI logo" height="16" style="margin-right: 4px;"> 
    <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" alt="OpenAI logo" height="20" style="margin-right: 4px;">
    <img src="https://s3.us-west-2.amazonaws.com/cube365-prod/related-content/9b767197-769f-44ea-9b17-9c93606799be.png" alt="OpenAI logo" height="16" style="margin-right: 4px;">
</div>
"""
st.markdown(powered_by, unsafe_allow_html=True)
st.divider()


# Generate image of mischa using Replicate API
def generate_image_mischa(prompt):
    prompt = prompt.replace("Mischa", "TOK").replace("mischa", "TOK")
    print(f"submitted {prompt}")
    output = replicate.run(
        "primodata/misch-ai:0cbdcb85378ed45e55e7a40dd892a029ff0818477f8d105155c322eb8bfe2031",
        input={"prompt": prompt},
    )
    return output[0]


prompt = st.text_input(
    "Generate an image of a cat named 'Mischa' using natural language.",
    help="",
)
with st.expander("Examples:"):
    city = st.button("Mischa in a city.")
    mountain = st.button("Mischa in on a mountain.")

generate_image = st.button("Generate Image")


if generate_image:
    # check if prompt contains 'Mischa'
    if "mischa" not in prompt.lower():
        st.error("'mischa' needs to be in your prompt.")
    else:
        with st.spinner(text="Generating. This could take a minute..."):
            image_url = generate_image_mischa(prompt)
        st.image(image_url)


# Examples
if mountain:
    with st.spinner(text="Generating. This could take a minute..."):
        time.sleep(5)
    st.image(
        "https://pbxt.replicate.delivery/2RephnDLCixkWKyFs5PtgAvw6PL15KfQSuZ2IBBleKfxRhwFB/out-0.png"
    )

if city:
    with st.spinner(text="Generating. This could take a minute..."):
        time.sleep(5)
    st.image(
        "https://pbxt.replicate.delivery/pb4BOopSt7LeaK9ApTBkpcV2cipCW22LEhGMsTTCPqqaREuIA/out-0.png"
    )
