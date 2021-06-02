from DingRobot import Robot

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=66024a8c991f7fb52283b6f43d2617d99defb251df6c7e80170e9f238a7b22f7'

users = {
    "赖其锋": "15015764532",
    "卢子博": "13924867630",
    "唐茂发": "13622512514",
    "张晓乐": "15917004860"
}
keyword = "demo"


if __name__ == '__main__':
    robot = Robot(webhook=webhook, keyword=keyword)
    robot.send_text("hello everyone!\nthis message used a class.")
    robot.send_text("你撤尼玛呢")
