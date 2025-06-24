import cv2
import os
from skimage.metrics import structural_similarity as ssim

def calculate_ssim(image1_path, image2_path):
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    
    if img1 is None or img2 is None:
        print(f"Error loading images: {image1_path}, {image2_path}")
        return None
    
    ssim_value, _ = ssim(img1, img2, full=True)
    return ssim_value

def compare_ssim_multiple(render_folder, gt_folder):
    render_images = sorted(os.listdir(render_folder))
    gt_images = sorted(os.listdir(gt_folder))
    
    if len(render_images) != len(gt_images):
        print("Warning: Number of images in both folders does not match!")
    
    ssim_scores = []
    
    for render_img, gt_img in zip(render_images, gt_images):
        render_path = os.path.join(render_folder, render_img)
        gt_path = os.path.join(gt_folder, gt_img)
        
        ssim_value = calculate_ssim(render_path, gt_path)
        if ssim_value is not None:
            print(f"SSIM for {render_img} and {gt_img}: {ssim_value:.4f}")
            ssim_scores.append(ssim_value)
    
    if ssim_scores:
        avg_ssim = sum(ssim_scores) / len(ssim_scores)
        print(f"Average SSIM: {avg_ssim:.4f}")

# 실행 예시
render_folder = "/home/jihwan/study/25_1/gaussian-splatting/output/orig/train/ours_10000/renders"
gt_folder = "/home/jihwan/study/25_1/gaussian-splatting/output/orig/train/ours_10000/gt"
compare_ssim_multiple(render_folder, gt_folder)