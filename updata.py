import open3d as o3d
import numpy as np

# 기존 sparse gaussians.ply 불러오기
sparse_ply = o3d.io.read_point_cloud("/home/jihwan/study/25_1/datasets/output/4/points3d.ply")

# Dense Point Cloud 불러오기
dense_ply = o3d.io.read_point_cloud("/home/jihwan/study/25_1/datasets/output/4/densech.ply")

# Dense Point Cloud의 일부만 선택 (예: 20% 샘플링)
num_samples = int(len(dense_ply.points) * 0.4)
indices = np.random.choice(len(dense_ply.points), num_samples, replace=False)
sampled_dense_ply = dense_ply.select_by_index(indices)

# Sparse + Sampled Dense 병합
merged_ply = sparse_ply + sampled_dense_ply

# 병합된 파일 저장
o3d.io.write_point_cloud("/home/jihwan/study/25_1/datasets/output/4/plusch40.ply", merged_ply)
