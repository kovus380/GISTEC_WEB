
# def decorator(func): # 인자로 함수를 받음
#     def decorated():
#         print("함수 시작!!")
#         func()
#         print("함수 끝!!")
#     return decorated
#
# @decorator
# def hello_world():
#     print("Hello World")
#
#
# hello_world()



def check_integer(func):
    def decorated(**kwargs):
        if kwargs['width'] >= 0 and kwargs['height'] >= 0:
            return func(**kwargs)
        else:
            raise ValueError("Input must be positive value")
    return decorated

def login_required(func):
    def decorated(**kwargs):
        if user.is_authenticated == True:
            return func(**kwargs)
        else:
            raise PermissionError("Logint required")
    return decorated()


@check_integer
@login_required
def rect_area(**kwargs):
    return kwargs['width'] * kwargs['height']

@check_integer
@login_required
def tr_area(**kwargs):
    return kwargs['width'] * kwargs['height'] / 2


class User():
    def __init__(self, auth):
        is_authenticated = auth

user = User(auth = True)

r_area = rect_area(user, width = 10, height = 10)
print(r_area)

t_area = tr_area(user, width = 10, height = 10)
print(t_area)