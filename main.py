def butane():
    air = int(input('주입하실 공기의양과 butane양을 입력해주세요:'))
    air1 = 0.0186 * air ## 부탄의양 = 0.019 * 주입할 공기의 양
    air2 = air - air1 ##  공기의양 = 전체공기의양-부탄의양

    bir1 = 0.0841 * air  ## 부탄의양 = 0.019 * 주입할 공기의 양
    bir2 = air - bir1  ##  공기의양 = 전체공기의양-부탄의양
    print('LEL: 공기의양: %f 부탄의양: %f' % (air2, air1))
    print('UEL: 공기의양: %f 부탄의양: %f' % (bir2, bir1))

def toluene():
    air = int(input('주입하실 공기의양과 toluene양을 입력해주세요:'))
    air1 = 0.0127 * air ## 부탄의양 = 0.019 * 주입할 공기의 양
    air2 = air - air1 ##  공기의양 = 전체공기의양-부탄의양

    bir1 = 0.0675 * air  ## 부탄의양 = 0.019 * 주입할 공기의 양
    bir2 = air - bir1  ##  공기의양 = 전체공기의양-부탄의양
    print('LEL: 공기의양: %f 부탄의양: %f' % (air2, air1))
    print('UEL: 공기의양: %f 부탄의양: %f' % (bir2, bir1))

def hydrogen():
    air = int(input('주입하실 공기의양과 hydrogen양을 입력해주세요:'))
    air1 = 0.04 * air ## 부탄의양 = 0.019 * 주입할 공기의 양
    air2 = air - air1 ##  공기의양 = 전체공기의양-부탄의양

    bir1 = 0.742 * air  ## 부탄의양 = 0.019 * 주입할 공기의 양
    bir2 = air - bir1  ##  공기의양 = 전체공기의양-부탄의양
    print('LEL: 공기의양: %f 부탄의양: %f' % (air2, air1))
    print('UEL: 공기의양: %f 부탄의양: %f' % (bir2, bir1))

def ammonia():
    air = int(input('주입하실 공기의양과 ammonia양을 입력해주세요:'))
    air1 = 0.155 * air ## 부탄의양 = 0.019 * 주입할 공기의 양
    air2 = air - air1 ##  공기의양 = 전체공기의양-부탄의양

    bir1 = 0.277 * air  ## 부탄의양 = 0.019 * 주입할 공기의 양
    bir2 = air - bir1  ##  공기의양 = 전체공기의양-부탄의양
    print('LEL: 공기의양: %f 부탄의양: %f' % (air2, air1))
    print('UEL: 공기의양: %f 부탄의양: %f' % (bir2, bir1))

def information():
    print('최고폭발한계 UEL(Upper Explosive Limit), 최저폭발 한계 LEL(Lower Explosive Limit)입니다.')
    print('물질이 폭발하기 위한 최대조건과 최소조건을 뜻합니다.')
    print('각물질의 LEL값과 UEL 값은 다음과 같습니다. \n butane 1.86~8.41 \n toluene 1.27~6.75 \n hydrogen 4~74.2 \n ammonia 15.5~27')

def idn():
    print('직접 LEL과 UEL의 값을 알려주세요')
    air = float(input('주입하실 공기의양과 물질의양을 입력해주세요:'))
    LEL = float(input('주입하실 물질의 LEL값을 입력해주세요:'))
    UEL = float(input('주입하실 물질의 UEL값을 입력해주세요:'))
    LEL = LEL * 0.01
    UEL = UEL * 0.01
    air1 = LEL * air  ## 부탄의양 = 0.019 * 주입할 공기의 양
    air2 = air - air1  ##  공기의양 = 전체공기의양-부탄의양

    bir1 = UEL * air  ## 부탄의양 = 0.019 * 주입할 공기의 양
    bir2 = air - bir1  ##  공기의양 = 전체공기의양-부탄의양
    print('LEL: 공기의양: %f 부탄의양: %f' % (air2, air1))
    print('UEL: 공기의양: %f 부탄의양: %f' % (bir2, bir1))

while True:
    print('--------------------------------------------------------------------------------')
    print('안녕하세요 LEL과 UEL을 계산해주는 프로그램 입니다.')
    print('1.butane(부탄) 2.toluene(톨루엔) 3.hydrogen(수소) 4.ammonia(암모니아) 5.information 6.임의 지정')
    print('프로그램을 종료하실려면 1~5외의 숫자를 입력해주세요')

    matter = int(input('계산하실 물질의 번호를 입력해주세요:'))

    if matter == 1:
        butane()
    elif matter == 2:
        toluene()
    elif matter == 3:
        hydrogen()
    elif matter == 4:
        ammonia()
    elif matter == 5:
        information()
    elif matter == 6:
        idn()
    else:
        break


