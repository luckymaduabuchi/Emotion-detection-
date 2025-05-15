# 🎙️ Emotion Detection in Speech Using Lightweight and Transformer-Based Models: A Comparative and Ablation Study

## 🎯 OBJECTIVE
This project performs **emotion classification from speech** using two lightweight transformer-based models:

- **DistilHuBERT** (self-supervised on raw waveform)
- **PaSST** (spectrogram transformer with patchout)

---

## 😄 EMOTIONS & DATASET

We use the **CREMA-D** dataset, which contains 7,442 audio clips labeled with the following six emotions:

- Happy  
- Sad  
- Angry  
- Fear  
- Disgust  
- Neutral

---

## 🛠 INSTALLATION

Install required dependencies:

```bash
pip install torch torchaudio s3prl hear21passt matplotlib seaborn scikit-learn numpy soundfile tqdm
