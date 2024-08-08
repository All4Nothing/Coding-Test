### n+1 카드게임
**1st Attempt**  
[*solution1*](https://github.com/All4Nothing/Coding-Test/blob/main/2024_KAKAO_WINTER_INTERNSHIP/n+1_카드게임/solution1.py)

> **정확성 : 8/20(시간초과 12)**

> *list의 요소 삭제를 remove를 사용한 게 시간초과 원인이라고 생각함. 시간초과 날 것을 알았지만, 알고리즘 구현이 우선이었어서, dictonary를 flag로 이용해서 성능 개선할 예정*

**2nd Attempt**  
[*solution1*](https://github.com/All4Nothing/Coding-Test/blob/main/2024_KAKAO_WINTER_INTERNSHIP/n+1_카드게임/solution2.py)

> **정확성 : 8/20(시간초과 12)**

> *dictonary 대신 list를 flag로 사용했다. python에서는 list를 함수 parameter로 넣어주면, 값이 아닌 주소를 넘긴다.(포인터 개념) 따라서, 값만을 넘길 경우, deepcoy를 써야한다. 그냥 copy는 shallow copy로 list는 서로 다른 객체를 가리키지만, list의 내부 요소는 공유한다.*
> deepcopy 보다 slicing이 더 빠른 속도를 보인다.
> early return 조건을 더 강하게 둬서, 쓸모없는 탐색을 줄이도록 개선해봐야겠다.
