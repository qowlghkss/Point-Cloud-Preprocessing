import cv2
import numpy as np
import os
import glob

def calculate_psnr(img1, img2):
    if img1 is None or img2 is None:
        raise ValueError("One or both input images are None. Check the file paths.")

    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')  # 무한대 처리
    
    return 20 * np.log10(255.0 / np.sqrt(mse))

# 폴더 경로 설정
render_folder = "/home/jihwan/study/25_1/gaussian-splatting/output/orig-/train/ours_10000/renders"
gt_folder = "/home/jihwan/study/25_1/gaussian-splatting/output/orig/train/ours_10000/gt" 

# 렌더링된 이미지 & GT 이미지 목록 가져오기
render_images = sorted(glob.glob(os.path.join(render_folder, "*.png")))  # 확장자 변경 가능
gt_images = sorted(glob.glob(os.path.join(gt_folder, "*.png")))

# 파일 개수 확인
if len(render_images) == 0 or len(gt_images) == 0:
    print("Error: No images found in one or both folders.")
    exit()

if len(render_images) != len(gt_images):
    print(f"Warning: Number of render images ({len(render_images)}) and GT images ({len(gt_images)}) do not match.")

# PSNR 계산
psnr_values = []
for r_img, gt_img in zip(render_images, gt_images):
    render_image = cv2.imread(r_img)
    gt_image = cv2.imread(gt_img)
    
    if render_image is None or gt_image is None:
        print(f"Error: Failed to load image: {r_img} or {gt_img}")
        continue
    
    psnr = calculate_psnr(render_image, gt_image)
    psnr_values.append(psnr)
    print(f"PSNR for {os.path.basename(r_img)}: {psnr:.2f} dB")

# 평균 PSNR 출력
if psnr_values:
    avg_psnr = sum(psnr_values) / len(psnr_values)
    print(f"\nAverage PSNR: {avg_psnr:.2f} dB")
