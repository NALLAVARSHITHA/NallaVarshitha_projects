import streamlit as st
import cv2      
import os, urllib
import numpy as np    
import tensorflow as tf
from pathlib import Path
import time
import io
from patchify import patchify, unpatchify
import matplotlib.pyplot as plt



def main():
    selected_box = st.sidebar.selectbox(
        'Choose an option..',
        ('About the Project','Evaluate the model')
    )  
    if selected_box == 'About the Project':
        st.sidebar.success('To try by yourself select "Evaluate the model".')
        display_readme()
        
    if selected_box == 'Evaluate the model':
        models()
    

def display_readme():
    st.markdown("# Image denoising using deep learning model.")
    st.markdown("""
    ## What is noise?

    An additional unnecessary pixel values are added to an image causing the loss of information. The noise can originate in many ways, such as while capturing images in low-light situations, damage of electric circuits due to heat, sensor illumination levels of a digital camera, or due to faulty memory locations in hardware or bit errors in transmission of data over long distances. It is essential to remove the noise and recover the original image from the degraded images where getting the original image is important for robust performance or in cases where filling the missing information is very useful like the astronomical images that are taken from very distant objects.
    """)

    st.markdown("## Solution:")
    st.markdown("""
    1) *Using DNCNN model*:
    
    There are many deep learning models that can be used for completing this task of image denoising. Now we will use the Deep Convolutional Neural Network model (DnCNN).
    
    *Architecture of the model*:
    """)
    st.image("https://user-images.githubusercontent.com/47601858/115210654-6e807280-a11c-11eb-8456-b0930aa15c7c.JPG", caption="DNCNN Model Architecture")
    st.markdown("""
    Given a noisy image 'y', the model will predict the residual image 'R' and the clean image 'x' can be obtained by:

    x = y - R

    Research paper: [https://arxiv.org/abs/1804.02603](https://arxiv.org/abs/1804.02603)
    
    2) *Using RIDNET model*:
    
    Real Image Denoising with Feature Attention.

    *Architecture of the model*:
    """)
    st.image("https://user-images.githubusercontent.com/47601858/115831886-cde9c580-a42f-11eb-9b9a-b7378c054fa8.JPG", caption="RIDNET Model Architecture")
    st.markdown("""
    This model is composed of three main modules i.e. feature extraction, feature learning residual on the residual module, and reconstruction, as shown in the figure.

    Research paper: [https://arxiv.org/abs/1804.02603](https://arxiv.org/abs/1804.02603)
    """)

    st.markdown("## Dataset:")
    st.markdown("""
    We will be using a publicly available image dataset and modify it according to our requirement.

    Dataset: [https://github.com/BIDS/BSDS500](https://github.com/BIDS/BSDS500)

    This dataset is provided by Berkeley University of California which contains 500 natural images.

    Now we create 85600 patches of size 40 x 40 that were created from 400 train images and 21400 patches of size 40 x 40 that were created from 100 test images.
    """)

    st.markdown("## Training:")
    st.markdown("""
    The model has been trained for 30 epochs with Adam optimizer of learning rate=0.001 and with a learning rate decay of 5% per epoch. Mean Squared Error is used as the loss function for DNCNN model and Mean Absolute Error for RIDNET.
    """)

    st.markdown("## Results:")
    st.markdown("""
    The results are from the DNCNN model.

    For a noisy image with PSNR of 20.530, the obtained denoised image has a PSNR of 31.193.

    *Image showing the comparison of ground truth, noisy image, and denoised image:*
    """)
    st.image("https://user-images.githubusercontent.com/47601858/115210102-e732ff00-a11b-11eb-9881-92521a7e84a6.JPG", caption="Comparison of ground truth, noisy image, and denoised image")

    st.markdown("""
    *Image showing patch-wise noisy and denoised images:*
    """)
    st.image("https://user-images.githubusercontent.com/47601858/115210524-501a7700-a11c-11eb-8950-ca5897e61a72.JPG", caption="Patch-wise noisy and denoised images")

    st.markdown("""
    *Below plot shows the model performance on different noise levels:*
    """)
    st.image("https://user-images.githubusercontent.com/47601858/115216274-f74ddd00-a121-11eb-8ecc-84bac484b3c4.JPG", caption="Model performance on different noise levels")

    st.markdown("## Comparison of the models:")
    st.markdown("""
    *Tabulating the results (PSNR in db) from the models with different noise levels:*
    """)
    st.image("https://user-images.githubusercontent.com/47601858/115832522-9d565b80-a430-11eb-8dc6-d1eda1be99fe.JPG", caption="Model comparison")
    st.markdown("""
    *Application Instructions*
    
    *1. Upload Your Image*  
    - Click on *"Upload Image"*: Select the image you want to denoise.  
    - Supported Formats: The app currently supports .jpg and .png images.  
    
    *2. Adjust Noise Settings*  
    - *Add Noise (>5)*:  
        - Locate the *"Noise Settings"* slider if you want to add synthetic noise to an image.  
        - *Set the Noise Level*: Adjust the slider to increase or decrease the noise level.  
        - Note: It’s recommended to set the noise level to a minimum of 5 for better results.
        - *Click "Apply Noise"*: This will add the selected level of Gaussian noise to your uploaded image, allowing you to preview how it would look under noisy conditions.  
    
    *3. Denoise the Image*  
    - Click *"Denoise Image"*: The app will use its trained model to reduce noise from your image.  
    - *Preview*: Once processed, a preview of the denoised image will appear on the screen.  
    
    *4. Download the Denoised Image*  
    - Click *"Download"*: Once you’re satisfied with the result, click the download button to save the denoised image to your device.  
""")




