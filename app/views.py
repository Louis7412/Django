from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random


def lotto(requset):
    # 1~49 不重覆六個數字跟排序
    numbers = random.sample(range(1, 50), 6)
    spec_number = random.randint(1, 49)
    numbers = sorted(numbers)

    # ["1","34","21","34","13","20"] => 1 13 20 34 45 34
    # numbers = " ".join([str(i) for i in numbers])
    numbers = " ".join(map(str, numbers))

    # 將numbers串成字串輸出跟排序

    result = {"numbers": numbers, "spec_number": spec_number}

    return render(requset, "lotto.html", result)


# Create your views here.
def hello(request):
    result = {"message": "測試!", "data": 123, "label": "文字"}
    return JsonResponse(result)
