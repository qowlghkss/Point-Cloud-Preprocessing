import open3d as o3d
import numpy as np

# 파일 경로 설정 (수정 가능)
sparse_ply_path = "/home/jihwan/study/25_1/datasets/NeRF_Data-20250321T084231Z-001/NeRF_Data/nerf_example_data/nerf_synthetic/lego/points3d.ply"
dense_ply_path = "/home/jihwan/study/25_1/datasets/output/3/output2/dense/dense.ply"
output_ply_path = "/home/jihwan/study/25_1/datasets/output/4/delplus.ply"

# 1️ 기존 Sparse Gaussian Point Cloud 불러오기
sparse_ply = o3d.io.read_point_cloud(sparse_ply_path)

# 2️ 불필요한 Sparse Point 제거 (너무 가까운 포인트 제거)
def remove_close_points(pcd, min_dist=0.01):
    points = np.asarray(pcd.points)
    new_points = []

    for i, p in enumerate(points):
        dists = np.linalg.norm(points - p, axis=1)
        if np.count_nonzero(dists < min_dist) < 5:  # 주변에 너무 가까운 점이 많으면 제거
            new_points.append(p)

    filtered_pcd = o3d.geometry.PointCloud()
    filtered_pcd.points = o3d.utility.Vector3dVector(np.array(new_points))
    return filtered_pcd

filtered_sparse = remove_close_points(sparse_ply)

# 3️ Dense Point Cloud 불러오기 및 일부 샘플링 (10~20% 선택)
dense_ply = o3d.io.read_point_cloud(dense_ply_path)
num_samples = int(len(dense_ply.points) * 0.2)  # 20% 샘플링
indices = np.random.choice(len(dense_ply.points), num_samples, replace=False)
sampled_dense_ply = dense_ply.select_by_index(indices)

# 4️ 최적화된 Point Cloud 병합
merged_ply = filtered_sparse + sampled_dense_ply

# 5️ 병합된 파일 저장
o3d.io.write_point_cloud(output_ply_path, merged_ply)

print(f"Optimized Gaussian Point Cloud saved at: {output_ply_path}")
