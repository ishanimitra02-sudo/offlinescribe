"""OfflineScribe: on-device meeting/lecture transcription + summary.

Skeleton: wire in the Whisper and LLM models exported from Qualcomm AI Hub
(https://aihub.qualcomm.com) at the marked TODOs, then test on your Snapdragon PC.
"""
import json, time, pathlib
import gradio as gr
import onnxruntime as ort

SESSIONS = pathlib.Path("sessions"); SESSIONS.mkdir(exist_ok=True)

def providers():
    """Prefer the Snapdragon NPU (QNN); fall back to CPU."""
    avail = ort.get_available_providers()
    if "QNNExecutionProvider" in avail:
        return [("QNNExecutionProvider", {"backend_path": "QnnHtp.dll"}), "CPUExecutionProvider"]
    return ["CPUExecutionProvider"]

def transcribe(audio_path: str) -> str:
    # TODO: load Whisper encoder/decoder ONNX from AI Hub with
    # ort.InferenceSession(path, providers=providers()), chunk audio (~30 s), decode text.
    raise NotImplementedError("Add Whisper model from Qualcomm AI Hub")

def summarize(text: str) -> str:
    # TODO: run a small on-device LLM with this prompt.
    prompt = ("Summarize the transcript. Give: 1) a 3-sentence summary, "
              "2) key points, 3) action items with owners.\n\n" + text)
    raise NotImplementedError("Add LLM from Qualcomm AI Hub / open-source")

def run(audio):
    t = transcribe(audio)
    s = summarize(t)
    (SESSIONS / f"{int(time.time())}.json").write_text(json.dumps({"transcript": t, "summary": s}))
    return t, s

with gr.Blocks(title="OfflineScribe") as demo:
    gr.Markdown("# OfflineScribe\nPrivate, on-device transcription and summaries. Nothing leaves this PC.")
    inp = gr.Audio(sources=["microphone", "upload"], type="filepath")
    btn = gr.Button("Transcribe & summarize")
    out_t = gr.Textbox(label="Transcript", lines=10)
    out_s = gr.Textbox(label="Summary, key points, action items", lines=10)
    btn.click(run, inp, [out_t, out_s])

if __name__ == "__main__":
    print("Execution providers:", providers())
    demo.launch()
