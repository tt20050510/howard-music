from src.h_music.Site import KuGou
from src.h_music.Site import KuWo
from src.h_music.Site import MiGu
from src.h_music.Site import NetEase
from src.h_music.Site import QQ
from src.h_music.Site import QianQian

if __name__ == '__main__':
    kw = KuWo()
    kg = KuGou()
    qq = QQ()
    ne = NetEase()
    mg = MiGu()
    qian = QianQian()

    # 完整示例
    # print(kw.search("alan").data.to_json())
    # print(kw.album("4974851").data.to_json())
    # print(kw.detail("40171818").data.to_json())

    # print(kg.search("alan").data.to_json())
    # print(kg.album("40351678").data.to_json())
    # print(kg.detail("40E8F9C4F6ADDFCF998D092512D69CAB","40351678").data.to_json())

    # print(qq.search("周杰伦").data.to_json())
    # print(qq.album("002Nt51E0q8Zoo").data.to_json())
    # print(qq.detail("0039MnYb0qxYhV").data.to_json())

    # print(ne.search("alan").data.to_json())
    # print(ne.album("36224021").data.to_json())
    # print(ne.detail("515453363").data.to_json())

    # print(mg.search("演员").data.to_json())
    # print(mg.album("1003463541").data.to_json())
    # print(mg.detail("1004417797","60084650813").data.to_json())

    # print(qian.search("演员").data.to_json())
    # print(qian.album("P10001774541").data.to_json())
    # print(qian.detail("T10040589088").data.to_json())





