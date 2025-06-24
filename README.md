# Pre-processing


3DGS 기반으로 진행된 연구이며 전처리 관련 코드만 있으므로 
실행및 결과 확인은 3DGS를 실행 해주셔야 합니다.

dataset의 경우 NeRF_LEGO dataset을 사용했습니다.

코드 내부 연결하고자 하는
주소 변경 일일히 해주셔야 합니다.

1번 프로그램은 2번 3번 프로그램 내부에 다 들어가 있으며

2번 프로그램은 3번 내부에 들어가 있습니다

1번 2번 3번 각각 사용하셔도 되며 중복적으로 사용하셔도 상관없습니다.


설치해야하는 패키지는 다음과 같습니다
```python
open3d                      0.17.0
numpy                       1.21.6
ConfigArgParse              1.7
```

![Image](https://github.com/user-attachments/assets/6079553d-73af-41b6-a249-a9c18538ff6f)

결과는 다음과 같이 나오며 1번 SfM Point Filtering , 2번 Point_Sampling 를 
동시에 사용했을시 기존 3DGS를 그냥 사용하였을때 보다 성능이 좋게 나오는걸 확인했습니다.


내용은 다음 논문에 정리 해뒀습니다
https://drive.google.com/file/d/1M__dwuk5AycMcA20g0ECIdrpHOrgqCj6/view?usp=sharing

