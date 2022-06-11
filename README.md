# Audio-Anamoly-detection-for-mechanical-failures
• Anomaly detection is the identification of rare events, items, or observations
which are suspicious because they differ significantly from standard behaviors
or patterns. Anomalies in data are also called standard deviations, outliers,
noise, novelties, and exceptions.

• This model makes use of autoencoder model for audio anomaly detection, the
autoencoder modelling is done using tensorflow(keras).

• This model can be used in many industries to check their equipment if there is
any abnormality in the working of certain equipments.

Methadalogy:
![image](https://user-images.githubusercontent.com/62985786/173177751-07f4f790-7e4b-44bf-8ff9-a577701ed397.png)

Signal Feature Extraction:

• We load the audio data in time-domain using librosa.
        Sampling-rate : 22050
        Duration of each sample : 10 sec.

• Spectrogram of the signal is obtained by computing the short time Fourier transforms(STFT) and by converting amplitude to decibels.
        Number of samples in a window per fft (n_fft) = 2048
        Amount of samples shifted after each fft (hop_length) = 512

• Mel-Spectrogram is computed by obtaining the frequency of the spectrogram in mel-scale.
        Number of mel-bins : 64

•Mel-spectrogram features is provided as input to the Auto-encoder
![image](https://user-images.githubusercontent.com/62985786/173177767-a12022e8-a601-492f-98a0-c51136e93120.png)

Auto-Encoder Model:
![image](https://user-images.githubusercontent.com/62985786/173177801-8bc2580e-c304-46f9-ad70-bb3445865a6c.png)

