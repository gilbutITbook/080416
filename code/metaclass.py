from math import sqrt
import os
import logging

log_level = os.environ.get("APP_LOG_LEVEL", 20)
logging.basicConfig(filename='app.log', level=log_level)

class PluginLoggerMeta(type):  # 자료형의 메타클래스가 아니라 상속받은 것임
    def __init__(cls, name, bases, attrs):
        logging.info(f"Registering: {name}"
                     f"({', '.join(b.__name__ for b in bases)}): "
                     f"\n  contains: {', '.join(attrs.keys())}")

class Plugin(metaclass=PluginLoggerMeta):
    pass

if True:  # 실제 환경에서는 다른 외부 조건이 있을 수 있음
    class Point2d(tuple, Plugin):
        def __new__(self, x, y):
            return tuple.__new__(self, (x, y))

        @property
        def distance(self):
            return sqrt(self[0]**2 + self[1]**2)

class Point3d(tuple, Plugin):
    def __new__(self, x, y, z):
        return tuple.__new__(self, (x, y, z))

    @property
    def distance(self):
        return sqrt(self[0]**2 + self[1]**2 + self[2]**2)

print(Point2d(4, 5).distance, Point3d(3, 5, 7).distance)
