import os
from tqdm import tqdm

def feature_extraction(input_folder):
    data = []
    for root, _, files in os.walk(input_folder):
        class_label = os.path.basename(root)
        files.sort()
        for file in tqdm(files, desc=f'Processing {class_label}', unit='file'):
            if file.endswith(('.wav', '.mp3')):  # Check for audio files
                audio_file = os.path.join(root, file)
                print(audio_file, "->", class_label)

feature_extraction("scream_test_data")
data_dir = 'scream_test_data'
for filename in os.listdir(data_dir):
    if filename.endswith('.wav'):
        filepath = os.path.join(data_dir, filename)
        ipd.display(ipd.Audio(filepath))
        plot(get_mel(filepath),"mfcc")
        plot(get_mel(filepath), "Mel Spectrogram")
        plot(get_STFT_mfcc(filepath), "STFT MFCC")
        plot(get_STFT_mfcc2(filepath), "STFT MFCC 2")
        plot(get_STFT_mel(filepath), "STFT Mel")
        plot(get_STFT_me1_mag(filepath), "STFT Mel 1 Magnitude")
        plot(get_STFT_melx(filepath), "STFT Melx")
        plot(stft_mel_mfcc(filepath), "STFT Mel MFCC")
        plot(get_stft_power_mel_mfcc(filepath), "STFT Power Mel MFCC")
        plot(mfcc(filepath), "MFCC")