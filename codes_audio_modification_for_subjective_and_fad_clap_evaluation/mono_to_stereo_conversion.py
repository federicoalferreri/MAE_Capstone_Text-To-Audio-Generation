import torch 
import torchaudio 
import torchvision
import os


def mono_to_stereo_conversion (mono_folder, stereo_folder):
    
    #makes sure the output folder exists
    os.makedirs(stereo_folder, exist_ok=True)

    files_converted=0
    
    #iterate over all mono files
    for filename in os.listdir(mono_folder):

        if filename.endswith('.wav'):

            try:
                mono_file_path=os.path.join(mono_folder, filename)
                stereo_file_path=os.path.join(stereo_folder, filename)

                #load the mono audio file and its sample rate
                mono_audio, sample_rate = torchaudio.load(mono_file_path)

                if mono_audio.size(0) != 1: # to ensure the audio is mono
                    print(f"Skipping {filename}: it's not a mono file")
                    continue

                #create a stereo version of the mono file by duplicating the mono channel
                stereo_audio=mono_audio.repeat(2,1)

                #save the stereo audio file
                torchaudio.save(stereo_file_path, stereo_audio, sample_rate)

                #print (f"Converted {filename} to stereo format and saved to {stereo_file_path}")
                files_converted +=1

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    if files_converted>0:
        print(f"Total files converted: {files_converted}")
    else: 
        print(f"No files have been converted")

# mono audio and stereo audio folders

mono_folder='path_mono_folder'
stereo_folder='path_stereo_folder'

# converting the audio files
mono_to_stereo_conversion(mono_folder, stereo_folder)

