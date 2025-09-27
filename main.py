import argparse
import subprocess
import shutil
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument("--weights", type=str, help="initial weights path")
parser.add_argument("--epochs", type=int, default=20, help="total training epochs")
parser.add_argument(
    "--imgsz", type=int, default=640, help="train, val image size (pixels)"
)
parser.add_argument("--imgw", type=int, default=640, help="export image width (pixels)")
parser.add_argument(
    "--imgh", type=int, default=640, help="export image height (pixels)"
)
opt = parser.parse_args()

shutil.rmtree("yolov5/runs", ignore_errors=True)
subprocess.run(
    [
        "python3",
        "-W",
        "ignore::FutureWarning",
        "train.py",
        "--data",
        "../resource/singtown-ai.yaml",
        "--weights",
        f"../weights/{opt.weights}",
        "--epochs",
        str(opt.epochs),
        "--img",
        str(opt.imgsz),
        "--batch-size",
        "-1",
    ],
    cwd="yolov5",
)
subprocess.run(
    [
        "python3",
        "export.py",
        "--rknpu",
        "--weights",
        "runs/train/exp/weights/best.pt",
        "--img",
        str(opt.imgw),
        str(opt.imgh),
    ],
    cwd="yolov5",
)
with zipfile.ZipFile("yolov5/runs/train/exp/output.zip", "w") as zipf:
    zipf.write("yolov5/runs/train/exp/weights/best.onnx", arcname="best.onnx")
    zipf.write("yolov5/RK_anchors.txt", arcname="RK_anchors.txt")
