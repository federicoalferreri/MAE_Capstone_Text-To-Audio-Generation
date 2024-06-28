# Text-to-Audio Generation: a comparative analysis for perceptual performance evaluation 
The following study was conducted within the context of the 'Music and Acoustic Engineering Capstone' course of MSc. in _Music and Acoustic Engineering @ Politecnico di Milano_ (a.y. 2023/2024) held by professor Alberto Bernardini. The paper presenting the study can be found [here](assets/MAE_Capstone_28june.pdf).

Authors:

- [Emma Coletta](https://github.com/emmaclt)
- [Federico Ferreri](https://github.com/federicoalferreri)
- [Lorenzo Previati](https://github.com/LorenzoPreviati22)


### Abstract
Advancements in the field of Artificial Intelligence Generated Content (AIGC) have led to the development of sophisticated Text-to-Audio (TTA) models. These models synthesize audio from textual descriptions, with potential applications ranging from video game sound effects to acoustic scene setting in movies. This study presents a comparative analysis of five TTA models: [AudioGen](https://arxiv.org/pdf/2209.15352), [AudioLDM](https://arxiv.org/pdf/2301.12503) (in two versions: '_m-full_' and '_l-full_'), and [AudioLDM2](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10530074&casa_token=hya2XRcl9OkAAAAA:ChBk4vUXM8uwiXZHJFXsqWWeI4Zl3r3V5iWA-4k7X1bZ4E6E3J1XtLg9JHl8nkFtegu6f2JB8w&tag=1) (in two versions: base and '_large_'). We evaluated these models using both objective and subjective methods. Objective evaluation involved calculating FAD scores with embeddings extracted using both the VGGish and CLAP models to measure alignment with input text and audio quality of the generated audio datasets. Subjective evaluation was conducted via a [web-based MUSHRA listening test](https://github.com/audiolabs/webMUSHRA/tree/master) administered to participants of varied ages and musical backgrounds. Our findings emphasize strengths and limitations of each generative model and of the proposed automatic perceptual evaluation, revealing its inaccuracy in assessing TTA models whose training datasets do not include the one used to compute the [FAD](https://arxiv.org/pdf/1812.08466) score. This study contributes to the field by providing insights into the accuracy of current automatic quality assessment methods for TTA models. 


## Table of Contents
- [Abstract](#abstract)
- [GitHub page content](#project-implementation)
- [How to replicate the experiment](#how-to-replicate)

## Project Implementation

In this section, we list all the code implementations used to conduct the study. 

- **[Generative prompts selection script](codes_for_the_captions_selection)**: to obtain the descriptive prompts needed for audio clips generation and so model evaluation, we implemented an algorithm to select one descriptive caption out of the five originally provided for each audio sample by the [Clotho](https://zenodo.org/records/3490684) 'evaluation' dataset based on how frequently each word appeared across all captions included in the original dataset. This method ensured that the selected captions provided the most specific and detailed descriptions possible, which is critical for generating accurate and contextually relevant audio samples. The folder also provides the [captions.xlsx](codes_for_the_captions_selection/captions.xlsx) file featuring captions later used to generate the audio samples used by us to conduct this experiment. 
- **Text-To-Audio Generative Models**: the audio generative process was implemented using the models mentioned above and their setup was based on each model’s default settings. All generated audio clips were set to be 10 seconds long. The notebooks for each model are available and ready to use, after importing the desired input dataset, at the following links: [AudioGen](audiogen_kaggle.ipynb), [AudioLDM](audio_ldm_kaggle.ipynb), [AudioLDM2](audio_ldm2_kaggle.ipynb).
- **[FAD Computation](fad_google_colab.ipynb)**: objective evaluation for quality assessment of the analyzed models was performed computing FAD scores of each model with embeddings extracted from both the VGGish and CLAP models. The notebook used for FAD computation is based on the toolkit provided [here](https://github.com/gudgud96/frechet-audio-distance.git). To compute the FAD using CLAP embeddings, a resampling of the genereated audios was necessary: [here](codes_audio_modification_for_subjective_and_fad_clap_evaluation/resampling.ipynb) the script used to perform the upsampling of audio clips from 16kHZ to 48kHz.
- **web-based MUSHRA listening test**: to obtain subjective perceptual evaluations of the models, we administered a listening test to participants of various ages and musical backgrounds by conducting a web-based MUSHRA listening test, momentarily available [here](https://text-to-audio-subjectivetest.000webhostapp.com). The _configs_ folder to replicate the test to your liking can be found [at this page](mushra_configs_folder/configs). Participants were asked to assess audio-text alignment and audio quality of samples selected with the following [script](codes_for_the_captions_selection/code_captions_selection_for_subjective_test/extract_captions_for_category.py) so that their generative caption described acoustic events from different categories and typical of diverse environments and everyday activities.

## How to replicate

