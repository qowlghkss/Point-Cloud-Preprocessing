import lpips
import torch
from torchvision import transforms
from PIL import Image
import os

# 모델 로드
lpips_model = lpips.LPIPS(net='alex').cuda()

# 이미지 전처리
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])

# 이미지 디렉토리 경로 설정
render_images_dir = '/home/jihwan/study/25_1/gaussian-splatting/output/careply3/train/ours_10000/renders'
gt_images_dir = '/home/jihwan/study/25_1/gaussian-splatting/output/careply3/train/ours_10000/gt'

# 이미지 파일 목록 가져오기
render_images_files = sorted(os.listdir(render_images_dir))
gt_images_files = sorted(os.listdir(gt_images_dir))

lpis_sum = 0
i = 0

# 이미지 쌍 비교
for render_file, gt_file in zip(render_images_files, gt_images_files):
    # 이미지 불러오기
    render_image = Image.open(os.path.join(render_images_dir, render_file)).convert('RGB')
    gt_image = Image.open(os.path.join(gt_images_dir, gt_file)).convert('RGB')

    # 이미지 전처리
    render_image_tensor = transform(render_image).unsqueeze(0).cuda()
    gt_image_tensor = transform(gt_image).unsqueeze(0).cuda()

    # LPIPS 계산
    lpips_value = lpips_model(render_image_tensor, gt_image_tensor)
    print(f"LPIPS for {render_file} and {gt_file}: {lpips_value.item()}")
    lpis_sum += lpips_value
    i += 1
print(lpis_sum/i)