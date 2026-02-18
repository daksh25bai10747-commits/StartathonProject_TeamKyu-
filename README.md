# StartathonProject_TeamKyu-

Desert Terrain Analysis Tool
(semantic segmentation based thingy)

This project is an optimization in the process infrastructure building in adversarial terrains and is essentially a layer to reduce friction by providing quantified results for comparative analysis.
The goal is to take images of desert / off-road terrain and roughly estimate what parts of the environment are going to be difficult or costly when infrastructure is planned on top of it (roads, construction, access paths, etc).

A pretrained semantic segmentation model (DeepLabV3) is used and some simple post-processing logic is applied on top of its outputs.
This is not meant to be “perfect” or production-grade. It is a feasibility / bottleneck analysis tool.


---

What this does (rough explanation)

The program takes a folder of terrain images.
Each image is passed through a segmentation model.
From the segmentation output, the system tries to estimate:

overall landscape complexity
surface irregularities

amount of clutter (rocks, bushes, obstacles, etc)

a rough score indicating how annoying / resource-heavy construction would be in that region


This is meant for early-stage analysis and exploration, not exact planning.


---

Setup used during development

Python version: 3.11.9
Tested on CPU (no dedicated GPU used)
Tested on Windows

Dependencies used:

python

torch

torchvision

opencv

numpy


If dependency installation fails, installing them one by one usually works better than installing everything together.


---

How to run

1. Clone or download the repository


2. Open a terminal inside the project folder


3. (optional) create and activate a virtual environment


4. Install dependencies


5. Run the main file



Basic run:

cd into the project folder
then run:

python main.py

The program automatically reads images from the data folder.
No image paths are hardcoded.


---

Project structure (approx)

main file: runs the pipeline

model file: loads segmentation model

utils / geometry: post-processing and scoring

data folder: sample images used for testing


Placing new images inside the data/images folder is enough to test on new inputs.


---

Output

The program prints analysis results to the terminal for each image.
This includes:

terrain complexity indicators

surface difficulty

clutter / obstacle estimates

an overall “construction difficulty” type score


No GUI is included.
Outputs are intentionally simple text-based.

Higher scores indicate more difficult terrain to work with.


---

Reproducing submitted results

Using the dataset already present in the repository and running:

python main.py

should produce the same type of outputs as during the hackathon submission.
No additional tuning is required to reproduce baseline behavior.


---

Notes / assumptions

The segmentation model is pretrained (DeepLabV3).

No training from scratch was performed.

Scoring logic is heuristic and approximate.

The system is meant for exploration, not authoritative decisions.



---

If something breaks

verify python version

verify torch / torchvision installation

restart terminal after installing python / pip

Windows users may need to allow script execution for venv activation


Most issues encountered were related to paths or missing dependencies.


---

That’s all

The project is intentionally simple, fast to run, and easy to extend.
It is designed to demonstrate how semantic segmentation can be used as a base layer for environmental feasibility analysis. This project is lightweight enough to run on even low spec devices hence facilitating in the bottleneck of computation and also keeping privacy intact by ensuring all computation can happen offline.

the values generated are comparative measures not absolute measures.

Due to compute and time constraints, we prioritized building a deployable feasibility analysis layer on top of a strong pretrained model instead of chasing leaderboard metrics. The model backbone can be fine-tuned later if higher segmentation accuracy is needed.

Quantitative metrics like IoU / mAP50 require pixel-level ground truth segmentation masks, which were not present in the provided dataset. Therefore, the model was evaluated qualitatively and via consistency across similar terrain scenes. Reported mAP@50 is a placeholder and not indicative of real-world performance.
