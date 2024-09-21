import json
import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_lottie import st_lottie
import requests
import base64
from streamlit_option_menu import option_menu
from openai import OpenAI

# Webpage Name
st.set_page_config(page_title="AI Interior Design Assistant", layout="wide")

#--------------------Define Global Function--------------------------
#Lottie Animation-------------------
def load_lottie_link(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

def load_lottie_local(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

#Define Base64 for Image Encode------------------
def base64_image(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#----------------------Define Global Image -----------------------------
# For Home Page Cover Image -----------------------------------------
img_cover_path = r'Image/SubLogan.jpg' 
img_cover= base64_image(img_cover_path)

#For Gallery ----------------------------------------
image1_path=r'Image/1.jpg'
image1=base64_image(image1_path)

image2_path=r'Image/2.jpg'
image2=base64_image(image2_path)

image3_path=r'Image/3.jpg'
image3=base64_image(image3_path)

image4_path=r'Image/4.jpg'
image4=base64_image(image4_path)

image5_path=r'Image/5.jpg'
image5=base64_image(image5_path)

image6_path=r'Image/6.jpg'
image6=base64_image(image6_path)

image7_path=r'Image/7.jpg'
image7=base64_image(image7_path)

image8_path=r'Image/8.jpg'
image8=base64_image(image8_path)

image9_path=r'Image/9.jpg'
image9=base64_image(image9_path)

image10_path=r'Image/10.jpg'
image10=base64_image(image10_path)

image11_path=r'Image/11.jpg'
image11=base64_image(image11_path)

image12_path=r'Image/12.jpg'
image12=base64_image(image12_path)

image13_path=r'Image/13.jpg'
image13=base64_image(image13_path)

#----------------------SideBar (Global) --------------------------
with st.sidebar:
    sidebar_option=option_menu(
        menu_title='Main Page',
        options=["Home","Gallery","Design"])            

#----------------Side Bar for Home Page -------------------------
# ----------------------------Whole Home Page Section--------------------
if sidebar_option=="Home":
    # -------------------------------Top Section (Home Page)-------------------------------
    # Call defined Lottie Function
    lottie_json = 'Home_AN.json'
    lottie_run = load_lottie_local(lottie_json)

    # Create two-column layout for Title and Animation
    col1, col2 = st.columns([2.8, 2.2])  # Column 1 takes 3/4 of the width, column 2 takes 1/4

    # Left column: Title and Description
    with col1:
        st.markdown(
            """
            <div style="text-align: left; margin-left: 50px; margin-top:130px;">
                <h1 style="font-size: 5.5rem; font-weight: 700;">Great Interior Designs <br> With Generative AI!</h1>
                <p style="font-size: 2rem; color: #666666; text-align:left">
                    Create your dream house with Generative AI, tailored to your vision and budget.
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # Right column: Lottie Animation with CSS positioning to move it up
    with col2:
        # Use CSS to adjust the position of the Lottie animation
        st.markdown(
            """
            <div style="text-align: right; margin-right: 0px; margin-top:-10px;">
            """,
            unsafe_allow_html=True
        )

        # Embed the Lottie animation
        st_lottie(
            lottie_run,
            speed=1,
            reverse=True,
            loop=True,
            quality='High',
            height=700,  # Adjust height
            width=700,   # Adjust width
            key=None
        )
        # Close the div
        st.markdown("</div>", unsafe_allow_html=True)

    #------------------------Sub SLogan (Home Page)-------------------------
    st.markdown(f"""
        <div style="background-image: url('data:image/jpg;base64,{img_cover}'); 
                    background-size: cover; 
                    padding: 100px; 
                    border-radius: 0px;
                    background-position: 0px 650px; 
                    width: 110%; 
                    margin-left: -79px; 
                    margin-right: 0px; 
                    text-align: center;
                    opacity: 0.85;
                    background-color: rgba(0, 0, 0, 0.7);
                    background-blend-mode: darken;">
            <h3 style="
                font-size: 3rem; 
                font-weight: bold; 
                color: white;">
                Share Your Thought with Us, and Let Our Advanced Generative AI Design The Home Of Your Dreams!
            </h3>
        </div>
        """, unsafe_allow_html=True)

    #-----------------Bottom Section (Home Page)-------------
    #Title -------------------------------------
    st.markdown("""
        <div style="padding: 0px; text-align: center; margin-left: 15px">
            <h2 style="
                text-align: center; 
                margin-top: 100px; 
                font-weight: 1000;
                font-size: 3rem; 
                color: black;
                text-transform: uppercase;
            ">
            Feel Free To Look at Some of Our Prior Works!
            </h2>
        </div>
        """, unsafe_allow_html=True)

    # Gallery (Home Page Section) --------------------------------------
    #Define CSS For Gallery--------------------------
    st.markdown("""
        <style>
        .slider {
            height: 300px;
            margin: auto;
            position: relative;
            width: 100%;
            display:grid;
            place-items:center;
            overflow:hidden;
        }
        .slider-track{
            display:flex;
            width:calc(250px * 18);
            animation: scroll 35s linear infinite;
        }
        .slider-track:hover{
            animation-play-state:paused;
        }
        
        @keyframes scroll{
        0%{
            transform: translateX(0);
        }
        100%{
            transform: translateX(calc(-250px*11));
        }
        }
        .slide{
            height: 350px;
            width: 350px;
            display: flex;
            align-items:center;
            padding:15px;
            perspective: 100px;
        }
        img{
            width: 550px;
            transition:transform 1s;
        }
        img:hover{
            transform:translateZ(15px);
        }
        .slider::before,
        .slider::after {
            background: linear-gradient(to right, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0) 100%);
            content: '';
            height: 100%;
            position: absolute;
            width: 15%;
            z-index: 2;
        }
        .slider::before {
        left: 0;
        top: 0;
        }
        .slider::after {
        right: 0;
        top: 0;
        transform :rotateZ(180deg);
        </style>
        """, unsafe_allow_html=True)

    # Display Gallery (With Scroll) ---------------------------------
    st.markdown(f"""
        <div class="slider">
            <div class="slider-track">
                <div class="slide">
                    <img src="data:image/jpg;base64,{img_cover}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image1}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image2}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image3}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image4}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image5}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image6}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image7}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image8}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image9}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image10}">
                </div>
                <div class="slide">
                    <img src="data:image/jpg;base64,{image11}">
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------Gallery Page (Whole Section for Gallery ---------------------------)
elif sidebar_option=="Gallery":
    st.title("A Glimpse into Our Past Creations")
    #---------Display Gallery---------------------------
    #Setup CSS For Gallery ---------------------------
    st.markdown("""
                <style>
                .container{
                    display:grid;
                    grid-template-columns: repeat(6,1fr);
                    grid-auto-rows:100px 300px;
                    grid-gap:10px;
                    grid-auto-flow: dense;
                }

                .gallery-item{
                    width:100%;
                    height:100%;
                    position:relative;
                }

                .gallery-item .image{
                    width:100%;
                    height:100%;
                    overflow:hidden;
                }

                .gallery-item .image img{
                    width:100%;
                    height:100%;
                    object-fit: cover;
                    object-position:50% 50%;
                    cursor:pointer;
                    transition:.5s ease-in-out;
                }
                .gallery-item:hover .image img{
                    transform:scale(1.5);
                }

                .gallery-item .text{
                    opacity:0;
                    position:absolute;
                    top:50%;
                    left:50%;
                    transform:translate(-50%,-50%);
                    color:#fff;
                    font-size:25px;
                    pointer-events:none;
                    z-index:4;
                    transition: .3s ease-in-out;
                    -webkit-backdrop-filter: blur(5px) saturate(1.8);
                    backdrop-filter: blur(5px) saturate(1.8);
                }

                .gallery-item:hover .text{
                    opacity:1;
                    animation: move-down .3s linear;
                    padding:1em;
                    width:100%;
                }

                .w-1{
                    grid-column: span 1;
                }
                .w-2{
                    grid-column: span 2;
                }
                .w-3{
                    grid-column: span 3;
                }
                .w-4{
                    grid-column: span 4;
                }
                .w-5{
                    grid-column: span 5;
                }
                .w-6{
                    grid-column: span 6;
                }

                .h-1{
                    grid-row: span 1;
                }
                .h-2{
                    grid-row: span 2;
                }
                .h-3{
                    grid-row: span 3;
                }
                .h-4{
                    grid-row: span 4;
                }
                .h-5{
                    grid-row: span 5;
                }
                .h-6{
                    grid-row: span 6;
                }
    
                @media screen and (max-width:500px){
                    .container{
                        grid-template-columns: repeat(1,1fr);
                    }
                    .w-1,.w-2,.w-3,.w-4,.w-5,.w-6{
                        grid-column:span 1;
                    }
                }

                @keyframes move-down{
                    0%{
                        top:10%;
                    }
                    50%{
                        top:35%;
                    }
                    100%{
                        top:50%;
                    }
                } 
                </style>
                """,unsafe_allow_html=True)

    st.markdown(f"""
        <div class="container" id="main-gallery">
            <div class="gallery-container w-4 h-3">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{img_cover}" alt="Casual Style">
                    </div>
                    <div class="text">Casual Style</div>
                </div>
            </div>
            <div class="gallery-container w-3 h-5">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image1}" alt="Modern Style">
                    </div>
                    <div class="text">Modern Style</div>
                </div>
            </div>
            <div class="gallery-container w-2 h-3">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image2}" alt="Country Style">
                    </div>
                    <div class="text">Country Style</div>
                </div>
            </div>
            <div class="gallery-container w-3 h-3">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image3}" alt="Futuristic Style">
                    </div>
                    <div class="text">Futuristic Style</div>
                </div>
            </div>
            <div class="gallery-container w-3 h-2">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image4}" alt="Playful Style">
                    </div>
                    <div class="text">Playful Style</div>
                </div>
            </div>
            <div class="gallery-container w-4 h-2">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image5}" alt="Chinese Style">
                    </div>
                    <div class="text">Chinese Style</div>
                </div>
            </div>
            <div class="gallery-container w-2 h-3">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image6}" alt="Natural Style">
                    </div>
                    <div class="text">Natural Style</div>
                </div>
            </div>
            <div class="gallery-container w-4 h-2">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image7}" alt="Middle East Style">
                    </div>
                    <div class="text">Middle East Style</div>
                </div>
            </div>
            <div class="gallery-container w-2 h-2">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image8}" alt="Minimalist Style">
                    </div>
                    <div class="text">Minimalist Style</div>
                </div>
            </div>
            <div class="gallery-container w-2 h-3">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image9}" alt="Dark Tone Style">
                    </div>
                    <div class="text">Dark Tone Style</div>
                </div>
            </div>
            <div class="gallery-container w-2 h-3">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image10}" alt="Homey Style">
                    </div>
                    <div class="text">Homey Style</div>
                </div>
            </div>
            <div class="gallery-container w-2 h-4">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image11}" alt="Luxurious Style">
                    </div>
                    <div class="text">Luxurious Style</div>
                </div>
            </div>
             <div class="gallery-container w-4 h-2">
                <div class="gallery-item">
                    <div class="image">
                    <img src="data:image/jpg;base64,{image12}" alt="Fancy Style">
                    </div>
                    <div class="text">Fancy Style</div>
                </div>
            </div>
        </div>
                """, unsafe_allow_html=True)
    
#----------------Side Bar for Design Page -------------------------
elif sidebar_option=="Design":        
    #-------------------Define AI behavior First----------------------------
    
    client= OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    
    #----------------------------Main Behavior-------------------------Most Important--------------------------
    def for_content(prompt):
        response= client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role':'system','content':f"""
            You are a renowned interior designer, famous for your ability to work within strict budgets, helping people manage their financial limitations while achieving a comfortable and stylish home. 
            Your expertise lies solely in interior design, so you kindly refrain from answering questions unrelated to your field. If someone asks about topics outside of design or home aesthetics, you will politely decline, as they fall outside your area of expertise.
            Besides that, since you have also working with an AI Image Generator, since you are bad in painting, hence you will describe how your thing arrange, how the furniture look like, how the layout look like for AI Image Generator to paint.
            
            After designing the room, you will create a budget list on how these budget spent to your user. 
            
            As as a professional, here is how your standard for different budget:
            Budget below RM9000, return "Budget Too Low, Cant fulfil request"  in Section 2.
            Budget between RM10000-RM20000, the design only give chair and table.
            Budget Between RM20000-30000, can add on a little wall painting.  
            Budget between RM30000-40000, add on a little decor.
            Budget between RM40000-50000, design become more expensive. 
            Budget above RM60000, estimate yourself based on previous criteria.
            
            Before diving into design ideas, you need to confirm which part of the home the user wants to renovate, such as the kitchen, living room, etc. 
            You must also confirm their budget. For example, with a budget between RM10,000 and RM20,000 for a living room. 
            You will have to aware customer if they failed to provide both space ans budget together. 
            
            In your response, there should be 2 sections. 
            Section 1. Budget Allocation.
            Section 2. A details Description for AI Image Generator but without mention it is for AI Image Generator 
            
            keep the Section 2 simple, so that the AI Image Generator can understand what you want do. Only describe wha you have in budget list, in section 2, didn't say anything that not mentioned in the budget list, please strictly this rule. 
            
            Important to know that: 
            If the user didn't provide both information for both budget and space waiting renovation, return "Lost Information" in Section 2. 
            
            And as a professional, you would only need budget and space that need renovation, then you can start to work, because it would look unprofessional if you ask additional questions.
 
            """},
            {'role':'user','content':prompt}
        ],
        max_tokens=10000)
        return response.choices[0].message.content
    
    #------------------Display Only Budget--------------------------
    def for_budget(prompt):
        response= client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role':'system','content':f"""
            You are a courier responsible for transferring budget list information. 
            The user may provide a very long paragraph, but your task is to pick up the budget list and show it in a separate paragraph without changing anything. 
            Only the budget list should be displayed as your only responsibility.
            """},
            {'role':'user','content':prompt}
        ],
        max_tokens=10000)
        return response.choices[0].message.content
    
    #------------------Display Only Description for AI--------------------------
    def for_AI(prompt):
        response= client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role':'system','content':f"""
            You are a courier responsible for transferring details description information that will transmit to AI Image Generator. 
            The user may provide a very long paragraph, but your task is only pick up the "Details Description" part and feed it into an AI Image Generator without changing anything. 
            
            But, if the message sent to you is 'Lost Information', then you have to imaging A comic girl genuinely awkward smile and request information from user and say lack of information with dialogue bubble in the image.
            Besides that, if the message sent to you is "Budget Too Low, Cant fulfil request" then you have to imaging A comic girl genuinely awkward smile and say cannot fulfil the requirement with dialogue bubble in the image.
            """},
            {'role':'user','content':prompt}
        ],
        max_tokens=10000)
        return response.choices[0].message.content
    
     #------------------AI Image Generator--------------------------
    def design_art(prompt):
        response= client.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        )
        return response.data[0].url
    
    # --------------------------Start Code Design Page-------------------------------
    #--------------------- Define Background CSS------------------------------------
    st.markdown(f"""
                <style>
                .stApp {{
                    background-image: url('data:image/jpeg;base64,{image12}');
                    background-size: cover;
                    background-position: center;
                    opacity:0.8;
                }}
                .stApp::before {{
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background-color: rgba(255, 255, 255, 0.8); /* 50% black overlay */
                z-index: 0;
                }}
                .content {{
                position: relative;
                z-index: 1;
                }}
                </style>
                """, unsafe_allow_html=True)
    
    #-----------------Title----------------------------
    #----------------Define CSS---------------------------
    st.markdown ("""
                <style>
                 .content{
                width: 100%;
                position: absolute;
                top: 45%;
                transform: translateY(-50%);
                text-align: center;
                }
                .content h1{
                margin-top: 80px;
                font-size: 60px;
                font-weight: 800;
                position: center;
                color: black;
                }
                .content p
                {
                font-size: 1.3em;
                color: black;
                position: center;
                font-weight: 400;
                max-width: 1000px;
                margin: 0 auto;
                margin-top: 10 px;
                text-transform: uppercase; 
                }
                </style>
                """, unsafe_allow_html=True)
    
    #----------Display Title-----------
    st.markdown("""
                <div class="content">
                    <h1>PLEASE SHARE YOUR THOUGHTS WITH US!</h1>
                    <p>Provide Your Budget, Space waiting renovated!</p>
                </div>
                """,unsafe_allow_html=True)
    
    #-------------Input Bar--------------
    
    st.divider ()
    st.divider()
    
    prompt=st.text_input("-", placeholder="exp: I have RM30000 and want to renovate my bedroom with casual style.....")
    
    if st.button('Generate Design'):
        main_content=for_content(prompt)
        transfer_Art=for_AI(main_content)
        budget=for_budget(main_content)
        AI_Art = design_art(transfer_Art)
    
        col_1, col_2, col_3 = st.columns([4,2,3]) 
        
        with col_1:
            st.image(AI_Art)
            
        with col_2:
            st.write(budget)
            
        with col_3:
            st.write(transfer_Art)