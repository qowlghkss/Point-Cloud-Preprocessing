# Pre-processing


3DGS 기반으로 진행된 연구이며 전처리 관련 코드만 있으므로 
실행및 결과 확인은 3DGS를 실행 해주셔야 합니다.

dataset의 경우 NeRF_LEGO dataset을 사용했습니다.

코드 내부 연결하고자 하는
주소 변경 일일히 해주셔야 합니다.

1번 프로그램은 2번 3번 프로그램 내부에 다 들어가 있으며

2번 프로그램은 3번 내부에 들어가 있습니다

1번 2번 3번 각각 사용하셔도 되며 중복적으로 사용하셔도 상관없습니다.



패키지
----
updata 실행을 위해 설치해야하는 패키지는 다음과 같습니다
```python
open3d                      0.17.0
numpy                       1.21.6
ConfigArgParse              1.7
```



실행결과
----
![Image](https://github.com/user-attachments/assets/6079553d-73af-41b6-a249-a9c18538ff6f)

각각 순서대로 Ground truth,  Original 3DGS,   OURs(updata,updata2 사용) 입니다.

결과는 다음과 같이 나오며 updata,updata2를 
동시에 사용했을때 기존 3DGS를 그냥 사용하였을때 보다 성능이 좋게 나오는걸 확인했습니다.

실행
---
실행,렌더링 명령어는 다음과 같습니다
```python
python train.py   --source_path (이미지와ply파일json파일등이 들어 가있는 곳)   --model_path (저장할곳)   --images (train 이미지 위치)   --iterations 20000   --checkpoint_iterations 10000   --save_iterations 10000 


python render.py  --model_path (train이 저정된곳)   --images (train 이미지 위치)   --resolution 1024   --iteration 10000
```

논문
----
내용은 다음 논문에 정리 해뒀습니다
https://drive.google.com/file/d/1M__dwuk5AycMcA20g0ECIdrpHOrgqCj6/view?usp=sharing




---
PSNR,SSIM,LPIPS 측정을 위의 코드를 이용했으며 위 코드를 사용하기 위해서는 해당 패키지 추가 설치가 필요합니다.
```python
lpips                       0.1.4
torchvision                 0.13.1
opencv-python               4.4.0.46
```
