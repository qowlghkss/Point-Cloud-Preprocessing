# Pre-processing
3DGS 기반으로 진행된 연구이며 전처리 관련 코드만 있으므로 
실행및 결과 확인은 3DGS를 실행 해주셔야 합니다

주소 변경 일일히 해주셔야 합니다

1번 프로그램은 2번 3번 프로그램 내부에 다 들어가 있으며

2번 프로그램은 3번 내부에 들어가 있습니다

1번 2번 3번 각각 사용하셔도 되며 중복적으로 사용하셔도 상관없습니다.


설치해야하는 패키지는 다음과 같습니다
```python
open3d                      0.17.0
numpy                       1.21.6
ConfigArgParse              1.7
```

![Image](https://github.com/user-attachments/assets/dc783bc6-10dc-44ee-87d4-23f9653a15fa)

결과는 다음과 같이 나오며 1번 SfM Point Filtering , 2번 Point_Sampling 를 
동시에 사용했을시 성능이 좋게 나오는걸 확인했습니다.
