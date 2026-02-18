import torch
import torchvision.transforms as T
from torchvision.models.segmentation import deeplabv3_resnet50

device = "cuda" if torch.cuda.is_available() else "cpu"

model = deeplabv3_resnet50(weights="DEFAULT").to(device)
model.eval()

transform = T.Compose([
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225])
])

def segment_image(img):
    x = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        out = model(x)["out"]
    mask = out.argmax(1).squeeze().cpu().numpy()
    return mask