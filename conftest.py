from pytest import fixture


@fixture(
    params=[
        (10, 10, "UT", 106.85),
        (30, 15, "TX", 478.12),
        (200, 3.99, "NV", 861.84),
        (7, 1000, "CA", 7047.07),
        (100, 20, "TX", 2061.25),
        (1000, 50, "AL", 44200.0),
    ]
)
def input_data_calc(request):
    data = request.param
    return data


@fixture(params=[(100, 1, 1), (5000, 20, 1000), (10, 5, 0.5)])
def input_data_per(request):
    data = request.param
    return data
