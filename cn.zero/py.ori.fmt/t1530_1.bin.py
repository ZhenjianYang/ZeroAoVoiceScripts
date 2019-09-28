from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1530_1.bin",                # FileName
        "t1530",                    # MapName
        "t1530",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 255, 0, 255],
    )

    BuildStringList((
        "t1530_1",                # 0
    ))

    ScpFunction((
        "Function_0_1D0",          # 00, 0
        "Function_1_1D4",          # 01, 1
        "Function_2_1072",         # 02, 2
        "Function_3_1076",         # 03, 3
        "Function_4_1B81",         # 04, 4
        "Function_5_2900",         # 05, 5
        "Function_6_2994",         # 06, 6
        "Function_7_2BD0",         # 07, 7
        "Function_8_39A7",         # 08, 8
        "Function_9_420B",         # 09, 9
        "Function_10_4369",        # 0A, 10
        "Function_11_504A",        # 0B, 11
        "Function_12_558A",        # 0C, 12
        "Function_13_56C7",        # 0D, 13
        "Function_14_61AE",        # 0E, 14
        "Function_15_6276",        # 0F, 15
        "Function_16_62EF",        # 10, 16
        "Function_17_63FB",        # 11, 17
        "Function_18_6E4C",        # 12, 18
        "Function_19_6F61",        # 13, 19
        "Function_20_757B",        # 14, 20
        "Function_21_7881",        # 15, 21
        "Function_22_793E",        # 16, 22
        "Function_23_79E3",        # 17, 23
        "Function_24_7A74",        # 18, 24
        "Function_25_7E68",        # 19, 25
        "Function_26_7E72",        # 1A, 26
        "Function_27_7FFE",        # 1B, 27
        "Function_28_81A7",        # 1C, 28
        "Function_29_8358",        # 1D, 29
        "Function_30_866D",        # 1E, 30
        "Function_31_88CB",        # 1F, 31
        "Function_32_8A2B",        # 20, 32
        "Function_33_8B7D",        # 21, 33
        "Function_34_8CA9",        # 22, 34
        "Function_35_8E21",        # 23, 35
        "Function_36_8F86",        # 24, 36
        "Function_37_90E2",        # 25, 37
        "Function_38_937A",        # 26, 38
        "Function_39_94F1",        # 27, 39
        "Function_40_9629",        # 28, 40
        "Function_41_98D9",        # 29, 41
        "Function_42_9A00",        # 2A, 42
        "Function_43_9B42",        # 2B, 43
        "Function_44_9C74",        # 2C, 44
        "Function_45_9F22",        # 2D, 45
        "Function_46_A0AE",        # 2E, 46
        "Function_47_A21A",        # 2F, 47
        "Function_48_A34F",        # 30, 48
        "Function_49_A4C9",        # 31, 49
        "Function_50_A737",        # 32, 50
        "Function_51_A87B",        # 33, 51
        "Function_52_AA73",        # 34, 52
        "Function_53_AC3E",        # 35, 53
        "Function_54_ADED",        # 36, 54
        "Function_55_AF73",        # 37, 55
        "Function_56_B0EC",        # 38, 56
        "Function_57_B214",        # 39, 57
        "Function_58_B384",        # 3A, 58
        "Function_59_B4E0",        # 3B, 59
        "Function_60_B65C",        # 3C, 60
        "Function_61_B82D",        # 3D, 61
        "Function_62_B9F3",        # 3E, 62
        "Function_63_BBBA",        # 3F, 63
        "Function_64_BD16",        # 40, 64
        "Function_65_BE79",        # 41, 65
        "Function_66_BFDF",        # 42, 66
        "Function_67_C148",        # 43, 67
        "Function_68_C172",        # 44, 68
        "Function_69_C193",        # 45, 69
        "Function_70_C23E",        # 46, 70
        "Function_71_C3A0",        # 47, 71
        "Function_72_C417",        # 48, 72
        "Function_73_C714",        # 49, 73
        "Function_74_C937",        # 4A, 74
        "Function_75_CF6A",        # 4B, 75
        "Function_76_D599",        # 4C, 76
        "Function_77_E613",        # 4D, 77
        "Function_78_EEDB",        # 4E, 78
    ))


    def Function_0_1D0(): pass

    label("Function_0_1D0")

    Call(1, 1)
    Return()

    # Function_0_1D0 end

    def Function_1_1D4(): pass

    label("Function_1_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA")
    Call(0, 9)
    Jump("loc_1071")

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_200")
    Call(0, 14)
    Jump("loc_1071")

    label("loc_200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D")
    Call(1, 76)
    Jump("loc_1071")

    label("loc_21D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_367")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC")

    #C0001
    ChrTalk(
        0x8,
        (
            "今天早上，黑月贸易公司的诸位\x01",
            "都自行出院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "明明还没有痊愈呢，\x01",
            "只是刚刚能行走，就坚持要……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F4")

    #C0003
    ChrTalk(
        0x10A,
        (
            "#0603F哼……该说不愧是曹的部下吗，\x01",
            "看来都经受过相当严酷的体能训练啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4")

    SetScenarioFlags(0x0, 0)
    Jump("loc_362")

    label("loc_2FC")


    #C0004
    ChrTalk(
        0x8,
        (
            "今天早上，黑月贸易公司的诸位\x01",
            "都自行出院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "我本来是想阻止的，\x01",
            "因为他们的枪伤还没有治好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362")

    Jump("loc_106E")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3CE")

    #C0006
    ChrTalk(
        0x8,
        (
            "看来你们已经和约亚西姆医生谈过了啊，\x01",
            "这真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "随时都欢迎诸位再来哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_446")

    #C0008
    ChrTalk(
        0x8,
        (
            "约亚西姆医生正在研究楼四层的\x01",
            "研究室里等候各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "……最好趁他还没有偷懒出去玩，\x01",
            "赶快过去找他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D")

    #C0010
    ChrTalk(
        0x8,
        (
            "欢迎来到圣乌尔斯拉医院。\x01",
            "您今天有何贵干呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x109,
        (
            "#0500F真是很久都没来\x01",
            "乌尔斯拉医院了啊。\x02\x03",

            "从那场狼形魔兽事件以后，\x01",
            "最多也就是巡逻时路过这里而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，这么说也许有些失礼，\x01",
            "不过，上士好像从不会生病啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        (
            "#0504F嗯，那当然啦。\x02\x03",

            "#0500F自从进了警备队，\x01",
            "我就一直很注重保持身体健康，\x01",
            "尽量让自己连小病也不要得。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "呵呵，真厉害啊。\x01",
            "尽量不要让自己生病就医，\x01",
            "这可比什么都重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "不过，身体一旦真的出现了什么问题，\x01",
            "也还是应该立刻来医院的。\x01",
            "因为有些事情，光靠自己是无法解决的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 5)
    Jump("loc_6BF")

    label("loc_64D")


    #C0016
    ChrTalk(
        0x8,
        (
            "调理好自己的身体，保持健康，\x01",
            "尽量不来医院，比什么都重要呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "呵呵，这位警备队员的健康理念\x01",
            "是非常正确的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF")

    Jump("loc_106E")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6D5")
    Call(1, 26)
    Jump("loc_106E")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_747")

    #C0018
    ChrTalk(
        0x8,
        (
            "约亚西姆医生的研究室\x01",
            "就在研究楼的四层。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "只要去病房楼的楼顶，\x01",
            "就很容易看到研究楼的位置了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D6")

    #C0020
    ChrTalk(
        0x8,
        "欢迎光临乌尔斯拉医院。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "各位教授今天都出差\x01",
            "参加教授会议去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "在确认过主治医生之后，\x01",
            "请办理诊察手续。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_82E")

    label("loc_7D6")


    #C0023
    ChrTalk(
        0x8,
        (
            "各位教授今天都出差\x01",
            "参加教授会议去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "在确认过主治医生之后，\x01",
            "请办理诊察手续。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82E")

    Jump("loc_106E")

    label("loc_833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_978")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F4")

    #C0025
    ChrTalk(
        0x8,
        (
            "今天好像有游客\x01",
            "前来接受身体检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "我虽然也能理解他们很想体验\x01",
            "最先进医疗设备的心情……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "但那样做的话，就可能会耽误\x01",
            "重病患者的检查。\x01",
            "总觉得有些不太好呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_973")

    label("loc_8F4")


    #C0028
    ChrTalk(
        0x8,
        (
            "好像有一些游客前来\x01",
            "做体检之类的诊断。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "……既然是外来的客人，\x01",
            "我们就不能怠慢……\x01",
            "但一想到他们的动机，心情还是很复杂。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_973")

    Jump("loc_106E")

    label("loc_978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A2C")
    OP_93(0x8, 0x10A, 0x0)
    OP_4B(0x17, 0xFF)

    #C0030
    ChrTalk(
        0x8,
        "啊，迪塔总裁……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "真是十分感谢您\x01",
            "今年也能光临本院。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "患者们一定也会很高兴吧。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x17,
        (
            "#2804F哪里的话，别那么客气。\x02\x03",

            "这只是我的个人行为而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x17, 0xFF)
    Jump("loc_106E")

    label("loc_A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BA1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD6")

    #C0034
    ChrTalk(
        0x8,
        (
            "听说塞茜尔小姐和其他护士们\x01",
            "把工作分配得很好，从而安排出了假期。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "真是羡慕她们啊。\x01",
            "事务部门这边的人手比较少，\x01",
            "所以几乎都没有休假。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9C")

    label("loc_AD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B3B")

    #C0036
    ChrTalk(
        0x8,
        (
            "如果今后再有什么问题，\x01",
            "欢迎随时光临本院。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "我们一定会诚心诚意地\x01",
            "为您服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9C")

    label("loc_B3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_B90")

    #C0038
    ChrTalk(
        0x8,
        (
            "必须让约亚西姆医生\x01",
            "快点回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        "诸位，一切都拜托你们了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9C")

    label("loc_B90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_B9C")

    label("loc_B9C")

    Jump("loc_106E")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_CA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C52")

    #C0040
    ChrTalk(
        0x8,
        (
            "职员宿舍的琪尔修宿舍长和\x01",
            "玛罗奈虽然算是\x01",
            "克拉克事务长的部下，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "你可不要把这些话告诉别人哦，\x01",
            "其实事务长在琪尔修宿舍长\x01",
            "的面前很恭顺呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C9C")

    label("loc_C52")


    #C0042
    ChrTalk(
        0x8,
        (
            "你可不要告诉别人哦，\x01",
            "其实克拉克事务长在琪尔修宿舍长\x01",
            "的面前很恭顺呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9C")

    Jump("loc_106E")

    label("loc_CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D52")

    #C0043
    ChrTalk(
        0x8,
        (
            "院长一直都巡游于各个国家之间，\x01",
            "进行技术交流并挖掘人才，\x01",
            "很少会出现在医院里。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "其实，这么一说，\x01",
            "连我也没有见到过院长……\x01",
            "到底是个怎样的人呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DAF")

    label("loc_D52")


    #C0045
    ChrTalk(
        0x8,
        (
            "院长十分忙碌，\x01",
            "几乎都不会\x01",
            "出现在医院里。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "实际上，医院的经营是\x01",
            "交由教授们来负责的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAF")

    Jump("loc_106E")

    label("loc_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_E21")

    #C0047
    ChrTalk(
        0x8,
        "今天的来访者接待就到此为止了。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "如果太晚的话，也会不安全，\x01",
            "请前来探病的客人抓紧时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_EB2")

    #C0049
    ChrTalk(
        0x8,
        (
            "临近傍晚，外来的患者及访客\x01",
            "也逐渐散去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "之前发生过利顿医生受伤的事情，\x01",
            "所以一定要趁天还没黑之前，\x01",
            "让大家都回到市里呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1065")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEE")

    #C0051
    ChrTalk(
        0x8,
        "……那个，塞茜尔小姐。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "再怎么说，这里也是工作场所，\x01",
            "是不是也该稍微收敛一点，\x01",
            "不要在别人面前进行太亲密的身体接触呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0006F……真不好意思。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x136,
        (
            "#1305F哎呀，罗伊德有什么\x01",
            "好道歉的啊？\x02\x03",

            "#1309F呵呵……塞拉小姐，\x01",
            "你是在羡慕我吧？\x01",
            "我有个这～么可爱的弟弟。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "唉……随你去好了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1060")

    label("loc_FEE")


    #C0056
    ChrTalk(
        0x8,
        (
            "……反正我已经不想阻止你了，\x01",
            "你们想继续抱在一起也好，\x01",
            "还是怎样也好，都请随意吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0006F（目瞪口呆……）\x02",
    )

    CloseMessageWindow()

    label("loc_1060")

    Jump("loc_106E")

    label("loc_1065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_106E")

    label("loc_106E")

    TalkEnd(0x8)

    label("loc_1071")

    Return()

    # Function_1_1D4 end

    def Function_2_1072(): pass

    label("Function_2_1072")

    Call(1, 3)
    Return()

    # Function_2_1072 end

    def Function_3_1076(): pass

    label("Function_3_1076")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_10F7")

    #C0058
    ChrTalk(
        0x9,
        (
            "虽然院长一直不在，\x01",
            "但医院的经营状况却非常不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "长年以来，在市民中积累的深厚信赖感\x01",
            "也起到了很大作用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_116F")

    #C0060
    ChrTalk(
        0x9,
        (
            "塞拉负责接待以及院内联络的工作，\x01",
            "她做得非常努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "单看工作量的话，\x01",
            "甚至都不会输给塞茜尔小姐呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11F7")

    #C0062
    ChrTalk(
        0x9,
        (
            "只要是送来的患者，就一定要救助。\x01",
            "这就是乌尔斯拉医院的座右铭。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "即使是面对十恶不赦的坏人，\x01",
            "本院也会贯彻这个原则。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_11F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_128B")

    #C0064
    ChrTalk(
        0x9,
        (
            "虽然本医院从各国的各机关\x01",
            "领取资金。\x01",
            "但在经营方针上，仍然是推崇节俭。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "要把资金尽量都用于补贴\x01",
            "那些负担不起医疗费用\x01",
            "的患者们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_128B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_131C")

    #C0066
    ChrTalk(
        0x9,
        (
            "既然在这间医院工作，\x01",
            "我们便不是普通的业务人员，\x01",
            "而是为了救助患者而工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "如果患者能面带笑容地出院，\x01",
            "我就会感到很幸福呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_13AF")

    #C0068
    ChrTalk(
        0x9,
        (
            "教授们既要搞研究，又要指导实习医生，\x01",
            "还要兼任复诊的工作，\x01",
            "所以非常繁忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "不过，约亚西姆医生例外，\x01",
            "他好像一直都不怎么忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_13AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_14E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144B")

    #C0070
    ChrTalk(
        0x9,
        (
            "我负责管理这间医院的\x01",
            "一切事务。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "从设备的预算分配，\x01",
            "到导力网络的调整……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "虽然工作多到让人头疼，\x01",
            "但是很有挑战性啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14E0")

    label("loc_144B")


    #C0073
    ChrTalk(
        0x9,
        (
            "尤其是导力网络的调整，真是非常辛苦。\x01",
            "因为医院里除了我之外，\x01",
            "再没有会操作的人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "如果可以的话，真希望能从\x01",
            "克洛斯贝尔市那边调来一位技师呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E0")

    Jump("loc_1B7D")

    label("loc_14E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_158F")
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0x42, 0xF, 0x0)
    OP_4B(0x42, 0xFF)

    #C0075
    ChrTalk(
        0x9,
        (
            "您想做健康诊断吗？\x01",
            "那么，请在这边的\x01",
            "文件上签名。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "因为是初诊，\x01",
            "所以可能会多花一些时间。\x01",
            "您可以等待一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x42,
        "嗯，没问题。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x42, 0xFF)
    Jump("loc_1B7D")

    label("loc_158F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15FF")

    #C0078
    ChrTalk(
        0x9,
        (
            "迪塔总裁每年都会\x01",
            "送来很多礼物，就算分给\x01",
            "全部患者也是足够的。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "哎呀，真是位了不起的人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_15FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FD")

    #C0080
    ChrTalk(
        0x9,
        (
            "我们正在商讨，是否应该\x01",
            "在接待处实行卡片制度。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "预先准备好记载着\x01",
            "个人信息的卡片钥匙，\x01",
            "这样就可以大大缩减接待处的手续量了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "只是，由于目前还存在着卡片量产体制，\x01",
            "以及个人情报保护工作等问题，\x01",
            "新制度的实行还很艰难呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_177C")

    label("loc_16FD")


    #C0083
    ChrTalk(
        0x9,
        (
            "我们正在商讨，是否应该\x01",
            "在接待处实行卡片制度。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "不过，也有不少问题\x01",
            "阻碍了新制度的施行……\x01",
            "看来在短时间之内还难以实现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177C")

    Jump("loc_1B7D")

    label("loc_1781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1824")

    #C0085
    ChrTalk(
        0x9,
        (
            "我本来在宿舍的食堂吃午饭，\x01",
            "结果宿舍长说『职员不要在中午过来』，\x01",
            "然后就把我赶出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "哎呀呀……\x01",
            "琪尔修宿舍长真是\x01",
            "让人敬畏啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1872")

    label("loc_1824")


    #C0087
    ChrTalk(
        0x9,
        (
            "哎呀呀……\x01",
            "琪尔修宿舍长真是\x01",
            "让人敬畏啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        "……这就是所谓的女强人吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1872")

    Jump("loc_1B7D")

    label("loc_1877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_19CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1944")

    #C0089
    ChrTalk(
        0x9,
        (
            "导力网络将乌尔斯拉医院\x01",
            "与克洛斯贝尔市紧密联系在了一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "市民还可以通过导力网络\x01",
            "进行预约服务，\x01",
            "虽然目前还在试验阶段。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "不过，因为普及率的问题，\x01",
            "它并没有被广泛利用。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19C7")

    label("loc_1944")


    #C0092
    ChrTalk(
        0x9,
        (
            "如果在导力网络上进行事先\x01",
            "预约服务，就可以免去等待\x01",
            "时间，顺利进行诊察。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "只不过，因为普及率的问题，\x01",
            "它还没有被广泛利用呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C7")

    Jump("loc_1B7D")

    label("loc_19CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1A31")

    #C0094
    ChrTalk(
        0x9,
        (
            "警察局的诸位……\x01",
            "感谢你们帮助\x01",
            "安置防护栏。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "但愿这样就能让\x01",
            "魔兽无法再进来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1A70")

    #C0096
    ChrTalk(
        0x9,
        (
            "警察局的诸位……\x01",
            "你们的调查有什么进展了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_1A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1B0B")

    #C0097
    ChrTalk(
        0x9,
        (
            "实在是不愿意相信有魔兽\x01",
            "闯入了医院……\x01",
            "如果那是真的，事情可就严重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "关于利顿是否真的遭到了魔兽袭击，\x01",
            "我希望你们能找出确凿的证据。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_1B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1B7D")

    #C0099
    ChrTalk(
        0x9,
        (
            "欢迎您光临圣乌尔斯拉\x01",
            "医科大学附属医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "旁边的接待处负责\x01",
            "接待业务。\x01",
            "如有需要，请您去那边咨询。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B7D")

    TalkEnd(0x9)
    Return()

    # Function_3_1076 end

    def Function_4_1B81(): pass

    label("Function_4_1B81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1BE4")
    TurnDirection(0xFE, 0x3C, 0)

    #C0101
    ChrTalk(
        0xFE,
        "哎呀，今天有何贵干呢？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "初诊的客人，请先在接待处\x01",
            "办理相关的手续。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_1BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1C64")

    #C0103
    ChrTalk(
        0xFE,
        (
            "之前送进来的那些伤员，\x01",
            "现在正在ＩＣＵ区的病房里休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "他们倒是没有性命之忧，\x01",
            "明天应该就能下地行走了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_1C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1CEF")

    #C0105
    ChrTalk(
        0xFE,
        (
            "今天送来的那些伤员，\x01",
            "总算是保住了性命。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "……从伤势状况可以看出，\x01",
            "似乎是遭受了枪击与殴打呢。\x01",
            "火药味真是相当重啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D70")
    TurnDirection(0xFE, 0x35, 0)

    #C0107
    ChrTalk(
        0xFE,
        (
            "哎呀，小朋友，你不要紧吗？\x01",
            "你好像发烧得很严重呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "把这个温度计夹在腋窝下面，\x01",
            "老老实实待一会哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_1D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1FBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F25")

    #C0109
    ChrTalk(
        0xFE,
        (
            "怎么回事，又被卷入到\x01",
            "什么纠纷中了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0006F没、没有啦……\x01",
            "并不是那么\x01",
            "严重的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "呵呵，警察弟弟真是有趣呢，\x01",
            "平常聊天时总是谈起你。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E50")

    #C0112
    ChrTalk(
        0x102,
        "#0100F呵呵，罗伊德好受欢迎啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F05")

    label("loc_1E50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EA9")

    #C0113
    ChrTalk(
        0x103,
        (
            "#0200F或许正是因为\x01",
            "有罗伊德前辈在，\x01",
            "才会发生各种各样的事件呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F05")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F05")

    #C0114
    ChrTalk(
        0x104,
        (
            "#0306F罗伊德在护士们中间\x01",
            "成为热门话题了吗？\x01",
            "真是个让人嫉妒的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F05")


    #C0115
    ChrTalk(
        0x101,
        "#0006F饶了我吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FB5")

    label("loc_1F25")


    #C0116
    ChrTalk(
        0xFE,
        "呵呵，警察弟弟真是有趣呢。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "那个……你和塞茜尔前辈\x01",
            "自那次之后又有什么进展了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0011F现、现在可不是说这些的时候，\x01",
            "我们先告辞了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB5")

    Jump("loc_28FC")

    label("loc_1FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_211F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B2")

    #C0119
    ChrTalk(
        0xFE,
        (
            "在我睡觉的时候，也经常会有急诊患者被送到，\x01",
            "然后被突然叫起来，几乎都没有休息时间呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "仔细想想，\x01",
            "像这种工作，如果不是非常喜欢的话，\x01",
            "实在是很难坚持下来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "我虽然是一个\x01",
            "没多少耐心的人，\x01",
            "但却意外地有韧性……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_211A")

    label("loc_20B2")


    #C0122
    ChrTalk(
        0xFE,
        (
            "如果不是非常喜欢的话，\x01",
            "真是很难把这项工作坚持做下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "塞茜尔前辈似乎\x01",
            "非常喜欢护士这项工作呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211A")

    Jump("loc_28FC")

    label("loc_211F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_23D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2312")

    #C0124
    ChrTalk(
        0xFE,
        (
            "里面的房间是\x01",
            "集中治疗室\x01",
            "和Ｘ光照片拍摄室。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "所谓的Ｘ光照片，\x01",
            "是我们最近同雷米菲利亚的设备制造厂商\x01",
            "共同开发的最新型医疗器材。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "它使用了特殊的感光回路，\x01",
            "是一种可以透过人体，把骨头与内脏\x01",
            "的状况映照在相片上的设备。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "只要有了它，无需开刀，\x01",
            "就可以直接发现病因了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        (
            "#0205F我之前听说过有关它的开发消息……\x01",
            "原来都已经进展到正式使用的阶段了啊。\x02\x03",

            "#0204F真不愧是乌尔斯拉医院呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0006F……哈哈，虽说我\x01",
            "只听懂了一半……\x01",
            "但也能感觉到，那是个非常厉害的东西呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23D0")

    label("loc_2312")


    #C0130
    ChrTalk(
        0xFE,
        (
            "所谓的Ｘ光照片，\x01",
            "是一种可以透过人体，把骨头与内脏\x01",
            "的状况映照在相片上的医疗器械。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "只要有了它，无需开刀，\x01",
            "就可以直接发现病因了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "……不过，关于详细的原理，\x01",
            "其实我也不怎么懂啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D0")

    Jump("loc_28FC")

    label("loc_23D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_247A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F0")
    Call(1, 23)
    Jump("loc_2475")

    label("loc_23F0")


    #C0133
    ChrTalk(
        0xFE,
        (
            "塞茜尔前辈真是个很勤劳的人。\x01",
            "不仅会把自己的工作做好，\x01",
            "还经常会给别人帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "像约亚西姆医生那样的人，\x01",
            "真应该好好向她学习啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2475")

    Jump("loc_28FC")

    label("loc_247A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_254B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FF")

    #C0135
    ChrTalk(
        0xFE,
        (
            "我在乌尔斯拉医院工作了很多年，\x01",
            "一到这个时期就很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "忙到根本没时间休息，\x01",
            "也是很平常的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2546")

    label("loc_24FF")


    #C0137
    ChrTalk(
        0xFE,
        (
            "这样一想的话，庆典第一天的时候，\x01",
            "我还休了一天假，已经很幸运了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2546")

    Jump("loc_28FC")

    label("loc_254B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_25E5")

    #C0138
    ChrTalk(
        0xFE,
        (
            "盖里教授的儿子\x01",
            "似乎混迹在克洛斯贝尔市的\x01",
            "不良团伙里……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "大概是正处于叛逆期吧。\x01",
            "我想，代沟这种东西，\x01",
            "随着时间的流逝就会慢慢消失的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_25E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2682")

    #C0140
    ChrTalk(
        0xFE,
        (
            "我去问过了塞茜尔前辈，\x01",
            "问她是不是认识彩虹剧团的\x01",
            "伊莉娅·普拉提耶。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "……结果她大大方方地直接承认了，\x01",
            "好像根本就没把它当成什么秘密呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_2682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_27B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276D")

    #C0142
    ChrTalk(
        0xFE,
        (
            "塞茜尔前辈好像\x01",
            "和一位超级名人很熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        "警察弟弟，你知道吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273B")

    #C0144
    ChrTalk(
        0x101,
        "#0005F…………是、是吗……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0145
    ChrTalk(
        0xFE,
        (
            "哦，你也不知道吗，\x01",
            "那究竟会是谁呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_273B")


    #C0146
    ChrTalk(
        0x101,
        "#0003F（……多半是指伊莉娅小姐吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_2765")

    SetScenarioFlags(0x0, 2)
    Jump("loc_27AE")

    label("loc_276D")


    #C0147
    ChrTalk(
        0xFE,
        (
            "塞茜尔前辈好像\x01",
            "和一位超级名人很熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "那究竟会是谁呢？\x02",
    )

    CloseMessageWindow()

    label("loc_27AE")

    Jump("loc_28FC")

    label("loc_27B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_282B")

    #C0149
    ChrTalk(
        0xFE,
        (
            "盖里教授的儿子\x01",
            "似乎正和一群可疑的人混在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "他明明有那么出色的父亲，\x01",
            "到底还有什么不满的呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_282B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2888")

    #C0151
    ChrTalk(
        0xFE,
        "哎呀，您是等候诊察的病人吗？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "如果您已经登记过了，\x01",
            "就请坐在这里候诊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_2888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_28C2")

    #C0153
    ChrTalk(
        0xFE,
        "……下一个接受诊察的……是那位患者吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28FC")

    label("loc_28C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_28FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28DD")
    Call(1, 5)
    Jump("loc_28FC")

    label("loc_28DD")


    #C0154
    ChrTalk(
        0xFE,
        (
            "请把这个体温计\x01",
            "夹在腋下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28FC")

    TalkEnd(0xFE)
    Return()

    # Function_4_1B81 end

    def Function_5_2900(): pass

    label("Function_5_2900")

    SetChrSubChip(0x19, 0x0)
    OP_4B(0xA, 0xFF)

    #C0155
    ChrTalk(
        0xA,
        "今天有什么地方不舒服吗？\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x19,
        (
            "啊，好像有点发烧……\x01",
            "大概是感冒了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        (
            "那么，在等待诊察的这段时间，\x01",
            "请先测量一下体温吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    SetChrSubChip(0x19, 0x0)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_5_2900 end

    def Function_6_2994(): pass

    label("Function_6_2994")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B2")
    Call(1, 11)
    Jump("loc_29C6")

    label("loc_29B2")


    #C0158
    ChrTalk(
        0xFE,
        "哇哇哇哇……！\x02",
    )

    CloseMessageWindow()

    label("loc_29C6")

    Jump("loc_2BCC")

    label("loc_29CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_29D9")
    Jump("loc_2BCC")

    label("loc_29D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_29E7")
    Jump("loc_2BCC")

    label("loc_29E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_29F5")
    Jump("loc_2BCC")

    label("loc_29F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2A03")
    Jump("loc_2BCC")

    label("loc_2A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2A11")
    Jump("loc_2BCC")

    label("loc_2A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A1F")
    Jump("loc_2BCC")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A3A")
    Call(1, 11)
    Jump("loc_2A50")

    label("loc_2A3A")


    #C0159
    ChrTalk(
        0xFE,
        "呀呀呀呀……！！\x02",
    )

    CloseMessageWindow()

    label("loc_2A50")

    Jump("loc_2BCC")

    label("loc_2A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A63")
    Jump("loc_2BCC")

    label("loc_2A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A71")
    Jump("loc_2BCC")

    label("loc_2A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A7F")
    Jump("loc_2BCC")

    label("loc_2A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9A")
    Call(1, 73)
    Jump("loc_2B6C")

    label("loc_2A9A")

    OP_4B(0x47, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0160
    ChrTalk(
        0xB,
        (
            "对了……之前那件事，\x01",
            "你考虑了没有啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x47,
        (
            "啊……是让我在研究楼\x01",
            "进行特别讲座的事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x47,
        (
            "嗯，因为临近纪念庆典，\x01",
            "现在越来越忙了，所以……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "嗯……真可惜，\x01",
            "但既然如此，我也就不勉强你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x47, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_2B6C")

    Jump("loc_2BCC")

    label("loc_2B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8C")
    Call(1, 11)
    Jump("loc_2BA2")

    label("loc_2B8C")


    #C0164
    ChrTalk(
        0xFE,
        "呜呼呼呼……！！\x02",
    )

    CloseMessageWindow()

    label("loc_2BA2")

    Jump("loc_2BCC")

    label("loc_2BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2BB5")
    Jump("loc_2BCC")

    label("loc_2BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2BC3")
    Jump("loc_2BCC")

    label("loc_2BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2BCC")

    label("loc_2BCC")

    TalkEnd(0xFE)
    Return()

    # Function_6_2994 end

    def Function_7_2BD0(): pass

    label("Function_7_2BD0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C64")
    Jump("loc_2CAE")

    label("loc_2C64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CAE")

    label("loc_2C84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CA4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CAE")

    label("loc_2CA4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CAE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2CE1")
    Jump("loc_399F")

    label("loc_2CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2EB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E45")

    #C0165
    ChrTalk(
        0xFE,
        (
            "在接待内科患者时，\x01",
            "我总是会这样想……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "像内科医术这种以促进身体自愈为主\x01",
            "的医疗方式，有时也存在效率不足的情况，\x01",
            "而此时凭借外科医术的速度优势，便有可能拯救患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "灵活地结合两种医术，互相弥补彼此的不足，\x01",
            "这才是理想中的医疗形态吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "……我与盖里教授之间可以说是水火不容，\x01",
            "所以从我嘴里说出这样的话，或许有点奇怪吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2EB4")

    label("loc_2E45")


    #C0169
    ChrTalk(
        0xFE,
        (
            "……咳咳！啊，算啦。\x01",
            "你就把我刚才说的话给忘掉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "……我刚才说的话，\x01",
            "无论如何也不能\x01",
            "告诉盖里教授哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB4")

    Jump("loc_399F")

    label("loc_2EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2F34")

    #C0171
    ChrTalk(
        0xFE,
        (
            "咳咳！\x01",
            "盖里教授那家伙，好像用外科手术\x01",
            "顺利救助了今早的那些伤员呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "……哼，外科医术\x01",
            "倒也有点用啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399F")

    label("loc_2F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2FBD")

    #C0173
    ChrTalk(
        0xFE,
        (
            "约亚西姆最近似乎\x01",
            "总是在研究室里埋头研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "虽说他平时总有偷懒的坏习惯，\x01",
            "但在专业研究方面，\x01",
            "却是个很能干的男人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399F")

    label("loc_2FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3014")

    #C0175
    ChrTalk(
        0xFE,
        "嗯……你们那么着急做什么？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "除了患者以外，\x01",
            "谁也没有来过这里哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399F")

    label("loc_3014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_31A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3120")

    #C0177
    ChrTalk(
        0xFE,
        (
            "咳咳！\x01",
            "干什么？你们几个。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#0005F那个，我们稍微有些事情，\x01",
            "要来找神经·药物学科的……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "啊，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "神经·药物学科确实是\x01",
            "属于内科的范畴，\x01",
            "但说到底，也还只是研究中的领域。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "要是有什么事的话，\x01",
            "直接去找约亚西姆就可以了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_319F")

    label("loc_3120")


    #C0182
    ChrTalk(
        0xFE,
        (
            "神经·药物学科确实是\x01",
            "属于内科的范畴，\x01",
            "但说到底，也还只是研究中的领域。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "要是有什么事的话，\x01",
            "直接去找约亚西姆就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319F")

    Jump("loc_399F")

    label("loc_31A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_31B2")
    Jump("loc_399F")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_31C0")
    Jump("loc_399F")

    label("loc_31C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_32F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328E")

    #C0184
    ChrTalk(
        0xFE,
        (
            "前段时间，\x01",
            "我试着把内科的诊断工作\x01",
            "托付给了古恩。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "她的技术水平虽然无可挑剔，\x01",
            "但对患者的关怀却还不够……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "为了不辱乌尔斯拉医院的\x01",
            "实习医生之名，\x01",
            "我希望她能更上一层楼。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32EF")

    label("loc_328E")


    #C0187
    ChrTalk(
        0xFE,
        (
            "如果想掌握确切的病情，\x01",
            "就需要拥有能与患者\x01",
            "良好沟通的能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "古恩在那方面\x01",
            "还不够成熟呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32EF")

    Jump("loc_399F")

    label("loc_32F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3370")

    #C0189
    ChrTalk(
        0xFE,
        (
            "自从纪念庆典开始之后，\x01",
            "实习医生们似乎就\x01",
            "有些松懈呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "嗯哼！\x01",
            "这种时候，就要给他们\x01",
            "一记当头棒喝才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399F")

    label("loc_3370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_35D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F5")

    #C0191
    ChrTalk(
        0xFE,
        (
            "给你们添了不少\x01",
            "麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "我马上还要讲课，\x01",
            "下次有机会再聊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "以后也请多多关照。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_345B")

    label("loc_33F5")


    #C0194
    ChrTalk(
        0xFE,
        (
            "在七耀教会学习的日子，\x01",
            "真是让人难以忘怀。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "以后得找个时间去向艾拉尔达\x01",
            "大主教表示感谢才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_345B")

    Jump("loc_35CF")

    label("loc_3460")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3475")
    Call(1, 75)
    Jump("loc_35CF")

    label("loc_3475")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3526")

    #C0196
    ChrTalk(
        0xFE,
        (
            "请去克洛斯贝尔大圣堂，\x01",
            "帮我向艾拉尔达大主教\x01",
            "要来『羽扇豆草』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "对了，我事先提醒一下……\x01",
            "大主教可是比我还要难相处的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "一定不能有失礼节啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35CF")

    label("loc_3526")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_353A")
    Call(1, 74)
    Jump("loc_35CF")

    label("loc_353A")


    #C0199
    ChrTalk(
        0xFE,
        (
            "……唔，只是这种无关紧要的请求，\x01",
            "他们真的会来吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "果然还是应该\x01",
            "去拜托游击士吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "不过，我又不想因为这种\x01",
            "程度的小事而花费米拉……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35CF")

    Jump("loc_399F")

    label("loc_35D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_35E2")
    Jump("loc_399F")

    label("loc_35E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_35F0")
    Jump("loc_399F")

    label("loc_35F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_367C")

    #C0202
    ChrTalk(
        0xFE,
        (
            "那天，让利顿\x01",
            "交报告的人是我……\x01",
            "真没想到会发生那样的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "嗯，其他的实习医生\x01",
            "没有再遭到袭击，\x01",
            "真是不幸中的万幸啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399F")

    label("loc_367C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3881")

    #C0204
    ChrTalk(
        0xFE,
        (
            "嗯哼！……有什么事吗？\x01",
            "你们好像不是这里的学生啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "……嗯，仔细一看的话，\x01",
            "似乎都是很聪明的孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "你们几个，要不要来挑战一下\x01",
            "明年的入学考试呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        (
            "#0305F噢！原来我们还有这种潜质吗！\x02\x03",

            "#0304F医生兰迪华丽的\x01",
            "护士后宫生活……\x01",
            "听起来好像很不错呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#0006F喂喂……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x102,
        (
            "#0111F话说回来，这间乌尔斯拉医院\x01",
            "也从邻国吸引了很多考生，\x01",
            "接受考试的人数可是非常多的。\x02\x03",

            "#0103F去年的录取率……\x01",
            "好像是一百二十分之一吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        "#0303F这么难啊，那还是放弃吧。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x103,
        "#0211F……放弃得真干脆。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3991")

    label("loc_3881")


    #C0212
    ChrTalk(
        0xFE,
        (
            "这间乌尔斯拉医院，\x01",
            "是一家连医疗大国雷米菲利亚也敬畏三分\x01",
            "的最尖端医疗研究所。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔本地就不必说了，\x01",
            "埃雷波尼亚帝国、卡尔瓦德共和国、\x01",
            "雷米菲利亚公国以及利贝尔王国……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "各国的优秀年轻人都以这里为目标，\x01",
            "经过拼命学习，并通过严格的考试，\x01",
            "才能得到入学的机会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3991")

    Jump("loc_399F")

    label("loc_3996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_399F")

    label("loc_399F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_2BD0 end

    def Function_8_39A7(): pass

    label("Function_8_39A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_39B8")
    Jump("loc_4207")

    label("loc_39B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3A1D")

    #C0215
    ChrTalk(
        0xFE,
        (
            "据说，今天用急救车送来的那些伤员\x01",
            "已经恢复意识了。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "本院医生的水平真是一流呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_3A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A2B")
    Jump("loc_4207")

    label("loc_3A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3AFE")

    #C0217
    ChrTalk(
        0xFE,
        (
            "前段时间，我又参加了\x01",
            "临床实习……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "我尽可能用\x01",
            "最温和的态度来接触患者，\x01",
            "结果，评价从Ｂ－变成了Ｂ＋呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "虽然只是很小的进步……\x01",
            "不过，距离我成为内科医生的梦想，\x01",
            "总算是又向前迈进了一步。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_3AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE7")

    #C0220
    ChrTalk(
        0xFE,
        (
            "刚才拉格教授在为病人诊察，\x01",
            "我看着他时，\x01",
            "忽然注意到一件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "就连那个难以相处的教授，\x01",
            "在患者面前也都会\x01",
            "表现得那么耐心和蔼……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "仔细想想，\x01",
            "我原来只注重技术方面的评价，\x01",
            "却忽视了这个重要的部分啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3C5C")

    label("loc_3BE7")


    #C0223
    ChrTalk(
        0xFE,
        (
            "就连那个坏脾气的拉格教授，\x01",
            "在患者的面前也都会\x01",
            "表现得那么耐心和蔼……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "我所缺少的东西，\x01",
            "大概就是那种态度吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5C")

    Jump("loc_4207")

    label("loc_3C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0E")

    #C0225
    ChrTalk(
        0xFE,
        (
            "拉格教授\x01",
            "给我的评价\x01",
            "总是不高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "就算我去问他到底有什么不足，\x01",
            "他也只会说『自己去体会』。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "可恶，既然如此，\x01",
            "我平时就要多观察教授了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3D62")

    label("loc_3D0E")


    #C0228
    ChrTalk(
        0xFE,
        (
            "既然如此，\x01",
            "我就来观察拉格教授好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "无论如何我也要找出\x01",
            "得到好评价的秘诀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D62")

    Jump("loc_4207")

    label("loc_3D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3DF7")

    #C0230
    ChrTalk(
        0xFE,
        (
            "教授今天不在，\x01",
            "所以必须努力和利顿配合，\x01",
            "把工作做好才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "但是……\x01",
            "这好像和评定分数没什么关系，\x01",
            "做起来真是没什么动力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_3DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7D")

    #C0232
    ChrTalk(
        0xFE,
        "那两位教授，彼此之间的关系很差呢。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "真搞不懂，两人在各方面都那么相似，\x01",
            "为什么就是看对方不顺眼呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3ED3")

    label("loc_3E7D")


    #C0234
    ChrTalk(
        0xFE,
        (
            "不过，毕竟没有像某些医院那样，\x01",
            "内外科之间还进行着龌龊的党派斗争……\x01",
            "也还算好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED3")

    Jump("loc_4207")

    label("loc_3ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F80")

    #C0235
    ChrTalk(
        0xFE,
        "昨天有临床实践呢。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "虽然我个人觉得\x01",
            "自己做得不错。\x01",
            "但教授却给了我Ｂ－的评价……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "可恶，通往女强人医生的\x01",
            "道路真是意外地艰难呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3FF9")

    label("loc_3F80")


    #C0238
    ChrTalk(
        0xFE,
        (
            "这几天的临床实习……\x01",
            "虽然我个人觉得\x01",
            "自己的表现足以拿到Ａ＋评价。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "但最后竟然是Ｂ－啊……\x01",
            "一定要继续努力才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF9")

    Jump("loc_4207")

    label("loc_3FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_400C")
    Jump("loc_4207")

    label("loc_400C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_401A")
    Jump("loc_4207")

    label("loc_401A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_40A7")

    #C0240
    ChrTalk(
        0xFE,
        (
            "利顿的伤好像已经治好了，\x01",
            "正在干劲十足地工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "但是，因为他太过努力，\x01",
            "好像连约亚西姆医生也把工作\x01",
            "都推到他身上了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_40A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_40DD")
    OP_93(0xFE, 0xB4, 0x0)

    #C0242
    ChrTalk(
        0xFE,
        (
            "教、教授～！\x01",
            "请冷静一点啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_40DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4187")

    #C0243
    ChrTalk(
        0xFE,
        (
            "不过，利顿\x01",
            "也真是不走运呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "好不容易把报告写好了，\x01",
            "竟然遇到了那样的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "居然会在自己学习的地方住院，\x01",
            "他一定没想到\x01",
            "自己会遇到这样的倒霉事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_4187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_41FE")

    #C0246
    ChrTalk(
        0xFE,
        (
            "由于利顿受伤的缘故，\x01",
            "轮值变得更加辛苦了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "说是被魔兽袭击了，\x01",
            "但到底是真的假的啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_41FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4207")

    label("loc_4207")

    TalkEnd(0xFE)
    Return()

    # Function_8_39A7 end

    def Function_9_420B(): pass

    label("Function_9_420B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4244")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4229")
    Call(1, 11)
    Jump("loc_423F")

    label("loc_4229")


    #C0248
    ChrTalk(
        0xFE,
        "哇哦哦哦哦……！\x02",
    )

    CloseMessageWindow()

    label("loc_423F")

    Jump("loc_4365")

    label("loc_4244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4252")
    Jump("loc_4365")

    label("loc_4252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4260")
    Jump("loc_4365")

    label("loc_4260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_426E")
    Jump("loc_4365")

    label("loc_426E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_427C")
    Jump("loc_4365")

    label("loc_427C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_428A")
    Jump("loc_4365")

    label("loc_428A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4298")
    Jump("loc_4365")

    label("loc_4298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_42D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42B3")
    Call(1, 11)
    Jump("loc_42CB")

    label("loc_42B3")


    #C0249
    ChrTalk(
        0xFE,
        "哦呀呀呀呀……！！\x02",
    )

    CloseMessageWindow()

    label("loc_42CB")

    Jump("loc_4365")

    label("loc_42D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42DE")
    Jump("loc_4365")

    label("loc_42DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_42EC")
    Jump("loc_4365")

    label("loc_42EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_42FA")
    Jump("loc_4365")

    label("loc_42FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4308")
    Jump("loc_4365")

    label("loc_4308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4323")
    Call(1, 11)
    Jump("loc_433B")

    label("loc_4323")


    #C0250
    ChrTalk(
        0xFE,
        "哇呀呀呀呀……！！\x02",
    )

    CloseMessageWindow()

    label("loc_433B")

    Jump("loc_4365")

    label("loc_4340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_434E")
    Jump("loc_4365")

    label("loc_434E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_435C")
    Jump("loc_4365")

    label("loc_435C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4365")

    label("loc_4365")

    TalkEnd(0xFE)
    Return()

    # Function_9_420B end

    def Function_10_4369(): pass

    label("Function_10_4369")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43FD")
    Jump("loc_4447")

    label("loc_43FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_441D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4447")

    label("loc_441D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_443D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4447")

    label("loc_443D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4447")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_447A")
    Jump("loc_5042")

    label("loc_447A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B5")

    #C0251
    ChrTalk(
        0xFE,
        (
            "今天早上救治重伤患者的时候……\x01",
            "不，其实我一直都在考虑\x01",
            "这个问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "即使是在外科的治疗现场，\x01",
            "也必须要有麻醉及\x01",
            "点滴之类的内科医疗技术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "我想，只有外科与内科\x01",
            "携手合作、互相弥补，\x01",
            "才是最理想的医疗状态吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "……但我和拉格教授\x01",
            "总是吵个没完，\x01",
            "说出这样的话，或许有点奇怪吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4620")

    label("loc_45B5")


    #C0255
    ChrTalk(
        0xFE,
        (
            "……咳咳！\x01",
            "一不小心说漏嘴了，\x01",
            "讲出了不该讲的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "听好，刚才那些话可千万不能\x01",
            "透露给拉格教授哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4620")

    Jump("loc_5042")

    label("loc_4625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_473C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46D1")

    #C0257
    ChrTalk(
        0xFE,
        (
            "就在刚才，从克洛斯贝尔市那边\x01",
            "送来了几名急救患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "我和约亚西姆他们一起\x01",
            "为患者做了些基本处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "呼，真是累坏了。\x01",
            "我也上年纪了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4737")

    label("loc_46D1")


    #C0260
    ChrTalk(
        0xFE,
        (
            "从克洛斯贝尔市送来一些急救患者，\x01",
            "总算是做完了基本处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "呼，真是累坏了。\x01",
            "我也上年纪了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4737")

    Jump("loc_5042")

    label("loc_473C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_48A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_481C")

    #C0262
    ChrTalk(
        0xFE,
        (
            "趁着还没忘记的时候，\x01",
            "不断复习学过的东西，\x01",
            "就能让它变成长期记忆。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "也就是说，作为『知识』\x01",
            "清晰地刻在脑子里。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "我们这里的实习医生之所以很优秀，\x01",
            "或许就是得益于养成了经常复习的\x01",
            "好习惯吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_489C")

    label("loc_481C")


    #C0265
    ChrTalk(
        0xFE,
        (
            "趁着还没忘记的时候，\x01",
            "不断复习学过的东西，\x01",
            "它就会变成『知识』，储藏在脑海里。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        "……哈，这也是从约亚西姆那里现学现卖的。\x02",
    )

    CloseMessageWindow()

    label("loc_489C")

    Jump("loc_5042")

    label("loc_48A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_49C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4953")

    #C0267
    ChrTalk(
        0xFE,
        (
            "护士刚才通知我说，\x01",
            "我儿子琴兹\x01",
            "来医院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "大概是我妻子让他来送饭，\x01",
            "他才会过来的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "虽然他现在可能\x01",
            "正在满嘴抱怨……\x01",
            "但我还是非常高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_49BF")

    label("loc_4953")


    #C0270
    ChrTalk(
        0xFE,
        (
            "我儿子琴兹\x01",
            "好像来医院\x01",
            "给我送饭了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "我真是很高兴啊。\x01",
            "呵呵，这样的表情，\x01",
            "可不能让拉格教授看见啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49BF")

    Jump("loc_5042")

    label("loc_49C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4A51")

    #C0272
    ChrTalk(
        0xFE,
        (
            "在病房楼楼顶的那个研究楼里，\x01",
            "保存着在至今为止的研究中\x01",
            "所得到的贵重资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "如果没有必要，\x01",
            "我希望外部人员最好不要进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5042")

    label("loc_4A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4A5F")
    Jump("loc_5042")

    label("loc_4A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4A6D")
    Jump("loc_5042")

    label("loc_4A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4B86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B25")

    #C0274
    ChrTalk(
        0xFE,
        (
            "……克洛斯贝尔市昨天发生的那起骚乱，\x01",
            "我的儿子琴兹似乎也参加了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "多亏有警察的干预，\x01",
            "好像并没有人受伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "……唉……\x01",
            "真希望他能让我少操点心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B81")

    label("loc_4B25")


    #C0277
    ChrTalk(
        0xFE,
        (
            "本来应该要好好教训他一番，\x01",
            "但我却无法到场……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "……唉……\x01",
            "我真是个不称职的父亲啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B81")

    Jump("loc_5042")

    label("loc_4B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4C1B")

    #C0279
    ChrTalk(
        0xFE,
        (
            "我本来打算明天和儿子一起去看\x01",
            "彩虹剧团的演出……\x01",
            "但目前看来，应该是去不成了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "……竟然去讨好孩子，\x01",
            "身为父亲，我真是很失败。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5042")

    label("loc_4C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4DF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D19")
    SetChrSubChip(0xFE, 0x0)

    #C0281
    ChrTalk(
        0xFE,
        (
            "在上上个月，那群不良团伙的成员\x01",
            "不是被送到医院了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "我当时很担心伤员中会不会有我儿子琴兹，\x01",
            "吓得脊背发凉。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "……明明发生了那样的事情，\x01",
            "他却还要继续\x01",
            "留在不良团伙里面……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "真是的，真希望\x01",
            "他能让我少操点心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4DEB")

    label("loc_4D19")


    #C0285
    ChrTalk(
        0xFE,
        (
            "……我在儿子心中的形象\x01",
            "似乎并不怎么好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "一直以来，我因为工作繁忙的缘故，\x01",
            "总是待在医院，很少在家里陪伴家人，\x01",
            "所以才得不到儿子的尊敬吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "我儿子会成为不良团伙的成员，\x01",
            "我或许应该承担一部分责任……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DEB")

    Jump("loc_5042")

    label("loc_4DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0B")
    Call(1, 12)
    Jump("loc_4E71")

    label("loc_4E0B")

    SetChrSubChip(0xFE, 0x0)

    #C0288
    ChrTalk(
        0xFE,
        (
            "听好了，阿修拉。\x01",
            "你已经是负责教授\x01",
            "机械医疗课程的主任了，\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        "总保持这种学生的心态可不行哦。\x02",
    )

    CloseMessageWindow()

    label("loc_4E71")

    Jump("loc_5042")

    label("loc_4E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4E84")
    Jump("loc_5042")

    label("loc_4E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F48")

    #C0290
    ChrTalk(
        0xFE,
        (
            "所谓外科，就是在近年\x01",
            "逐渐普及开来的\x01",
            "一种近代医疗手段。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "但是，不管怎么说，\x01",
            "它还是一种新技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "用手术刀割开身体，\x01",
            "这样的事，直到现在\x01",
            "也难以得到大众的理解。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4FD6")

    label("loc_4F48")


    #C0293
    ChrTalk(
        0xFE,
        (
            "包括那个拉格教授在内，\x01",
            "对外科医术持有偏见的人\x01",
            "并不在少数，这便是现状。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "不过，那种跟不上近代医疗\x01",
            "进化速度的落伍老头，\x01",
            "我才懒得理呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD6")

    Jump("loc_5042")

    label("loc_4FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5039")

    #C0295
    ChrTalk(
        0xFE,
        (
            "阿修拉……\x01",
            "今天好像也迟到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "都多少次了，总是不知悔改。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5042")

    label("loc_5039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5042")

    label("loc_5042")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_4369 end

    def Function_11_504A(): pass

    label("Function_11_504A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xB, 0xE, 0)
    TurnDirection(0xE, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_517A")

    #C0297
    ChrTalk(
        0xB,
        (
            "嗯哼！\x01",
            "我还以为是谁呢，这不是盖里教授嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xE,
        "哎呀，原来是拉格教授。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "……啊，对了。\x01",
            "关于昨天那个重伤患者的处理……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xE,
        (
            "啊呀，您已经听说了\x01",
            "我昨天的成果了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xE,
        (
            "哼哼哼，你们内科的时代\x01",
            "就快要面临终结了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        "#4S……你说什么！？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xE,
        "#4S……想打架吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_557E")

    label("loc_517A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_5188")
    Jump("loc_557E")

    label("loc_5188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5196")
    Jump("loc_557E")

    label("loc_5196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_51A4")
    Jump("loc_557E")

    label("loc_51A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_51B2")
    Jump("loc_557E")

    label("loc_51B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_51C0")
    Jump("loc_557E")

    label("loc_51C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_51CE")
    Jump("loc_557E")

    label("loc_51CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5376")

    #C0304
    ChrTalk(
        0xB,
        (
            "嗯哼！我还以为是谁呢，\x01",
            "这不是盖里教授嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xB,
        (
            "您那脏兮兮的胡子，\x01",
            "今天也给医生的形象抹黑了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xE,
        (
            "哎呀呀，\x01",
            "拉格教授您也不逊色啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xE,
        (
            "您那好像被野火烧尽一样的秃头，\x01",
            "竟然还没有春风吹又生，真是让人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xB,
        (
            "……您那难看的胡子……\x01",
            "就用您擅长的外科手术，\x01",
            "把它永久拔除如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xE,
        (
            "……您那荒芜的头顶才是呢，\x01",
            "您对内科医疗这么拿手，\x01",
            "怎么就没让它恢复茂密啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        "#4S……你说什么！？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xE,
        "#4S……想打架吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_557E")

    label("loc_5376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5384")
    Jump("loc_557E")

    label("loc_5384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5392")
    Jump("loc_557E")

    label("loc_5392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_53A0")
    Jump("loc_557E")

    label("loc_53A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_53AE")
    Jump("loc_557E")

    label("loc_53AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5559")

    #C0312
    ChrTalk(
        0xB,
        (
            "嗯哼！\x01",
            "……那张肮脏的胡子脸，我还以为是谁呢，\x01",
            "这不是盖里教授嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xE,
        (
            "哎呀呀，原来是拉格教授啊。\x01",
            "哎呀，您的光头今天也亮得刺眼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xB,
        (
            "……哼！\x01",
            "真是让人叹息啊，\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "那些前途无量的实习医生们竟然要\x01",
            "向您这样的人学习用刀子切人的手法。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xE,
        (
            "……哼！\x01",
            "这么说来，您可真是轻松呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xE,
        (
            "有了七耀教会遗留的，现成的过时技术……\x01",
            "光凭这点本事，就能摆出资深教授的架子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xB,
        "#4S……你说什么！？\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xE,
        "#4S……想打架吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_557E")

    label("loc_5559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5567")
    Jump("loc_557E")

    label("loc_5567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5575")
    Jump("loc_557E")

    label("loc_5575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_557E")

    label("loc_557E")

    SetScenarioFlags(0x0, 5)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_11_504A end

    def Function_12_558A(): pass

    label("Function_12_558A")

    OP_4B(0x13, 0xFF)
    SetChrSubChip(0xF, 0x0)
    TurnDirection(0x13, 0xF, 0)

    #C0320
    ChrTalk(
        0xF,
        (
            "阿修拉……\x01",
            "你又迟到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xF,
        (
            "都已经是讲课的老师了，\x01",
            "竟然还迟到，真是岂有此理！\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x13,
        "非、非常抱歉……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x13,
        (
            "我昨天光顾着研究新到的器材，\x01",
            "结果完全入迷了，不知不觉就\x01",
            "研究了一整夜。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x13,
        (
            "然后稍微小睡了一下，\x01",
            "结果一直睡到刚才……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xF,
        (
            "……呼……\x01",
            "你和学生时代相比，\x01",
            "真是完全没有变化呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_12_558A end

    def Function_13_56C7(): pass

    label("Function_13_56C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_57D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5793")
    TurnDirection(0xFE, 0x14, 0)

    #C0326
    ChrTalk(
        0xFE,
        (
            "阿修拉主任……\x01",
            "不管怎么说，在这里\x01",
            "睡觉还是不太好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "哎呀，趁盖里教授他们\x01",
            "吵架结束之前，要快点起来才行……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x14,
        "嗯～嗯……再睡五分钟……\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        "还是不行啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_57D2")

    label("loc_5793")


    #C0330
    ChrTalk(
        0xFE,
        (
            "没办法，最后还是\x01",
            "纵容了阿修拉主任呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        "她困得不行……\x02",
    )

    CloseMessageWindow()

    label("loc_57D2")

    Jump("loc_61AA")

    label("loc_57D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_5950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58C2")

    #C0332
    ChrTalk(
        0xFE,
        (
            "阿修拉主任最活跃\x01",
            "的研究时间，\x01",
            "毫无疑问是在晚上。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "……只不过，出于这个原因，\x01",
            "主任变成了睡懒觉大王，\x01",
            "这也是事实。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "虽然拥有副教授的头衔，\x01",
            "但在她身上却感觉不到主任的威严，\x01",
            "或许就是因为这个缘故吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_594B")

    label("loc_58C2")


    #C0335
    ChrTalk(
        0xFE,
        (
            "阿修拉主任就是所谓的夜猫子呢，\x01",
            "因此也是个睡懒觉大王。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "虽然拥有副教授的头衔，\x01",
            "但却感觉不到主任的威严，\x01",
            "或许就是因为这个缘故吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_594B")

    Jump("loc_61AA")

    label("loc_5950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_59F8")

    #C0337
    ChrTalk(
        0xFE,
        (
            "虽然器械的开发很困难，\x01",
            "但能使用新技术\x01",
            "也是乐趣所在。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "一想到在这里研发出来的医疗器械\x01",
            "将会在未来的医疗领域中发挥巨大作用，\x01",
            "就不由自主地心潮澎湃。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_59F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5A7E")

    #C0339
    ChrTalk(
        0xFE,
        (
            "哎呀……真希望阿修拉主任\x01",
            "别再硬撑了，继续睡懒觉去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "话说回来，她毕竟都熬了快一个通宵，\x01",
            "早上很难起得来吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_5A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_5AF9")

    #C0341
    ChrTalk(
        0xFE,
        (
            "阿修拉主任睡懒觉\x01",
            "是预料之中的事情……\x01",
            "事到如今，连教授都懒得再生气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "呼，我也耐心地\x01",
            "等着她来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_5AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5B61")

    #C0343
    ChrTalk(
        0xFE,
        (
            "……阿修拉主任今天好像\x01",
            "又睡懒觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "没办法，今天研究的准备工作\x01",
            "就让我来做吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_5B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5BDE")

    #C0345
    ChrTalk(
        0xFE,
        (
            "盖里教授和阿修拉主任\x01",
            "不在的时候，\x01",
            "这间诊察室真是冷清呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "现在有些人手不足，\x01",
            "要不要把芙萝拉叫来呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_5BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5C74")

    #C0347
    ChrTalk(
        0xFE,
        (
            "……一切都和往日没有任何不同，\x01",
            "根本感觉不到自己处在纪念庆典中呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "看样子，就算我去劝解应该也没用，\x01",
            "不如还是去找本书看看吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_5C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5C82")
    Jump("loc_61AA")

    label("loc_5C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5D0C")

    #C0349
    ChrTalk(
        0xFE,
        "……已经是纪念庆典的第二天了吧，\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "我陪着阿修拉主任进行了\x01",
            "三天三夜的研究，一直没有睡觉，\x01",
            "所以都不太清楚日期了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_5D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5DD1")

    #C0351
    ChrTalk(
        0xFE,
        (
            "阿修拉主任的职位虽然是\x01",
            "『主任』，但实际地位\x01",
            "却相当于副教授。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "但是，比起去传道授业，\x01",
            "主任更愿意闷在研究室\x01",
            "里面搞开发呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "在某种意义上说，\x01",
            "或许算是个地位很特殊的人物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_5DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EB2")

    #C0354
    ChrTalk(
        0xFE,
        (
            "目前，诸多国家都在致力于开发\x01",
            "各式各样的导力器，其中，医疗器械的研究\x01",
            "还是要属雷米菲利亚公国的技术最为尖端。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "在这所医院中所使用的医疗器械，\x01",
            "也几乎都是由雷米菲利亚公国的\x01",
            "赛兰德公司所制造的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5F68")

    label("loc_5EB2")


    #C0356
    ChrTalk(
        0xFE,
        (
            "说起赛兰德公司，\x01",
            "可是整个大陆中首屈一指的医疗器械制造商，\x01",
            "同时也是这所医院的赞助商之一呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "所谓的医疗器械科，\x01",
            "主要工作就是将医疗器械进行临床应用，\x01",
            "同时摸索它们的改良余地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F68")

    Jump("loc_61AA")

    label("loc_5F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5F7B")
    Jump("loc_61AA")

    label("loc_5F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_60E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_605C")

    #C0358
    ChrTalk(
        0xFE,
        (
            "在这栋研究楼中，\x01",
            "正在研究着最先进的\x01",
            "医疗技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "特别是『医疗器械科』，\x01",
            "正在日夜不停地研究着\x01",
            "运用导力的医疗器械。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "……医疗器械科中有位阿修拉主任，\x01",
            "今天还没来上班，\x01",
            "她是那里的一把手呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_60E2")

    label("loc_605C")


    #C0361
    ChrTalk(
        0xFE,
        (
            "医疗器械的研究工作，比所谓的\x01",
            "近代医学领域——外科还要更加高深……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "你能想象在这个部门担任一把手的\x01",
            "阿修拉主任有多么优秀了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60E2")

    Jump("loc_61AA")

    label("loc_60E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_61A1")

    #C0363
    ChrTalk(
        0xFE,
        (
            "我的梦想，就是在祖国埃雷波尼亚帝国\x01",
            "建立一所大医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "这所乌尔斯拉医院\x01",
            "正是最适合实现\x01",
            "这个梦想的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "因为这里拥有最尖端的医学技术，\x01",
            "并汇聚了最优秀的医生呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AA")

    label("loc_61A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_61AA")

    label("loc_61AA")

    TalkEnd(0xFE)
    Return()

    # Function_13_56C7 end

    def Function_14_61AE(): pass

    label("Function_14_61AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61C3")
    Call(1, 16)
    Jump("loc_6272")

    label("loc_61C3")


    #C0366
    ChrTalk(
        0x11,
        (
            "#2400F虽然我也会帮忙查房，\x01",
            "不过日常工作还是以研究为主。\x02\x03",

            "以现在的状况来看，似乎是一直在给\x01",
            "贝尔达因医生增加负担呢。\x02\x03",

            "#2406F利顿可要尽快恢复过来，\x01",
            "给我精精神神地干活才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6272")

    TalkEnd(0xFE)
    Return()

    # Function_14_61AE end

    def Function_15_6276(): pass

    label("Function_15_6276")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_628B")
    Call(1, 16)
    Jump("loc_62EB")

    label("loc_628B")


    #C0367
    ChrTalk(
        0xFE,
        (
            "我接待了一位病情比较复杂的患者，\x01",
            "刚刚才结束了诊察工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "……呼……\x01",
            "去食堂喝杯红茶吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62EB")

    TalkEnd(0xFE)
    Return()

    # Function_15_6276 end

    def Function_16_62EF(): pass

    label("Function_16_62EF")

    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0369
    ChrTalk(
        0x11,
        (
            "#2400F贝尔达因医生，\x01",
            "您好像是累坏了啊。\x02\x03",

            "不介意的话，给您开一剂\x01",
            "添加了蜂王浆的营养剂如何？\x02\x03",

            "#2409F那可是阿尔摩利卡产的东西，\x01",
            "效果很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x12,
        "啊，还是算了吧。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x12,
        (
            "因为你的营养剂实在是太有效果了。\x01",
            "要是产生了依赖性可就麻烦啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_16_62EF end

    def Function_17_63FB(): pass

    label("Function_17_63FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_640C")
    Jump("loc_6E48")

    label("loc_640C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_649C")

    #C0372
    ChrTalk(
        0xFE,
        "哼哼哼哼……¤\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "呵呵，一到了晚上就睡不着，\x01",
            "工作效率反倒会提升呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "很好，从现在开始的十二个小时……\x01",
            "要好好干活啦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E48")

    label("loc_649C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_65CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_654D")

    #C0375
    ChrTalk(
        0xFE,
        (
            "对于医疗类导力器的开发而言，\x01",
            "首先应该保证的就是安全性。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "既然作用对象是人体，\x01",
            "就绝对不能出现什么差错。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        "这就是开发医疗器械的困难之处吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_65CA")

    label("loc_654D")


    #C0378
    ChrTalk(
        0xFE,
        (
            "对于医疗类导力器的开发而言，\x01",
            "安全性比什么都重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "有关对人体影响的确切数据，\x01",
            "并不一定仅仅通过小白鼠实验\x01",
            "就能得到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65CA")

    Jump("loc_6E48")

    label("loc_65CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_68A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_665C")

    #C0380
    ChrTalk(
        0xFE,
        (
            "啊，那个挂坠扣\x01",
            "派上什么用场了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "那是用即使被魔兽踩踏也不会损坏\x01",
            "的耐久型合金制成的，\x01",
            "一定能保存很久呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68A0")

    label("loc_665C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6703")

    #C0382
    ChrTalk(
        0xFE,
        (
            "那个挂坠扣可是非常结实的东西，\x01",
            "它曾被卷入到实验失败时的爆炸中，\x01",
            "但也仍然完好无损呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "运气这么好的东西，\x01",
            "一定非常适合当作制作礼物的材料呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68A0")

    label("loc_6703")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6717")
    Call(1, 78)
    Jump("loc_68A0")

    label("loc_6717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_680F")

    #C0384
    ChrTalk(
        0xFE,
        (
            "我总是睡懒觉，\x01",
            "经常给夏鲁鲁添麻烦，\x01",
            "所以从上周开始就想努力早起。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "早晨设定十二个闹铃，\x01",
            "我差不多就能起床了……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "哎呀，就算熬了将近一通宵，\x01",
            "只要努努力，也还是可以起来的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0387
    ChrTalk(
        0xFE,
        "………………唔。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_68A0")

    label("loc_680F")


    #C0388
    ChrTalk(
        0xFE,
        "………………呼。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "啊、啊啊……我可没睡着哦！\x01",
            "只是稍微有点累了而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        "好、好啦！今天也要努力地研究研究再研究！\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        "………………唔。\x02",
    )

    CloseMessageWindow()

    label("loc_68A0")

    Jump("loc_6E48")

    label("loc_68A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_68B3")
    Jump("loc_6E48")

    label("loc_68B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_68C1")
    Jump("loc_6E48")

    label("loc_68C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_68CF")
    Jump("loc_6E48")

    label("loc_68CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_68DD")
    Jump("loc_6E48")

    label("loc_68DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6A04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69C0")
    OP_93(0xFE, 0x5A, 0x0)

    #C0392
    ChrTalk(
        0xFE,
        "…………啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0393
    ChrTalk(
        0xFE,
        "那、那个，开始讲课了哦。\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "今天的课程是关于\x01",
            "医疗器械中使用的结晶回路的构造……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#0006F那个……\x01",
            "我们并不是这里的学生……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        "#0100F好像是睡迷糊了呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    BeginChrThread(0x13, 0, 0, 0)
    Jump("loc_69FF")

    label("loc_69C0")


    #C0397
    ChrTalk(
        0xFE,
        (
            "啊……那个……对不起。\x01",
            "授课的时候，外部人员是禁止入内的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69FF")

    Jump("loc_6E48")

    label("loc_6A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6ADD")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A91")

    #C0398
    ChrTalk(
        0xFE,
        "……呼～……呼～…………\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        "#0005F站、站着就睡着了……！？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x103,
        (
            "#0200F真厉害啊，\x01",
            "真想学会这个绝技。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6AD8")

    label("loc_6A91")


    #C0401
    ChrTalk(
        0xFE,
        (
            "……呼～……呼～…………\x01",
            "……呼噜。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        "……呼～……呼～…………\x02",
    )

    CloseMessageWindow()

    label("loc_6AD8")

    Jump("loc_6E48")

    label("loc_6ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6C7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BF6")

    #C0403
    ChrTalk(
        0xFE,
        (
            "我身为一个技术人员，\x01",
            "有个非常尊敬的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "那就是利贝尔·ＺＣＦ的\x01",
            "艾莉卡·拉塞尔博士……\x01",
            "也就是那个有名的Ａ·拉塞尔博士的女儿。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "她虽然身为女性，\x01",
            "却拥有利贝尔王国\x01",
            "最顶级的技术知识……\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "身为一名女医生，我也想在医疗器械\x01",
            "领域建立伟大的功绩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6C79")

    label("loc_6BF6")


    #C0407
    ChrTalk(
        0xFE,
        (
            "利贝尔的艾莉卡博士……\x01",
            "她是足以与Ａ·拉塞尔博士比肩的\x01",
            "优秀技术员。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "身为一名女医生，我也想在医疗器械\x01",
            "领域建立伟大的功绩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C79")

    Jump("loc_6E48")

    label("loc_6C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6D25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C99")
    Call(1, 12)
    Jump("loc_6D20")

    label("loc_6C99")


    #C0409
    ChrTalk(
        0xFE,
        (
            "（唔……这么下去的话，想从盖里教授\x01",
            "　手中逃出去就难了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xF,
        "……你在听吗，阿修拉！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xF, 500)

    #C0411
    ChrTalk(
        0xFE,
        (
            "啊，是！\x01",
            "我以后会多加注意的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D20")

    Jump("loc_6E48")

    label("loc_6D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_6E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DD0")
    OP_93(0xFE, 0x5A, 0x0)

    #C0412
    ChrTalk(
        0xFE,
        (
            "（稀里哗啦\x01",
            "  稀里哗啦）\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "……原来如此……\x01",
            "这个结晶回路应该这样……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        (
            "#0101F（似乎完全没有注意到我们。\x01",
            "  好强的专注力啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6E1E")

    label("loc_6DD0")


    #C0415
    ChrTalk(
        0xFE,
        (
            "……嗯？\x01",
            "房间外面似乎有些吵啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "算啦，不管了，不管了。\x01",
            "继续继续～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E1E")

    Jump("loc_6E48")

    label("loc_6E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_6E31")
    Jump("loc_6E48")

    label("loc_6E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_6E3F")
    Jump("loc_6E48")

    label("loc_6E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6E48")

    label("loc_6E48")

    TalkEnd(0xFE)
    Return()

    # Function_17_63FB end

    def Function_18_6E4C(): pass

    label("Function_18_6E4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EEF")

    #C0417
    ChrTalk(
        0xFE,
        "……呼～……呼～…………\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "……呵呵，完成了～…………\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "这样一来……与我的偶像艾莉卡博士\x01",
            "之间的距离就又拉近了一步……吧。\x01",
            "……唔。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6F5D")

    label("loc_6EEF")


    #C0420
    ChrTalk(
        0xFE,
        "……呼～……呼～…………\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        (
            "这样一来……与我的偶像艾莉卡博士\x01",
            "之间的距离就又拉近了一步……吧。\x01",
            "……呼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F5D")

    TalkEnd(0xFE)
    Return()

    # Function_18_6E4C end

    def Function_19_6F61(): pass

    label("Function_19_6F61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6FD6")

    #C0422
    ChrTalk(
        0xFE,
        (
            "啊啊……\x01",
            "又开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "他们两位应该都很认同对方的实力，\x01",
            "但彼此之间的关系却莫名地恶劣呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7577")

    label("loc_6FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_6FE4")
    Jump("loc_7577")

    label("loc_6FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_707C")

    #C0424
    ChrTalk(
        0xFE,
        "今天的值班是到傍晚为止。\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "一想到可以离开约亚西姆医生，\x01",
            "我的心情就感到无比平静……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "嗯，回到自己的房间之后，\x01",
            "好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7577")

    label("loc_707C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7125")

    #C0427
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生所在的药物学·神经科\x01",
            "一直进行着各种各样的研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "在外科手术中使用的麻醉剂，\x01",
            "还有用于滋补健体的营养剂等药剂，\x01",
            "都是在那里研究调配出的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7577")

    label("loc_7125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_72AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721D")

    #C0429
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生所管理的\x01",
            "药物学·神经科，\x01",
            "是一个让人深感兴趣的领域呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "作为近代医疗体系的一部分，\x01",
            "同时也涉及到心理与精神领域……\x01",
            "真是非常神秘啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "我之所以会以内科医生为目标，\x01",
            "也是出于对约亚西姆医生的崇拜之情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_72AA")

    label("loc_721D")


    #C0432
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生所管理的\x01",
            "药物学·神经科，\x01",
            "是一个让人深感兴趣的领域呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "我之所以会以内科医生为目标，\x01",
            "也是出于对约亚西姆医生的崇拜之情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72AA")

    Jump("loc_7577")

    label("loc_72AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7346")

    #C0434
    ChrTalk(
        0xFE,
        (
            "嗯，你们是要去\x01",
            "约亚西姆医生那里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "教授和副教授的研究室\x01",
            "在研究楼的四层。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        (
            "其他教授的研究室也都在那里，\x01",
            "你们可别搞错了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7577")

    label("loc_7346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_740D")

    #C0437
    ChrTalk(
        0xFE,
        (
            "拉格教授他们要出席教授会议，\x01",
            "今天不会回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "在教授会议中，\x01",
            "众多医院的教授们\x01",
            "为了医术交流而聚集一堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "医学就是依靠这样的互补互助，\x01",
            "才能一步一步向前发展吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_747E")

    label("loc_740D")


    #C0440
    ChrTalk(
        0xFE,
        (
            "在教授会议中，\x01",
            "众多医院的教授们\x01",
            "为了技术交流而聚集一堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xFE,
        (
            "为了医学的进步，\x01",
            "教授们每天也都在进行学习呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_747E")

    Jump("loc_7577")

    label("loc_7483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7491")
    Jump("loc_7577")

    label("loc_7491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_749F")
    Jump("loc_7577")

    label("loc_749F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_74AD")
    Jump("loc_7577")

    label("loc_74AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_74BB")
    Jump("loc_7577")

    label("loc_74BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74D6")
    Call(1, 21)
    Jump("loc_753F")

    label("loc_74D6")

    TurnDirection(0x15, 0x16, 0)

    #C0442
    ChrTalk(
        0xFE,
        (
            "算了，这种事情，\x01",
            "我也没办法强行执行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xFE,
        (
            "跟你的爷爷说，让他趁着\x01",
            "病情恶化之前到这里来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_753F")

    Jump("loc_7577")

    label("loc_7544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_7552")
    Jump("loc_7577")

    label("loc_7552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_7560")
    Jump("loc_7577")

    label("loc_7560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_756E")
    Jump("loc_7577")

    label("loc_756E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7577")

    label("loc_7577")

    TalkEnd(0xFE)
    Return()

    # Function_19_6F61 end

    def Function_20_757B(): pass

    label("Function_20_757B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_760F")
    Jump("loc_7659")

    label("loc_760F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_762F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7659")

    label("loc_762F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_764F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7659")

    label("loc_764F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7659")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_768C")
    Jump("loc_7879")

    label("loc_768C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_769A")
    Jump("loc_7879")

    label("loc_769A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_76A8")
    Jump("loc_7879")

    label("loc_76A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_76B6")
    Jump("loc_7879")

    label("loc_76B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_76C4")
    Jump("loc_7879")

    label("loc_76C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_76D2")
    Jump("loc_7879")

    label("loc_76D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_76E0")
    Jump("loc_7879")

    label("loc_76E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_76EE")
    Jump("loc_7879")

    label("loc_76EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_76FC")
    Jump("loc_7879")

    label("loc_76FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7756")

    #C0444
    ChrTalk(
        0xFE,
        (
            "我是来\x01",
            "帮爷爷取药的。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xFE,
        "哎呀……\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "我希望爷爷能够\x01",
            "按时吃药呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7879")

    label("loc_7756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7764")
    Jump("loc_7879")

    label("loc_7764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_77B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_777F")
    Call(1, 21)
    Jump("loc_77AE")

    label("loc_777F")

    SetChrSubChip(0x16, 0x0)

    #C0447
    ChrTalk(
        0xFE,
        (
            "一直都是我替他来……\x01",
            "医生，真对不起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77AE")

    Jump("loc_7879")

    label("loc_77B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_77C1")
    Jump("loc_7879")

    label("loc_77C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_77CF")
    Jump("loc_7879")

    label("loc_77CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_77DD")
    Jump("loc_7879")

    label("loc_77DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7839")

    #C0448
    ChrTalk(
        0xFE,
        (
            "我是来\x01",
            "帮爷爷取药的。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "因为爷爷讨厌医院，\x01",
            "所以不自己来取。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7879")

    label("loc_7839")


    #C0450
    ChrTalk(
        0xFE,
        (
            "我的爷爷\x01",
            "特别顽固呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "呼…其实医生本来\x01",
            "要求他住院呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7879")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_757B end

    def Function_21_7881(): pass

    label("Function_21_7881")

    TurnDirection(0x15, 0x16, 0)
    SetChrSubChip(0x16, 0x0)
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0452
    ChrTalk(
        0x16,
        (
            "我爷爷\x01",
            "还是应该来住院才\x01",
            "比较利于病情的恢复吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x15,
        (
            "话是这么说……\x01",
            "但他实在太顽固了。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x16,
        (
            "对、对不起……\x01",
            "我虽然一直劝他，\x01",
            "哪怕偶尔来趟医院也好……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Return()

    # Function_21_7881 end

    def Function_22_793E(): pass

    label("Function_22_793E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7953")
    Call(1, 23)
    Jump("loc_79DF")

    label("loc_7953")


    #C0455
    ChrTalk(
        0x44,
        (
            "#1305F……啊，罗伊德！\x02\x03",

            "#1306F我虽然很想和你多聊聊，\x01",
            "但今天的时间实在有些紧呢。\x01",
            "……抱歉哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        "#0003F（塞茜尔姐姐……似乎很忙呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_79DF")

    TalkEnd(0xFE)
    Return()

    # Function_22_793E end

    def Function_23_79E3(): pass

    label("Function_23_79E3")

    OP_4B(0x44, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x44, 0xA, 0)
    TurnDirection(0xA, 0x44, 0)

    #C0457
    ChrTalk(
        0x44,
        (
            "#1300F贝尔达因医生要的\x01",
            "病例就是这个。\x02\x03",

            "稍后可以帮我交给他吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xA,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x44,
        "#1309F呵呵，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x44, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_23_79E3 end

    def Function_24_7A74(): pass

    label("Function_24_7A74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D79")

    #C0460
    ChrTalk(
        0x101,
        "#0005F迪塔总裁……？\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x17,
        (
            "#2800F呀，诸位，\x01",
            "能在这里会面，真是很巧啊。\x02\x03",

            "#2805F……难道你们在执行任务时\x01",
            "受了什么重伤吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x104,
        (
            "#0305F不，这倒是\x01",
            "没有啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        "#0200F总裁您呢，不会是哪里不舒服吧？\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x102,
        (
            "#0102F呵呵……\x02\x03",

            "叔叔虽然身为总裁，\x01",
            "但同时还是位个人性质的慈善事业家，\x01",
            "参与着若干项慈善事业。\x02\x03",

            "作为其中的一环，\x01",
            "在每年的这个时候，他都会给\x01",
            "正在住院的患者们赠送礼品。\x02\x03",

            "#0102F算是弥补他们无法参加纪念庆典的遗憾。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        "#0005F……原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x17,
        (
            "#2804F哈哈……虽说是慈善事业，\x01",
            "但其实根本就没花多少钱。\x02\x03",

            "#2800F偶尔做些这样的事情，\x01",
            "也可以暂时从工作中解脱出来。\x02\x03",

            "或许有人会说我只是为了自我满足，\x01",
            "但不管别人怎么说，这也是我自己的原则。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#0303F（这、这还真是……\x01",
            "  让人意外的一面呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x103,
        (
            "#0200F（一直都感觉是个单纯爽朗的大叔，\x01",
            "  但也考虑得很多呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 3)
    Jump("loc_7E64")

    label("loc_7D79")


    #C0469
    ChrTalk(
        0x17,
        (
            "#2803F虽说是慈善事业，\x01",
            "但其实根本就没花多少钱，\x01",
            "只是我个人的一点坚持而已。\x02\x03",

            "#2800F尽管如此……玛丽亚贝尔\x01",
            "每年也都会陪我一起来。\x02\x03",

            "哈哈，身边的人一直都给予\x01",
            "着我理解与支持啊。\x02\x03",

            "#2803F……这份温暖的感觉，\x01",
            "我想尽可能地分享给周围的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E64")

    TalkEnd(0xFE)
    Return()

    # Function_24_7A74 end

    def Function_25_7E68(): pass

    label("Function_25_7E68")

    TalkBegin(0xFE)
    Call(1, 26)
    TalkEnd(0xFE)
    Return()

    # Function_25_7E68 end

    def Function_26_7E72(): pass

    label("Function_26_7E72")

    OP_4B(0x8, 0xFF)
    OP_4B(0x18, 0xFF)
    TurnDirection(0x8, 0x18, 0)
    TurnDirection(0x18, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F7C")

    #C0470
    ChrTalk(
        0x8,
        (
            "啊，你是盖里医生的\x01",
            "儿子吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "如果要找医生的话，\x01",
            "我可以立刻帮你去叫……\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x18,
        (
            "哼……哼……！\x01",
            "那种男人，\x01",
            "我根本就连他的脸都不想看到。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x18,
        (
            "帮我把饭交给他就好啦。\x01",
            "我这就回去了！\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x8,
        (
            "呵呵……老是这样子，\x01",
            "一点也不坦率呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7FF5")

    label("loc_7F7C")


    #C0475
    ChrTalk(
        0x18,
        (
            "我、我只是受老妈所托，\x01",
            "来给他送东西而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x18,
        (
            "行了，只要帮我把东西\x01",
            "给他送去就好啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x8,
        (
            "好的，那我就\x01",
            "先保管了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF5")

    OP_4C(0x8, 0xFF)
    OP_4C(0x18, 0xFF)
    Return()

    # Function_26_7E72 end

    def Function_27_7FFE(): pass

    label("Function_27_7FFE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8092")
    Jump("loc_80DC")

    label("loc_8092")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80B2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_80DC")

    label("loc_80B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80D2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_80DC")

    label("loc_80D2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_80DC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8140")

    #C0478
    ChrTalk(
        0xFE,
        (
            "好像果然有点感冒啊……\x01",
            "提前过来真是太对了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_819F")

    label("loc_8140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_819F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_815B")
    Call(1, 5)
    Jump("loc_819F")

    label("loc_815B")


    #C0479
    ChrTalk(
        0xFE,
        (
            "唔，体温计……\x01",
            "刚夹的时候会被冰一下，\x01",
            "所以稍微有点怕这东西呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_819F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_7FFE end

    def Function_28_81A7(): pass

    label("Function_28_81A7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_823B")
    Jump("loc_8285")

    label("loc_823B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_825B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8285")

    label("loc_825B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_827B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8285")

    label("loc_827B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8285")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8312")

    #C0480
    ChrTalk(
        0xFE,
        (
            "哎，做饭的时候被烫伤了，\x01",
            "我还以为会有多严重呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        (
            "结果没什么大事，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8350")

    label("loc_8312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8350")

    #C0482
    ChrTalk(
        0xFE,
        (
            "今天人不多，真是得救了。\x01",
            "我最害怕的就是排队了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8350")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_81A7 end

    def Function_29_8358(): pass

    label("Function_29_8358")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83EC")
    Jump("loc_8436")

    label("loc_83EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_840C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8436")

    label("loc_840C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_842C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8436")

    label("loc_842C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8436")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_84DE")

    #C0483
    ChrTalk(
        0xFE,
        (
            "我还是第一次来医院，\x01",
            "稍微有点不知所措呢。\x01",
            "诊察终于结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xFE,
        (
            "嗯嗯，这还真是个不错的地方。\x01",
            "今后我会再来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8665")

    label("loc_84DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85EB")

    #C0485
    ChrTalk(
        0xFE,
        (
            "……哦，那个护士，\x01",
            "正偷偷看向这边呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "嗯，护士小姐大多都是\x01",
            "非常漂亮的美人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x104,
        (
            "#0309F完全赞同！\x01",
            "是吧，塞茜尔小姐！\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x136,
        (
            "#1309F哎呀呀……呵呵。\x01",
            "就算你这么说，我也没有任何好东西给你哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x101,
        "#0006F（塞茜尔姐姐，太容易亲近了……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_861C")

    label("loc_85EB")


    #C0490
    ChrTalk(
        0xFE,
        (
            "嗯，马上就要轮到我了。\x01",
            "得作好心理准备才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_861C")

    Jump("loc_8665")

    label("loc_8621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8665")

    #C0491
    ChrTalk(
        0xFE,
        (
            "嗯，我是第一次来这个医院……\x01",
            "倒是个干净漂亮的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8665")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_8358 end

    def Function_30_866D(): pass

    label("Function_30_866D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8701")
    Jump("loc_874B")

    label("loc_8701")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8721")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_874B")

    label("loc_8721")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8741")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_874B")

    label("loc_8741")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_874B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_87BD")

    #C0492
    ChrTalk(
        0xFE,
        (
            "今天就是最后一天了。\x01",
            "呼，这么快就能将病治愈，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88C3")

    label("loc_87BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_883E")

    #C0493
    ChrTalk(
        0xFE,
        (
            "如果只是治病的话，\x01",
            "去大圣堂那里配药\x01",
            "倒是更便宜些。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "不过在这里能接受各种各样的检查，\x01",
            "感觉更加放心一点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88C3")

    label("loc_883E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_88C3")

    #C0495
    ChrTalk(
        0xFE,
        (
            "这间医院真不错呢，\x01",
            "医生会非常亲切地为病人进行诊察。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        (
            "虽然离市区稍微有点远，\x01",
            "不过幸好有巴士，所以花费不了多长时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88C3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_866D end

    def Function_31_88CB(): pass

    label("Function_31_88CB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_895F")
    Jump("loc_89A9")

    label("loc_895F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_897F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89A9")

    label("loc_897F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_899F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89A9")

    label("loc_899F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_89A9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0497
    ChrTalk(
        0xFE,
        (
            "我至今为止，只服用过\x01",
            "七耀教会开的药呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        "像医院这种地方，总觉得不太可信……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_88CB end

    def Function_32_8A2B(): pass

    label("Function_32_8A2B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8ABF")
    Jump("loc_8B09")

    label("loc_8ABF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8ADF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B09")

    label("loc_8ADF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AFF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B09")

    label("loc_8AFF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B09")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0499
    ChrTalk(
        0xFE,
        (
            "嘿嘿……希望有个漂亮\x01",
            "的女医生为我诊察。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        "一定不要是个大叔啊！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_8A2B end

    def Function_33_8B7D(): pass

    label("Function_33_8B7D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C11")
    Jump("loc_8C5B")

    label("loc_8C11")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8C31")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C5B")

    label("loc_8C31")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C51")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C5B")

    label("loc_8C51")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C5B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0501
    ChrTalk(
        0xFE,
        (
            "喂！\x01",
            "在医院里安静一点！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_8B7D end

    def Function_34_8CA9(): pass

    label("Function_34_8CA9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D3D")
    Jump("loc_8D87")

    label("loc_8D3D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D5D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D87")

    label("loc_8D5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D7D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D87")

    label("loc_8D7D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D87")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0502
    ChrTalk(
        0xFE,
        (
            "知道给我看病的医生\x01",
            "是位教授的时候，\x01",
            "我还稍微有点害怕呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        (
            "不过他说话很和蔼，\x01",
            "是位很不错的医生呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_8CA9 end

    def Function_35_8E21(): pass

    label("Function_35_8E21")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EB5")
    Jump("loc_8EFF")

    label("loc_8EB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8ED5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EFF")

    label("loc_8ED5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EF5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EFF")

    label("loc_8EF5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8EFF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0504
    ChrTalk(
        0xFE,
        (
            "啊，今天还有生意要谈，\x01",
            "希望能早点回去啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xFE,
        (
            "唔，好困啊。\x01",
            "真希望能快点排到我啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_8E21 end

    def Function_36_8F86(): pass

    label("Function_36_8F86")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_901A")
    Jump("loc_9064")

    label("loc_901A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_903A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9064")

    label("loc_903A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_905A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9064")

    label("loc_905A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9064")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0506
    ChrTalk(
        0xFE,
        (
            "我稍微有点\x01",
            "着凉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xFE,
        (
            "……在大半夜\x01",
            "一直开着窗子睡觉，\x01",
            "果然是不行的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_8F86 end

    def Function_37_90E2(): pass

    label("Function_37_90E2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9176")
    Jump("loc_91C0")

    label("loc_9176")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9196")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91C0")

    label("loc_9196")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91B6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91C0")

    label("loc_91B6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91C0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_933A")
    SetChrSubChip(0xFE, 0x0)

    #C0508
    ChrTalk(
        0xFE,
        "呼噜……\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9295")
    Jump("loc_92DF")

    label("loc_9295")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_92B5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_92DF")

    label("loc_92B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92D5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_92DF")

    label("loc_92D5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_92DF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0509
    ChrTalk(
        0xFE,
        (
            "……啊！\x01",
            "都已经等了好久了，\x01",
            "差点睡过去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_9372")

    label("loc_933A")


    #C0510
    ChrTalk(
        0xFE,
        (
            "呼，好险好险。\x01",
            "总觉得医院的候诊室\x01",
            "有点催眠效果呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9372")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_90E2 end

    def Function_38_937A(): pass

    label("Function_38_937A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_940E")
    Jump("loc_9458")

    label("loc_940E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_942E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9458")

    label("loc_942E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_944E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9458")

    label("loc_944E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9458")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0511
    ChrTalk(
        0xFE,
        (
            "我去参观了一下开幕式，\x01",
            "结果在人群中被挤得腰痛。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xFE,
        (
            "纪念庆典才刚刚开始。\x01",
            "真想赶快治好，去玩个痛快啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_937A end

    def Function_39_94F1(): pass

    label("Function_39_94F1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9585")
    Jump("loc_95CF")

    label("loc_9585")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_95A5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95CF")

    label("loc_95A5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95C5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95CF")

    label("loc_95C5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95CF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0513
    ChrTalk(
        0xFE,
        (
            "这间医院还是老样子，\x01",
            "看起来好像很忙呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_94F1 end

    def Function_40_9629(): pass

    label("Function_40_9629")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96BD")
    Jump("loc_9707")

    label("loc_96BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_96DD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9707")

    label("loc_96DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96FD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9707")

    label("loc_96FD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9707")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9895")
    OP_52(0x27, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x27, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97CA")
    Jump("loc_9814")

    label("loc_97CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_97EA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9814")

    label("loc_97EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_980A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9814")

    label("loc_980A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9814")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0514
    ChrTalk(
        0xFE,
        (
            "喂喂，\x01",
            "在医院里要安静一点哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "只要烧退下去，\x01",
            "我就带你去看纪念庆典哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x1, 6)
    Jump("loc_98D1")

    label("loc_9895")


    #C0516
    ChrTalk(
        0xFE,
        (
            "这孩子，似乎因为太期待\x01",
            "纪念庆典而失眠，\x01",
            "所以发烧了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98D1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_9629 end

    def Function_41_98D9(): pass

    label("Function_41_98D9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_996D")
    Jump("loc_99B7")

    label("loc_996D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_998D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99B7")

    label("loc_998D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99B7")

    label("loc_99AD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_99B7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0517
    ChrTalk(
        0xFE,
        "哇哇，我想去纪念庆典。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_41_98D9 end

    def Function_42_9A00(): pass

    label("Function_42_9A00")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A94")
    Jump("loc_9ADE")

    label("loc_9A94")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AB4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9ADE")

    label("loc_9AB4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AD4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9ADE")

    label("loc_9AD4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9ADE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0518
    ChrTalk(
        0xFE,
        (
            "咳咳……\x01",
            "呜，好难受。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        "该不会是被传染了吧……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_42_9A00 end

    def Function_43_9B42(): pass

    label("Function_43_9B42")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BD6")
    Jump("loc_9C20")

    label("loc_9BD6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9BF6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C20")

    label("loc_9BF6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C16")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C20")

    label("loc_9C16")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C20")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x2)

    #C0520
    ChrTalk(
        0xFE,
        (
            "喂喂，\x01",
            "你可别传染给我啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_9B42 end

    def Function_44_9C74(): pass

    label("Function_44_9C74")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D08")
    Jump("loc_9D52")

    label("loc_9D08")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9D28")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D52")

    label("loc_9D28")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D48")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D52")

    label("loc_9D48")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D52")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EDF")

    #C0521
    ChrTalk(
        0xFE,
        (
            "昨天，在克洛斯贝尔市的旧城区\x01",
            "发生了非常热闹的事件哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "我也去观战了，\x01",
            "因为兴奋过头，不小心摔了一跤。\x01",
            "结果就成了这副德行。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x104,
        (
            "#0306F（……从某种意义上说，\x01",
            "　好像是我们间接\x01",
            "　导致他受伤了吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        (
            "#0005F（这、这个嘛……\x01",
            "  我觉得你有点\x01",
            "  想多了吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "算啦，虽然受伤了，不过都怪自己。\x01",
            "不管怎么说，反正那天挺开心的，无所谓啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_9F1A")

    label("loc_9EDF")


    #C0526
    ChrTalk(
        0xFE,
        (
            "那个比赛，如果每年都搞一场的话，\x01",
            "肯定会相当受欢迎吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F1A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_44_9C74 end

    def Function_45_9F22(): pass

    label("Function_45_9F22")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FB6")
    Jump("loc_A000")

    label("loc_9FB6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FD6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A000")

    label("loc_9FD6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FF6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A000")

    label("loc_9FF6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A000")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0527
    ChrTalk(
        0xFE,
        (
            "呼～复查日偏偏赶在今天，\x01",
            "真是倒霉啊。\x01",
            "看来是彻底错过游行活动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        (
            "算啦，只要不是明天就好。\x01",
            "赶快接受诊察，然后回家去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_9F22 end

    def Function_46_A0AE(): pass

    label("Function_46_A0AE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A142")
    Jump("loc_A18C")

    label("loc_A142")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A162")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A18C")

    label("loc_A162")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A182")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A18C")

    label("loc_A182")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A18C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0529
    ChrTalk(
        0xFE,
        (
            "按照预定的话，\x01",
            "我的疗程到今天就结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xFE,
        (
            "接受完诊察之后，\x01",
            "就陪老伴一起\x01",
            "逛逛纪念庆典吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_A0AE end

    def Function_47_A21A(): pass

    label("Function_47_A21A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2AE")
    Jump("loc_A2F8")

    label("loc_A2AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A2CE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2F8")

    label("loc_A2CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2F8")

    label("loc_A2EE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2F8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0531
    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "我老伴的心态\x01",
            "一直都很年轻呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_47_A21A end

    def Function_48_A34F(): pass

    label("Function_48_A34F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A3E3")
    Jump("loc_A42D")

    label("loc_A3E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A403")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A42D")

    label("loc_A403")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A423")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A42D")

    label("loc_A423")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A42D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0532
    ChrTalk(
        0xFE,
        (
            "现在去接受诊察，\x01",
            "然后坐巴士回到市里，\x01",
            "接着去乘坐水上巴士……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        (
            "嗯，好像还有时间玩呢。\x01",
            "太好了，太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_48_A34F end

    def Function_49_A4C9(): pass

    label("Function_49_A4C9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A55D")
    Jump("loc_A5A7")

    label("loc_A55D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A57D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5A7")

    label("loc_A57D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A59D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5A7")

    label("loc_A59D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5A7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0534
    ChrTalk(
        0xFE,
        (
            "我今天傍晚和男朋友\x01",
            "约好要去米修拉姆呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x2E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x2E, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A68D")
    Jump("loc_A6D7")

    label("loc_A68D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A6AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A6D7")

    label("loc_A6AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A6D7")

    label("loc_A6CD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A6D7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2E, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2E, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0535
    ChrTalk(
        0xFE,
        (
            "……哎呀，下一个就是我了吧，\x01",
            "快点叫我啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_49_A4C9 end

    def Function_50_A737(): pass

    label("Function_50_A737")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7CB")
    Jump("loc_A815")

    label("loc_A7CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A7EB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A815")

    label("loc_A7EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A80B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A815")

    label("loc_A80B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A815")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0536
    ChrTalk(
        0xFE,
        (
            "明明是纪念庆典最后一天了，\x01",
            "但今天也有不少人来呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_50_A737 end

    def Function_51_A87B(): pass

    label("Function_51_A87B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A90F")
    Jump("loc_A959")

    label("loc_A90F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A92F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A959")

    label("loc_A92F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A94F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A959")

    label("loc_A94F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A959")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_AA14")

    #C0537
    ChrTalk(
        0xFE,
        (
            "我被忠告说，不应该依赖药物，\x01",
            "而应该换一种更加健康的生活方式。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xFE,
        (
            "但由于工作原因，这很困难吧……\x01",
            "呼，没有任何东西能够替代健康呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA6B")

    label("loc_AA14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_AA6B")

    #C0539
    ChrTalk(
        0xFE,
        (
            "咳咳……果然还是该早点来\x01",
            "接受诊察呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xFE,
        (
            "我总是全心投入到\x01",
            "工作之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA6B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_51_A87B end

    def Function_52_AA73(): pass

    label("Function_52_AA73")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB07")
    Jump("loc_AB51")

    label("loc_AB07")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AB27")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB51")

    label("loc_AB27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB51")

    label("loc_AB47")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB51")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_ABD3")

    #C0541
    ChrTalk(
        0xFE,
        "已经从医生那里开完药了。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "吃下这个药，公公的病情\x01",
            "应该就会有所好转吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC36")

    label("loc_ABD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_AC36")

    #C0543
    ChrTalk(
        0xFE,
        (
            "在大厅里排队，\x01",
            "总会感觉时间特别漫长。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        (
            "如果是陪同别人前来，\x01",
            "这种感觉就更明显了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC36")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_52_AA73 end

    def Function_53_AC3E(): pass

    label("Function_53_AC3E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACD2")
    Jump("loc_AD1C")

    label("loc_ACD2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ACF2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD1C")

    label("loc_ACF2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD12")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD1C")

    label("loc_AD12")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD1C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_AD91")

    #C0545
    ChrTalk(
        0xFE,
        "按顺序算的话，就快到我了吧。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xFE,
        "嗯，要是带本书来就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADE5")

    label("loc_AD91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_ADE5")

    #C0547
    ChrTalk(
        0xFE,
        "呼，真够麻烦的。\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xFE,
        (
            "不过，为了让诊察顺利进行，\x01",
            "这也是没办法的事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADE5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_53_AC3E end

    def Function_54_ADED(): pass

    label("Function_54_ADED")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AE81")
    Jump("loc_AECB")

    label("loc_AE81")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AEA1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AECB")

    label("loc_AEA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEC1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AECB")

    label("loc_AEC1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AECB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_AF48")

    #C0549
    ChrTalk(
        0xFE,
        (
            "我的老毛病似乎\x01",
            "快要完全治好了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xFE,
        (
            "坚持来接受复查，\x01",
            "真是值得啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF6B")

    label("loc_AF48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_AF6B")

    #C0551
    ChrTalk(
        0xFE,
        "真希望快点轮到我……\x02",
    )

    CloseMessageWindow()

    label("loc_AF6B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_54_ADED end

    def Function_55_AF73(): pass

    label("Function_55_AF73")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B007")
    Jump("loc_B051")

    label("loc_B007")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B027")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B051")

    label("loc_B027")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B047")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B051")

    label("loc_B047")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B051")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_B0BB")

    #C0552
    ChrTalk(
        0xFE,
        (
            "呵呵，爷爷的病情似乎好转了，\x01",
            "我也总算放下心来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0E4")

    label("loc_B0BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_B0E4")

    #C0553
    ChrTalk(
        0xFE,
        "爷爷，静下心来，慢慢等吧。\x02",
    )

    CloseMessageWindow()

    label("loc_B0E4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_55_AF73 end

    def Function_56_B0EC(): pass

    label("Function_56_B0EC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B180")
    Jump("loc_B1CA")

    label("loc_B180")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B1A0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1CA")

    label("loc_B1A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1C0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1CA")

    label("loc_B1C0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B1CA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0554
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "似乎有点发热……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_56_B0EC end

    def Function_57_B214(): pass

    label("Function_57_B214")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B2A8")
    Jump("loc_B2F2")

    label("loc_B2A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B2C8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B2F2")

    label("loc_B2C8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B2E8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B2F2")

    label("loc_B2E8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B2F2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0555
    ChrTalk(
        0xFE,
        (
            "咳咳……\x01",
            "我自作主张，不来复诊，\x01",
            "结果病症很快就复发了。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        (
            "过于相信自己的判断，\x01",
            "果然很危险呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_57_B214 end

    def Function_58_B384(): pass

    label("Function_58_B384")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B418")
    Jump("loc_B462")

    label("loc_B418")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B438")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B462")

    label("loc_B438")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B458")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B462")

    label("loc_B458")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B462")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0557
    ChrTalk(
        0xFE,
        (
            "这里的实习医生都在\x01",
            "专心学习着，真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        "我不由自主就想给他们加油呢。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_58_B384 end

    def Function_59_B4E0(): pass

    label("Function_59_B4E0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B574")
    Jump("loc_B5BE")

    label("loc_B574")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B594")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5BE")

    label("loc_B594")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5B4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5BE")

    label("loc_B5B4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B5BE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0559
    ChrTalk(
        0xFE,
        (
            "为了锻炼，我正在练习一种\x01",
            "模仿东方拳法动作的运动……\x01",
            "结果用力过猛摔倒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xFE,
        (
            "哎呀，真不该勉强呢，\x01",
            "哇哈哈。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_59_B4E0 end

    def Function_60_B65C(): pass

    label("Function_60_B65C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6F0")
    Jump("loc_B73A")

    label("loc_B6F0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B710")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B73A")

    label("loc_B710")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B730")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B73A")

    label("loc_B730")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B73A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_B7C0")

    #C0561
    ChrTalk(
        0xFE,
        "马上就要轮到我接受诊察了啊。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        (
            "如果耗到太晚，\x01",
            "还是住在院内的招待所为好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B825")

    label("loc_B7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B825")

    #C0563
    ChrTalk(
        0xFE,
        (
            "我还是第一次看到\x01",
            "被急救车送来的患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        (
            "哎呀……还是不看为好……\x01",
            "好像真的很疼呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B825")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_60_B65C end

    def Function_61_B82D(): pass

    label("Function_61_B82D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B8C1")
    Jump("loc_B90B")

    label("loc_B8C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B8E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B90B")

    label("loc_B8E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B901")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B90B")

    label("loc_B901")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B90B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_B9AE")

    #C0565
    ChrTalk(
        0xFE,
        (
            "虽然已经接受医生的诊察了……\x01",
            "但真的只是普通的感冒吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        (
            "要是出现什么严重的并发症，\x01",
            "那可如何是好啊！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9EB")

    label("loc_B9AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B9EB")

    #C0567
    ChrTalk(
        0xFE,
        (
            "哦，女神啊，\x01",
            "求您保佑我的女儿\x01",
            "不要患上重病……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9EB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_61_B82D end

    def Function_62_B9F3(): pass

    label("Function_62_B9F3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BA87")
    Jump("loc_BAD1")

    label("loc_BA87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BAA7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BAD1")

    label("loc_BAA7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAC7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BAD1")

    label("loc_BAC7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BAD1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_BB6D")

    #C0568
    ChrTalk(
        0xFE,
        (
            "……真是的，妈妈\x01",
            "吓得惊慌失措的，\x01",
            "真让人难为情……\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "医生都说过了，\x01",
            "只是普通的感冒，不必担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB2")

    label("loc_BB6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BBB2")

    #C0570
    ChrTalk(
        0xFE,
        (
            "咳咳……\x01",
            "真是的，妈妈就是爱操心，\x01",
            "只是普通的感冒而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBB2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_62_B9F3 end

    def Function_63_BBBA(): pass

    label("Function_63_BBBA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BC4E")
    Jump("loc_BC98")

    label("loc_BC4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BC6E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC98")

    label("loc_BC6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC8E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BC98")

    label("loc_BC8E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BC98")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0571
    ChrTalk(
        0xFE,
        "嗯，原来是这样的内部构造啊。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "哎呀，这里太大了，\x01",
            "我都有点转晕了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_63_BBBA end

    def Function_64_BD16(): pass

    label("Function_64_BD16")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDAA")
    Jump("loc_BDF4")

    label("loc_BDAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BDCA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF4")

    label("loc_BDCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BDEA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF4")

    label("loc_BDEA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDF4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0573
    ChrTalk(
        0xFE,
        (
            "说起医院，\x01",
            "好像总有一种特殊的味道。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "应该是消毒用的酒精……\x01",
            "我好像有些喜欢呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_64_BD16 end

    def Function_65_BE79(): pass

    label("Function_65_BE79")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BF0D")
    Jump("loc_BF57")

    label("loc_BF0D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF2D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BF57")

    label("loc_BF2D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF4D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BF57")

    label("loc_BF4D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF57")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0575
    ChrTalk(
        0xFE,
        "刚刚上午就有这么多人……\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xFE,
        (
            "对于克洛斯贝尔人来说，\x01",
            "这里似乎是非常值得信赖的设施呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_65_BE79 end

    def Function_66_BFDF(): pass

    label("Function_66_BFDF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C073")
    Jump("loc_C0BD")

    label("loc_C073")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C093")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0BD")

    label("loc_C093")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0B3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C0BD")

    label("loc_C0B3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C0BD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0577
    ChrTalk(
        0xFE,
        (
            "我明明是一大早赶来的，\x01",
            "竟然要等这么久……\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "快点啊，真是的！\x01",
            "我的腰部正在发出悲鸣啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_66_BFDF end

    def Function_67_C148(): pass

    label("Function_67_C148")

    TalkBegin(0xFE)

    #C0579
    ChrTalk(
        0xFE,
        (
            "嗯，奶奶的病房\x01",
            "是在哪里呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_67_C148 end

    def Function_68_C172(): pass

    label("Function_68_C172")

    TalkBegin(0xFE)

    #C0580
    ChrTalk(
        0xFE,
        "哇哇～医院可真大啊！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_68_C172 end

    def Function_69_C193(): pass

    label("Function_69_C193")

    TalkBegin(0xFE)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0x42, 0xF, 0x0)
    OP_4B(0x9, 0xFF)

    #C0581
    ChrTalk(
        0x9,
        (
            "您是来做健康检查的吗？\x01",
            "那么，请您在这边的\x01",
            "文件上签个字。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x9,
        (
            "因为是首次诊断，\x01",
            "可能要多花费一些时间，\x01",
            "可以稍等片刻吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xFE,
        "嗯，没问题。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_69_C193 end

    def Function_70_C23E(): pass

    label("Function_70_C23E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C31F")

    #C0584
    ChrTalk(
        0xFE,
        (
            "嗯？写着什么？\x01",
            "『关于全面体检的通知』……\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "『为了在早期发现体内隐藏的疾病，\x01",
            "  我们推荐您做一次\x01",
            "  使用最新器械的综合检查』……\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xFE,
        (
            "原来如此，不愧是\x01",
            "有名的乌尔斯拉医院呢。\x01",
            "在别处都见不到这种东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C39C")

    label("loc_C31F")


    #C0587
    ChrTalk(
        0xFE,
        (
            "全面体检吗……\x01",
            "虽然现在没时间做……\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xFE,
        (
            "但乌尔斯拉医院果然很先进呢。\x01",
            "这里被誉为最新医疗技术的宝库，\x01",
            "看来真是名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C39C")

    TalkEnd(0xFE)
    Return()

    # Function_70_C23E end

    def Function_71_C3A0(): pass

    label("Function_71_C3A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_C3E2")

    #C0589
    ChrTalk(
        0x45,
        (
            "我、我昨天宵夜吃得太多了。\x01",
            "肚子好疼啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C413")

    label("loc_C3E2")


    #C0590
    ChrTalk(
        0x45,
        "肚、肚子好疼……\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x45,
        "还没轮到我吗……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_C413")

    TalkEnd(0xFE)
    Return()

    # Function_71_C3A0 end

    def Function_72_C417(): pass

    label("Function_72_C417")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C698")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0592
    ChrTalk(
        0x101,
        "#0005F哎，这不是那位游击士吗……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x102,
        (
            "#0101F难道是……\x01",
            "发生了什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xFE,
        (
            "嗯，有位旅行者钻入密林，\x01",
            "似乎是被毒蛇之类的东西\x01",
            "咬伤了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xFE,
        (
            "我们急忙赶了过去，\x01",
            "然后就把他送来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        (
            "还好，艾欧莉娅已经为他\x01",
            "做了适当处理，应该不会有什么大碍。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x104,
        (
            "#0305F处理吗……\x01",
            "游击士竟然连\x01",
            "这种技术都会啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        "是艾欧莉娅比较特殊啦。\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xFE,
        (
            "她出身于医疗发达国家雷米菲利亚，\x01",
            "而且好像还拥有医生资格证呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        (
            "#0211F……真难想象现在说的这个人，\x01",
            "就是每次见面时都要粘着我的那位游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "哈哈，虽然她平时那个样子，\x01",
            "但其实是个非常厉害的人呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_C710")

    label("loc_C698")


    #C0602
    ChrTalk(
        0xFE,
        (
            "艾欧莉娅出身于雷米菲利亚，\x01",
            "而且还持有医生资格证。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xFE,
        (
            "虽然平时对可爱的东西没有抵抗力，\x01",
            "但其实是个非常厉害的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C710")

    TalkEnd(0xFE)
    Return()

    # Function_72_C417 end

    def Function_73_C714(): pass

    label("Function_73_C714")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C933")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8B0")
    OP_4B(0x47, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0x47, 0xB, 0)

    #C0604
    ChrTalk(
        0xB,
        (
            "那位旅行者正在集中治疗室\x01",
            "保持静养。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xB,
        (
            "哎呀，那个时候如果稍有闪失，\x01",
            "搞不好就必须得截肢了……\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xB,
        (
            "幸好有艾欧莉娅在，\x01",
            "才避免了那么严重的后果。\x01",
            "总是给你们添麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x47,
        (
            "哪里哪里，身为游击士，\x01",
            "这些都是我们应该做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x104,
        (
            "#0307F#4S（可恶，真让人羡慕！！）\x02\x03",

            "#0304F（我也好想接受\x01",
            "　艾欧莉娅小姐的温柔护理啊！）\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x103,
        "#0211F（……请不要莫名其妙地兴奋起来。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    OP_4C(0x47, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_C933")

    label("loc_C8B0")


    #C0610
    ChrTalk(
        0x47,
        (
            "啊～！！\x01",
            "这不是小缇欧和各位嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x47,
        (
            "呵呵，稍等一下哦。\x01",
            "等我的工作结束之后，\x01",
            "就把满腔的爱意献给你⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x103,
        "#0206F……恕我谢绝。\x02",
    )

    CloseMessageWindow()

    label("loc_C933")

    TalkEnd(0xFE)
    Return()

    # Function_73_C714 end

    def Function_74_C937(): pass

    label("Function_74_C937")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(49870, 1000, 57910, 0)
    MoveCamera(64, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20540, 0)
    SetChrPos(0x101, 48800, 0, 57000, 0)
    SetChrPos(0x102, 50000, 0, 57000, 0)
    SetChrPos(0x103, 48800, 0, 55500, 0)
    SetChrPos(0x104, 50000, 0, 55500, 0)
    SetChrSubChip(0xC, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0613
    ChrTalk(
        0xC,
        (
            "#5P……唔，只是这种无关紧要的请求，\x01",
            "他们真的会来吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xC,
        (
            "#5P果然还是应该\x01",
            "去拜托游击士吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xC,
        (
            "#5P可是，我又不想为这种程度的\x01",
            "小事花费米拉……\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x101,
        (
            "#12P#0006F（呃，不太好搭话呢……）\x02\x03",

            "#0000F那、那个……\x01",
            "我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xC, 0x1)

    #C0617
    ChrTalk(
        0xC,
        "#5P哦哦……你们来了啊！\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xC,
        (
            "#5P我一直在等你们呢，\x01",
            "来来，快过来坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x101,
        (
            "#12P#0003F不用了，我们站着就行。\x02\x03",

            "#0000F可以请您将委托内容\x01",
            "详细说给我们听听吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0xC,
        "#5P嗯，好、好的。\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xC,
        (
            "#5P……咳咳。\x01",
            "那个，所谓的委托其实很简单。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xC,
        (
            "#5P这次内科研究中，需要用到一种药草，\x01",
            "希望你们能帮我取来。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xC,
        (
            "#5P它的名字叫做『羽扇豆草』……\x01",
            "如今已是一种\x01",
            "很稀少的药草了。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x103,
        (
            "#12P#0205F说到羽扇豆的话……\x01",
            "就会让人联想起流经\x01",
            "克洛斯贝尔港湾区的『羽扇河』呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x104,
        (
            "#12P#0300F您是想让我们去采摘\x01",
            "那种珍奇的药草吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xC,
        "#5P不，严格来说并非如此。\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0xC,
        (
            "#5P其实，这种药草在\x01",
            "克洛斯贝尔大圣堂有少量储备。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xC,
        (
            "#5P我已经和艾拉尔达大主教\x01",
            "联系过了，希望你们\x01",
            "能作为我的代理人，去帮我取来。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xC,
        (
            "#5P……其实本来应该由我亲自去的……\x01",
            "嗯……不过因为有些忙嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x101,
        "#12P#0005F……？\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x102,
        (
            "#12P#0100F原来如此，我们知道了。\x01",
            "去找克洛斯贝尔大圣堂的\x01",
            "艾拉尔达大主教就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xC,
        "#5P嗯，那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xC,
        (
            "#5P拿到『羽扇豆草』之后，\x01",
            "请把它拿到我这里来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0634
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【稀有药草的回收】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50500, 1000, 57500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_29(0x13, 0x1, 0x0)
    SetChrPos(0x0, 50500, 0, 57500, 0)
    SetChrPos(0x1, 50500, 0, 57500, 0)
    SetChrPos(0x2, 50500, 0, 57500, 0)
    SetChrPos(0x3, 50500, 0, 57500, 0)
    Sleep(500)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_74_C937 end

    def Function_75_CF6A(): pass

    label("Function_75_CF6A")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(49870, 1000, 57910, 0)
    MoveCamera(64, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20540, 0)
    SetChrPos(0x101, 48800, 0, 57000, 0)
    SetChrPos(0x102, 50000, 0, 57000, 0)
    SetChrPos(0x103, 48800, 0, 55500, 0)
    SetChrPos(0x104, 50000, 0, 55500, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0635
    ChrTalk(
        0xC,
        "#5P哦，是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xC,
        (
            "#5P已经帮我把羽扇豆草\x01",
            "顺利取来了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，已经拿来了。\x02\x03",

            "这就是我们取来的物品。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0638
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x341),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('选秀活动特别奖纪念盾', 1)

    #C0639
    ChrTalk(
        0xC,
        (
            "#5P嗯，就是它，\x01",
            "我要向你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xC,
        (
            "#5P嗯……嗯……\x01",
            "然后，那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xC,
        (
            "#5P……艾拉尔达大主教\x01",
            "说过什么关于我的话吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x103,
        (
            "#12P#0203F……不，并没说什么。\x02\x03",

            "#0200F而且他似乎也没有看过\x01",
            "教授您写给他的信。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xC,
        "#5P……唔，果然是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xC,
        (
            "#5P我等了好久也没有等到\x01",
            "回音，就已经想到\x01",
            "会是这么一回事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x104,
        (
            "#12P#0301F什么嘛，之前还说已经联络过了，\x01",
            "原来是骗人的啊。\x02\x03",

            "#0306F我们到了之后，才发现你们根本就\x01",
            "没有联系过，紧张得都冒冷汗了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xC,
        (
            "#5P唔……真抱歉啊，\x01",
            "因为有些难以启齿。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xC,
        (
            "#5P我有些害怕见到大主教，\x01",
            "所以没法自己去取，\x01",
            "不得已之下，才会拜托你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x102,
        (
            "#12P#0100F祭司和我们说了很多。\x02\x03",

            "他说，艾拉尔达大主教虽然有些顽固，\x01",
            "但对拉格教授肯定\x01",
            "还是持认同态度的。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xC,
        "#5P是吗……\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0xC,
        (
            "#5P我当然也是一样啊。\x01",
            "直到如今，我也非常\x01",
            "尊敬艾拉尔达大主教。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xC,
        (
            "#5P我一直在想，如果有朝一日\x01",
            "先进的医疗技术能得到普及，\x01",
            "我一定要去向他道歉，并郑重表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x101,
        (
            "#12P#0000F是吗……\x01",
            "那真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xC,
        (
            "#5P……那么，真是\x01",
            "给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xC,
        "#5P如果再有什么事情，还要拜托你们了。\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x101,
        "#12P#0000F嗯，我们随时恭候。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0656
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【稀有药草的回收】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50500, 1000, 57500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_29(0x13, 0x1, 0x3)
    OP_29(0x13, 0x4, 0x10)
    SetChrPos(0x0, 50500, 0, 57500, 0)
    SetChrPos(0x1, 50500, 0, 57500, 0)
    SetChrPos(0x2, 50500, 0, 57500, 0)
    SetChrPos(0x3, 50500, 0, 57500, 0)
    Sleep(500)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_75_CF6A end

    def Function_76_D599(): pass

    label("Function_76_D599")

    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x0, 0x8, 0)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15620, 400, 7920, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 14410, 0, 6710, 90)
    SetChrPos(0x102, 13420, 0, 4760, 90)
    SetChrPos(0x103, 12160, 0, 4910, 90)
    SetChrPos(0x104, 12810, 0, 6540, 90)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    SetChrPos(0x15, 11940, 1230, 16600, 0)
    SetChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0657
    ChrTalk(
        0x8,
        "#11P哎呀……医生到底去哪里了……\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x101,
        (
            "#6P#0001F塞拉小姐，您好。\x02\x03",

            "我们是接到了支援请求而来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0659
    ChrTalk(
        0x8,
        "#11P特别任务支援科的诸位……\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x8,
        (
            "#11P太好了，\x01",
            "你们能来，可真是帮了我大忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0661
    ChrTalk(
        0x8,
        "#11P……嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x101,
        (
            "#6P#0006F那、那个……\x02\x03",

            "#0005F委托中好像说一位副教授失踪了，\x01",
            "希望我们进行搜寻……对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x104,
        (
            "#6P#0305F但是，您却这么镇定，\x01",
            "让人感觉有些奇怪呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x8,
        "#11P哦，这个嘛。\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x8,
        (
            "#11P与其说是镇定……\x01",
            "倒不如说是\x01",
            "已经麻木了。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x102,
        "#12P#0105F麻、麻木了……？\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x103,
        (
            "#6P#0203F……那个，如果可以的话，\x01",
            "请把详细情况告诉我们吧。\x02\x03",

            "#0200F看样子，这和我们所想象的失踪事件\x01",
            "似乎在严重程度上有很大差距呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x8,
        "#11P嗯，好的。\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x8,
        (
            "#11P失踪的那位\x01",
            "副教授名叫\x01",
            "约亚西姆·琼塔……\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x8,
        (
            "#11P约亚西姆医生他，那个……\x01",
            "虽然是位很优秀的医生，但是\x01",
            "偶尔却会突然失踪。\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x101,
        (
            "#6P#0003F约亚西姆医生……\x01",
            "啊，就是那位蓝色头发，戴眼镜的……\x02\x03",

            "#0005F也就是说，那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x104,
        "#6P#0306F简单来说，就是偷懒旷工吧。\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x8,
        "#11P没错，说白了其实就是那样。\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x8,
        (
            "#11P今天也是，把大量的工作丢下不管，\x01",
            "不知跑到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x102,
        (
            "#12P#0106F……就是说……\x02\x03",

            "#0100F约亚西姆医生只是不知道\x01",
            "跑到哪里去玩了……\x01",
            "是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x8,
        "#11P就、就是这样啦。\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x8,
        (
            "#11P对不起，我把委托写成\x01",
            "『行踪不明』，\x01",
            "也许是有些轻率了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0678
    ChrTalk(
        0x101,
        "#6P#0003F……要怎么办呢，各位？\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x103,
        (
            "#6P#0203F……说实话，我觉得这个不妨延后处理。\x02\x03",

            "#0200F从了解到的情报来看，\x01",
            "紧急性似乎很低呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x104,
        (
            "#6P#0306F但毕竟是塞拉小姐的请求，\x01",
            "我还是很想帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x102,
        (
            "#12P#0105F不过，那位医生也许真的被卷入到\x01",
            "某些事件中了呢。以防万一，或许还是应该……\x02",
        )
    )

    CloseMessageWindow()

    #N0682
    NpcTalk(
        0x15,
        "男人的声音",
        "#4S塞、塞——塞拉小姐！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_DD90():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DD90)

    def lambda_DD9D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DD9D)

    def lambda_DDAA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DDAA)

    def lambda_DDB7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_DDB7)

    def lambda_DDC4():

        label("loc_DDC4")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_DDC4")

    QueueWorkItem2(0x8, 1, lambda_DDC4)
    OP_68(14200, 600, 9330, 1500)
    MoveCamera(45, 18, 0, 1500)
    OP_6E(400, 1500)
    SetCameraDistance(25000, 1500)
    Sleep(1500)
    ClearChrFlags(0x15, 0x80)
    OP_95(0x15, 11810, 0, 9710, 7000, 0x0)

    def lambda_DE20():
        OP_95(0xFE, 13460, 0, 8990, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DE20)
    OP_68(14770, 600, 8480, 500)
    MoveCamera(45, 18, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(25000, 500)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x0)

    #C0683
    ChrTalk(
        0x15,
        "#5P呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x8,
        (
            "#11P啊……利顿医生，\x01",
            "在医院里不可以大声喊叫哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x15,
        (
            "#5P呼、呼……\x01",
            "对……对不起……\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x104,
        (
            "#6P#0300F啊，这不是之前住院的\x01",
            "那位实习医生吗？\x01",
            "身体还好吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x104, 0)

    #C0687
    ChrTalk(
        0x15,
        (
            "#5P……啊，你、你们好。\x01",
            "当时可真是多谢了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x8, 0)

    #C0688
    ChrTalk(
        0x15,
        (
            "#5P……不对！现在不是说这些的时候！\x01",
            "塞拉小姐，约亚西姆医生呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x8,
        (
            "#11P那个，对不起。\x01",
            "他好像还没回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x15,
        "#5P怎、怎么会这样……\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x15,
        (
            "#5P呜呜……\x01",
            "那么大的工作量，让我这个\x01",
            "实习医生如何是好啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x15,
        (
            "#5P……啊啊，没时间在这里抱怨了！\x01",
            "再不赶快去处理的话，可就……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E07A():

        label("loc_E07A")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_E07A")

    QueueWorkItem2(0x8, 1, lambda_E07A)
    OP_95(0x15, 11810, 0, 9710, 6000, 0x0)
    OP_95(0x15, 11940, 1230, 16600, 7000, 0x0)
    SetChrFlags(0x15, 0x80)
    Sleep(800)

    #C0693
    ChrTalk(
        0x101,
        "#6P#0005F刚、刚才那是……？\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_E0E0():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E0E0)

    def lambda_E0ED():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E0ED)

    def lambda_E0FA():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E0FA)

    def lambda_E107():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E107)
    Sleep(100)
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x12C)
    Sleep(200)

    #C0694
    ChrTalk(
        0x8,
        (
            "#11P约亚西姆医生经常把\x01",
            "工作硬推给利顿医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x8,
        (
            "#11P医生这次偷跑出去，\x01",
            "留下的一大堆烂摊子也正是\x01",
            "由他在拼命收拾呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x102,
        "#12P#0106F真、真是辛苦啊……\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x104,
        (
            "#6P#0306F嗯，看起来，这件事\x01",
            "果然还是不能放着不管啊。\x02\x03",

            "#0300F其它的先不说，\x01",
            "毕竟那个家伙太可怜了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x103,
        (
            "#6P#0206F……我也有同感。\x01",
            "不过，该说他是倒霉才对吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        (
            "#6P#0006F是啊……\x02\x03",

            "#0000F塞拉小姐，关于约亚西姆医生\x01",
            "有可能去的地方，\x01",
            "您有没有什么线索……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0700
    ChrTalk(
        0x8,
        (
            "#11P啊，诸位愿意接受\x01",
            "这个委托吗，\x01",
            "真是很感谢你们！\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        (
            "#11P约亚西姆医生最近好像\x01",
            "一直在到处宣扬\x01",
            "『要在纪念庆典中参加钓鱼大赛』。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x8,
        (
            "#11P他这次的行踪或许跟这个大赛\x01",
            "有什么关联吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x8,
        (
            "#11P约亚西姆医生是在\x01",
            "工作途中直接偷跑出去的，\x01",
            "身上应该还穿着白大褂。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x8,
        "#11P所以一定比较显眼，即使离很远也能认出来。\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#6P#0006F钓鱼大赛吗……\x01",
            "他还真是很喜欢钓鱼啊。\x02\x03",

            "#0003F（既然如此，去东街的那个设施里\x01",
            "　问问的话，说不定会有什么线索呢。）\x02\x03",

            "#0000F……总之，我们正式接受委托。\x01",
            "找到他之后，会再与您联络的。\x01",
            "可以先在这里等我们的消息吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x8,
        (
            "#11P明白了，\x01",
            "那就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0707
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【搜寻副教授的请求】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14410, 1000, 6710, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 14410, 0, 6710, 90)
    SetChrPos(0x1, 14410, 0, 6710, 90)
    SetChrPos(0x2, 14410, 0, 6710, 90)
    SetChrPos(0x3, 14410, 0, 6710, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    ClearChrFlags(0x15, 0x40)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    OP_29(0x16, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_76_D599 end

    def Function_77_E613(): pass

    label("Function_77_E613")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_68(15690, 500, 7880, 0)
    MoveCamera(51, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25880, 0)
    SetChrPos(0x101, 14410, 0, 6210, 0)
    SetChrPos(0x102, 13420, 0, 4260, 0)
    SetChrPos(0x104, 12160, 0, 4410, 0)
    SetChrPos(0x103, 12810, 0, 6140, 0)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    SetChrPos(0x11, 13650, 0, 7450, 90)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    Sleep(500)
    SetCameraDistance(24880, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0708
    ChrTalk(
        0x8,
        (
            "#11P真是的……您之前\x01",
            "到底跑到哪里去了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x8,
        (
            "#11P因为医生您擅自离开，给别人添了\x01",
            "多大的麻烦，您到底知不知道啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x11,
        (
            "#6P#2409F哈哈哈，其实我去参加了一个叫做\x01",
            "『费瑟尔杯』的重要比赛呢。\x02\x03",

            "#2400F既然我肩负着钓公师团的名誉，\x01",
            "就绝对不能错过这种比赛，对不对？\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x8,
        (
            "#11P好啦，您多少也该对本职工作\x01",
            "认真一点吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x8,
        (
            "#11P利顿他直到现在，\x01",
            "都在替约亚西姆医生\x01",
            "您拼命工作呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x11,
        (
            "#6P#2405F哦哦，利顿啊！\x02\x03",

            "#2400F哎呀，能有这么一个有出息的学生，\x01",
            "我可真是幸福啊。\x02\x03",

            "#2403F我现在过去打断他的积极工作也不好……\x01",
            "不然，干脆就把剩下的工作\x01",
            "都交给他算了～\x02\x03",

            "#2409F嗯嗯，果然还是这样最好啊。\x01",
            "对他的成长也一定很有帮助……\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x8,
        (
            "#11P#4S#200W请　#200W您　#200W赶　#200W快\x01",
            "#200W回　#200W去　#200W工　#200W作　#200W好　#200W吗　#200W？\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x11,
        "#6P#2406F……是。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0716
    ChrTalk(
        0x101,
        (
            "#12P#0006F（这个人……一直\x01",
            "　都是那种状态吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x103,
        (
            "#12P#0200F（既然身为副教授，\x01",
            "　应该是一位很优秀的人才对……）\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x104,
        "#12P#0309F（天才和那个什么，其实只有一线之隔吧。）\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x102,
        "#12P#0106F（喂……会被听到啦。）\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x12C)
    Sleep(300)

    #C0720
    ChrTalk(
        0x11,
        (
            "#5P#2400F……那么，诸位，\x01",
            "我就此失陪啦。\x02\x03",

            "#2409F如果今后再有机会，\x01",
            "我们还要一起去享受钓鱼的乐趣哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EB88():

        label("loc_EB88")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_EB88")

    QueueWorkItem2(0x0, 1, lambda_EB88)

    def lambda_EB9A():

        label("loc_EB9A")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_EB9A")

    QueueWorkItem2(0x1, 1, lambda_EB9A)

    def lambda_EBAC():

        label("loc_EBAC")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_EBAC")

    QueueWorkItem2(0x2, 1, lambda_EBAC)

    def lambda_EBBE():

        label("loc_EBBE")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_EBBE")

    QueueWorkItem2(0x3, 1, lambda_EBBE)

    def lambda_EBD0():

        label("loc_EBD0")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_EBD0")

    QueueWorkItem2(0x8, 1, lambda_EBD0)
    OP_95(0x11, 11810, 0, 9710, 2000, 0x0)
    OP_95(0x11, 11940, 1230, 16600, 2000, 0x0)
    SetChrFlags(0x11, 0x80)
    Sleep(800)

    #C0721
    ChrTalk(
        0x8,
        "#11P……还要？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_EC36():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EC36)

    def lambda_EC43():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EC43)

    def lambda_EC50():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_EC50)

    def lambda_EC5D():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_EC5D)
    Sleep(300)

    #C0722
    ChrTalk(
        0x101,
        (
            "#6P#0003F那、那个……\x01",
            "请您不必在意。\x02\x03",

            "#0000F总之……\x01",
            "这样应该就算是\x01",
            "完成任务了吧。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x12C)
    Sleep(200)

    #C0723
    ChrTalk(
        0x8,
        (
            "#11P嗯，是的。\x01",
            "真是非常感谢，\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x8,
        (
            "#11P医生能这么快就\x01",
            "回到这里，\x01",
            "全都是诸位的功劳。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x8,
        (
            "#11P如果诸位以后有什么需要，\x01",
            "欢迎随时光临本院哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x8,
        (
            "#11P我们一定会拿出最大的诚意\x01",
            "来接待大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，到时候就要麻烦你们了。\x01",
            "……那么，我们告辞了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0728
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【搜寻副教授的请求】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14410, 1000, 6710, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 14410, 0, 6710, 90)
    SetChrPos(0x1, 14410, 0, 6710, 90)
    SetChrPos(0x2, 14410, 0, 6710, 90)
    SetChrPos(0x3, 14410, 0, 6710, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x11, 0xFF)
    ClearChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    OP_29(0x16, 0x4, 0x10)
    OP_29(0x16, 0x1, 0x6)
    SetScenarioFlags(0x0, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_77_E613 end

    def Function_78_EEDB(): pass

    label("Function_78_EEDB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(55410, 1000, -55440, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 55250, 0, -54750, 135)
    SetChrPos(0x102, 54080, 0, -54680, 90)
    SetChrPos(0x103, 54670, 0, -57660, 45)
    SetChrPos(0x104, 53490, 0, -57740, 45)
    SetChrPos(0x109, 52630, 0, -56430, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0x13, 0x10E, 0x0)
    SetChrSubChip(0x13, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    #C0729
    ChrTalk(
        0x13,
        "#11P呼啊啊……\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x13,
        (
            "#11P昨天我通宵研究了\x01",
            "医疗器械呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x13,
        (
            "#11P虽然想出了非常方便的\x01",
            "便携式设计，\x01",
            "但是进行得并不顺利……\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x101,
        (
            "#5P#0005F（这个人……\x01",
            "　是负责开发医疗器械的啊。）\x02\x03",

            "#0003F（对了！要帮小滴\x01",
            "　找的礼物材料……\x01",
            "　她这里或许会有什么合适的东西吧。）\x02\x03",

            "#0000F那个……打扰一下。\x01",
            "可以和您说几句话吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x13,
        "#11P啊？有什么事吗？\x02",
    )

    CloseMessageWindow()

    #A0734
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德把收集礼物材料\x01",
            "的事情做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0735
    ChrTalk(
        0x101,
        (
            "#5P#0000F……事情就是这样，\x01",
            "如果您有什么不需要的东西，\x01",
            "可以送给我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x13,
        (
            "#11P啊，原来如此，\x01",
            "想亲手给父亲做礼物，\x01",
            "小滴她还真是很可爱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x13,
        (
            "#11P这个嘛，嗯……\x01",
            "这个东西应该很合适吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0738
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x342),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('选秀活动特别奖纪念盾', 1)

    #C0739
    ChrTalk(
        0x101,
        (
            "#5P#0005F这是……\x01",
            "可以镶嵌宝石的\x01",
            "挂坠扣吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x13,
        "#11P嗯，没错。\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x13,
        (
            "#11P这是我在研究\x01",
            "『坠饰型便携式医疗器械』的过程中，\x01",
            "失败之后得到的副产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        (
            "#12P#0205F便携式医疗器械……\x01",
            "竟然还出了那种东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x13,
        (
            "#11P不不，目前还只是试制品而已，\x01",
            "还无法投入到实际应用中呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x13,
        (
            "#11P使用带有治疗效果的结晶回路，\x01",
            "通过它来促进身体的自愈能力。\x01",
            "这就是我的构想。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x104,
        (
            "#12P#0305F呼……\x01",
            "真不愧是乌尔斯拉医院，\x01",
            "所做的研究都很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x109,
        (
            "#6P#0500F如果以后能成为警备队的\x01",
            "实战装备，应该会非常有用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x102,
        (
            "#6P#0105F不过，您刚才好像说，\x01",
            "实验失败了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x13,
        (
            "#11P嗯，昨天晚上，\x01",
            "我试着做出了试制品……\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x13,
        (
            "#11P但不知是哪里出了差错，\x01",
            "将做完的试制品启动之后，\x01",
            "竟然发生了爆炸。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0750
    ChrTalk(
        0x101,
        "#5P#0006F啊，真危险啊……\x02",
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x13,
        (
            "#11P不过，那个挂坠扣\x01",
            "当时就在爆炸的正中心，\x01",
            "结果却奇迹般地毫无伤痕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x13,
        (
            "#11P运气这么好的东西，\x01",
            "一定很适合作为制作礼物的材料吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x101,
        (
            "#5P#0006F（身为研究医疗器械的人，\x01",
            "  说的话还真是缺乏科学性啊……）\x02\x03",

            "#0000F……那么，非常感谢您。\x01",
            "我们就不客气地收下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x13,
        "#11P收下吧～收下吧～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6F9")

    #C0755
    ChrTalk(
        0x101,
        (
            "#5P#0003F（把小滴的\x01",
            "  石头镶嵌在里面，\x01",
            "  就可以做成护身符了吧。）\x02\x03",

            "#0000F（只要再有个链子之类的东西，\x01",
            "  就能做成一条漂亮的\x01",
            "　项链了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6F9")

    OP_29(0x2C, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F79F")
    OP_29(0x2C, 0x1, 0x5)

    #C0756
    ChrTalk(
        0x101,
        (
            "#5P#0000F（制作礼物的材料都收集好了，\x01",
            "  包装用的盒子和丝带也已经找到了……）\x02\x03",

            "（好，我们立刻给\x01",
            "  小滴送去吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F79F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x13, 0x5A, 0x0)
    SetChrPos(0x0, 54500, 0, -55500, 90)
    SetChrPos(0x1, 54500, 0, -55500, 90)
    SetChrPos(0x2, 54500, 0, -55500, 90)
    SetChrPos(0x3, 54500, 0, -55500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_78_EEDB end

    SaveToFile()

Try(main)
