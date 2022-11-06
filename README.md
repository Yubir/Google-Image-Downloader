
# 사용방법

* 처음 사용할 경우
`> pip install google_images_download`

* 사용 방법
`> python3 main.py`

`다운로드 시도 횟수 -> [다운로드 할 이미지 갯 수]`
`검색 키워드 -> [검색 할 키워드]`
`GIF / JPG / PNG -> [gif/jpg/png 파일 형식]`

입력 후 `main.py` 안 `/downloads/(keyword)`에 다운로드 시작

* 예시

![header](https://cdn.discordapp.com/attachments/1038694488647925814/1038694875262111775/image.png)

![header](https://cdn.discordapp.com/attachments/1038694488647925814/1038694975069769749/image.png)

# 오류

* ValueError: invalid literal for int() with base 10: ' '
> 숫자 입력란을 숫자가 아닌 다른 문자로 입력한 경우

* KeyError: ' '
> 정해진 특정 단어가 아닌 다른 문자를 입력한 경우

* unfortunately all 20 could not be downloaded because some images were not downloadable. 0 is all we got for this search filter!

><a href="https://skmouse.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B5%AC%EA%B8%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%ED%81%AC%EB%A1%A4%EB%A7%81uh-oh-keywords-is-a-required-argument-unfortunately-all-20-could-not-be-downloaded-because-some-images-were-not-downloadable-0-is-all-we-got-for-this-search-filter-1"> 해당 오류는 여기를 눌러 오류 해결</a>
