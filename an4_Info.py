# 파일 생성
!cat << 'EOF' > espnet_an4_summary.py
#!/usr/bin/env python3
import os, glob, sys, soundfile as sf, numpy as np
from espnet2.bin.asr_inference import Speech2Text

def show_an4_summary():
    print("=== AN4 Dataset Info ===")
    for split in ["train","dev","test"]:
        scp = f"data/{split}/wav.scp"
        if os.path.exists(scp):
            print(f"  {split}: {sum(1 for _ in open(scp))} utts")

    exp = "exp/asr_train_raw_en_char"
    print("\n=== Model Checkpoints ===")
    for ck in sorted(glob.glob(f"{exp}/*.pth"), key=os.path.getmtime):
        print(" ", os.path.basename(ck))
    
    print("\n=== Recent Training Log ===")
    logs = sorted(glob.glob(f"{exp}/*_train_*/train.log"), key=os.path.getmtime)
    if logs:
        print("Last 20 lines of:", logs[-1])
        os.system(f"tail -n 20 {logs[-1]}")
    else:
        print("  (no logs)")

class AN4Recognizer:
    def __init__(self, exp="exp/asr_train_raw_en_char"):
        cfg = os.path.join(exp, "config.yaml")
        mdl = sorted(glob.glob(f"{exp}/*.pth"), key=os.path.getmtime)[-1]
        self.rec = Speech2Text(
            asr_train_config=cfg,
            asr_model_file=mdl,
            beam_size=1,
            device="cuda" if __import__('torch').cuda.is_available() else "cpu"
        )

    def transcribe(self, wav):
        speech, sr = sf.read(wav)
        assert sr == 16000, f"Sample rate mismatch: {sr}"
        return self.rec(speech)[0][0]

if __name__=="__main__":
    show_an4_summary()
    if len(sys.argv)==2:
        hyp = AN4Recognizer().transcribe(sys.argv[1])
        print("\n=== Inference Result ===")
        print("Hypothesis:", hyp)
    else:
        print("\nUsage: python espnet_an4_summary.py <wav_file>")
EOF
chmod +x espnet_an4_summary.py
