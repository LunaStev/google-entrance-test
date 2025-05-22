strs = [
    "flantastimagniflexiconormousization", "flower", "flow", "flight", "flame", "flash", "flap", "flavor", "flock",
    "flee", "fleet", "flesh", "flex", "flick", "flip", "flirt", "float",
    "flog", "flood", "floor", "flora", "flour", "fluff", "fluid", "fluke",
    "flume", "flung", "flush", "flute", "fly", "flyer", "flyover", "flimsy",
    "flinch", "flirtation", "flamboyant", "flannel", "flatter", "flavorful",
    "flustered", "flawed", "flawless", "flair", "flaking", "flanked",
    "flavored", "flaring", "flavored", "flamethrower", "flashlight",
    "flashy", "flat", "flatline", "flatten", "flaky", "flail", "flourish"
]

print(f"단어: {strs}")

# 1. 첫 번째 단어를 기준으로 접두사를 시작
prefix = strs[0]

# 2. 단어들을 하나씩 보면서 접두사를 점점 줄여나갈 거야
for word in strs[1:]:
    print(f"비교 중: 기준 접두사(prefix) = '{prefix}', 비교 대상 단어 = '{word}'")

    # 접두사가 현재 단어의 앞부분이 아닐 때까지 줄이기
    while True:
        # 만약 현재 단어가 접두사로 시작하면 OK
        if word.startswith(prefix):
            print(f"→ '{word}'는 '{prefix}'로 시작함. 유지!")
            break

        # 접두사 한 글자 줄이기
        print(f"→ '{word}'는 '{prefix}'로 시작하지 않음. 접두사 줄이기!")
        prefix = prefix[:-1]
        print(f"→ 접두사 줄인 결과: '{prefix}'")

        # 접두사가 완전히 사라졌으면 공통 접두사 없음
        if prefix == "":
            print("→ 공통 접두사가 없음!")
            break

print(f"\n최종 공통 접두사: '{prefix}'")
