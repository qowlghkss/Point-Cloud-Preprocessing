import open3d as o3d
import numpy as np
import argparse

def process_point_clouds(points3d_path, densepoint_path, output_path):
    # 1. points3d.ply 파일 로드
    pcd_points3d = o3d.io.read_point_cloud(points3d_path)

    # 2. 포인트 배열을 numpy로 변환
    points3d = np.asarray(pcd_points3d.points)

    # 3. 불필요한 포인트 필터링 (예: Z 값 기준으로 필터링)
    filtered_points3d = points3d[(points3d[:, 2] > -1) & (points3d[:, 2] < 1)]

    # 4. Dense Point Cloud (colmap MVS 결과) 로드
    pcd_dense = o3d.io.read_point_cloud(densepoint_path)
    dense_points = np.asarray(pcd_dense.points)

    # 5. dense_points에서 랜덤으로 10~20% 선택
    num_dense_points_to_add = int(len(dense_points) * np.random.uniform(0.1, 0.2))  # 10~20% 랜덤 선택
    random_indices = np.random.choice(len(dense_points), num_dense_points_to_add, replace=False)
    selected_dense_points = dense_points[random_indices]

    # 6. filtered_points3d와 selected_dense_points 결합
    combined_points = np.vstack((filtered_points3d, selected_dense_points))

    # 7. 새로운 포인트 클라우드 생성
    combined_pcd = o3d.geometry.PointCloud()
    combined_pcd.points = o3d.utility.Vector3dVector(combined_points)

    # 8. 결과를 시각화
    o3d.visualization.draw_geometries([combined_pcd])

    # 9. 수정된 포인트 클라우드를 파일로 저장 (필요한 경우)
    o3d.io.write_point_cloud(output_path, combined_pcd)


if __name__ == "__main__":
    # 1. argparse를 사용해 명령줄 인자 받기
    parser = argparse.ArgumentParser(description="Process point clouds and combine filtered points with dense points.")
    parser.add_argument('--points3d_path', type=str, required=True, help="/home/jihwan/study/25_1/datasets/output/4/points3d.ply")
    parser.add_argument('--densepoint_path', type=str, required=True, help="/home/jihwan/study/25_1/datasets/output/3/output2/dense/dense.ply")
    parser.add_argument('--output_path', type=str, required=True, help="/home/jihwan/study/25_1/datasets/output/deplus2.ply")
    
    args = parser.parse_args()

    # 2. 포인트 클라우드 처리 함수 실행
    process_point_clouds(args.points3d_path, args.densepoint_path, args.output_path)
