from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0140.bin",                # FileName
        "c0140",                    # MapName
        "c0140",                    # Location
        0x0006,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0140",                  # 0
        "查珂",                   # 1
        "温蒂",                   # 2
        "菲尔纳德",               # 3
        "米泽特",                 # 4
        "巴吉利奥",               # 5
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9329,    0,       -1350,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1519,   0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4480,   0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    2650,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       -1360,   1000,    9330,    1500,    -1350,   0x007E, 0,  7,  0x0000)

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_3D1",          # 02, 2
        "Function_3_570",          # 03, 3
        "Function_4_5A4",          # 04, 4
        "Function_5_720",          # 05, 5
        "Function_6_E75",          # 06, 6
        "Function_7_17BD",         # 07, 7
        "Function_8_17C1",         # 08, 8
        "Function_9_24D4",         # 09, 9
        "Function_10_3B5A",        # 0A, 10
        "Function_11_429D",        # 0B, 11
        "Function_12_4530",        # 0C, 12
        "Function_13_504E",        # 0D, 13
        "Function_14_58C9",        # 0E, 14
        "Function_15_63C3",        # 0F, 15
        "Function_16_66A5",        # 10, 16
        "Function_17_71BB",        # 11, 17
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_208"),
        (1, "loc_214"),
        (2, "loc_220"),
        (3, "loc_22C"),
        (4, "loc_238"),
        (5, "loc_244"),
        (6, "loc_250"),
        (SWITCH_DEFAULT, "loc_25C"),
    )


    label("loc_208")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_214")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_220")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_22C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_238")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_244")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_250")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_27F")

    Return()

    # Function_0_1C8 end

    def Function_1_280(): pass

    label("Function_1_280")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D0")
    OP_95(0xFE, -4480, 0, 9380, 2000, 0x0)
    OP_95(0xFE, -1380, 0, 11120, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 6900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 5230, 0, 1000, 2000, 0x0)
    OP_95(0xFE, 3800, 0, 930, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1350, 0, 930, 2000, 0x0)
    OP_95(0xFE, -1310, 0, -1230, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1310, 0, 2990, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 4640, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 7440, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_280")

    label("loc_3D0")

    Return()

    # Function_1_280 end

    def Function_2_3D1(): pass

    label("Function_2_3D1")

    BeginChrThread(0xB, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3EC")
    OP_93(0xA, 0x0, 0x0)
    Jump("loc_55D")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40B")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_419")
    Jump("loc_55D")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_427")
    Jump("loc_55D")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_43A")
    SetChrFlags(0xC, 0x80)
    Jump("loc_55D")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_448")
    Jump("loc_55D")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_467")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_486")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4A5")
    SetChrPos(0xA, 11420, 4000, 7630, 270)
    Jump("loc_55D")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4B3")
    Jump("loc_55D")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_55D")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4E0")
    SetChrPos(0xC, -4700, 0, -1320, 90)
    Jump("loc_55D")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_527")
    SetChrPos(0xA, 820, 0, 850, 270)
    SetChrPos(0xB, -530, 0, 850, 90)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, 11800, 4000, -1260, 90)
    Jump("loc_55D")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_546")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_554")
    Jump("loc_55D")

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_55D")

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56F")
    Event(0, 15)

    label("loc_56F")

    Return()

    # Function_2_3D1 end

    def Function_3_570(): pass

    label("Function_3_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5A3")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5A3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5A3")

    label("loc_5A3")

    Return()

    # Function_3_570 end

    def Function_4_5A4(): pass

    label("Function_4_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_716")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66B")

    #C0001
    ChrTalk(
        0x8,
        (
            "啊，你们就是温蒂前辈的\x01",
            "朋友吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "你们知道吗～？\x01",
            "我们最近新推出了更换\x01",
            "战术导力器外壳的服务哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "有各种时尚漂亮的款式\x01",
            "可供选择～\x01",
            "请一定要看一看～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 4)

    label("loc_66B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_675")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "更换外壳\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EA")
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_709")

    label("loc_6EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_709")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_709")

    Jump("loc_675")

    label("loc_70E")

    TalkEnd(0x8)
    Jump("loc_71F")

    label("loc_716")

    TalkBegin(0x8)
    Call(0, 6)
    TalkEnd(0x8)

    label("loc_71F")

    Return()

    # Function_4_5A4 end

    def Function_5_720(): pass

    label("Function_5_720")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_72A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E74")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_770")
    MenuCmd(1, 0, "蓝色警官　　　　      已经购买")
    MenuCmd(3, 0, 0x0)
    Jump("loc_792")

    label("loc_770")

    MenuCmd(1, 0, "蓝色警官　　　　      1000米拉")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_7C6")
    MenuCmd(1, 0, "和平绿　　        　　已经购买")
    MenuCmd(3, 0, 0x1)
    Jump("loc_7E8")

    label("loc_7C6")

    MenuCmd(1, 0, "和平绿        　　　　1000米拉")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_81C")
    MenuCmd(1, 0, "黑猫            　　　已经购买")
    MenuCmd(3, 0, 0x2)
    Jump("loc_83E")

    label("loc_81C")

    MenuCmd(1, 0, "黑猫            　　　1000米拉")

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_872")
    MenuCmd(1, 0, "危险橙            　　已经购买")
    MenuCmd(3, 0, 0x3)
    Jump("loc_894")

    label("loc_872")

    MenuCmd(1, 0, "危险橙            　　1000米拉")

    label("loc_894")

    MenuCmd(1, 0, "放弃")

    #A0004
    AnonymousTalk(
        0x8,
        (
            scpstr(0x18),
            "要更换为哪一个～？\x02",
        )
    )

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E3")
    Sleep(1)
    Return()

    label("loc_8E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_923")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis172.itp")
    Jump("loc_9DE")

    label("loc_923")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_963")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis173.itp")
    Jump("loc_9DE")

    label("loc_963")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A3")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis174.itp")
    Jump("loc_9DE")

    label("loc_9A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DE")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis175.itp")

    label("loc_9DE")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A73")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是罗伊德专用的。\x01",
            "购入后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB5")

    label("loc_A73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE0")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是艾莉专用的。\x01",
            "购入后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB5")

    label("loc_AE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4D")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是缇欧专用的。\x01",
            "购入后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB5")

    label("loc_B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB5")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是兰迪专用的。\x01",
            "购入后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB5")


    #A0009
    AnonymousTalk(
        0x8,
        "好的，确定要更换为这种款式吗～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【确定更换】\x01",      # 0
            "【还是算了】\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E57")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C96")

    #C0010
    ChrTalk(
        0x8,
        (
            "咦～您的米拉好像不够呢。\x01",
            "这样是没办法更换的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E48")

    label("loc_C96")


    #C0011
    ChrTalk(
        0x8,
        (
            "明白啦。\x01",
            "请稍等一下哦～⊥\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0012
    ChrTalk(
        0x8,
        "好了，让您久等啦。\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D32")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了罗伊德的战术导力器外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 5)
    Jump("loc_DE4")

    label("loc_D32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6F")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了艾莉的战术导力器外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 6)
    Jump("loc_DE4")

    label("loc_D6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAC")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了缇欧的战术导力器外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 7)
    Jump("loc_DE4")

    label("loc_DAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE4")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了兰迪的战术导力器外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 0)

    label("loc_DE4")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E1F")
    OP_DE(0x16, 0x0)

    label("loc_E1F")


    #C0017
    ChrTalk(
        0x8,
        (
            "呵呵，期待您的\x01",
            "下次光临～\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_E48")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E61")

    label("loc_E57")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E61")

    OP_CA(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_72A")

    label("loc_E74")

    Return()

    # Function_5_720 end

    def Function_6_E75(): pass

    label("Function_6_E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_EF8")

    #C0018
    ChrTalk(
        0x8,
        (
            "真是的，爸爸难道\x01",
            "仍然在意着那件事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "我都已经不在意啦。\x01",
            "现在的工作也让我很满意，\x01",
            "所以根本不用再烦恼了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_F61")

    #C0020
    ChrTalk(
        0x8,
        (
            "温蒂前辈每天早上都是一副\x01",
            "睡眼惺忪的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "总是这样的话，会把店长惹怒的哦～……\x02",
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_FE1")

    #C0022
    ChrTalk(
        0x8,
        (
            "……昨天明明都说得那么明白了，\x01",
            "结果爸爸还是过来看我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "嗯嗯，看来也只能放着他不管，\x01",
            "直到他看够为止了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_FEF")
    Jump("loc_17BC")

    label("loc_FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1098")

    #C0024
    ChrTalk(
        0x8,
        (
            "我对偷偷过来看我的爸爸说，\x01",
            "让他以后不要再来我的工作地点偷看了，\x01",
            "结果他一脸悲伤地回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "呜呜，我明明没有做错任何事，\x01",
            "但却有很强烈的罪恶感呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1106")

    #C0026
    ChrTalk(
        0x8,
        (
            "呜～爸爸今天又偷偷\x01",
            "来看我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "虽然很高兴他这么关心我，\x01",
            "但这么做会让我没法专心工作的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1160")

    #C0028
    ChrTalk(
        0x8,
        (
            "就算是同样价位的导力器，\x01",
            "如果制造商不同，\x01",
            "也会存在一些微妙的性能差异。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_11D1")

    #C0029
    ChrTalk(
        0x8,
        (
            "在购买导力器时，\x01",
            "犹豫不决地进行比较挑选\x01",
            "其实正是购物中最快乐的部分。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "就请您慢慢\x01",
            "挑选吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_11D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1246")

    #C0031
    ChrTalk(
        0x8,
        (
            "藏在那边的那个人\x01",
            "是我的爸爸……\x01",
            "早就暴露了嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "真是的，怎么一直都\x01",
            "不能接受孩子独立的现实呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_12CD")

    #C0033
    ChrTalk(
        0x8,
        (
            "就算是同种类型的导力器，\x01",
            "也不全是同一家制造商所制造的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "每个客人喜爱的品牌\x01",
            "也未必一样，\x01",
            "这也是件挺有趣的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_12CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_132F")

    #C0035
    ChrTalk(
        0x8,
        (
            "虽然我并不是很熟悉温蒂\x01",
            "前辈的师傅……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "但据说是一位非常厉害的\x01",
            "导力技师呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_132F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_142A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CA")

    #C0037
    ChrTalk(
        0x8,
        (
            "店长他今天早上\x01",
            "又对温蒂前辈\x01",
            "说了些冷嘲热讽的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "昨天明明还刚请\x01",
            "温蒂前辈帮过忙的……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "店长的性格真的\x01",
            "是很差劲啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1425")

    label("loc_13CA")


    #C0040
    ChrTalk(
        0x8,
        (
            "昨天明明还刚请\x01",
            "温蒂前辈帮过忙的……\x01",
            "今天就说这样的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "店长的性格\x01",
            "真是很差啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1425")

    Jump("loc_17BC")

    label("loc_142A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_14BB")

    #C0042
    ChrTalk(
        0x8,
        (
            "啊，店长他虽然性格差，\x01",
            "但对待客人态度还是很好的～\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "店长是个导力器盲，\x01",
            "相关的知识连我都不如……\x01",
            "但却把商店经营得很不错呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_14BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1554")

    #C0044
    ChrTalk(
        0x8,
        (
            "早～上～好☆\x01",
            "刚才有位游击士来了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "他有着清爽飘逸的黑发，\x01",
            "还有一双漂亮的琥珀色眼睛……⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "呀呀，我好像都对他\x01",
            "一见钟情了呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_15C1")

    #C0047
    ChrTalk(
        0x8,
        (
            "哇～……\x01",
            "爸爸又来窥视\x01",
            "我的工作状况了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "总是把我当小孩子看待，\x01",
            "我都觉得很不好意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_15C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1633")

    #C0049
    ChrTalk(
        0x8,
        (
            "欢迎光临～☆\x01",
            "这里是销售柜台。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "如果需要修理导力产品，\x01",
            "请去旁边的服务台，\x01",
            "欢迎您光顾哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168F")

    #C0051
    ChrTalk(
        0x8,
        (
            "各位，你们好像认识\x01",
            "温蒂前辈吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "我是销售员查珂。\x01",
            "请多多指教～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 0)
    Jump("loc_17BC")

    label("loc_168F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1778")

    #C0053
    ChrTalk(
        0x8,
        (
            "这家商店，自从开业之后，\x01",
            "来客每天都络绎不绝呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "但我并不是\x01",
            "很懂导力制品哦……\x01",
            "所以总是要向前辈请教。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "温蒂前辈的知识\x01",
            "真是非常渊博呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0000F（知识渊博吗……\x01",
            "  她只是从以前开始就很喜欢这些罢了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17BC")

    label("loc_1778")


    #C0057
    ChrTalk(
        0x8,
        (
            "温蒂前辈的知识\x01",
            "真是非常渊博呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "她总是会教我\x01",
            "很多东西呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BC")

    Return()

    # Function_6_E75 end

    def Function_7_17BD(): pass

    label("Function_7_17BD")

    Call(0, 8)
    Return()

    # Function_7_17BD end

    def Function_8_17C1(): pass

    label("Function_8_17C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17EB")
    Call(0, 17)
    Return()

    label("loc_17EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_180C")
    Call(0, 16)
    Return()

    label("loc_180C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2156")
    EventBegin(0x0)
    Fade(500)
    OP_68(7380, 1500, -2280, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 6900, 0, -2250, 90)
    SetChrPos(0x102, 6900, 0, -1100, 90)
    SetChrPos(0x103, 5600, 0, -2250, 90)
    SetChrPos(0x104, 5600, 0, -1100, 90)
    OP_93(0x9, 0x10E, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_6F(0x10)
    OP_0D()

    #C0059
    ChrTalk(
        0x9,
        (
            "#11P啊～！您好～！\x01",
            "欢迎光临『原点工房』……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "#11P……错了，\x01",
            "欢迎光临导力商店『原点』～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x9,
        (
            "#11P哎……\x01",
            "哇哇，这不是罗伊德嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0011F#6P温蒂！？\x01",
            "你在这里干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        "#11P呼～好失礼啊～\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "#11P这还用问嘛，\x01",
            "我当然是这个商店里的技师啦～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A1E")
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    label("loc_1A1E")


    #C0065
    ChrTalk(
        0x101,
        (
            "#0011F#6P是、是吗！？\x01",
            "说起来，确实是听说过你已经工作了……\x02\x03",

            "#0002F不过，还是稍微\x01",
            "有些意外呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0302F#5P怎么，这位是罗伊德的青梅竹马吗？\x01",
            "嘿～很可爱的女孩嘛。\x02\x03",

            "#0309F下次和我去约个会如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#0106F#6P……你在趁乱\x01",
            "打什么主意呢？\x02\x03",

            "#0100F你好。\x01",
            "之前就对这里有所耳闻，\x01",
            "还真是一家相当漂亮的店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        "#11P啊，各位是罗伊德的同事吗？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "#11P啊哈哈，其实本店的装潢\x01",
            "完全都是按照店长个人的喜好来设计的～\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "#11P顺便一说，这里是\x01",
            "客户服务柜台哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#11P具体营业内容就是\x01",
            "战术导力器的维修保养之类的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0000F#6P是吗，看来只要拜托温蒂，\x01",
            "就能轻松解决这类问题了呢。\x02\x03",

            "#0005F啊，不过我们的导力器\x01",
            "是名为『艾尼格玛』的新型号，\x01",
            "……没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "#11P哎……罗伊德，你们\x01",
            "也开始使用新型战术导力器了啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "#11P嗯嗯，交给我吧。\x01",
            "新型导力器用的回路调整器这里也有……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#11P其实，前段时间就有不少的游击士\x01",
            "来我们店调整导力器了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#0011F#6P是、是这样……吗？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#0203F#6P看来游击士协会那边\x01",
            "也开始将艾尼格玛\x01",
            "用于实战配备了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#0302F#5P哈哈，游击士\x01",
            "果然行动迅速啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        "#0106F#6P亏你还笑得出来呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0080
    ChrTalk(
        0x101,
        (
            "#0012F#6P啊，反正也不是什么\x01",
            "大不了的事情啦。\x02\x03",

            "#0000F总之，我想今后可能会\x01",
            "经常来找温蒂帮忙的。\x01",
            "请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        "#11P嗯，彼此彼此，请多关照啦！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "#11P想对导力器进行改造时\x01",
            "就来找我，然后选择\x01",
            "『改造·合成』就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "#11P另外，如果对导力器\x01",
            "有什么不明白，\x01",
            "不管是什么都可以随时来问。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        "#11P毕竟我也是个职业技师呢。\x02",
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 180, 60, -1)

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在导力商店选择『改造·合成』，\x01",
            "  就可以合成新的回路，\x01",
            "  或开封战术导力器的结晶孔。\x02\x03",

            "※合成新的回路，并将其镶嵌至导力器中，\x01",
            "  就可以使用各种各样的导力魔法了。\x01",
            "  （请在菜单中选择[QUARTZ]。）\x02\x03",

            "※开封结晶孔后，\x01",
            "  可镶嵌的回路不仅会增加，\x01",
            "  同时，最大ＥＰ值也会得到提升。\x01",
            "  （请在菜单中选择[SLOT]。）\x02\x03",

            "※在利用各项服务时，\x01",
            "  需要使用被称为『耀晶片』的结晶碎片。\x01",
            "  『耀晶片』则可通过打倒魔兽来获得。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0x4C, 1)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 6980, 0, -1400, 90)
    EventEnd(0x5)
    Return()

    label("loc_2156")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2394")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_217D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "改造·合成\x01",        # 1
            "询问\x01",              # 2
            "询问委托内容\x01",      # 3
            "放弃\x01",              # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21E5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_21E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2205")
    Call(0, 11)

    label("loc_2205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2215")
    OP_AF(0xF)
    Jump("loc_2257")

    label("loc_2215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2225")
    OP_AF(0xE)
    Jump("loc_2257")

    label("loc_2225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2235")
    OP_AF(0xD)
    Jump("loc_2257")

    label("loc_2235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2245")
    OP_AF(0xC)
    Jump("loc_2257")

    label("loc_2245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2255")
    OP_AF(0xB)
    Jump("loc_2257")

    label("loc_2255")

    OP_AF(0xA)

    label("loc_2257")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_238A")

    label("loc_2266")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2287")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_238A")

    label("loc_2287")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235A")

    #C0086
    ChrTalk(
        0x9,
        (
            "为了评估艾尼格玛的性能，\x01",
            "请试着使用一次\x01",
            "『让敌人无法发现自己的魔法』。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "请各位在实战中使用\x01",
            "这个魔法，并确认一下\x01",
            "它究竟有没有效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "测试结束之后，\x01",
            "请来找我进行报告哦。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_238A")

    label("loc_235A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_236E")
    Jump("loc_238A")

    label("loc_236E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_238A")

    Jump("loc_217D")

    label("loc_238F")

    Jump("loc_24D0")

    label("loc_2394")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_239E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "改造·合成\x01",      # 1
            "询问\x01",            # 2
            "放弃\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_23F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2419")
    Call(0, 11)

    label("loc_2419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2429")
    OP_AF(0xF)
    Jump("loc_246B")

    label("loc_2429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2439")
    OP_AF(0xE)
    Jump("loc_246B")

    label("loc_2439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2449")
    OP_AF(0xD)
    Jump("loc_246B")

    label("loc_2449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2459")
    OP_AF(0xC)
    Jump("loc_246B")

    label("loc_2459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2469")
    OP_AF(0xB)
    Jump("loc_246B")

    label("loc_2469")

    OP_AF(0xA)

    label("loc_246B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24CB")

    label("loc_247A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_24CB")

    label("loc_249B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AF")
    Jump("loc_24CB")

    label("loc_24AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24CB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_24CB")

    Jump("loc_239E")

    label("loc_24D0")

    TalkEnd(0x9)
    Return()

    # Function_8_17C1 end

    def Function_9_24D4(): pass

    label("Function_9_24D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_257D")

    #C0089
    ChrTalk(
        0x9,
        (
            "话说，你们真是帮了大忙呢～\x01",
            "用户的意见果然很宝贵啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "罗伊德，如果以后再有什么事情，\x01",
            "到时就麻烦你啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#0000F嗯，不用客气，\x01",
            "尽管委托给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B59")

    label("loc_257D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2684")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2625")

    #C0092
    ChrTalk(
        0x9,
        (
            "不知为何，菲尔纳德先生也\x01",
            "变得好相处了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "而且，最近好像也开始\x01",
            "学习导力器方面的知识了。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "呵呵，机会难得，\x01",
            "下次我再教教他好啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_267F")

    label("loc_2625")


    #C0095
    ChrTalk(
        0x9,
        (
            "和菲尔纳德先生的关系\x01",
            "似乎变得比以前好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "下次再辅导他\x01",
            "学习导力器方面的知识吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_267F")

    Jump("loc_3B59")

    label("loc_2684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26D6")

    #C0097
    ChrTalk(
        0x9,
        "呼～……早上总是容易犯困啊～\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "真羡慕查珂，一直那么有活力。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B59")

    label("loc_26D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_280F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A2")

    #C0099
    ChrTalk(
        0x9,
        (
            "最初还担心这里的工作不适合自己，\x01",
            "但现在看来，导力商店也不坏哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "因为器材齐全，所以修理工作\x01",
            "也能顺利完成，比工房时代\x01",
            "更能吸引客人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "嗯～外观果然也是很重要的啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_280A")

    label("loc_27A2")


    #C0102
    ChrTalk(
        0x9,
        (
            "不久之前，在街上遇到的客人\x01",
            "还特意为我帮他修理东西的事情道谢呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "能从事这份工作\x01",
            "真是很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280A")

    Jump("loc_3B59")

    label("loc_280F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_281D")
    Jump("loc_3B59")

    label("loc_281D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2876")

    #C0104
    ChrTalk(
        0x9,
        "爸爸又出差了哦。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "啊～把照顾潘莎的事情都推给我，\x01",
            "他倒是很轻松呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B59")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D16")

    #C0106
    ChrTalk(
        0x9,
        "啊，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "好久不见了啊～\x01",
            "呀哈～！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x153,
        (
            "#1110F呀哈～！\x01",
            "好棒的店呀～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x153, 500)
    Sleep(300)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1800)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2957")

    #C0109
    ChrTalk(
        0x102,
        (
            "#0100F小琪雅，\x01",
            "又在如此绝妙的时机下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D2")

    label("loc_2957")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2997")

    #C0110
    ChrTalk(
        0x103,
        (
            "#0200F又在这种\x01",
            "绝妙的时机插话了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D2")

    label("loc_2997")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29D2")

    #C0111
    ChrTalk(
        0x104,
        (
            "#0300F阿琪，你插嘴得\x01",
            "还真是时候呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D2")

    OP_64(0x9)

    #C0112
    ChrTalk(
        0x9,
        "怎么回事，这孩子……真是好可爱啊。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，连温蒂\x01",
            "也这么觉得吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0114
    ChrTalk(
        0x9,
        (
            "什么嘛，我又不是\x01",
            "只会欣赏机械。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "不过还真是大吃一惊啊……罗伊德\x01",
            "竟然如此有责任心。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#0000F哎…………责任心？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "她就是在纪念庆典时和家人失散的那个孩子吧，\x01",
            "之后就被暂时寄养在支援科了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "啊，你之所以一周都没来过，\x01",
            "原来就是在忙这件事啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#0003F（倒也不能说她完全说错了……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BB3")

    #C0120
    ChrTalk(
        0x102,
        (
            "#0100F这个孩子是小琪雅……\x01",
            "我们目前正在调查\x01",
            "有关她身份的信息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5C")

    label("loc_2BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C0A")

    #C0121
    ChrTalk(
        0x103,
        (
            "#0200F这个孩子是琪雅……\x01",
            "我们目前正在调查\x01",
            "有关她身份的信息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5C")

    label("loc_2C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C5C")

    #C0122
    ChrTalk(
        0x104,
        (
            "#0300F这小鬼叫琪雅，\x01",
            "目前倒还真是身份不明，\x01",
            "还在继续调查呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5C")


    #C0123
    ChrTalk(
        0x9,
        (
            "果然如此。\x01",
            "嗯～虽然我也没有什么线索……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "不过，如果遇到什么困难，可要和我说哦。\x01",
            "我也有个妹妹，\x01",
            "所以早就习惯照顾小孩啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0000F多谢哦，如果有什么事，\x01",
            "到时再麻烦你。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 6)
    Jump("loc_2DE3")

    label("loc_2D16")

    TurnDirection(0x9, 0x153, 0)

    #C0126
    ChrTalk(
        0x9,
        (
            "小琪雅吗……\x01",
            "或许比我家的潘莎\x01",
            "还要小一点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "小琪雅，如果走累了，\x01",
            "就要马上告诉罗伊德哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "罗伊德那家伙有时比较\x01",
            "粗心大意，注意不到这些的。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x153,
        "#1109F嗯，知道了～！\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        "#0000F哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_2DE3")

    Jump("loc_3B59")

    label("loc_2DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E4C")

    #C0131
    ChrTalk(
        0x9,
        (
            "说起来，\x01",
            "爸爸下个月就该出差归来啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "应该能赶上纪念庆典呢，\x01",
            "太好了，太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B59")

    label("loc_2E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE7")

    #C0133
    ChrTalk(
        0x9,
        (
            "车站里那些来来往往的列车，\x01",
            "是由帝国的莱恩福尔特公司制造的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "车头前的那个独角兽装饰，\x01",
            "让人一看知道就是帝国制造的呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F23")

    label("loc_2EE7")


    #C0135
    ChrTalk(
        0x9,
        (
            "莱恩福尔特公司的产品\x01",
            "经常给人一种\x01",
            "大气、粗犷的感觉呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F23")

    Jump("loc_3B59")

    label("loc_2F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2F9A")

    #C0136
    ChrTalk(
        0x9,
        "差不多也该回去了啊。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        (
            "要不要去面包咖啡馆买一些\x01",
            "点心面包之类的东西，\x01",
            "带回去给潘莎当礼物呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B59")

    label("loc_2F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_30B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3074")

    #C0138
    ChrTalk(
        0x9,
        (
            "你知道放置在店内的导力车\x01",
            "是怎样搬进店里的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "正确答案是……\x01",
            "环绕着导力车建造商店！\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0005F是、是这样的吗！？\x01",
            "原来如此，这就是所谓的逆向思维啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        "……这明显是在开玩笑嘛。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30B0")

    label("loc_3074")


    #C0142
    ChrTalk(
        0x9,
        (
            "啊哈哈，罗伊德\x01",
            "真是个超级老实人，\x01",
            "想骗你真是太容易了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B0")

    Jump("loc_3B59")

    label("loc_30B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_31D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3172")

    #C0143
    ChrTalk(
        0x9,
        (
            "罗伊德，爱普斯泰恩公司制造的\x01",
            "新型导力扫除机今天刚到货哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#0000F那个，温蒂，\x01",
            "你是推荐让我买吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            "啊哈哈，没有啦～\x01",
            "请自便就好，\x01",
            "我只是随便说说而已～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31D0")

    label("loc_3172")


    #C0146
    ChrTalk(
        0x9,
        (
            "爱普斯泰恩公司制造的\x01",
            "新型导力吸尘器今天刚到货哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "我最喜欢新产品的\x01",
            "那种独特味道了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31D0")

    Jump("loc_3B59")

    label("loc_31D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3459")

    #C0148
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔警备队好像\x01",
            "追加了特殊装甲车的订单呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "嗯～那里的装备\x01",
            "还是一如既往地高级啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        "身为技师，也想去那里工作看看呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3454")

    #C0151
    ChrTalk(
        0x104,
        (
            "#0300F哈，毕竟是守卫着自治州的\x01",
            "治安维持部队嘛。\x02\x03",

            "#0304F至于去那里工作什么的，\x01",
            "我劝你还是打消这种念头比较好。\x02\x03",

            "#0300F哼哼……对你这种可爱的女孩来说，\x01",
            "应该有比那里更加合适的工作地点啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x9,
        "哇～谢谢你，兰迪先生！\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "我果然还是应该\x01",
            "以发明工房之类的地方为目标啊！\x02",
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
    Sleep(1000)

    #C0154
    ChrTalk(
        0x104,
        "#0306F（不行，她都不上钩的啊。）\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x103,
        (
            "#0200F（兰迪前辈，继医院之后\x01",
            "  第二次搭讪失败呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 4)

    label("loc_3454")

    Jump("loc_3B59")

    label("loc_3459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_34BD")

    #C0156
    ChrTalk(
        0x9,
        (
            "店长真是的……\x01",
            "明明是个导力器盲，\x01",
            "却还那么死要面子。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        "我稍后必须去帮帮他呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B59")

    label("loc_34BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3621")

    #C0158
    ChrTalk(
        0x9,
        (
            "早上好～罗伊德，还有各位。\x01",
            "工作还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，这个嘛，\x01",
            "反正还算正常吧……大概。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x103,
        (
            "#0203F形形色色的工作堆积如山，\x01",
            "确实有些吃不消呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "啊哈哈哈哈……\x01",
            "嗯嗯，看起来很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "在外出之前，\x01",
            "一定要仔细确认一下\x01",
            "导力器的状态哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        "否则事后就算出现麻烦，也无法补救哦～\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#0000F嗯，明白了。\x01",
            "谢啦，温蒂。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 5)
    Jump("loc_3762")

    label("loc_3621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3710")

    #C0165
    ChrTalk(
        0x9,
        (
            "游击士们最近似乎\x01",
            "也开始使用新型的\x01",
            "战术导力器了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "而且昨天来了一位叫达德利的警官，\x01",
            "他所使用的也是新型导力器……\x01",
            "看来新型号也已经相当普及了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#0300F看来我们也只能\x01",
            "坚持用下去了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        "#0106F也是啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3762")

    label("loc_3710")


    #C0169
    ChrTalk(
        0x9,
        (
            "经常会有警察和\x01",
            "游击士来我们店。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "使用新型导力器的人\x01",
            "好像也增加了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3762")

    Jump("loc_3B59")

    label("loc_3767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_385B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F4")

    #C0171
    ChrTalk(
        0x9,
        (
            "我们店的店长，\x01",
            "以前好像是个很有名的设计师。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "他确实是有一定的审美品位……\x01",
            "但性格稍微有些让人难以亲近呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3856")

    label("loc_37F4")


    #C0173
    ChrTalk(
        0x9,
        (
            "这家商店的内部装潢\x01",
            "都是店长自己设计的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "……其实只要观察一下，\x01",
            "就能大致感觉出来了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3856")

    Jump("loc_3B59")

    label("loc_385B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3B59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4A")

    #C0175
    ChrTalk(
        0x9,
        (
            "这家导力商店直到去年\x01",
            "都还只是一家普通的工房。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "但自从前店长被换下去之后，\x01",
            "无论是店内装潢，还是经营方针，\x01",
            "全都焕然一新了，让人眼前一亮。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "但我还是更喜欢\x01",
            "简陋粗糙的老式工房呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈……\x01",
            "确实，那种地方才比较\x01",
            "符合温蒂的风格呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        "……喂，罗伊德，你刚才说了什么吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0180
    ChrTalk(
        0x101,
        (
            "#0006F十分抱歉，\x01",
            "我什么都没说。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        (
            "对了对了，我在工房时的那位师傅\x01",
            "好像在旧城区开了家店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        (
            "罗伊德，你们以后如果有空，\x01",
            "不妨也过去看一看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 0)
    Jump("loc_3B59")

    label("loc_3A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B16")

    #C0183
    ChrTalk(
        0x9,
        (
            "这家导力商店直到去年\x01",
            "都还只是一家普通的工房呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "我的老师也曾说过要在这里\x01",
            "大显身手呢……不过最后还是由于\x01",
            "不喜欢这里的风格，所以离开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "我也比较喜欢\x01",
            "简陋粗糙的老式工房呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B59")

    label("loc_3B16")


    #C0186
    ChrTalk(
        0x9,
        (
            "听说老师在旧城区\x01",
            "开了一家店……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        "要不要偷偷去看看情况呢？\x02",
    )

    CloseMessageWindow()

    label("loc_3B59")

    Return()

    # Function_9_24D4 end

    def Function_10_3B5A(): pass

    label("Function_10_3B5A")


    #C0188
    ChrTalk(
        0x9,
        (
            "ＯＫ。\x01",
            "想问哪方面的问题呢？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_428F")
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "关于战术导力器\x01",      # 0
            "关于回路\x01",            # 1
            "关于结晶孔\x01",          # 2
            "关于导力魔法\x01",        # 3
            "放弃\x01",                # 4
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C06")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_3C06")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3C28"),
        (1, "loc_3DEF"),
        (2, "loc_3F1C"),
        (3, "loc_401F"),
        (SWITCH_DEFAULT, "loc_427B"),
    )


    label("loc_3C28")


    #C0189
    ChrTalk(
        0x9,
        (
            "所谓的『战术导力器』，\x01",
            "就是一种专门用于个人战斗的\x01",
            "便携式小型导力器。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "不仅能强化使用者的能力，\x01",
            "还可以用来发动导力魔法。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "一般情况下，我们就把它\x01",
            "简称为『导力器』啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "你们所使用的，\x01",
            "就是其中的最新型号——\x01",
            "名为『艾尼格玛』的导力器。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "为了配合每个人的具体情况与使用习惯，\x01",
            "我们会对导力器进行完美的微调，\x01",
            "所以其构造会因人而异。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        (
            "像限定属性的结晶孔啦，连接结晶孔的\x01",
            "结晶链形状啦，都会有所不同。\x01",
            "各位可以自行比较一下每个人的导力器。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_3DEF")


    #C0195
    ChrTalk(
        0x9,
        (
            "所谓回路，就是将耀晶片进行精炼后\x01",
            "所制造出的，战术导力器专用的『结晶回路』。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "如果携带有足够数量的耀晶片，\x01",
            "就可以在我们这里进行合成。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "每种回路都有各自的特性效果，\x01",
            "同一条结晶链上的回路属性值达到一定数值后，\x01",
            "就可以使用特定的导力魔法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        "如果你们攒够了耀晶片，可以进行多种尝试呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_3F1C")


    #C0199
    ChrTalk(
        0x9,
        (
            "导力器的结晶孔，\x01",
            "在最初时几乎都是未开封的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "所以如果想要镶嵌回路，\x01",
            "首先需要开封结晶孔。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "多开封一些结晶孔，\x01",
            "不仅可以镶嵌更多的回路，\x01",
            "同时也能提升最大ＥＰ值。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "开封虽然也需要使用耀晶片，\x01",
            "但开封之后会非常便利。\x01",
            "所以请大家积极开封哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_401F")


    #C0203
    ChrTalk(
        0x9,
        (
            "利用战术导力器发动的魔法\x01",
            "统称为导力魔法，在多数情况下，\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        "我们习惯将它简称为『魔法』。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "其实，魔法是由安置在导力器内部的机械装置\x01",
            "和回路与使用者产生连锁共鸣，\x01",
            "从而引发的现象……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        "算了，这种细节知识不说也罢。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "而可发动的魔法，是由\x01",
            "『每条结晶链上所镶嵌的回路属性总值』\x01",
            "所决定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x9,
        (
            "这个稍微有些复杂，怎么说好呢……\x01",
            "对了，举个例子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x9,
        (
            "在处于同一条结晶链上的\x01",
            "结晶孔中镶嵌回路，\x01",
            "如果地属性的总值超过了２……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        (
            "就可以使用『地震波』\x01",
            "这个魔法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "镶嵌的回路数越多，\x01",
            "可使用的魔法种类\x01",
            "也就越多。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        (
            "至于发动其它魔法所需的属性值，\x01",
            "应该都记录在魔法列表中了。\x01",
            "请随时参考吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_427B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_428A")

    label("loc_428A")

    Jump("loc_3B85")

    label("loc_428F")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_3B5A end

    def Function_11_429D(): pass

    label("Function_11_429D")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    #C0213
    ChrTalk(
        0x9,
        (
            "对了，罗伊德，\x01",
            "你们有没有带着『高级回路』呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#0005F『高级回路』……？\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        (
            "嗯嗯，这种回路由于效果强大，\x01",
            "所以无法镶嵌于普通的结晶孔中。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x9,
        (
            "如果想要镶嵌这种回路，\x01",
            "就需要对结晶孔本身进行强化哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F2")

    #C0217
    ChrTalk(
        0x9,
        (
            "虽然在我们店也\x01",
            "暂时没法合成高级回路……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        (
            "但结晶孔的强化还是没有问题的，\x01",
            "有需要的时候就请和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4448")

    label("loc_43F2")


    #C0219
    ChrTalk(
        0x9,
        (
            "我们店也开始提供结晶孔的强化和\x01",
            "高级回路的合成服务了，\x01",
            "有需要的时候就请和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4448")

    OP_5A()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※今后可以对结晶孔进行强化了。\x02",
        )
    )

    CloseMessageWindow()

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※选择[SLOT]之后，\x01",
            "  再选择已经开封过的结晶孔，\x01",
            "  就可以强化结晶孔的等级了。\x02",
        )
    )

    CloseMessageWindow()

    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※强化之后，\x01",
            "  不仅可以镶嵌高级回路，\x01",
            "  最大ＥＰ值也会得到进一步提升。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)
    Return()

    # Function_11_429D end

    def Function_12_4530(): pass

    label("Function_12_4530")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_465B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F0")
    OP_93(0xFE, 0x0, 0x0)

    #C0223
    ChrTalk(
        0xFE,
        "嗯……嗯嗯，原来如此……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "可能是由于导力灯的插座\x01",
            "太脏而引起的接触不良……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0225
    ChrTalk(
        0xFE,
        (
            "失、失礼了。\x01",
            "请问有何贵干？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 2)
    Return()

    label("loc_45F0")


    #C0226
    ChrTalk(
        0xFE,
        "想咨询关于导力器的问题？\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "不好意思啊，我现在也正在学习……\x01",
            "还是请您去那边的\x01",
            "服务柜台咨询吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_465B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_46C1")

    #C0228
    ChrTalk(
        0xFE,
        (
            "……嗯……温蒂那磕睡虫，\x01",
            "又趴在柜台上睡着了……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "哼，稍后一定要\x01",
            "好好说说她啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_46C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4728")

    #C0230
    ChrTalk(
        0xFE,
        (
            "前一段时间，温蒂\x01",
            "第一次夸赞了我\x01",
            "陈列商品的方式呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "……我、我可没\x01",
            "觉得高兴哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_4728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4736")
    Jump("loc_504A")

    label("loc_4736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_47DA")

    #C0232
    ChrTalk(
        0xFE,
        (
            "温蒂来问我，\x01",
            "除了修理之外，\x01",
            "她能不能也负责接待……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "……老实说，多亏了她，\x01",
            "使店里也有了不少回头客。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "是不是应该\x01",
            "好好考虑一下她的提议呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_47DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48EA")

    #C0235
    ChrTalk(
        0xFE,
        (
            "哎呀……莫非您想购买\x01",
            "本店的高级导力车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x153,
        (
            "#1105F那个那个，\x01",
            "可以摸一摸吗？\x02\x03",

            "#1100F（伸手摸～……）\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#0005F哇～不行不行！\x01",
            "万一摸坏了，\x01",
            "我们可是赔不起的啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x153,
        "#1106F什么～嘛。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "……请看好您的孩子，\x01",
            "不要让她离开您的视线范围啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_494C")

    label("loc_48EA")


    #C0240
    ChrTalk(
        0xFE,
        (
            "……咳咳。\x01",
            "……请看好您的孩子，\x01",
            "不要让她离开您的视线范围啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        "#0006F（引起警惕了呢……）\x02",
    )

    CloseMessageWindow()

    label("loc_494C")

    Jump("loc_504A")

    label("loc_4951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_49D6")

    #C0242
    ChrTalk(
        0xFE,
        (
            "就我个人来说，也很希望导力车的\x01",
            "销售能步入正轨呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "作为其措施之一，就是希望\x01",
            "自治州政府能够大力推进\x01",
            "普及工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_49D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4AA2")

    #C0244
    ChrTalk(
        0xFE,
        (
            "呜呜，可恶的温蒂……\x01",
            "居然对我这华丽的商品\x01",
            "陈列方式妄加批评。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "……不过，令人不甘心的是，\x01",
            "她似乎还真是一针见血地戳中了要害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "不愧是这里成为导力商店之前\x01",
            "就在工房工作的人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_4AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7A")

    #C0247
    ChrTalk(
        0xFE,
        (
            "本店正在展示运用最新技术的\x01",
            "导力网络……总之就是\x01",
            "这类东西的终端哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "虽然我不太了解具体情况，\x01",
            "但这东西十分昂贵。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "呵呵……如果各位有兴趣，\x01",
            "欢迎参观二层爱普斯泰恩财团的\x01",
            "展览角。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4C0F")

    label("loc_4B7A")


    #C0250
    ChrTalk(
        0xFE,
        (
            "放置在二层展览角的那个东西\x01",
            "好像是由爱普斯泰恩财团所开发的\x01",
            "最新型的什么什么终端。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "……在不久的将来，即使是这种\x01",
            "尖端产品大概也会普及开来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C0F")

    Jump("loc_504A")

    label("loc_4C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4CA7")

    #C0252
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，我们准备推出\x01",
            "导力相机的打折销售活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "相机的价格最近在不断降低，\x01",
            "渐渐成为了普通市民也可以购买的\x01",
            "商品了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_4CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4CFC")

    #C0254
    ChrTalk(
        0xFE,
        (
            "趁着纪念庆典，\x01",
            "我们准备进一些新产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        "呵呵，很期待下个月啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_4CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4D76")

    #C0256
    ChrTalk(
        0xFE,
        (
            "可恶的温蒂，昨天\x01",
            "竟然让我如此蒙羞……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "就算对产品的了解比我稍微详细一点，\x01",
            "但未免也太得意忘形了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_4D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4DC2")
    OP_93(0xFE, 0x10E, 0x0)

    #C0258
    ChrTalk(
        0xFE,
        (
            "那、那个～所以呢……\x01",
            "这个吸、吸引力……什么的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_4DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4E41")

    #C0259
    ChrTalk(
        0xFE,
        (
            "好，今天也抓紧时间，\x01",
            "充满干劲地学习一天吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "目标是打倒『时代』百货店。\x01",
            "这个月一定要刷新\x01",
            "最高销售记录！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_504A")

    label("loc_4E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F26")

    #C0261
    ChrTalk(
        0xFE,
        (
            "说到工房，无非就是陈旧杂乱的陈列架，\x01",
            "还有七扭八歪的丑陋装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "但是从今以后，工房也必须\x01",
            "要装修得整洁美观才行！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "出于这样的考虑，我才开设了\x01",
            "这家环境整洁，装潢设计美观的\x01",
            "『原点』导力商店。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4F60")

    label("loc_4F26")


    #C0264
    ChrTalk(
        0xFE,
        (
            "如今已经进入\x01",
            "万物皆需美感的时代了！\x01",
            "这就是我的信念。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F60")

    Jump("loc_504A")

    label("loc_4F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_504A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF5")

    #C0265
    ChrTalk(
        0xFE,
        (
            "导力商店『原点』提供\x01",
            "各种各样的商品，\x01",
            "使人们的生活更加便利。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "其中一定有可以让您满意的产品，\x01",
            "请尽情挑选吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_504A")

    label("loc_4FF5")


    #C0267
    ChrTalk(
        0xFE,
        (
            "顺便一说，这辆高级导力车的\x01",
            "价格是一百五十万米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "……客人，您意下如何呢？\x02",
    )

    CloseMessageWindow()

    label("loc_504A")

    TalkEnd(0xFE)
    Return()

    # Function_12_4530 end

    def Function_13_504E(): pass

    label("Function_13_504E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_50C9")

    #C0269
    ChrTalk(
        0xFE,
        (
            "在以前，我们从来都没有\x01",
            "想到还能以车代步呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "将来大概还会有更多\x01",
            "我们想象不到的东西被发明出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_50C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5102")

    #C0271
    ChrTalk(
        0xFE,
        (
            "一大早就过来，\x01",
            "感觉也不错呢……呵呵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_5102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5173")

    #C0272
    ChrTalk(
        0xFE,
        (
            "导力器果然是非常棒啊，\x01",
            "使我们的生活变得\x01",
            "如此便利。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "我觉得最初发明它的人\x01",
            "实在是太伟大了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_5173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5181")
    Jump("loc_58C5")

    label("loc_5181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_525D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5219")

    #C0274
    ChrTalk(
        0xFE,
        (
            "这里的店员态度很亲切呢，\x01",
            "我把坏掉的导力灯带来之后，\x01",
            "她当场就给修理好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "阿姨我很惊讶呢。\x01",
            "这世上真是能人辈出啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5258")

    label("loc_5219")


    #C0276
    ChrTalk(
        0xFE,
        (
            "阿姨我很喜欢导力产品，\x01",
            "但对它的结构和原理却是一窍不通呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5258")

    Jump("loc_58C5")

    label("loc_525D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_52F2")

    #C0277
    ChrTalk(
        0xFE,
        (
            "啊呀，你们也是来买\x01",
            "导力烤炉的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "阿姨我现在正在\x01",
            "比较这些新产品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "买这种大件商品的时候，\x01",
            "一定要慎重选择才行呀，呵呵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_52F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5375")

    #C0280
    ChrTalk(
        0xFE,
        (
            "听店里的人说，\x01",
            "下周好像会有乌尔努公司\x01",
            "制造的导力相机到货呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "呵……这可不能错过呢，\x01",
            "看来下周还得再来一趟～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_5375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5412")

    #C0282
    ChrTalk(
        0xFE,
        (
            "逛导力商店为什么\x01",
            "会让人如此开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "琳琅满目的导力产品……\x01",
            "复杂精致的机械之美……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "真是的，光是看一看，\x01",
            "就令人快乐得不可思议呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_5412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_54A1")

    #C0285
    ChrTalk(
        0xFE,
        (
            "之前买了台吸尘器，\x01",
            "这个月准备再买台冰箱。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "该买哪种好呢～\x01",
            "挑选大件商品时虽然很苦恼，\x01",
            "但阿姨我果然还是喜欢款式可爱的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_54A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_553B")

    #C0287
    ChrTalk(
        0xFE,
        (
            "哎呀，这是时尚的新产品呢！\x01",
            "果然还是新产品最好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "虽然不了解那些结构性能之类难懂的知识，\x01",
            "但完全无法抗拒这种令人耳目一新的外观呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_553B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_55BA")

    #C0289
    ChrTalk(
        0xFE,
        (
            "阿姨我对彩虹剧团\x01",
            "并没有多大兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "虽然也有一点想去看……\x01",
            "在买门票之前，\x01",
            "还是想先买个最新款的冰箱呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_55BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_56A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_565F")

    #C0291
    ChrTalk(
        0xFE,
        (
            "这家店也有很多游客\x01",
            "来光顾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        "阿姨我也明白他们的心情呢。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "这家店即使是从远处望去也十分显眼，\x01",
            "所以不由自主就会被吸引过来哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_569F")

    label("loc_565F")


    #C0294
    ChrTalk(
        0xFE,
        (
            "而『导力商店』这样的地方，\x01",
            "在外国人的眼中就更加\x01",
            "少见了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_569F")

    Jump("loc_58C5")

    label("loc_56A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5700")
    OP_93(0xFE, 0x5A, 0x0)

    #C0295
    ChrTalk(
        0xFE,
        "我想买个吸尘器哦。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "那台红色的和那台白色的\x01",
            "究竟有什么差别呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_5700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_576C")

    #C0297
    ChrTalk(
        0xFE,
        (
            "啊呀，这个月好像推出了\x01",
            "新的吸尘器产品吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "呵呵……阿姨我也下定决心，\x01",
            "买一台好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_576C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_57E0")

    #C0299
    ChrTalk(
        0xFE,
        (
            "嗯嗯，最近好像增加了\x01",
            "不少时尚的新产品啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "那个是……ＺＣＦ制造的，\x01",
            "这到底是哪里的制造商呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C5")

    label("loc_57E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_58C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5892")

    #C0301
    ChrTalk(
        0xFE,
        (
            "不愧是导力商店啊，\x01",
            "真是个商品繁多的店……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "我本来只想买个导力灯，\x01",
            "但来到这里之后，注意力马上就转移了。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "啊呀，那边的那个东西\x01",
            "是什么呢！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_58C5")

    label("loc_5892")


    #C0304
    ChrTalk(
        0xFE,
        (
            "你们也是来买东西的吗？\x01",
            "呵呵，和阿姨我一样呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58C5")

    TalkEnd(0xFE)
    Return()

    # Function_13_504E end

    def Function_14_58C9(): pass

    label("Function_14_58C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_59C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599A")

    #C0305
    ChrTalk(
        0xFE,
        (
            "查珂原本想去百货店\x01",
            "当一名接待员……\x01",
            "但我提出了反对。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "因为感到有些愧疚，\x01",
            "所以为了让她能顺利工作，我决定\x01",
            "在一旁默默照看她。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "现在她还很不成熟，\x01",
            "所以不能放着她不管啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_59BB")

    label("loc_599A")


    #C0308
    ChrTalk(
        0xFE,
        (
            "查珂……\x01",
            "爸爸在你身边哦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59BB")

    Jump("loc_63BF")

    label("loc_59C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5A37")

    #C0309
    ChrTalk(
        0xFE,
        (
            "我有时也会想，自己在这里\x01",
            "说不定会给查珂\x01",
            "添麻烦吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "不过，我最后都会说服自己\x01",
            "这是不可能的啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_5A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AED")

    #C0311
    ChrTalk(
        0xFE,
        (
            "虽然昨天被查珂\x01",
            "那样说了……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "但担心独生女儿的工作情况，\x01",
            "对一名父亲来说，也是理所当然的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "反正，今后只要注意别被发现，\x01",
            "然后默默守护她就好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5B48")

    label("loc_5AED")


    #C0314
    ChrTalk(
        0xFE,
        "尽量装成是无关人士……\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "（偷看）\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "……嗯，查珂很努力呢。\x01",
            "爸爸也很高兴啊……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B48")

    Jump("loc_63BF")

    label("loc_5B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5B5B")
    Jump("loc_63BF")

    label("loc_5B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5B69")
    Jump("loc_63BF")

    label("loc_5B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5BEF")

    #C0317
    ChrTalk(
        0xFE,
        (
            "……我女儿今天也\x01",
            "充满活力地工作着呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "她在导力商店工作，我虽然也担心过……\x01",
            "但现在对她努力的样子感到很佩服呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_5BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5C60")

    #C0319
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "必须要看看查珂的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "她好像已经注意到\x01",
            "我来这里了，\x01",
            "所以行动时必须要小心谨慎……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_5C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5CED")

    #C0321
    ChrTalk(
        0xFE,
        (
            "目前来说，配备了导力网络的企业\x01",
            "只有一部分而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "像ＩＢＣ那种规模的\x01",
            "大型企业，大概已经达到\x01",
            "完全能够投入实用的等级了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_5CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5DA9")

    #C0323
    ChrTalk(
        0xFE,
        (
            "啊啊，查珂……\x01",
            "我那年轻可爱的女儿\x01",
            "竟然要工作到这么晚。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "在回来的路上要是被歹徒袭击，\x01",
            "可该如何是好啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "我已经准备好了热腾腾的晚饭，\x01",
            "真希望她能早点回家啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_5DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5E0D")

    #C0326
    ChrTalk(
        0xFE,
        (
            "不过……导力相机吗，\x01",
            "差不多也该考虑买一台了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "而且相机也\x01",
            "越来越轻便了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_5E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EF2")

    #C0328
    ChrTalk(
        0xFE,
        (
            "嗯嗯，这个是\x01",
            "ＺＣＦ制的新产品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "ＺＣＦ就是『蔡斯中央工房』的缩写，\x01",
            "前身是利贝尔王国的钟表工房，\x01",
            "那里聚集了许多技术人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "他们拥有十分先进的技术水平，\x01",
            "特别是飞行船技术，堪称世界第一呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5F60")

    label("loc_5EF2")


    #C0331
    ChrTalk(
        0xFE,
        (
            "ＺＣＦ是全世界最早实现\x01",
            "导力飞行船实用化的组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "直到现在，那些国际定期飞行船\x01",
            "也都是ＺＣＦ制造的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F60")

    Jump("loc_63BF")

    label("loc_5F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6020")

    #C0333
    ChrTalk(
        0xFE,
        (
            "噢，这是乌尔努公司制造的\x01",
            "新式小型照明灯啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "……我就在乌尔努公司\x01",
            "旗下的工房工作，\x01",
            "这是我同事研制的东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "终于得以产品化了，\x01",
            "总觉得感慨颇深呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_604F")

    label("loc_6020")


    #C0336
    ChrTalk(
        0xFE,
        (
            "是吗，终于完成了啊……\x01",
            "总觉得感慨颇深呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_604F")

    Jump("loc_63BF")

    label("loc_6054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_611D")

    #C0337
    ChrTalk(
        0xFE,
        (
            "帝国的莱恩福尔特公司\x01",
            "是以制造武器而闻名的。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "但它实际上是个巨大的综合型企业呢，\x01",
            "也制造了很多其它导力产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "不过多是一些设计朴实刚毅的东西，\x01",
            "这大概也反映出了帝国人的气质吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_611D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_629D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6213")

    #C0340
    ChrTalk(
        0xFE,
        (
            "现在，最有名的导力器\x01",
            "制造商有四家。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "帝国的莱恩福尔特公司、共和国的乌尔努公司、\x01",
            "爱普斯泰恩财团，还有利贝尔的ＺＣＦ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "在他们当中，爱普斯泰恩财团\x01",
            "多以研究为目的而进行开发。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "面向普通大众的产品比较少呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6298")

    label("loc_6213")


    #C0344
    ChrTalk(
        0xFE,
        (
            "爱普斯泰恩财团\x01",
            "多以研究为目的而进行开发。\x01",
            "面向大众的产品比较少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "所以其中有很多新颖独特的产品，\x01",
            "观察一下也是很有意思的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6298")

    Jump("loc_63BF")

    label("loc_629D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_633D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62FE")

    #C0346
    ChrTalk(
        0xFE,
        (
            "……嗯，查珂工作\x01",
            "很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "我因为担心，总是\x01",
            "过来偷偷看她。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6338")

    label("loc_62FE")


    #C0348
    ChrTalk(
        0xFE,
        (
            "……先、先说好哦，\x01",
            "我可绝对不是\x01",
            "跟踪狂之类的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6338")

    Jump("loc_63BF")

    label("loc_633D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_63BF")

    #C0349
    ChrTalk(
        0xFE,
        (
            "我曾经也在导力器制造业工作，\x01",
            "但现在已经退休了。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔汇集了\x01",
            "全世界各个品牌的\x01",
            "商品。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "很有鉴赏价值啊。\x02",
    )

    CloseMessageWindow()

    label("loc_63BF")

    TalkEnd(0xFE)
    Return()

    # Function_14_58C9 end

    def Function_15_63C3(): pass

    label("Function_15_63C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(11560, 1500, 5410, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26850, 0)
    SetChrPos(0x101, -2990, 0, 1860, 89)
    SetChrPos(0x102, -3340, 0, 3240, 45)
    SetChrPos(0x103, -4740, 0, 3260, 45)
    SetChrPos(0x104, -4310, 0, 1920, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetCameraDistance(24490, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(14920, 1500, 20510, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(43880, 0)
    OP_68(4170, 1500, 6370, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-2550, 1500, 2270, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22240, 0)
    OP_0D()

    #C0352
    ChrTalk(
        0x104,
        (
            "#0305F#6P咦……\x01",
            "这里就是『导力商店』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x102,
        (
            "#0105F#5P从最新型的导力车\x01",
            "到家庭用的生活导力产品，真是一应俱全呢……\x02\x03",

            "#0102F而且这种全新的装潢风格，\x01",
            "有种未来世界的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        (
            "#0011F#5P三年前还只是个\x01",
            "普通的工房啊……\x02\x03",

            "#0001F那个，总之，\x01",
            "去拜托店员调整导力器吧。\x01",
            "具体地点是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0355
    ChrTalk(
        0x103,
        (
            "#0203F#5P听说店里有个\x01",
            "服务柜台。\x02\x03",

            "#0200F去委托柜台的店员，\x01",
            "应该就可以进行各种调整了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0356
    ChrTalk(
        0x101,
        (
            "#0000F#11P是吗……\x01",
            "好，去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3570, 0, 2660, 89)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetScenarioFlags(0x4B, 2)
    EventEnd(0x5)
    Return()

    # Function_15_63C3 end

    def Function_16_66A5(): pass

    label("Function_16_66A5")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(800)
    OP_68(6570, 1500, -1770, 0)
    MoveCamera(49, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6620, 0, -1810, 90)
    SetChrPos(0x102, 5650, 0, -2670, 90)
    SetChrPos(0x103, 5650, 0, -1320, 90)
    SetChrPos(0x104, 5650, 0, -200, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0357
    ChrTalk(
        0x9,
        (
            "#11P啊，罗伊德，还有各位。\x01",
            "欢迎光临～！\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#6P#0000F温蒂，\x01",
            "艾尼格玛的实战测试……\x01",
            "这项支援请求是你发出的吧？\x02\x03",

            "我们在支援科收到了委托，然后就过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x9,
        "#11P啊，那个啊？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x9,
        "#11P嗯嗯，是我发出的哦。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x9,
        (
            "#11P其实是财团那边交代的事情……\x01",
            "我想最好请艾尼格玛的\x01",
            "实际使用者来提供协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x9,
        (
            "#11P现在你们应邀而来了，\x01",
            "真是帮大忙了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#6P#0100F如果是我们力所能及之事，很乐意效劳。\x02\x03",

            "那么，工作内容到底\x01",
            "是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x9,
        (
            "#11P嘿嘿嘿，其实\x01",
            "也没有多难啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0365
    ChrTalk(
        0x9,
        (
            "只是希望各位能\x01",
            "参加我们对艾尼格玛的\x01",
            "『性能评估计划』！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(500)

    #C0366
    ChrTalk(
        0x101,
        "#6P#0005F那个，那到底是……\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x9,
        (
            "#11P就是爱普斯泰恩财团针对\x01",
            "经营『艾尼格玛』的工房\x01",
            "而展开的一次调查活动啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x9,
        (
            "#11P你看，艾尼格玛是最新型的产品，\x01",
            "才刚刚开始普及，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x9,
        (
            "#11P财团那边也正在对它的具体规格进行调整。\x01",
            "而作为工房，也需要了解一下其\x01",
            "具体性能，以及使用状况之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x103,
        (
            "#6P#0203F这就是爱普斯泰恩财团的\x01",
            "『性能评估计划』……\x02\x03",

            "#0200F也就是在实用过程中\x01",
            "收集有关其耐用性、使用感觉\x01",
            "以及故障缺陷等情报吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)
    Sleep(300)

    #C0371
    ChrTalk(
        0x104,
        (
            "#5P#0300F话说回来，阿缇你\x01",
            "不也是财团的相关人员吗，\x01",
            "难道什么都不知道吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6BA1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BA1)

    def lambda_6BAE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BAE)
    Sleep(100)
    TurnDirection(0x103, 0x104, 400)
    Sleep(300)

    #C0372
    ChrTalk(
        0x103,
        (
            "#12P#0200F嗯，不知道，因为我是\x01",
            "魔导杖开发小组的。\x02\x03",

            "而眼下正在负责魔导杖的\x01",
            "实战测试。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0373
    ChrTalk(
        0x101,
        (
            "#11P#0000F对啊……\x01",
            "不小心都忘记这点了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x9,
        (
            "#11P啊哈哈……\x01",
            "看来在财团中，各个小组\x01",
            "都在进行着各种不同的测试呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CE4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6CE4)

    def lambda_6CF1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6CF1)

    def lambda_6CFE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6CFE)

    def lambda_6D0B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6D0B)
    Sleep(500)

    #C0375
    ChrTalk(
        0x9,
        (
            "#11P那个，大多数的评估项目\x01",
            "我都已经写完了，不过呢，\x01",
            "问题就是『实战中的性能评估』这项。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x9,
        (
            "#11P哎，虽然我也可以\x01",
            "随便试着用一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x9,
        (
            "#11P不过，身为一名专业技师，\x01",
            "还是应该好好听一听\x01",
            "实际使用者的意见吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x102,
        "#6P#0100F原来如此，所以你才发来了委托啊。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#6P#0000F这理由真有温蒂的风格呢……\x02\x03",

            "明白了，我们接受这个委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x9,
        "#11P谢谢啦，罗伊德～！\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#6P#0000F哈哈，因为这也不是什么\x01",
            "很困难的委托啊。\x02\x03",

            "那么，具体应该\x01",
            "做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x9,
        (
            "#11P嗯，很简单啦。\x01",
            "就是希望你们能试着用一次\x01",
            "『让敌人无法发现自己的魔法』。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x9,
        (
            "#11P这个好像是只有用艾尼格玛\x01",
            "才能发动的新型魔法呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#6P#0000F『让敌人无法发现自己的魔法』……\x01",
            "只要将其正确\x01",
            "发动出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x103,
        (
            "#6P#0200F从效果来看，\x01",
            "好像是相当特殊的魔法呢。\x02\x03",

            "似乎有必要好好考虑一下\x01",
            "回路的组合方法……\x01",
            "算了，总之就多尝试几次吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        (
            "#5P#0309F哈哈，那么这个就拜托你啦，\x01",
            "阿缇。\x02\x03",

            "#0300F接下来……还要在实际的战斗中使用，\x01",
            "以确认它的具体效果呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#6P#0100F嗯，那我们就来确认一下吧。\x02\x03",

            "顺便也要注意\x01",
            "使用感觉之类的情况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x9,
        "#11P拜托了啊。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x9,
        (
            "#11P那么，在确认了魔法的效果之后，\x01",
            "再来向我报告吧。\x01",
            "拜托了！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【艾尼格玛的实战测试】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearScenarioFlags(0x5A, 7)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0xE, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_16_66A5 end

    def Function_17_71BB(): pass

    label("Function_17_71BB")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(800)
    OP_68(6570, 1500, -1770, 0)
    MoveCamera(49, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6620, 0, -1810, 90)
    SetChrPos(0x102, 5650, 0, -2670, 90)
    SetChrPos(0x103, 5650, 0, -1320, 90)
    SetChrPos(0x104, 5650, 0, -200, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0391
    ChrTalk(
        0x9,
        "#11P啊，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x9,
        (
            "#11P有关艾尼格玛的实战测试，\x01",
            "完成得怎么样了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，没问题，\x01",
            "已经在实战中使用过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x103,
        (
            "#6P#0203F那种魔法就是『虚空幻域』吧。\x02\x03",

            "#0200F确实有着让对手\x01",
            "无法发现自己的效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x104,
        (
            "#5P#0300F可以说是将幻属性的特性\x01",
            "发挥到最大限度的魔法吧。\x02\x03",

            "艾尼格玛在平时就能发挥很大作用，\x01",
            "这次又发现了可使用的新魔法，\x01",
            "真是变得更加便利了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#6P#0100F是啊，除了可以在战斗中使用之外，\x01",
            "还有通讯功能，真是非常方便。\x02\x03",

            "不过……回路的合成，\x01",
            "还有结晶孔的开封还是\x01",
            "和旧型号一样麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        (
            "#11P嗯嗯，原来如此啊……\x01",
            "（奋笔疾书……）\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x9,
        (
            "#11P嗯，这样一来，报告书\x01",
            "应该就趋于完美了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0399
    ChrTalk(
        0x9,
        (
            "#11P罗伊德，还有各位，\x01",
            "非常感谢你们的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x9,
        (
            "#11P虽然区区薄礼不成敬意……\x01",
            "但还请收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0401
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '丹精'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('丹精', 1)

    #C0402
    ChrTalk(
        0x101,
        "#6P#0005F这是……？\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x9,
        (
            "#11P好像是在遗迹中挖掘出来的，\x01",
            "中世纪时期的古董回路吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x9,
        (
            "#11P是我在这家店以前的仓库里\x01",
            "翻出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x104,
        (
            "#5P#0305F挖掘出的……\x01",
            "那种东西还能用吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x103,
        (
            "#6P#0200F从理论上来说，\x01",
            "就算可以运作也不足为奇。\x02\x03",

            "毕竟，导力技术本身\x01",
            "就是通过解析古代的\x01",
            "结晶回路而诞生的。\x02\x03",

            "据报告说，还有人成功使用了\x01",
            "大崩坏之前的结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x9,
        (
            "#11P是这样的，\x01",
            "听起来让人很兴奋呢，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x9,
        (
            "#11P不过呢，虽然不能１００％保证它的性能，\x01",
            "但总之还是有导力反应的。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x9,
        (
            "#11P而且已经进行过简单的加工了，\x01",
            "我想应该可以嵌入艾尼格玛中正常使用的！\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x101,
        (
            "#6P#0000F哈哈，那么，这可以算是温蒂私藏的宝物了啊……\x02\x03",

            "多谢，那我就收下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x104,
        (
            "#5P#0300F我们会\x01",
            "好好使用它的。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x102,
        (
            "#6P#0100F温蒂小姐，\x01",
            "如果以后再有什么需要，\x01",
            "还请委托给支援科哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x9,
        "#11P嗯，到时就麻烦你们啦！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0414
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【艾尼格玛的实战测试】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0xE, 0x4, 0x10)
    OP_29(0xE, 0x1, 0x2)
    SetScenarioFlags(0x0, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_71BB end

    SaveToFile()

Try(main)
