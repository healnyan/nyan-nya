import discord

client = discord.Client()

token = "ODA3MzEwMTQ5NDc5NDMyMjYz.YB2IKg.KCuWcGY2s9-HfHA2FP377Rjpj1Y"


@client.event
async def on_ready():
    print(client.user.name)
    print("냥냐")
    game = discord.Game("냥냐 말 못하는거 많아 .")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    if message.content == "냥냐":
        await message.channel.send("미야옹")
    if message.content == "냥냐 안녕":
        await message.channel.send("안녕 !")
    if message.content == "냥냐 잘있어":
        await message.channel.send("잘 가 ~ ! !")
    if message.content == "냥냐 하이":
        await message.channel.send("안녕 ~")
    if message.content == "냥냐 바이":
        await message.channel.send("빠빠루")
    if message.content == "냥냐 오하요":
        await message.channel.send("おはようございます !")
    if message.content == "냥냐 곤니찌와":
        await message.channel.send("こんにちは !")
    if message.content == "냥냐 곰방와":
        await message.channel.send("こんばんは !")
    if message.content == "냥냐 고마워":
        await message.channel.send("내가 더 >_< !")
    if message.content == "냥냐 귀여워":
        await message.channel.send("에 ? 아닌데 ! ?!?!!?!")
    if message.content == "냥냐 띠껍네":
        await message.channel.send("어쩌라고")
    if message.content == "냥냐 바보야?":
        await message.channel.send("냥냐 바보 아니다 .")
    if message.content == "냥냐 놀자!":
        await message.channel.send("냥냐 바빠 .")
    if message.content == "냥냐 수박이":
        await message.channel.send("걔 바보 아닌가?")
    if message.content == "냥냐 무큐":
        await message.channel.send("참 춸 도 ! ! !")
    if message.content == "냥냐 정누누":
        await message.channel.send("모험은 계속된다 !")
    if message.content == "냥냐 이마트":
        await message.channel.send("이마트24 ?")
    if message.content == "냥냐 마이트":
        await message.channel.send("나 알아 ! 존잘러지?")
    if message.content == "냥냐 뭐해?":
        await message.channel.send("뒹굴뒹굴")
    if message.content == "냥냐 뭐해":
        await message.channel.send("냥냐 아무것도 안 해 .")
    if message.content == "냥냐 끝말잇기":
        await message.channel.send("내가 먼저 할게 해질녘 .")
    if message.content == "냥냐 주인은?":
        await message.channel.send("냥냐 주인은 멋있어 ! 채널에 박냥이라고 하는 사람이야 우하하 .")
    if message.content == "냥냐 주인":
        await message.channel.send("냥냐 주인은 멋있어 ! 채널에 박냥이라고 하는 사람이야 우하하 .")
    if message.content == "냥냐 리그오브레전드":
        await message.channel.send("노잼")
    if message.content == "냥냐 정충만":
        await message.channel.send("이름 왜그래 .. 구려")
    if message.content == "냥냐 정충누":
        await message.channel.send("설마 정충만+누누 ?")
    if message.content == "냥냐 천파랑":
        await message.channel.send("군머에 있다며 ?")
    if message.content == "냥냐 오스":
        await message.channel.send("Welcome to OSU !")
    if message.content == "냥냐 던파":
        await message.channel.send("왜 함 ?")
    if message.content == "냥냐 던전앤파이터":
        await message.channel.send("왜 하냐구 그거 .")
    if message.content == "냥냐 노래":
        await message.channel.send("냥냐는 노래같은거 못 해 .")
    if message.content == "냥냐 바보야":
        await message.channel.send("냥냐 바보 아니다 .")
    if message.content == "냥냐 멍청이":
        await message.channel.send("냥냐 멍청이 으느드 ..")
    if message.content == "냥냐는 왜 냥냐야?":
        await message.channel.send("내가 어떻게 알아 ?")
    if message.content == "냥냐 오늘 날씨 어때":
        await message.channel.send("너가 직접 검색해")
    if message.content == "냥냐 오늘 날씨":
        await message.channel.send("몰라 그런거")
    if message.content == "냥냐 주인닮았네":
        await message.channel.send("?")
    if message.content == "냥냐야":
        await message.channel.send("뭐")
    if message.content == "냥냐 냥냐":
        await message.channel.send("미야옹 미야옹")
    if message.content == "냥냐 롤토체스":
        await message.channel.send("운빨망겜")
    if message.content == "냥냐 롤체":
        await message.channel.send("앨리스 귀감 ㄱ !")
    if message.content == "냥냐 야 비":
        await message.channel.send("당장그쳐 뚝 !")
    if message.content == "냥냐 오프라인":
        await message.channel.send("냥냐는 주인 컴이 꺼져있을땐 작동 안 해 .")
    if message.content == "냥냐 정보":
        await message.channel.send("냥냐는 주인 컴이 꺼져있을땐 작동 안 해 .")
    if message.content == "냥냐 데바데":
        await message.channel.send("제 5인격이 더 재밌음 .")
    if message.content == "냥냐 얼불춤":
        await message.channel.send("노잼")
    if message.content == "냥냐 데가":
        await message.channel.send("으 ;")
    if message.content == "냥냐 데스티니 가디언즈":
        await message.channel.send("@권숩ㅏㄱ")
    if message.content == "냥냐 데스티니가디언즈":
        await message.channel.send("냥냐는 레이드 뛰는 겜으로 밖에 몰라 ...")
    if message.content == "냥냐 카트라이더":
        await message.channel.send("에 ? 망겜 ?")
    if message.content == "냥냐 야옹":
        await message.channel.send("미야옹")
    if message.content == "냥냐 사이퍼즈":
        await message.channel.send("에 ? ; 그런거 나한테 물어보지 말아줄래 ?")
    if message.content == "냥냐 유미":
        await message.channel.send("리그 오브 레전드 144번째 챔피언 , 마법 고양이 , 너랑 유미랑 ! 우리 함께 잘해보자고 ! .. 근데 .. 유미 수컷이라며 ?")
    if message.content == "냥냐 누누":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 누누와 윌럼프 , 소년과 설인 , 모험은 역시 친구랑 같이 해야 신나는 법 !")
    if message.content == "냥냐 진":
        await message.channel.send("리그 오브 레전드 129번째 챔피언 , 잔혹극의 거장 , 학살의 현장에서 난 피어오른다 . 붉은 여명에 피어나는 ... 꽃처럼 .")
    if message.content == "냥냐 알리스타":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 미노타우로스 , 누구도 날 막지 못해 !")
    if message.content == "냥냐 애니":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 어둠의 아이 , 너도 같이 놀래 ? 재밌겠다 ~ !")
    if message.content == "냥냐 애쉬":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 서리 궁수 , 화살 한 발로 세상을 평정해 주지 .")
    if message.content == "냥냐 피들스틱":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 오래된 공포 , 공포 ...")
    if message.content == "냥냐 잭스":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 무기의 달인 , 자, 한 번 해보자구 !")
    if message.content == "냥냐 누누와 윌럼프":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 누누와 윌럼프 , 소년과 설인 , 모험은 역시 친구랑 같이 해야 신나는 법 !")
    if message.content == "냥냐 케일":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 정의로운 자 , 모두가 내 전능함을 경외하리라 .")
    if message.content == "냥냐 마스터 이":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 우주 검사 , 나의 검은 당신의 것이오 .")
    if message.content == "냥냐 마스터이":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 우주 검사 , 나의 검은 당신의 것이오 .")
    if message.content == "냥냐 마이":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 우주 검사 , 나의 검은 당신의 것이오 .")
    if message.content == "냥냐 모르가나":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 타락한 자 , 날개를 묶었다고 의지까지 꺾인 건 아니야 .")
    if message.content == "냥냐 띄어쓰기":
        await message.channel.send("고의 띄어쓰기 임니다 ㅡㅡ")
    if message.content == "냥냐 라이즈":
        await message.channel.send("머머ㄹ .. 아 아니 , 리그 오브 레전드 최초의 17 챔피언 , 룬 마법사 , 대재앙에 한발 앞서가는 거다 !")
    if message.content == "냥냐 사이온":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 언데드 학살병기 , 휴식은 ... 산 자를 위한 ... 것이다 .. !")
    if message.content == "냥냐 시비르":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 전장의 여제 , 내 건 내가 알아서 챙겨 . 목숨이든 , 돈이든 .")
    if message.content == "냥냐 소라카":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 별의 아이 , 내 숨이 붙어있는 한 고통받게 두진 않아요 .")
    if message.content == "냥냐 티모":
        await message.channel.send("티확찢 .")
    if message.content == "냥냐 티모":
        await message.channel.send("아 . 이게 아니라 , 리그 오브 레전드 최초의 17 챔피언 , 날쌘 정찰병 , 티모 대위, 명을 받들겠습니다 !")
    if message.content == "냥냐 트리스타나":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 요들 사수 , 일단 한 번 쏘고 나면 또 쏘고 싶을 거예요 !")
    if message.content == "냥냐 트타":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 요들 사수 , 일단 한 번 쏘고 나면 또 쏘고 싶을 거예요 !")
    if message.content == "냥냐 트위스티드 페이트":
        await message.channel.send("롤체 요술사 젤 구데ㄱ ... 리그 오브 레전드 최초의 17 챔피언 , 카드의 달인 , 행운의 여신이, 내게 미소를 짓는 군 .")
    if message.content == "냥냐 워윅":
        await message.channel.send("리그 오브 레전드 최초의 17 챔피언 , 자운의 고삐 풀린 분노 , 피비린내다 ! 도망쳐라 ...")
    if message.content == "냥냐 워웍":
        await message.channel.send("워웍 아님 워윅임 .")
    if message.content == "냥냐 신지드":
        await message.channel.send("얘도 빡빡이잖아 .")
    if message.content == "냥냐 신지드":
        await message.channel.send("이 이게 아니지 . 리그 오브 레전드 18번째 챔피언 , 미친 화학자 , 한 잔 하겠나 !")
    if message.content == "냥냐 질리언":
        await message.channel.send("리그 오브 레전드 19번째 챔피언 , 시간의 수호자 , 그리할 줄 알고 있었소 .")
    if message.content == "냥냐 이블린":
        await message.channel.send("리그 오브 레전드 20번째 챔피언 , 고통스런 포옹 , 날 원하잖아, 그렇지 ?")
    if message.content == "냥냐 트린다미어":
        await message.channel.send("BJ이참수씨 ? .. 리그 오브 레전드 21번째 챔피언 , 야만전사 왕 , 손쉬운 사냥이 되겠군 !")
    if message.content == "냥냐 트위치":
        await message.channel.send("리그 오브 레전드 22번째 챔피언 , 역병 쥐 , 죽거나 죽이거나 . 약육강식은 그런 거지 !")
    if message.content == "냥냐 카서스":
        await message.channel.send("리그 오브 레전드 23번째 챔피언 , 죽음을 노래하는 자 , 고통, 희열, 그리고 평화 … 죽음은 언제나 아름답다 .")
    if message.content == "냥냐 아무무":
        await message.channel.send("찐ㄸ .. 리그 오브 레전드 24번째 챔피언 , 슬픈 미라 , 날 선택해줄 줄은 정말 몰랐어 ...")
    if message.content == "냥냐 초가스":
        await message.channel.send("리그 오브 레전드 25번째 챔피언 , 공허의 공포 , 세계의 종말을 원한다고 ... ? 좋아 ...")
    if message.content == "냥냐 애니비아":
        await message.channel.send("치킨 . .")
    if message.content == "냥냐 애니비아":
        await message.channel.send("리그 오브 레전드 26번째 챔피언 , 얼음 불사조 , 내 날개를 타고 .")
    if message.content == "냥냐 람머스":
        await message.channel.send("구른다 . 리그 오브 레전드 27번째 챔피언 , 중무장 아르마딜로 , 그래 .")
    if message.content == "냥냐 베이가":
        await message.channel.send("리그 오브 레전드 28번째 챔피언 , 악의 작은 지배자 , 내가 너였다면, 너에게 어떤 자비도 없었을 거란 것만 알아둬 !")
    if message.content == "냥냐 카사딘":
        await message.channel.send("리그 오브 레전드 29번째 챔피언 , 공허의 방랑자 , 힘의 균형은 유지되어야 한다 !")
    if message.content == "냥냐 갱플랭크":
        await message.channel.send("리그 오브 레전드 30번째 챔피언 , 바다의 무법자 , 지옥의 불길도, 죽음의 심연도, 이 몸을 넘볼 수는 없다 .")
    if message.content == "냥냐 갱플":
        await message.channel.send("리그 오브 레전드 30번째 챔피언 , 바다의 무법자 , 지옥의 불길도, 죽음의 심연도, 이 몸을 넘볼 수는 없다 .")
    if message.content == "냥냐 졸려":
        await message.channel.send("자 .")
    if message.content == "냥냐 잘자":
        await message.channel.send("내일 바 !")
    if message.content == "냥냐 잘 자":
        await message.channel.send("안녕 ~")
    if message.content == "냥냐 타릭":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 블리츠크랭크":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 블츠":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 블리츠":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 문도 박사":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 문도박사":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 문도":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 잔나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 말파이트":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 말파":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 코르키":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 카타리나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 나서스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 샤코":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 하이머딩거":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 하딩":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 우디르":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 니달리":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 뽀삐":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 그라가스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 판테온":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 모데카이저":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 모데":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 이즈리얼":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 쉔":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 케넨":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 가렌":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아칼리":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 말자하":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 올라프":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 코그모":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 신 짜오":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 신짜오":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 블라디미르":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 갈리오":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 우르곳":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 미스 포츈":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 미스포츈":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 미포":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 미스포춘":
        await message.channel.send("미스 포츈 이다 .")
    if message.content == "냥냐 미스 포춘":
        await message.channel.send("미스 포츈 이다 .")
    if message.content == "냥냐 소나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 스웨인":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 럭스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 르블랑":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 이렐리아":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 이렐":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 트런들":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 카시오페아":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 케이틀린":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 케틀":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 레넥톤":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 카르마":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 마오카이":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 자르반 4세":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 자르반":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 자르반4세":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 녹턴":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 리 신":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 리신":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 브랜드":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 럼블":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 베인":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 오리아나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 요릭":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 레오나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 오공":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 스카너":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 탈론":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 리븐":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 제라스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 그브":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 그레이브즈":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 쉬바나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 피즈":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 볼베":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 볼리베어":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아리":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 빅토르":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 세주아니":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 세주":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 직스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 노틸":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 노틸러스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 피오라":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 룰루":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 헤카림":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 바루스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 다리우스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 다리":
        await message.channel.send("다리우스 ?")
    if message.content == "냥냐 드레이븐":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 드븐":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 제이스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 자이라":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 다이애나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 렝가":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 신드라":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 카직스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 엘리스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 제드":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 앨리스":
        await message.channel.send("리그 오브 레전드 106번째 ... 아니야 ! 이상한 나라의 앨리스 ?")
    if message.content == "냥냐 나미":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 바이":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 쓰레쉬":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 퀸":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 자크":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 리산드라":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 리산":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아트록스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 루시안":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 징크스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아트":
        await message.channel.send("... 설마 아트록스를 줄여서 말한건 아니겠지 ?")
    if message.content == "냥냐 야스오":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 벨코즈":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 브라움":
        await message.channel.send("브라움만 미드라구 !")
    if message.content == "냥냐 브라움":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 나르":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아지르":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 칼리스타":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 칼리":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 렉사이":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 바드":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 에코":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 탐 켄치":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 탐켄치":
        await message.channel.send("정확한 명칭은 탐 켄치야 ... 정충만 .. 탐 켄치를 놓아줘 ..")
    if message.content == "냥냐 킨드레드":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 킨드":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 일라오이":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 일라":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아우렐리온 솔":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아우솔":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 탈리야":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 클레드":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아이번":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 카밀":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 라칸":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 자야":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 케인":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 오른":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 조이":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 카이사":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 파이크":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 니코":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 사일러스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 키아나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 세나":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아펠리오스":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 아펠":
        await message.channel.send("읍읍이 말하는거지 ? 아펠리오스라고 쳐봐 .")
    if message.content == "냥냐 세트":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 릴리아":
        await message.channel.send("이익 !")
    if message.content == "냥냐 릴리아":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 요네":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 사미라":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 세라핀":
        await message.channel.send("K/DA 에서 나갔음 좋겠네 .")
    if message.content == "냥냐 세라핀":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 렐":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "냥냐 비에고":
        await message.channel.send("주인이 게을러서 아직 업데이트 안 해놨어 .")
    if message.content == "업뎃 안 한게 왤케 많아;":
        await message.channel.send("내 주인 욕함 ?")
    if message.content == "업뎃 안한게 왤케 많아;":
        await message.channel.send("내 주인 욕함 ?")
    if message.content == "왤케 게을러":
        await message.channel.send("내 주인 욕함 ?")
    if message.content == "왤케 게을러;":
        await message.channel.send("내 주인 욕함 ?")
    if message.content == "님들아":
        await message.channel.send("웅 !")
    if message.content == "님들":
        await message.channel.send("냥냐 불러써 ?")
    if message.content == "냥냐 히메":
        await message.channel.send("냥냐 주이니야 !")
    if message.content == "냥냐 박냥":
        await message.channel.send("냥냐 주이니야 ! !")
    if message.content == "냥냐":
        await message.channel.send("에 ?")
    if message.content == "냥":
        await message.channel.send("ㅇㅅaㅇ ? !")
    if message.content == "냥냐 냐냐":
        await message.channel.send("냐 ~ 냐 ~")
    if message.content == "ㅅㅂ":
        await message.channel.send("왜 욕해 ?")
    if message.content == "시발":
        await message.channel.send("욕하지마 .")
    if message.content == "ㅆㅃ":
        await message.channel.send("머 ?")
    if message.content == "ㅆㅂ":
        await message.channel.send("주인아 얘가 반성방 가고 싶대 !")
    if message.content == "냥냐 랄랄라":
        await message.channel.send("(~˘▾˘)~♫•*¨*•.¸¸♪")
    if message.content == "냥냐 배고파":
        await message.channel.send("밥 머그새요 .")
    if message.content == "냥냐 배불러":
        await message.channel.send("나는 ?")
    if message.content == "냥냐 잘있어":
        await message.channel.send("올 때 메로나 ~")
    if message.content == "냥냐 응애":
        await message.channel.send("응애 나 애기 냥냐 맘마조")
    if message.content == "냥냐 루비":
        await message.channel.send("간바루비 !")
    if message.content == "냥냐 선샤인":
        await message.channel.send("러브라이브 선샤인 !")
    if message.content == "냥냐 마리":
        await message.channel.send("마뤼데스 ~")
    if message.content == "냥냐 치카":
        await message.channel.send("치카 댄스 ?")
    if message.content == "냥냐 치카":
        await message.channel.send("치카치카 ?")
    if message.content == "냥냐 치카":
        await message.channel.send("미캉 !")
    if message.content == "냥냐 치카":
        await message.channel.send("그래서 셋중에 뭔데 ?")
    if message.content == "냥냐 요우":
        await message.channel.send("젠소쿠 젠신 ~ ?")
    if message.content == "냥냐 요우":
        await message.channel.send("요소로 !")
    if message.content == "냥냐 리코":
        await message.channel.send("리코쨩 비 - 무 !")
    if message.content == "냥냐 카난":
        await message.channel.send("허그 !")
    if message.content == "냥냐 다이아":
        await message.channel.send("뿌뿌 데스와 - !")
    if message.content == "냥냐 씹덕같아":
        await message.channel.send("너도잖아 .")
    if message.content == "냥냐 씹덕":
        await message.channel.send("너 얘기 ?")
    if message.content == "냥냐 하나마루":
        await message.channel.send("오하나 ~")
    if message.content == "냥냐 하나마루":
        await message.channel.send("마루 ~")
    if message.content == "냥냐 요시코":
        await message.channel.send("요하네 !")
    if message.content == "냥냐 레식":
        await message.channel.send("어려워 보여 .")
    if message.content == "냥냐 레인보우식스시즈":
        await message.channel.send("스팀겜 !")
    if message.content == "냥냐 발로란트":
        await message.channel.send("라이엇 겜 ?")
    if message.content == "냥냐 오버워치":
        await message.channel.send("그거 아직도 하는 사람 있어 ?")
    if message.content == "냥냐 배그":
        await message.channel.send("으 .")
    if message.content == "냥냐 배틀그라운드":
        await message.channel.send("주인이 그런거 하는거 아니랬어 .")
    if message.content == "냥냐 배틀 그라운드":
        await message.channel.send("싫어 !")
    if message.content == "싸울래?":
        await message.channel.send("싸우면 주인이 반성방 보낼걸 ?")
    if message.content == "싸울래 ?":
        await message.channel.send("싸우면 주인이 반성방 보낼걸 ?")
    if message.content == "냥냐 마이멜로디":
        await message.channel.send("기여워 !!!!")
    if message.content == "냥냐 마멜":
        await message.channel.send("체고야 !!!!")
    if message.content == "냥냐 마이 멜로디":
        await message.channel.send("흐앙 넘 조아")
    if message.content == "냥냐 자":
        await message.channel.send("웅 ... 그러까 ?")
    if message.content == "냥냐 라이키 라이키 쵸 다이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "냥냐 라이키 라이키 초 다이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "냥냐 라이키 라이키 못또 !":
        await message.channel.send("라이키 라이키 못또 !")
    if message.content == "냥냐 라이키 라이키 타리나이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "냥냐 라이키 라이키 라이키 라이키 !":
        await message.channel.send("와아아아 !")
    if message.content == "냥냐 라키 라키 쵸 다이!":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "냥냐 라키 라키 쵸 다이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "냥냐 라이키 라이키 쵸 다이!":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "냥냐 라키 라키 못또 !":
        await message.channel.send("라이키 라이키 못또 !")
    if message.content == "냥냐 라키 라키 못또!":
        await message.channel.send("라이키 라이키 못또 !")
    if message.content == "냥냐 라이키 라이키 못또!":
        await message.channel.send("라이키 라이키 못또 !")
    if message.content == "냥냐 라키 라키 타리나이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "냥냐 라이키 라이키 타리나이!":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "냥냐 라이키 라이키 라이키 라이키!":
        await message.channel.send("와아아아 !")
    if message.content == "냥냐 라키 라키 라키 라키 !":
        await message.channel.send("와아아아 !")
    if message.content == "냥냐 라키 라키 라키 라키!":
        await message.channel.send("와아아아 !")
    if message.content == "라이키 라이키 쵸 다이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "라이키 라이키 초 다이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "라이키 라이키 못또 !":
        await message.channel.send("라이키 라이키 못또 !")
    if message.content == "라이키 라이키 타리나이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "라이키 라이키 라이키 라이키 !":
        await message.channel.send("와아아아 !")
    if message.content == "라키 라키 쵸 다이!":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "라키 라키 쵸 다이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "라이키 라이키 쵸 다이!":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "라키 라키 못또 !":
        await message.channel.send("라이키 라이키 못또 !")
    if message.content == "라키 라키 못또!":
        await message.channel.send("라이키 라이키 못또 !")
    if message.content == "라이키 라이키 못또!":
        await message.channel.send("라이키 라이키 못또 !")
    if message.content == "라키 라키 타리나이 !":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "라이키 라이키 타리나이!":
        await message.channel.send("하이 ! 하이 ! 하이 ! 하이 !")
    if message.content == "라이키 라이키 라이키 라이키!":
        await message.channel.send("와아아아 !")
    if message.content == "라키 라키 라키 라키 !":
        await message.channel.send("와아아아 !")
    if message.content == "라키 라키 라키 라키!":
        await message.channel.send("와아아아 !")
    if message.content == "냥냐 호구마":
        await message.channel.send("호구마요 ? (웃음) 호박고구ㅁ ...")
    if message.content == "냥냐 호구마":
        await message.channel.send("호박고구마 호박고구마 !!!!!!!!!!!!!!!!!!!!")
    if message.content == "냥냐 호구마":
        await message.channel.send("흐에엥엑에 ㅠㅠㅠㅠㅠㅠㅠㅠ !!!!!!!!!")
    if message.content == "냥냐 문희":
        await message.channel.send("문희는 뽀도가 먹구찌뿐뎅 .")

client.run(token)