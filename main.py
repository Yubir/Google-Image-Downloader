from google_images_download import google_images_download   #importing the library

var1 = int(input("다운로드 시도 횟수 -> "))
var2 = str(input("검색 키워드 -> "))
var3 = str(input("GIF / JPG / PNG -> "))

response = google_images_download.googleimagesdownload()   #class instantiation
arguments = {"keywords":var2,"limit":var1,"print_urls":True, "format": var3}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)

print('\033[95m' + '\n완료 (Done)\n' + '\033[0m')