from io import BytesIO
from pathlib import Path
from random import randint

import cv2
import httpx
import numpy as np
import streamlit as st
from PIL import Image

PROCESSED_SIZE = (416, 416)


@st.experimental_singleton
def load_model():
    """
    Will use config and weights to initialize model in Python
    """
    class_names = Path("coco.names").read_text().split("\n")
    colors = [(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in class_names]
    model = cv2.dnn_DetectionModel("yolov4-tiny.cfg", "yolov4-tiny.weights")
    model.setInputParams(size=PROCESSED_SIZE, scale=1 / 255, swapRB=True)
    return model, class_names, colors


@st.experimental_memo
def process_image(raw_image):
    """
    Given an image, makes a copy and performs some processing on it.
    Returns the copy

    Args:
        raw_image (np.ndarray): Image as numpy array

    Returns:
        np.ndarray: Image with YOLO detection boxes painted on
    """
    model, class_names, colors = load_model()
    image = cv2.resize(raw_image, dsize=PROCESSED_SIZE, interpolation=cv2.INTER_AREA)

    classes, scores, boxes = model.detect(image, 0.25, 0.5)
    for classid, score, box in zip(classes, scores, boxes):
        color = colors[classid]
        label = f"{class_names[classid]} : {score:.5f}"
        x, y, width, height = box
        cv2.rectangle(image, (x, y), (x + width, y + height), color, 2)
        cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)

    return image


@st.experimental_memo
def fetch_image_from_url(image_url):
    """
    Tries to return the bytes from a given url.
    Prints any exception and returns None if so. Might interact poorly with memo

    Args:
        image_url (str): URL of the image to be loaded with PIL

    Returns:
        bytes: Raw http response body content
    """
    try:
        image_response = httpx.get(image_url)
    except Exception as e:
        print(e)
        return None
    return image_response.content


st.title("{{ cookiecutter.project_name }}")

use_link = "Fetch an image by URL"
use_upload = "Upload an Image"
use_camera = "Use Camera to take a Photo"
image_method = st.selectbox("How to select Image", [use_link, use_upload, use_camera])

if image_method == use_link:
    image_url = st.text_input(
        "Image URL 🔗",
        "https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/dog.jpg",
    )
    image_bytes = fetch_image_from_url(image_url)
    if image_bytes is None:
        st.error(f"Could not fetch image from '{image_url}' 😓")
        st.stop()
    image_file = BytesIO(image_bytes)
elif image_method == use_upload:
    image_file = st.file_uploader(
        "Upload Image File 🌄", ["png", "jpg", "jpeg"], accept_multiple_files=False
    )
elif image_method == use_camera:
    image_file = st.camera_input("Take a Photo 📸")

if image_file is None:
    st.info("Select an Image to proceed")
    st.stop()

try:
    image = Image.open(image_file)
except Exception:
    st.error("Error: Invalid image")
    st.stop()

with st.expander("Raw Image"):
    st.image(image)

painted_image = process_image(np.asarray(image))
st.image(painted_image)
