# Text-to-Audio Generation: a comparative analysis for perceptual performance evaluation 
The following study was conducted within the context of the 'Music and Acoustic Engineering Capstone' course of MSc. in _Music and Acoustic Engineering @ Politecnico di Milano_ (a.y. 2023/2024) held by professor Alberto Bernardini. The papper presenting the study can be found [here]()

Authors:

- [Emma Coletta](https://github.com/emmaclt)
- [Federico Ferreri](https://github.com/federicoalferreri)
- [Lorenzo Previati](https://github.com/LorenzoPreviati22)


### Abstract
Advancements in the field of Artificial Intelligence Generated Content (AIGC) have led to the development of sophisticated Text-to-Audio (TTA) models. These models synthesize audio from textual descriptions, with potential applications ranging from video game sound effects to acoustic scene setting in movies. This study presents a comparative analysis of five TTA models: [AudioGen](https://arxiv.org/pdf/2209.15352), [AudioLDM](https://arxiv.org/pdf/2301.12503) (in two versions: '_m-full_' and '_l-full_'), and [AudioLDM2](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10530074&casa_token=hya2XRcl9OkAAAAA:ChBk4vUXM8uwiXZHJFXsqWWeI4Zl3r3V5iWA-4k7X1bZ4E6E3J1XtLg9JHl8nkFtegu6f2JB8w&tag=1) (in two versions: base and '_large_'). We evaluated these models using both objective and subjective methods. Objective evaluation involved calculating FAD scores with embeddings extracted using both the VGGish and CLAP models to measure alignment with input text and audio quality of the generated audio datasets. Subjective evaluation was conducted via a [web-based MUSHRA listening test](https://github.com/audiolabs/webMUSHRA/tree/master) administered to participants of varied ages and musical backgrounds. Our findings emphasize strengths and limitations of each generative model and of the proposed automatic perceptual evaluation, revealing its inaccuracy in assessing TTA models whose training datasets do not include the one used to compute the [FAD](https://arxiv.org/pdf/1812.08466) score. This study contributes to the field by providing insights into the accuracy of current automatic quality assessment methods for TTA models. 


## Table of Contents
- [Abstract](#abstract)
- [Page content]()
- [How to replicate the experiment]()