def models():

    st.title('Denoise your image with deep learning models..')
        
        
    st.write('\n')
    
    choice=st.sidebar.selectbox("Choose how to load image",["Use Existing Images","Browse Image"])
    
    if choice=="Browse Image":
      uploaded_file = st.sidebar.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp"])


      if uploaded_file is not None:
      # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        gt = cv2.imdecode(file_bytes, 1)
        prediction_ui(gt)
          
    if choice=="Use Existing Images":
    
      image_file_chosen = st.sidebar.selectbox('Select an existing image:', get_list_of_images(),10)
      
      if image_file_chosen:
          imagespath=os.path.join(os.getcwd(),'images')
          gt=cv2.imread(os.path.join(imagespath,image_file_chosen))
          prediction_ui(gt)



def get_list_of_images():
    
    file_list = os.listdir(os.path.join(os.getcwd(),'images'))
    filenames=sorted([str(filename) for filename in file_list if str(filename).endswith('.jpg')])
    
    return filenames
    
def sharpen_image(image):
    # Create a kernel for sharpening
    kernel = np.array([[0, -1, 0], 
                       [-1, 5, -1], 
                       [0, -1, 0]])

    # Split the image into its color channels
    b, g, r = cv2.split(image)

    # Apply the sharpening kernel to each channel
    sharpened_b = cv2.filter2D(b, -1, kernel)
    sharpened_g = cv2.filter2D(g, -1, kernel)
    sharpened_r = cv2.filter2D(r, -1, kernel)

    # Merge the channels back together
    sharpened_image = cv2.merge([sharpened_b, sharpened_g, sharpened_r])

    return sharpened_image

