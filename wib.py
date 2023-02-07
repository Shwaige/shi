import datetime
import uvicorn
from fastapi import FastAPI

# 返回当前剩余时间
timeLeftApi = FastAPI()


@timeLeftApi.get('/timeLeft')
def timeLeft():
    xbNow_str = datetime.datetime.now().strftime("%FT18:30:00")
    xbNow = datetime.datetime.strptime(xbNow_str, "%Y-%m-%dT%H:%M:%S")
    timeNow = datetime.datetime.now()
    seconds = (xbNow - timeNow).seconds
    h = int(seconds / 3600)
    if h >= 9:
        return "已下班，别乱寄吧查"
    m = int((seconds - h * 3600) / 60)
    s = seconds - h * 3600 - m * 60
    return "还有" + str(h) + "小时" + str(m) + "分钟" + str(s) + "秒" + "下班"

# 从语雀查数据并返回
# 工具接口


if __name__ == "__main__":
    uvicorn.run(app=timeLeftApi, host="0.0.0.0", port=27015)
# cs