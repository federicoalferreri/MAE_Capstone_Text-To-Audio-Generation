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
- **Text-To-Audio Generative Models**: the audio generative process was implemented using the models mentioned above and their setup was based on each model’s default settings. All generated audio clips were set to be 10 seconds long. The notebooks for each model are available and ready to use, after importing the desired input dataset. You can find more detailed information about their usage and settings at each model demo page: [AudioGen-demo](https://github.com/facebookresearch/audiocraft/blob/main/demos/audiogen_demo.ipynb), [AudioLDM-demo and AudioLDM2-demo](https://colab.research.google.com/github/sanchit-gandhi/notebooks/blob/main/AudioLDM-2.ipynb#scrollTo=111ebd91-f261-488c-b3f5-371f4eea2423)
- **[FAD Computation](fad_google_colab.ipynb)**: objective evaluation for quality assessment of the analyzed models was performed computing FAD scores of each model with embeddings extracted from both the VGGish and CLAP models. The notebook used for FAD computation is based on the toolkit provided [here](https://github.com/gudgud96/frechet-audio-distance.git). To compute the FAD using CLAP embeddings, a resampling of the genereated audios was necessary: [here](codes_audio_modification_for_subjective_and_fad_clap_evaluation/resampling.ipynb) the script used to perform the upsampling of audio clips from 16kHZ to 48kHz.
- **web-based MUSHRA listening test**: to obtain subjective perceptual evaluations of the models, we administered a listening test to participants of various ages and musical backgrounds by conducting a web-based MUSHRA listening test, momentarily available [here](https://text-to-audio-subjectivetest.000webhostapp.com). The _configs_ folder to replicate the test to your liking can be found [at this page](mushra_configs_folder/configs). Participants were asked to assess audio-text alignment and audio quality of samples selected with the following [script](codes_for_the_captions_selection/code_captions_selection_for_subjective_test/extract_captions_for_category.py) so that their generative caption described acoustic events from different categories and typical of diverse environments and everyday activities.

## How to replicate

### Captions Selection
To select the captions from the Clotho dataset according to the criteria explained in the paper, you must first run the Python script [freq_words.py](codes_for_the_captions_selection/words_frequencies/freq_words.py), providing the correct path to the file containing all the captions of the Clotho evaluation dataset, named [clotho_captions_evaluation.xlsx](codes_for_the_captions_selection/clotho_captions_evaluation.xlsx). This script generates the file [word_freq.xlsx](codes_for_the_captions_selection/words_frequencies/word_freq.xlsx), which contains the number of occurrences of each word present in the captions.
Next, run the script [select_captions.py](codes_for_the_captions_selection/select_captions.py) to obtain the file containing all the selected captions for their respective audio files. Ensure you modify the paths for the file containing the word frequencies (in our case, [word_freq_final.xlsx](codes_for_the_captions_selection/words_frequencies/word_freq_final.xlsx) was used, which excludes superfluous words) and [clotho_captions_evaluation.xlsx](codes_for_the_captions_selection/clotho_captions_evaluation.xlsx). Once the file named '_captions.xlsx_' is obtained, the captions will be used to generate the audio using different generative models.


### Audio Samples Generation
The notebooks for generating the audio using the generative models were executed on Kaggle using GPU to speed up the computation. To run the notebooks, upload the captions.xlsx file to Kaggle. To use the models Audiogen, AudioLDM, and AudioLDM2, you must use the scripts [audiogen_kaggle.ipynb](audiogen_kaggle.ipynb), [audio_ldm_kaggle.ipynb](audio_ldm_kaggle.ipynb), and [audio_ldm2_kaggle.ipynb](audio_ldm2_kaggle.ipynb) respectively, and modify the path for the captions file, `captions.xlsx`. To use different models for AudioLDM and AudioLDM2, change the model name within the code. For AudioLDM2: model_id = `cvssp/audioldm2` or model_id = `cvssp/audioldm2-large`. For AudioLDM: model_id =  `cvssp/audioldm-m-full` or model_id =  `cvssp/audioldm-l-full`.

For Audiogen, the default parameters were used except for the duration of the audio files, which was set to 10 seconds. For AudioLDM and AudioLDM2, the recommendations indicated in the notebook at the provided link were followed, including:
- A negative prompt that discourages the model from generating low-quality audio in the outputs.
- Conversion of the model weights and computations to float16 (half) precision, which improves inference time and GPU memory with an imperceptible change to generation quality.
- Choosing a more efficient scheduler, specifically `DPMSolverMultistepScheduler`, which requires only 20-25 inference steps to achieve similar results. We set the inference steps to 20, the audio duration to 10 seconds, and the seed to 0 for reproducibility to allow us to tweak our prompts and observe the effect that they have on the generations by fixing the starting latents in the LDM model.

Once all the datasets containing the generated audio according to the different generative models used are obtained, the FAD can be calculated using the Clotho dataset for evaluation. To perform the calculation, upload all the datasets to Google Drive, run the script [fad_google_colab.ipynb](fad_google_colab.ipynb) on Google Colab, selecting the GPU for computation, and replace the respective dataset paths. To use the VGGish model for evaluation, set `model_name="vggish"`. To use the CLAP model, first perform the resampling of the audio files using the notebook [resampling.ipynb](codes_audio_modification_for_subjective_and_fad_clap_evaluation/resampling.ipynb) and then set the sample rate to 48kHz and `model_name="clap"` for the FAD calculation. Our results can be found in the file [FAD_results.xlsx](results/FAD_results.xlsx).




