import cv2
import numpy as np

def compute_geometry_score(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)
    edge_density = edges.sum() / edges.size

    lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    slope_proxy = (gx**2 + gy**2).mean()

    geometry_score = 0.4 * edge_density + 0.3 * lap_var + 0.3 * slope_proxy
    return float(geometry_score)