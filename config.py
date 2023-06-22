'''
插件仓库地址：https://github.com/Nao-desu/sv_plugin
作者： Nao_desu
下面的配置可以按需更改
'''

#绘制卡牌信息时各职业边框颜色
clan_color = {0:(220,220,220),
              1:(0,128,0),
              2:(238,232,170),
              3:(25,25,112),
              4:(205,133,63),
              5:(147,112,219),
              6:(220,20,60),
              7:(255,250,250),
              8:(70,130,180)}

#绘制卡牌时文字颜色
text_color = (255,255,255)

#抽卡时高于此稀有度卡牌出现概率，单位万分之一，前七包和第八包概率不同
prob1 = {
    1:150,
    2:750,
    3:3250,
    4:10000
}
prob2 = {
    1:150,
    2:600,
    3:10000,
    4:10000
}

max_400 = 5#一天抽井的次数
max_coin = 10000#一天使用金币抽卡的次数