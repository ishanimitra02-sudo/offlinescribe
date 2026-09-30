# OfflineScribe

Private, on-device meeting and lecture assistant for Snapdragon-powered HP PCs.
Speech-to-text (Whisper) and summarization (small LLM) run locally on the NPU via
ONNX Runtime QNN, using models from [Qualcomm AI Hub](https://aihub.qualcomm.com).
No audio or text leaves the device.

## Features
- Record or upload audio, get transcript, summary, key points and action items
- Runs on the Snapdragon NPU, with automatic CPU fallback
- Sessions saved locally in `sessions/`

## Setup (Windows on Snapdragon)
```
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Download the Whisper and LLM models from Qualcomm AI Hub and set their paths in `app.py`.

## Status
Working skeleton: UI, NPU/CPU provider selection and session storage are in place.
Model wiring (`transcribe`, `summarize`) is marked TODO.

## License
MIT. Third-party models are under their own licenses.