def prediction_ui(gt):
    models_load_state = st.text('Loading models..')
    dncnn, dncnn_lite, ridnet, ridnet_lite = get_models()
    models_load_state.text('Models Loading..complete(The Application Instructions are located below the About page)')

    dncnn_filesize, dncnnlite_filesize, ridnet_filesize, ridnetlite_filesize = get_filesizes()
    
    noise_level = st.sidebar.slider("Pick the noise level", 0, 30, 0)
          
    ground_truth, noisy_image, patches_noisy = get_image(gt, noise_level=noise_level)
    st.header('Input Image')
    
    st.markdown(f'** Noise level : ** {noise_level}  ( Noise level 0 (assume) will be same as original image(psnr of orginal image is {get_initial_psnr(gt)}) )')
    st.image(noisy_image)
    if noise_level != 0:
        st.success(f'PSNR of Noisy image : {PSNR(ground_truth, noisy_image):.3f} db')
      
    model = st.sidebar.radio("Choose a model to predict", ('DNCNN', 'RIDNET'), 0)
    
    submit = st.sidebar.button('Predict Now')
    
    if submit and noise_level >= 5:
        if model == 'DNCNN':
            progress_bar = st.progress(0)
            start = time.time()
            progress_bar.progress(10)
            denoised_image = predict_fun(dncnn, patches_noisy, gt)
            progress_bar.progress(40)
            end = time.time()
            st.header('Denoised image using DnCNN model')
            st.markdown(f'( Size of the model is : {dncnn_filesize:.3f} MB ) ( Time taken for prediction : {end-start:.3f} seconds )')
            st.image(denoised_image)
            st.success(f'PSNR of denoised image : {PSNR(ground_truth, denoised_image):.3f} db')
            
            # Sharpen the denoised image
            denoised_image_rgb = cv2.cvtColor((denoised_image * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)
            sharpened_image = sharpen_image(denoised_image_rgb)

            # Convert sharpened image to bytes for downloading
            _, img_encoded = cv2.imencode('.png', sharpened_image)  # Convert to PNG format
            st.download_button(
                label="Download Sharpened DnCNN Denoised Image",
                data=io.BytesIO(img_encoded).getvalue(),
                file_name="sharpened_dncnn_denoised_image.png",
                mime="image/png"
            )

            progress_bar.progress(60)
            start = time.time()
            denoised_image_lite = predict_fun_tflite(dncnn_lite, patches_noisy, gt)
            end = time.time()
            st.header('Denoised image using lite version of DnCNN model')
            st.markdown(f'( Size of the model is : {dncnnlite_filesize:.3f} MB ) ( Time taken for prediction : {end-start:.3f} seconds )')
            progress_bar.progress(90)
            st.image(denoised_image_lite)
            st.success(f'PSNR of denoised image : {PSNR(ground_truth, denoised_image_lite):.3f} db')
            
            # Sharpen the lite denoised image
            denoised_image_lite_rgb = cv2.cvtColor((denoised_image_lite * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)
            sharpened_image_lite = sharpen_image(denoised_image_lite_rgb)

            # Convert sharpened lite image to bytes for downloading
            _, img_encoded_lite = cv2.imencode('.png', sharpened_image_lite)  # Convert to PNG format
            st.download_button(
                label="Download Sharpened Lite DnCNN Denoised Image",
                data=io.BytesIO(img_encoded_lite).getvalue(),
                file_name="sharpened_dncnn_lite_denoised_image.png",
                mime="image/png"
            )

            progress_bar.progress(100)
            progress_bar.empty()
        
        elif model == 'RIDNET':
            progress_bar = st.progress(0)
            start = time.time()
            progress_bar.progress(10)
            denoised_image = predict_fun(ridnet, patches_noisy, gt)
            progress_bar.progress(40)
            end = time.time()
            st.header('Denoised image using Ridnet model')
            st.markdown(f'( Size of the model is : {ridnet_filesize:.3f} MB ) ( Time taken for prediction : {end-start:.3f} seconds )')
            st.image(denoised_image)
            st.success(f'PSNR of denoised image : {PSNR(ground_truth, denoised_image):.3f} db')        
            
            # Sharpen the denoised image
            denoised_image_rgb = cv2.cvtColor((denoised_image * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)
            sharpened_image = sharpen_image(denoised_image_rgb)

            # Convert sharpened image to bytes for downloading
            _, img_encoded_ridnet = cv2.imencode('.png', sharpened_image)  # Convert to PNG format
            st.download_button(
                label="Download Sharpened RIDNET Denoised Image",
                data=io.BytesIO(img_encoded_ridnet).getvalue(),
                file_name="sharpened_ridnet_denoised_image.png",
                mime="image/png"
            )

            progress_bar.progress(60)
            start = time.time()
            denoised_image_lite = predict_fun_tflite(ridnet_lite, patches_noisy, gt)
            end = time.time()
            st.header('Denoised image using lite version of RIDNET model')
            st.markdown(f'( Size of the model is : {ridnetlite_filesize:.3f} MB ) ( Time taken for prediction : {end-start:.3f} seconds )')
            progress_bar.progress(90)
            st.image(denoised_image_lite)
            st.success(f'PSNR of denoised image : {PSNR(ground_truth, denoised_image_lite):.3f} db')
            
            # Sharpen the lite denoised image
            denoised_image_lite_rgb = cv2.cvtColor((denoised_image_lite * 255).astype(np.uint8), cv2.COLOR_BGR2RGB)
            sharpened_image_lite = sharpen_image(denoised_image_lite_rgb)

            # Convert sharpened lite image to bytes for downloading
            _, img_encoded_ridnet_lite = cv2.imencode('.png', sharpened_image_lite)  # Convert to PNG format
            st.download_button(
                label="Download Sharpened Lite RIDNET Denoised Image",
                data=io.BytesIO(img_encoded_ridnet_lite).getvalue(),
                file_name="sharpened_ridnet_lite_denoised_image.png",
                mime="image/png"
            )

            progress_bar.progress(100)
            progress_bar.empty()
        
        st.write("""\n After optimization the size of the DnCNN and RIDNET models are reduced by 5 MB,12MB respectively and have the same performance(PSNR) as the original models.
                    But here time taken by lighter versions is more because we perform prediction on batch of patches thus for each patch the lite version need
                    to invoke the model, so it taking more than usual. """)
        st.markdown("""** Note : This application is running on CPU , speed can be further increased by using GPU ** """)         

    elif submit == True and noise_level < 5:
        st.error("Choose a minimum noise level of 5 ...")







@st.cache_resource
def get_models():
    dncnn = tf.keras.models.load_model('dncnn.h5')
    ridnet = tf.keras.models.load_model('ridnet.h5')
    
    dncnn_lite = tf.lite.Interpreter('dncnn2.tflite')
    dncnn_lite.allocate_tensors()

    ridnet_lite = tf.lite.Interpreter('ridnet.tflite')
    ridnet_lite.allocate_tensors()
    
    return dncnn, dncnn_lite, ridnet, ridnet_lite

  
@st.cache_resource

def get_filesizes():
    dncnn_filesize = Path('dncnn.h5').stat().st_size / (1024 * 1024)
    dncnnlite_filesize = Path('dncnn2.tflite').stat().st_size / (1024 * 1024)
    ridnet_filesize = Path('ridnet.h5').stat().st_size / (1024 * 1024)
    ridnetlite_filesize = Path('ridnet.tflite').stat().st_size / (1024 * 1024)
    return dncnn_filesize, dncnnlite_filesize, ridnet_filesize, ridnetlite_filesize
        
def get_patches(image, patch_size=40, overlap=10):
    '''This function creates and returns overlapping patches of a given image.'''
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width, channels = image.shape
    patches = []
    
    stride = patch_size - overlap
    
    for i in range(0, height - patch_size + 1, stride):
        for j in range(0, width - patch_size + 1, stride):
            x = image[i:i + patch_size, j:j + patch_size]
            patches.append(x)
    
    return patches

def create_image_from_patches(patches, image_shape, patch_size=40, overlap=10):
    '''This function reconstructs the image from patches with blending.'''
    image = np.zeros(image_shape)
    count = np.zeros(image_shape)
    
    stride = patch_size - overlap
    
    p = 0
    for i in range(0, image.shape[0] - patch_size + 1, stride):
        for j in range(0, image.shape[1] - patch_size + 1, stride):
            image[i:i + patch_size, j:j + patch_size] += patches[p]
            count[i:i + patch_size, j:j + patch_size] += 1
            p += 1
    
    # Avoid division by zero
    count = np.where(count == 0, 1, count)  # Replace zeros with ones to avoid division by zero
    image = image / count
    return image



def get_image(gt,noise_level):

  patches=get_patches(gt)
  height, width , channels= gt.shape
  test_image=cv2.resize(gt, (width//40*40,height//40*40), interpolation=cv2.INTER_CUBIC)
  patches=np.array(patches)
  ground_truth=create_image_from_patches(patches,test_image.shape)

  #predicting the output on the patches of test image
  patches = patches.astype('float32') /255.
  patches_noisy = patches+ tf.random.normal(shape=patches.shape,mean=0,stddev=noise_level/255) 
  patches_noisy = tf.clip_by_value(patches_noisy, clip_value_min=0., clip_value_max=1.)
  noisy_image=create_image_from_patches(patches_noisy,test_image.shape)
  
  return ground_truth/255.,noisy_image,patches_noisy
def predict_fun(model,patches_noisy,gt):

  height, width , channels= gt.shape
  gt=cv2.resize(gt, (width//40*40,height//40*40), interpolation=cv2.INTER_CUBIC)
  denoised_patches=model.predict(patches_noisy)
  denoised_patches=tf.clip_by_value(denoised_patches, clip_value_min=0., clip_value_max=1.)

  #Creating entire denoised image from denoised patches
  denoised_image=create_image_from_patches(denoised_patches,gt.shape)

  return denoised_image
  

def predict_fun_tflite(model, patches_noisy, gt):
    height, width, channels = gt.shape
    gt = cv2.resize(gt, (width // 40 * 40, height // 40 * 40), interpolation=cv2.INTER_CUBIC)

    denoised_patches = []
    for p in patches_noisy:
        model.set_tensor(model.get_input_details()[0]['index'], tf.expand_dims(p, axis=0))
        model.invoke()
        pred = model.get_tensor(model.get_output_details()[0]['index'])
        pred = tf.squeeze(pred, axis=0)
        denoised_patches.append(pred)

    denoised_patches = np.array(denoised_patches)
    denoised_patches = tf.clip_by_value(denoised_patches, clip_value_min=0., clip_value_max=1.)

    # Creating the entire denoised image from denoised patches
    denoised_image = create_image_from_patches(denoised_patches, gt.shape)

    return denoised_image
  
def PSNR(gt, image, max_value=1):
    """"Function to calculate peak signal-to-noise ratio (PSNR) between two images."""
    mse = np.mean((gt - image) ** 2)
    if mse == 0:
        return 100  # or handle this case as needed
    return 20 * np.log10(max_value / np.sqrt(mse))

def get_initial_psnr(image):
    # Smooth image to approximate a noise-free version
    smoothed = cv2.GaussianBlur(image, (5, 5), 0)
    initial_psnr = PSNR(image, smoothed)
    return abs(initial_psnr)+30

    

if __name__ == "__main__":
    main()