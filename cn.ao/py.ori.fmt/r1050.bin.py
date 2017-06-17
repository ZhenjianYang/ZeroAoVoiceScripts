from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r1050.bin",                # FileName
        "r1050",                    # MapName
        "r1050",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x05,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 1, 0, 2],
    )

    BuildStringList((
        "r1050",                  # 0
        "索妮亚司令",             # 1
        "多诺邦警督",             # 2
        "格蕾丝",                 # 3
        "米蕾优三尉",             # 4
        "雷蒙德搜查官",           # 5
        "雷因兹",                 # 6
        "警官",                   # 7
        "警官",                   # 8
        "警官",                   # 9
        "警备队员",               # 10
        "警备队员",               # 11
        "警备队员",               # 12
        "警备队员",               # 13
        "乘务员",                 # 14
    ))

    AddCharChip((
        "chr/ch05700.itc",                   # 00
        "chr/ch30300.itc",                   # 01
        "chr/ch06000.itc",                   # 02
        "chr/ch32600.itc",                   # 03
        "chr/ch30200.itc",                   # 04
        "chr/ch28100.itc",                   # 05
        "chr/ch30000.itc",                   # 06
        "chr/ch31200.itc",                   # 07
        "chr/ch31300.itc",                   # 08
        "chr/ch28302.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   4,   255,  0)

    DeclActor(-8780,   0,       -820,    3000,    -8780,   3000,    -820,    0x007C, 0,  19, 0x0000)
    DeclActor(-14130,  0,       -620,    2000,    -14130,  3000,    -620,    0x007C, 0,  20, 0x0000)
    DeclActor(-36100,  0,       9060,    3000,    -36100,  2000,    9560,    0x007C, 0,  21, 0x0000)
    DeclActor(-55520,  0,       9690,    3000,    -55520,  2000,    10190,   0x007C, 0,  22, 0x0000)
    DeclActor(-65239,  0,       9800,    3000,    -65239,  2000,    10300,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(956, 0)                                        # 0

    ScpFunction((
        "Function_0_3BC",          # 00, 0
        "Function_1_46C",          # 01, 1
        "Function_2_4A3",          # 02, 2
        "Function_3_4EC",          # 03, 3
        "Function_4_65A",          # 04, 4
        "Function_5_C8B",          # 05, 5
        "Function_6_D25",          # 06, 6
        "Function_7_F4F",          # 07, 7
        "Function_8_1246",         # 08, 8
        "Function_9_1430",         # 09, 9
        "Function_10_15A4",        # 0A, 10
        "Function_11_16E5",        # 0B, 11
        "Function_12_1944",        # 0C, 12
        "Function_13_19B7",        # 0D, 13
        "Function_14_1A4B",        # 0E, 14
        "Function_15_1AB8",        # 0F, 15
        "Function_16_1B46",        # 10, 16
        "Function_17_1BDF",        # 11, 17
        "Function_18_1C4B",        # 12, 18
        "Function_19_1C9C",        # 13, 19
        "Function_20_1FF9",        # 14, 20
        "Function_21_22F6",        # 15, 21
        "Function_22_2304",        # 16, 22
        "Function_23_2312",        # 17, 23
        "Function_24_2320",        # 18, 24
        "Function_25_2C04",        # 19, 25
        "Function_26_3D5B",        # 1A, 26
        "Function_27_3FA7",        # 1B, 27
        "Function_28_5D6D",        # 1C, 28
    ))


    def Function_0_3BC(): pass

    label("Function_0_3BC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3F4"),
        (1, "loc_400"),
        (2, "loc_40C"),
        (3, "loc_418"),
        (4, "loc_424"),
        (5, "loc_430"),
        (6, "loc_43C"),
        (SWITCH_DEFAULT, "loc_448"),
    )


    label("loc_3F4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_400")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_40C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_418")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_424")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_430")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_43C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_448")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_454")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_46B")

    Return()

    # Function_0_3BC end

    def Function_1_46C(): pass

    label("Function_1_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47D")
    Call(0, 3)

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_493")
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4A2")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)

    label("loc_4A2")

    Return()

    # Function_1_46C end

    def Function_2_4A3(): pass

    label("Function_2_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_4B5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B5")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EB")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_4EB")

    Return()

    # Function_2_4A3 end

    def Function_3_4EC(): pass

    label("Function_3_4EC")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541")
    SetChrFlags(0xA, 0x10)

    label("loc_541")

    SetChrChipByIndex(0x15, 0x9)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56B")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)

    label("loc_56B")

    SetChrPos(0x8, 4770, 0, 5830, 180)
    SetChrPos(0x9, -23110, 0, -1910, 315)
    SetChrPos(0xA, 2240, 0, -2630, 288)
    SetChrPos(0xB, -58480, 0, -11340, 225)
    SetChrPos(0xC, -29410, 0, -6490, 346)
    SetChrPos(0xD, 1110, 0, -4130, 279)
    SetChrPos(0xE, -35240, 0, -6360, 315)
    SetChrPos(0xF, -44860, 0, -8410, 77)
    SetChrPos(0x10, -56970, 160, 900, 137)
    SetChrPos(0x11, 4230, 0, 3880, 359)
    SetChrPos(0x12, 5440, 0, 3940, 359)
    SetChrPos(0x13, -59570, 0, -12240, 45)
    SetChrPos(0x14, -67820, 170, 440, 180)
    SetChrPos(0x15, -52090, 0, -18010, 98)
    Return()

    # Function_3_4EC end

    def Function_4_65A(): pass

    label("Function_4_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF9")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -50420, 0, -17890, 270)
    SetChrPos(0x102, -50870, 0, -16710, 225)
    SetChrPos(0x104, -49670, 0, -18710, 270)
    SetChrPos(0x103, -49820, 0, -17210, 270)
    SetChrPos(0x109, -50030, 0, -15940, 225)
    SetChrPos(0x105, -49100, 0, -15920, 225)
    OP_68(-48700, 2210, -19060, 0)
    MoveCamera(302, 24, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(12640, 0)
    OP_0D()
    Sleep(500)

    #C0001
    ChrTalk(
        0xFE,
        "唉，真倒霉。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "但和那些被送走的人相比，\x01",
            "毫发无伤的我\x01",
            "还算是幸运吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "真没想到列车\x01",
            "居然会脱轨。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#12P#00003F您就是那辆列车的\x01",
            "乘务员吧？\x02\x03",

            "#00000F如果方便，您能向我们描述一下\x01",
            "事故发生时的情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "这个嘛，只要是我知道的事情，\x01",
            "我当然愿意全部告诉你们……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "但那边那位警察刚才询问我的时候，\x01",
            "我根本就说不出什么有用的信息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "因为事故就\x01",
            "发生在一瞬间，\x01",
            "所以我的脑子有些混乱……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#12P#10106F嗯……这次事故非常严重，\x01",
            "您无法清晰回想起当时的一切，\x01",
            "也是可以理解的。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#12P#00108F而且您受到了严重的惊吓，\x01",
            "难免会思绪混乱……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#12P#00003F哪怕只是一些微不足道的\x01",
            "小事也没关系。\x02\x03",

            "#00001F请问，您当时有没有注意到\x01",
            "什么让您在意的事情？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "让我在意的事情……\x01",
            "唔……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0012
    ChrTalk(
        0xFE,
        "啊，如此说来……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        "#12P#00305F#6P想起什么了吗？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "发生脱轨事故之前，我正在\x01",
            "和司机进行工作联络……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "说到一半时，他突然大声尖叫了起来──\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0016
    ChrTalk(
        0xFE,
        "『哇！这是什么！？』……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "随后就发生了事故。\x01",
            "先是车头脱轨，然后其它车厢也\x01",
            "一个接一个地脱轨了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "再然后……\x01",
            "就变成了现在这个样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#12P#00200F尖叫道\x01",
            "『哇！这是什么！？』……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x105,
        (
            "#12P#10302F听起来，似乎是看到了\x01",
            "某些难以置信的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#00003F司机到底\x01",
            "看到了什么呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 6)
    OP_29(0xA8, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCD")
    Call(0, 26)
    Return()

    label("loc_BCD")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -50180, 0, -17560, 257)
    EventEnd(0x5)
    Jump("loc_C8A")

    label("loc_BF9")

    TalkBegin(0xFE)

    #C0022
    ChrTalk(
        0xFE,
        (
            "发生脱轨事故之前，我正在\x01",
            "和司机进行工作联络……\x01",
            "他在说到一半时突然大声尖叫了起来──\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "『哇！这是什么！？』……\x01",
            "随后就发生了事故。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_C8A")

    Return()

    # Function_4_65A end

    def Function_5_C8B(): pass

    label("Function_5_C8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_D21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA9")
    Call(0, 11)
    Jump("loc_D21")

    label("loc_CA9")


    #C0024
    ChrTalk(
        0xFE,
        (
            "#02003F在起重机运达之前，\x01",
            "我们警备队也会协助各位\x01",
            "进行现场取证。\x02\x03",

            "#02000F我已经通知过队员们了，\x01",
            "你们可以\x01",
            "自由调查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D21")

    TalkEnd(0xFE)
    Return()

    # Function_5_C8B end

    def Function_6_D25(): pass

    label("Function_6_D25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED8")

    #C0025
    ChrTalk(
        0xFE,
        (
            "哎呀呀，现场状况好可怕，\x01",
            "这真是一起严重事故啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "发生如此严重的脱轨事故，却没有出现死难者，\x01",
            "还真是不幸中的万幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00200F几乎所有乘客都被\x01",
            "分批送往共和国\x01",
            "或医院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00006F真希望能先问那些人\x01",
            "几个问题啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "算啦，这也是没办法的事。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "对了，你们和正在那边休息的\x01",
            "乘务员谈过了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "我们刚才询问的时候，\x01",
            "没有得到什么有用的信息，\x01",
            "但他现在说不定已经想起什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "你们别忘了找他谈谈哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 2)
    Jump("loc_F4B")

    label("loc_ED8")


    #C0033
    ChrTalk(
        0xFE,
        (
            "你们和正在那边休息的\x01",
            "乘务员谈过了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "他是现在唯一一位可以提供\x01",
            "事故当时情况的人，\x01",
            "你们别忘了找他谈谈哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4B")

    TalkEnd(0xFE)
    Return()

    # Function_6_D25 end

    def Function_7_F4F(): pass

    label("Function_7_F4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119B")

    #C0035
    ChrTalk(
        0xFE,
        (
            "#02102F罗伊德，怎么样了，\x01",
            "你们有什么新发现吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00006F不，目前还无法下定论。\x02\x03",

            "#00001F格蕾丝小姐，您那边\x01",
            "有没有什么新的发现？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "#02106F唔……这个嘛。\x01",
            "其实列车事故偶尔也会发生……\x02\x03",

            "#02101F但这次的事故，\x01",
            "无论是发生时间还是发生地点\x01",
            "都太过凑巧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        (
            "#00108F……的确。\x01",
            "由于独立提案的缘故，\x01",
            "现在的状况本就已经十分紧张了……\x02\x03",

            "#00103F这次的事件说不定\x01",
            "是人为策划的……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "#02106F但这种想法在目前还毫无证据，\x01",
            "我并不打算把个人的猜想\x01",
            "强加于你们。\x02\x03",

            "#02109F总之，你们就加油\x01",
            "调查事故的真相吧！\x01",
            "如果有什么新发现，记得要让我采访哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00002F哈哈，我明白了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x17B, 1)
    Jump("loc_1242")

    label("loc_119B")


    #C0041
    ChrTalk(
        0xFE,
        (
            "#02103F其实列车事故偶尔也会发生……\x01",
            "但此次事故的发生时间和发生地点都太过凑巧了。\x02\x03",

            "#02109F总之，你们就加油\x01",
            "调查事故的真相吧！\x01",
            "如果有什么新发现，记得要让我采访哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1242")

    TalkEnd(0xFE)
    Return()

    # Function_7_F4F end

    def Function_8_1246(): pass

    label("Function_8_1246")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CA")

    #C0042
    ChrTalk(
        0x104,
        (
            "#00300F米蕾优，\x01",
            "修复工作进展如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "#07901F哦，和你们的调查任务\x01",
            "正在同时进行……\x02\x03",

            "#07906F但如果不用起重机\x01",
            "把列车挪开，\x01",
            "实在是无法有什么实质性的进展。\x02\x03",

            "#07900F总之，我们现在只能先把散落到四处的\x01",
            "碎片等东西清理干净。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#00003F我们也来帮忙吧……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "#07904F不，这倒不必。\x01",
            "你们就专心调查\x01",
            "事故的发生原因吧。\x02\x03",

            "#07902F我们要是有了什么新的发现，\x01",
            "也会通知你们的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 4)
    Jump("loc_142C")

    label("loc_13CA")


    #C0046
    ChrTalk(
        0xFE,
        (
            "#07904F你们就专心调查\x01",
            "事故的发生原因吧。\x02\x03",

            "#07902F我们要是有了什么新的发现，\x01",
            "也会通知你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142C")

    TalkEnd(0xFE)
    Return()

    # Function_8_1246 end

    def Function_9_1430(): pass

    label("Function_9_1430")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153C")

    #C0047
    ChrTalk(
        0xFE,
        (
            "我们已经在翻倒的车厢里\x01",
            "做了一番细致调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "但是并没有找到\x01",
            "什么有用的线索～\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x105,
        (
            "#10302F里面没有什么\x01",
            "可疑物品吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "嗯，全都是乘客行李\x01",
            "之类的东西，\x01",
            "没什么可疑物品～\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "看来这应该是一起\x01",
            "因为外部原因而\x01",
            "引发的事故～\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        "#00303F唔……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 3)
    Jump("loc_15A0")

    label("loc_153C")


    #C0053
    ChrTalk(
        0xFE,
        (
            "我们在翻倒的车厢里\x01",
            "没有发现任何\x01",
            "有用的线索～\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "看来这应该是一起\x01",
            "因为外部原因而\x01",
            "引发的事故～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A0")

    TalkEnd(0xFE)
    Return()

    # Function_9_1430 end

    def Function_10_15A4(): pass

    label("Function_10_15A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1665")

    #C0055
    ChrTalk(
        0xFE,
        (
            "唉，事故现场一片狼藉，\x01",
            "光是看着都觉得很受刺激。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "但为了向民众传达真实的情况，\x01",
            "我必须要拍下大量的清晰照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "因为哪怕只是一张照片，\x01",
            "也有可能会成为\x01",
            "重要的证据。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E1")

    label("loc_1665")


    #C0058
    ChrTalk(
        0xFE,
        (
            "在事故现场取材\x01",
            "真让人受刺激……\x01",
            "但我必须要拍下大量的清晰照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "因为哪怕只是一张照片，\x01",
            "也有可能会成为\x01",
            "重要的证据。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E1")

    TalkEnd(0xFE)
    Return()

    # Function_10_15A4 end

    def Function_11_16E5(): pass

    label("Function_11_16E5")

    OP_4B(0x8, 0x0)
    OP_4B(0x11, 0x0)
    OP_4B(0x12, 0x0)

    #C0060
    ChrTalk(
        0x8,
        (
            "#02000F我问你们，\x01",
            "起重机还需要\x01",
            "多久才能送来？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x11,
        (
            "报告长官，预计会在\x01",
            "三十分钟之内送达现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x12,
        (
            "可是……把时间分配到调查\x01",
            "工作上，真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x12,
        (
            "如果在傍晚之前还无法\x01",
            "修复其中一条铁路……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#02005F无法修复……？\x01",
            "不必担心这个问题。\x02\x03",

            "#02001F无论用什么方法，\x01",
            "都必须要把\x01",
            "这项任务完成。\x02\x03",

            "#02003F……你们应该也明白\x01",
            "这一点吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x11,
        "#5P#1K当、当然！！\x02",
    )


    #C0066
    ChrTalk(
        0x12,
        "#6P#1K当、当然！！\x02",
    )

    OP_57(0x1)
    OP_5A()

    #C0067
    ChrTalk(
        0x104,
        "#00306F（她的作风还是这么严厉啊……）\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        "#10102F（真不愧是索妮亚司令。）\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00006F（我们好不容易才得到了\x01",
            "  这个难得的机会……）\x02\x03",

            "#00001F（无论如何也要查清\x01",
            "  事故的原因。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0x0)
    OP_4C(0x11, 0x0)
    OP_4C(0x12, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x17B, 0)
    Return()

    # Function_11_16E5 end

    def Function_12_1944(): pass

    label("Function_12_1944")

    TalkBegin(0xFE)

    #C0070
    ChrTalk(
        0xFE,
        (
            "唔……如果离得太近，\x01",
            "可能会有危险呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "虽说现在勉强保持着平衡，\x01",
            "但要是突然倒下来，可就不得了了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1944 end

    def Function_13_19B7(): pass

    label("Function_13_19B7")

    TalkBegin(0xFE)

    #C0072
    ChrTalk(
        0xFE,
        (
            "唉……又是玻璃又是杂物，\x01",
            "散落得四处都是……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "哪怕只是一颗小石子，\x01",
            "也会给铁道带来危险，所以必须要在\x01",
            "傍晚之前把这些东西全部清理干净。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_19B7 end

    def Function_14_1A4B(): pass

    label("Function_14_1A4B")

    TalkBegin(0xFE)

    #C0074
    ChrTalk(
        0xFE,
        (
            "这次的脱轨事件居然把两条轨道\x01",
            "都波及到了……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "坐在那辆列车上的乘客们……\x01",
            "当时肯定非常恐惧吧？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1A4B end

    def Function_15_1AB8(): pass

    label("Function_15_1AB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_1B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD6")
    Call(0, 11)
    Jump("loc_1B42")

    label("loc_1AD6")


    #C0076
    ChrTalk(
        0xFE,
        (
            "起重设备预计在三十分钟之内\x01",
            "运达现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "在那之前，即使进度缓慢，\x01",
            "我们也必须要尽可能地处理修复工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B42")

    TalkEnd(0xFE)
    Return()

    # Function_15_1AB8 end

    def Function_16_1B46(): pass

    label("Function_16_1B46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_1BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B64")
    Call(0, 11)
    Jump("loc_1BDB")

    label("loc_1B64")


    #C0078
    ChrTalk(
        0xFE,
        (
            "调查工作是必需的，同时又不能\x01",
            "推迟原定的修复时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "唉，真没办法啊。\x01",
            "虽然时间非常紧张，\x01",
            "但也只能尽力而为了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDB")

    TalkEnd(0xFE)
    Return()

    # Function_16_1B46 end

    def Function_17_1BDF(): pass

    label("Function_17_1BDF")

    TalkBegin(0xFE)

    #C0080
    ChrTalk(
        0xFE,
        (
            "刚接到联络时，\x01",
            "完全没想到这次的事故\x01",
            "会如此严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "光是修补铁道的材料，\x01",
            "就需要相当大的数量。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1BDF end

    def Function_18_1C4B(): pass

    label("Function_18_1C4B")

    TalkBegin(0xFE)

    #C0082
    ChrTalk(
        0xFE,
        (
            "这里的铁轨\x01",
            "断掉了一大截。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "估计列车就是从这附近\x01",
            "开始脱轨的吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1C4B end

    def Function_19_1C9C(): pass

    label("Function_19_1C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F76")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -5900, 0, -3220, 315)
    SetChrPos(0x103, -5230, 0, -1840, 315)
    SetChrPos(0x104, -5870, 0, -4650, 315)
    SetChrPos(0x105, -4270, 0, -990, 315)
    SetChrPos(0x109, -7140, 0, -4500, 315)
    SetChrPos(0x102, -4660, 0, -3090, 315)
    OP_68(-8420, 1510, -430, 0)
    MoveCamera(322, 8, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(17870, 0)
    OP_0D()
    Sleep(500)

    #C0084
    ChrTalk(
        0x102,
        "#12P#00100F这节车厢就是车头了。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        (
            "#12P#00203F是引领导力列车前进的\x01",
            "最重要车厢呢。\x02\x03",

            "#00200F内部应该备有莱恩福尔特公司\x01",
            "制造的列车专用导力引擎\x01",
            "与操作室。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        (
            "#12P#10305F嗯……话说回来，\x01",
            "你们不觉得有点奇怪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#6P#00303F是啊，伤痕要比想象中\x01",
            "少很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x109,
        (
            "#6P#10105F确、确实……\x01",
            "车头前端几乎完好无损，\x01",
            "感觉有些不正常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#12P#00001F是啊……\x01",
            "如果正面撞上了什么东西，\x01",
            "车头前端不可能保持得如此完好。\x02\x03",

            "#00008F也就是说，这起脱轨事故\x01",
            "恐怕另有其它原因……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 3)
    OP_29(0xA8, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F4A")
    Call(0, 26)
    Return()

    label("loc_1F4A")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -6920, 0, -2370, 315)
    EventEnd(0x5)
    Jump("loc_1FF8")

    label("loc_1F76")

    TalkBegin(0xFF)

    #C0090
    ChrTalk(
        0x101,
        (
            "#00003F如果正面撞上了什么东西，\x01",
            "车头前端不可能保持得如此完好。\x02\x03",

            "#00008F也就是说，这起脱轨事故\x01",
            "恐怕另有其它原因…………\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1FF8")

    Return()

    # Function_19_1C9C end

    def Function_20_1FF9(): pass

    label("Function_20_1FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2284")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -14120, 0, -3340, 33)
    SetChrPos(0x102, -15310, 0, -3410, 33)
    SetChrPos(0x103, -13250, 0, -3620, 33)
    SetChrPos(0x104, -12440, 0, -4610, 33)
    SetChrPos(0x109, -13500, 0, -4730, 33)
    SetChrPos(0x105, -14610, 0, -4320, 33)
    OP_68(-13690, 2009, -2900, 0)
    MoveCamera(345, 9, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(16170, 0)
    OP_0D()
    Sleep(500)

    #C0091
    ChrTalk(
        0x101,
        "#6P#00005F这是……？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        (
            "#6P#10105F莫非是当时发生了山石崩落，\x01",
            "砸到了这里吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#6P#00203F从这圆形凹陷来看，\x01",
            "确实有可能呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#6P#00301F唔……但凹陷正中的\x01",
            "那道爪痕般的痕迹\x01",
            "又是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        (
            "#6P#10300F另外，仔细想想的话，\x01",
            "这个凹陷的位置\x01",
            "未免也太高了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        (
            "#6P#00108F唔……如果只是普通的山石崩落，\x01",
            "应该不会造成这样的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#6P#00003F究竟撞到了什么东西呢……？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 4)
    OP_29(0xA8, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2258")
    Call(0, 26)
    Return()

    label("loc_2258")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -13530, 0, -2950, 45)
    EventEnd(0x5)
    Jump("loc_22F5")

    label("loc_2284")

    TalkBegin(0xFF)

    #C0098
    ChrTalk(
        0x102,
        (
            "#00108F唔……如果只是普通的山石崩落，\x01",
            "应该不会造成这样的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#00003F究竟撞到了什么东西呢……？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_22F5")

    Return()

    # Function_20_1FF9 end

    def Function_21_22F6(): pass

    label("Function_21_22F6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_21_22F6 end

    def Function_22_2304(): pass

    label("Function_22_2304")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_22_2304 end

    def Function_23_2312(): pass

    label("Function_23_2312")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_23_2312 end

    def Function_24_2320(): pass

    label("Function_24_2320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B63")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23BF")
    SetChrPos(0x101, -35490, 0, 7260, 0)
    SetChrPos(0x102, -38000, 0, 7070, 300)
    SetChrPos(0x103, -36900, 0, 7230, 330)
    SetChrPos(0x104, -34470, 0, 6820, 60)
    SetChrPos(0x109, -34930, 0, 5800, 60)
    SetChrPos(0x105, -36170, 0, 6550, 0)
    Jump("loc_24AE")

    label("loc_23BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2439")
    SetChrPos(0x101, -55340, 0, 8020, 30)
    SetChrPos(0x102, -57740, 0, 8050, 330)
    SetChrPos(0x103, -56530, 0, 8270, 0)
    SetChrPos(0x104, -54080, 0, 7400, 60)
    SetChrPos(0x109, -56190, 0, 6600, 30)
    SetChrPos(0x105, -57360, 0, 7060, 300)
    Jump("loc_24AE")

    label("loc_2439")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24AE")
    SetChrPos(0x101, -62900, 0, 8740, 0)
    SetChrPos(0x102, -65170, 0, 7220, 300)
    SetChrPos(0x103, -64310, 0, 8130, 330)
    SetChrPos(0x104, -61540, 0, 8920, 30)
    SetChrPos(0x109, -61980, 0, 7950, 60)
    SetChrPos(0x105, -63300, 0, 7610, 0)

    label("loc_24AE")

    OP_68(-12460, 600, 9000, 0)
    MoveCamera(23, 46, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28500, 0)
    OP_68(-65230, 600, 11100, 11000)
    MoveCamera(23, 35, 0, 4000)
    Sleep(11500)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2530")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_258B")

    label("loc_2530")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2560")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_258B")

    label("loc_2560")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258B")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_258B")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(500)

    #C0100
    ChrTalk(
        0x101,
        (
            "#12P#00005F这里……\x01",
            "有非常明显的痕迹啊。\x02\x03",

            "#00001F岩壁上到处都是凹痕。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        (
            "#6P#00105F地面也有痕迹留下，\x01",
            "列车当时应该是朝左侧脱轨的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x105,
        (
            "#6P#10305F对了，岩壁上那些\x01",
            "蓝色的东西是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        (
            "#6P#00200F看起来像是沾上了\x01",
            "某种颜料……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D1")
    OP_68(-30920, 800, 4590, 3000)
    MoveCamera(76, 34, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(22500, 3000)
    Jump("loc_2750")

    label("loc_26D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2713")
    OP_68(-30920, 800, 4590, 4000)
    MoveCamera(76, 34, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(22500, 3000)
    Jump("loc_2750")

    label("loc_2713")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2750")
    OP_68(-30920, 800, 4590, 5000)
    MoveCamera(76, 34, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(22500, 5000)

    label("loc_2750")


    def lambda_2755():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2755)
    Sleep(50)

    def lambda_2765():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2765)
    Sleep(50)

    def lambda_2775():
        OP_93(0xFE, 0x6E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2775)
    Sleep(50)

    def lambda_2785():
        OP_93(0xFE, 0x69, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2785)
    Sleep(50)

    def lambda_2795():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2795)
    Sleep(50)

    def lambda_27A5():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27A5)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E8")

    #C0104
    ChrTalk(
        0x109,
        (
            "#N#10100F#12P从那辆发生事故的列车来看……\x01",
            "这应该是涂在车身上的\x01",
            "蓝色油漆。\x02\x03",

            "#10103F这就可以证明……\x01",
            "列车与岩壁发生了接触，\x01",
            "并且继续行驶了一段距离吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#6P#00301F是啊，不过……\x01",
            "那会造成这么长的\x01",
            "摩擦痕迹吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#N#6P#00003F看来有必要认真\x01",
            "思考一下，在什么状况下\x01",
            "才能形成这样的痕迹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A18")

    label("loc_28E8")

    SetMessageWindowPos(220, 140, -1, -1)

    #A0107
    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10100F从那辆发生事故的列车来看……\x01",
            "这应该是涂在车身上的\x01",
            "蓝色油漆。\x02\x03",

            "#10103F这就可以证明……\x01",
            "列车与岩壁发生了接触，\x01",
            "并且继续行驶了一段距离吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0108
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00301F是啊，不过……\x01",
            "那会造成这么长的\x01",
            "摩擦痕迹吗？\x02",
        )
    )

    CloseMessageWindow()

    #A0109
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F看来有必要认真\x01",
            "思考一下，在什么状况下\x01",
            "才能形成这样的痕迹。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2A18")

    OP_5A()
    SetScenarioFlags(0x17A, 5)
    OP_29(0xA8, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ADE")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6C")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_2AC7")

    label("loc_2A6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9C")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_2AC7")

    label("loc_2A9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC7")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_2AC7")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Call(0, 26)
    Return()

    label("loc_2ADE")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B17")
    SetChrPos(0x0, -35980, 0, 7690, 339)
    Jump("loc_2B5C")

    label("loc_2B17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3C")
    SetChrPos(0x0, -56210, 0, 8260, 24)
    Jump("loc_2B5C")

    label("loc_2B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5C")
    SetChrPos(0x0, -65200, 0, 8340, 294)

    label("loc_2B5C")

    EventEnd(0x5)
    Jump("loc_2C03")

    label("loc_2B63")

    TalkBegin(0xFF)

    #C0110
    ChrTalk(
        0x109,
        (
            "#10100F留在岩壁痕迹上的颜料……\x01",
            "从当时的状况来分析，\x01",
            "可以确定这是列车的油漆。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#00000F看来有必要认真\x01",
            "思考一下，在什么状况下\x01",
            "才能形成这样的痕迹。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2C03")

    Return()

    # Function_24_2320 end

    def Function_25_2C04(): pass

    label("Function_25_2C04")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, 10050, 0, -10800, 315)
    SetChrPos(0x102, 9850, 0, -11950, 315)
    SetChrPos(0x103, 11450, 0, -12190, 315)
    SetChrPos(0x104, 11600, 0, -10950, 315)
    SetChrPos(0x109, 10250, 0, -13300, 315)
    SetChrPos(0x105, 11600, 0, -13350, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D68")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Call(0, 3)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0x8, -800, 0, 6350, 180)
    SetChrPos(0x9, -2000, 0, 6350, 180)
    SetChrPos(0xA, -1400, 0, 4550, 0)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)

    label("loc_2D68")

    OP_68(10700, 1300, -11950, 0)
    MoveCamera(315, 29, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19750, 0)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    SetCameraDistance(18750, 2500)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0112
    ChrTalk(
        0x101,
        "#00013F#12P……！\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x109,
        "#10107F#6P这、这是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    ReplaceBGM("ed7205", "ed7151")
    Fade(1000)
    OP_68(-65000, 1500, -500, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(38750, 0)
    OP_68(-10000, 1500, -500, 15000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x101, 6880, 0, -2350, 315)
    SetChrPos(0x104, 8500, 0, -4240, 315)
    SetChrPos(0x109, 7880, 0, -1770, 315)
    SetChrPos(0x102, 8189, 0, -3020, 315)
    SetChrPos(0x103, 7170, 0, -3840, 315)
    SetChrPos(0x105, 9130, 0, -2510, 315)
    OP_68(-1400, 1000, 5450, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19400, 0)
    SetCameraDistance(17900, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0114
    ChrTalk(
        0xA,
        (
            "#02103F#6P哎呀～居然发生了\x01",
            "这么严重的事故！\x02\x03",

            "#02101F引发这起脱轨事故的原因究竟是什么呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        "#5P如你所见，我们正在进行调查。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "#5P依照我们的推测，最大的可能性还是\x01",
            "山石崩落到了铁轨上，从而导致车头脱轨。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#02003F#11P不好意思，请媒体界的人员\x01",
            "离开这里。\x02\x03",

            "#02000F因为我们马上就要\x01",
            "开始抢修铁道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x1F4)

    #C0118
    ChrTalk(
        0xA,
        "#02105F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        "#5P可是，司令……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)

    #C0120
    ChrTalk(
        0x8,
        (
            "#02006F#12P我也明白，你作为警察，\x01",
            "自然希望能在第一时间完成现场取证工作。\x02\x03",

            "#02001F但这条铁道可以说是\x01",
            "塞姆里亚大陆的大动脉……\x02\x03",

            "铁道公司、帝国和共和国，\x01",
            "还有迪塔市长都已发来通知，\x01",
            "要求我们立刻加急抢修。\x02\x03",

            "我们警备队\x01",
            "必须要服从命令。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "#5P这个……我也明白这些道理……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "#02101F#6P但是，如果不查明具体原因，\x01",
            "类似的事故说不定还会再次发生……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(200)

    #C0123
    ChrTalk(
        0x8,
        (
            "#02003F#11P关于这个问题，也只能在抢修的同时\x01",
            "进行调查了。\x02\x03",

            "#02001F总之，最迟也要在傍晚之前\x01",
            "让其中一条铁路恢复运行。\x02\x03",

            "在起重设备运达之前——\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#00011F#5P请等一等！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_337F():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_337F)
    Sleep(50)

    def lambda_338F():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_338F)
    Sleep(50)

    def lambda_339F():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_339F)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    Sleep(100)
    Fade(500)
    OP_68(3340, 1400, 1660, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20650, 0)
    OP_68(780, 1400, 3820, 3000)
    SetCameraDistance(20650, 3000)

    def lambda_340B():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_340B)
    Sleep(0)

    def lambda_3423():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3423)
    Sleep(0)

    def lambda_343B():
        OP_9B(0x0, 0x102, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_343B)
    Sleep(0)

    def lambda_3453():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3453)
    Sleep(0)

    def lambda_346B():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_346B)
    Sleep(0)

    def lambda_3483():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3483)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    #C0125
    ChrTalk(
        0x8,
        "#02005F#11P是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        "#02105F#5P哎呀，罗伊德，是你们啊！？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        "#5P哦哦，你们也来了啊。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x109,
        (
            "#10106F#12P那个，司令……\x02\x03",

            "#10113F您打算跳过现场取证的步骤，\x01",
            "直接开始抢修铁道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#02006F#11P你也是警备队的一员，\x01",
            "应该很清楚这条铁道的重要性吧？\x02\x03",

            "#02001F虽然很难启齿……\x02\x03",

            "但说实话，抢修进度稍有延误，\x01",
            "就足以导致帝国和共和国\x01",
            "强行介入干涉了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x109,
        "#10111F#12P这……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        "#00106F#6P……确实很有可能。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "#5P呼……既然您都这么说了，\x01",
            "那我们也就不再勉强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "#02106F#5P唔……但我们也身肩\x01",
            "探寻真相这一使命啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0134
    ChrTalk(
        0x101,
        (
            "#00003F#6P索妮亚司令。\x02\x03",

            "#00001F三十分钟……不，您只要把起重设备\x01",
            "运达之前的时间让给我们就够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x8,
        "#02005F#11P让给你们……？\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00006F#6P是的，在这种特殊时期，\x01",
            "克洛斯贝尔发生了这样的事故……\x02\x03",

            "#00001F我认为这绝不是\x01",
            "单纯的偶然。\x02\x03",

            "是不是有必要好好调查一下\x01",
            "这次的事故中是否存在什么『必然因素』呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        "#02001F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#00201F#6P而且还有可能是那种『幻兽』\x01",
            "造成了这起事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#00300F#6P是啊，象征性地给我们\x01",
            "一点时间总没问题吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0140
    ChrTalk(
        0x8,
        (
            "#02006F#11P……你们说的没错，\x01",
            "我似乎有些操之过急了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    #C0141
    ChrTalk(
        0x8,
        (
            "#02002F#12P多诺邦警督，\x01",
            "短时间之内，优先进行现场取证吧。\x02\x03",

            "但在我们正式开始抢修铁道之后，\x01",
            "就必须要把精力集中在那边的工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        "#5P好的，我没有异议。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x2D, 0x1F4)

    #C0143
    ChrTalk(
        0xA,
        (
            "#02109F#6P不好意思～如果可以的话，\x01",
            "可以让我们留在这里取材吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)

    #C0144
    ChrTalk(
        0x8,
        (
            "#02003F#11P在我们正式开始抢修铁道之前，\x01",
            "敬请随意。\x02\x03",

            "#02000F不过……\x01",
            "请不要妨碍到现场取证工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        "#02110F#6P嗯！那当然！\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#00001F#6P警督，可以让我们\x01",
            "也一起进行现场取证吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B6C():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3B6C)
    Sleep(50)

    def lambda_3B7C():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3B7C)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0xA, 0)

    #C0147
    ChrTalk(
        0x9,
        "#5P没问题，我们分头行事吧。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "#5P对了，在那边休息的那位乘务员\x01",
            "当时就在发生事故的列车上。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "#5P司机已经被送往医院了，但你们可以\x01",
            "向他打听一下事故发生时的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#00003F#6P我明白了。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x105,
        "#10302F#12P那我们这就开始调查吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21150, 1500)
    OP_6F(0x79)
    OP_0D()
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Call(0, 3)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    SetChrPos(0x0, -1000, 0, 1850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 1)
    OP_29(0xA8, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_25_2C04 end

    def Function_26_3D5B(): pass

    label("Function_26_3D5B")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0152
    ChrTalk(
        0x101,
        (
            "#00003F……好了，判断案情所需要的情报\x01",
            "已经大致收集够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3E37():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3E37)
    Sleep(50)

    def lambda_3E47():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E47)
    Sleep(50)

    def lambda_3E57():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E57)
    Sleep(50)

    def lambda_3E67():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E67)
    Sleep(50)

    def lambda_3E77():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3E77)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0153
    ChrTalk(
        0x109,
        "#10105F咦？已经够了吗？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        "#00202F……真不愧是罗伊德前辈。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#00306F我到现在还完全搞不懂\x01",
            "这是怎么一回事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x105,
        (
            "#10302F其实我也\x01",
            "察觉到几个要点了……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#00101F如何？\x01",
            "我们这就开始整理情报吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "把司令和警督他们也叫来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 27)
    Return()

    # Function_26_3D5B end

    def Function_27_3FA7(): pass

    label("Function_27_3FA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis257.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis258.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis259.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis260.itp")
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(852)
    SoundLoad(891)
    SetChrPos(0x101, 200, 0, 2550, 0)
    SetChrPos(0x102, -650, 0, 2100, 0)
    SetChrPos(0x103, 1500, 0, 2050, 0)
    SetChrPos(0x104, -800, 0, 1100, 0)
    SetChrPos(0x109, 850, 0, 1450, 0)
    SetChrPos(0x105, 1050, 0, 400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrPos(0x8, 0, 0, 4500, 180)
    SetChrPos(0x9, -1000, 0, 4750, 180)
    SetChrPos(0xA, 2250, 0, 4100, 225)
    SetChrPos(0xB, 800, 0, 4950, 180)
    SetChrPos(0xC, -900, 0, 5850, 180)
    SetChrPos(0xD, 600, 0, 6100, 180)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_68(90, 900, 3590, 0)
    MoveCamera(310, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21550, 0)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20650, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0159
    ChrTalk(
        0x8,
        (
            "#02001F#11P那么……\x01",
            "你们调查到什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#00006F#6P是的，首先……山石崩落在铁道上，\x01",
            "从而造成了脱轨事故这种可能性……\x02\x03",

            "#00001F已经可以\x01",
            "彻底排除了。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xC,
        "#11P为、为什么呢？\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "#5P也就是说，你们发现了可以\x01",
            "否定那种可能性的证据？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        "#00000F#6P是的，那就是──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K排除山石崩落这种可能性的证据是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "乘务员听到司机尖叫\x01",      # 0
            "车头前端的伤痕太少\x01",      # 1
            "车头右侧的巨大凹陷\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_43C2"),
        (1, "loc_44B4"),
        (2, "loc_4529"),
        (SWITCH_DEFAULT, "loc_4649"),
    )


    label("loc_43C2")


    #C0165
    ChrTalk(
        0x105,
        (
            "#10306F#6P不对，那个证据并不能\x01",
            "排除山石崩落的可能性吧？\x02\x03",

            "#10301F说不定他正是因为看到前方\x01",
            "发生了落石，所以才会尖叫。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00008F#5P嗯……说的也是。\x02\x03",

            "#00013F……关键问题应该是\x01",
            "车头前端的伤痕太少。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        "#10302F#6P嗯，我也是这样想的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4649")

    label("loc_44B4")

    OP_2C(0xA8, 0x2)

    #C0168
    ChrTalk(
        0x101,
        (
            "#00003F#6P我们刚才发现了好几个\x01",
            "可疑的证据……\x02\x03",

            "#00013F但真正具有决定性作用的，\x01",
            "是车头前端的伤痕太少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4649")

    label("loc_4529")

    OP_2C(0xA8, 0x1)

    #C0169
    ChrTalk(
        0x105,
        (
            "#10306F#6P不对，虽然那确实是一条\x01",
            "十分重要的证据，但它并不能\x01",
            "排除山石崩落的可能性吧？\x02\x03",

            "#10300F山石有可能是从右侧的岩壁滚落了下来，\x01",
            "所以在那个位置撞出了凹陷。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#00008F#5P嗯……说的也是。\x02\x03",

            "#00013F……关键问题应该是\x01",
            "车头前端的伤痕太少。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x105,
        "#10302F#6P嗯，我也是这样想的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4649")

    label("loc_4649")


    #C0172
    ChrTalk(
        0x8,
        "#02005F#11P为什么这么说？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "#07901F#11P车头前端的确\x01",
            "没有什么伤痕呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    SetMessageWindowPos(300, 200, -1, -1)

    #A0174
    AnonymousTalk(
        0x101,
        (
            "#00003F一般来说，在因山石崩落而引发\x01",
            "脱轨的事故中，车头都会撞到\x01",
            "滚落到铁轨上的岩石。\x02\x03",

            "高速行驶的列车\x01",
            "在相撞之后失去平衡，\x01",
            "脱离铁轨……\x02\x03",

            "#00001F除非发生了这样的情况，\x01",
            "否则很难引起如此严重的脱轨事故。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0175
    ChrTalk(
        0xA,
        "#02101F#12P哦哦，原来如此……！\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "#5P但在车头前端却找不到\x01",
            "什么伤痕。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "#5P所以首先就可以排除掉这个\x01",
            "看似可能性最高的判断了！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "#02006F#11P……原来如此，\x01",
            "这个问题确实很关键。\x02\x03",

            "#02001F既然如此，还有其它原因\x01",
            "能导致脱轨事故吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#00008F#6P有的……\x01",
            "一开始我还考虑过，会不会是\x01",
            "引爆了某些爆炸物品。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_48F8():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_48F8)
    Sleep(50)

    def lambda_4908():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4908)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0180
    ChrTalk(
        0x102,
        "#00101F#5P你、你的意思是……！？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#10107F#6P怀疑这是某个武装集团发动的\x01",
            "恐怖活动吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#00303F#6P其实我最先想到的\x01",
            "也是这个可能性。\x02\x03",

            "#00301F但在四下调查了一圈之后，\x01",
            "并没有找到任何\x01",
            "使用爆炸物的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xB,
        (
            "#07906F#11P是啊，到目前为止，\x01",
            "我们也没有这方面的发现。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#00003F#6P既然如此，\x01",
            "要说还有其它可能……\x02\x03",

            "#00013F恐怕也就只有『某种东西』\x01",
            "直接冲撞到列车右侧了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0185
    ChrTalk(
        0x9,
        "#5P你、你说什么！？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        (
            "#11P直、直接冲撞？\x01",
            "那也太荒唐了吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "#02105F#12P如果是在赛车比赛中，\x01",
            "倒是有可能发生那种碰撞，可是……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0188
    ChrTalk(
        0x103,
        (
            "#00203F#12P原来如此……\x02\x03",

            "#00201F车头的右侧确实\x01",
            "留下了巨大凹陷。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00008F#5P嗯，当时多半就是\x01",
            "发生了这种状况。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 0, -1, -1)

    #A0190
    AnonymousTalk(
        0x101,
        (
            "#00003F『某种东西』落到了正在飞速行驶的\x01",
            "列车车头的旁边。\x02\x03",

            "#00001F司机恐怕就是在那个时候\x01",
            "发出了惊恐万分的尖叫声。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 200, -1, -1)

    #A0191
    AnonymousTalk(
        0x101,
        (
            "#00008F『它』与列车并排前进，\x01",
            "并猛力撞击车头的右侧……\x02\x03",

            "车身一侧突然受力，\x01",
            "致使车头向左侧脱轨。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(0, 200, -1, -1)

    #A0192
    AnonymousTalk(
        0x101,
        (
            "#00013F随后，『它』把车头\x01",
            "摁在左侧的岩壁上……\x02\x03",

            "留下一段极长的摩擦痕迹之后，\x01",
            "终于逼停了列车。\x02\x03",

            "#00003F所以后面的普通车厢正如现在所见，\x01",
            "也都完全脱轨了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x9)
    OP_64(0xC)
    OP_64(0x8)
    OP_64(0xB)
    OP_64(0xA)
    OP_64(0xD)

    #C0193
    ChrTalk(
        0x101,
        (
            "#00000F#6P……这就是我们\x01",
            "在现阶段的推测。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xC,
        "#11P哇……！\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        "#07902F#11P……非常出色。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "#5P哎呀呀，单论推理，\x01",
            "你说不定都已经超越你大哥了。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "#02104F#12P是啊……\x01",
            "盖伊先生是那种更喜欢\x01",
            "凭借直觉展开调查的类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        "#00309F#6P哈哈，大受好评啊。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00109F#5P呵呵……\x01",
            "真让人骄傲。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#10302F#6P哎呀呀，连我都没能\x01",
            "设想得如此完善呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "#02004F#11P呵呵，真有一手啊。\x02\x03",

            "#02001F那么，罗伊德。\x02\x03",

            "能够做到那种事情的『东西』，\x01",
            "会不会是魔兽？\x02\x03",

            "而且是最近出现的那种『幻兽』？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#00008F#6P这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K引起事故的『某种东西』到底是什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "很可能是『幻兽』\x01",      # 0
            "目前还无法断言\x01",        # 1
        )
    )

    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis261.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis262.itp")
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_52CC"),
        (1, "loc_5437"),
        (SWITCH_DEFAULT, "loc_557A"),
    )


    label("loc_52CC")


    #C0204
    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯，对方拥有可以使\x01",
            "飞速行驶中的列车\x01",
            "侧翻脱轨的惊人蛮力……\x02\x03",

            "#00001F首先会联想到的，\x01",
            "自然是大型幻兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#00205F#12P不过，罗伊德前辈……\x02\x03",

            "#00200F如果真的是幻兽所为，\x01",
            "我应该会感知到上级属性……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        "#00011F#5P啊，把这个问题忘了……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "#02006F#11P……唔，而且也没有发现你们在\x01",
            "昨天的报告中提到的那种『蓝花』……\x02\x03",

            "#02008F那到底会是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_557A")

    label("loc_5437")

    OP_2C(0xA8, 0x1)

    #C0208
    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯，对方拥有可以使\x01",
            "飞速行驶中的列车\x01",
            "侧翻脱轨的惊人蛮力……\x02\x03",

            "#00008F如果按照一般的思路考虑，\x01",
            "自然会联想到大型幻兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x103,
        (
            "#00203F#12P但如果真的是幻兽所为，\x01",
            "我应该会感知到上级属性……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        (
            "#10308F#6P而且我们并没有在这里\x01",
            "发现那种『蓝花』。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "#02006F#11P说的也是……\x02\x03",

            "#02008F那到底会是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_557A")

    label("loc_557A")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #C0212
    ChrTalk(
        0x101,
        (
            "#00006F#6P（说到其它可能性，\x01",
            "  大概也就是『结社』的智能兵器了……）\x02\x03",

            "#00008F（但那些家伙会采取如此直接的行动吗？）\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    Sound(891, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(2000)
    CancelBlur(1000)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0213
    ChrTalk(
        0xB,
        "#07905F#11P刚、刚才那是……！？\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        "#11P魔、魔兽的吼叫……！？\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#00108F#5P但、但听起来为何会\x01",
            "那么诡异……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x103,
        "#00201F#6P我马上启动永世系统……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(300)
    OP_68(600, 900, 3450, 1500)

    def lambda_5878():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5878)

    def lambda_5885():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5885)

    def lambda_5892():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5892)

    def lambda_589F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_589F)

    def lambda_58AC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_58AC)

    def lambda_58B9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_58B9)

    def lambda_58C6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_58C6)

    def lambda_58D3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_58D3)

    def lambda_58E0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_58E0)

    def lambda_58ED():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_58ED)

    def lambda_58FA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_58FA)

    def lambda_5907():
        OP_95(0xFE, 2500, 0, 2050, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5907)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x103, 3, 0, 28)
    Sleep(3000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(200)
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(100)
    OP_93(0xA, 0x10E, 0x1F4)
    Sleep(200)
    TurnDirection(0xA, 0xD, 500)

    #C0217
    ChrTalk(
        0xA,
        (
            "#02101F#6P在哪里！？到底在哪里！？\x02\x03",

            "雷因兹，\x01",
            "一定要把它拍下来！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xD,
        "#5P您就别为难我了～！\x02",
    )

    CloseMessageWindow()
    Sound(891, 0, 50, 0)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x103, 3)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    ReplaceBGM("ed7205", "ed7203")
    ReplaceBGM("ed7250", "ed7203")
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(500)

    #C0219
    ChrTalk(
        0x103,
        (
            "#00207F#12P目标距离这里１０赛尔矩！\x01",
            "正在朝西方不断远去……！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#00010F#5P唔……！\x02\x03",

            "#00007F各位，我们追上去吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        "#00307F#5P嗯，收到！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x109,
        "#10101F#6P明白了！\x02",
    )

    CloseMessageWindow()

    def lambda_5AD0():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_5AD0)
    Sleep(50)

    def lambda_5AE0():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_5AE0)
    Sleep(50)

    def lambda_5AF0():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5AF0)
    Sleep(50)

    def lambda_5B00():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_5B00)
    Sleep(50)

    def lambda_5B10():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_5B10)
    Sleep(50)

    def lambda_5B20():
        OP_93(0xD, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_5B20)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    #C0223
    ChrTalk(
        0x9,
        "#5P喂喂，你们别太乱来啊！\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xB,
        "#07907F#11P警备队也跟去增援吧！\x02",
    )

    CloseMessageWindow()

    def lambda_5B89():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5B89)
    Sleep(50)

    def lambda_5B99():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5B99)
    Sleep(50)

    def lambda_5BA9():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5BA9)
    Sleep(50)

    def lambda_5BB9():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5BB9)
    Sleep(50)

    def lambda_5BC9():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5BC9)
    Sleep(50)

    def lambda_5BD9():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5BD9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0225
    ChrTalk(
        0x101,
        (
            "#00013F#6P不用了，请各位\x01",
            "集中精力抢修铁道吧！\x02\x03",

            "我们先追上去就好！\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        "#07906F#11P唉……说的也是。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#02003F#11P……起重机就快送来了，\x01",
            "看来也只能照你说的做了。\x02\x03",

            "#02001F如果遇到了什么危险，我们会立刻\x01",
            "赶去增援的，务必要及时联络我们！\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x109,
        "#10107F#6P我明白了！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x105,
        "#10308F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21650, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_3FA7 end

    def Function_28_5D6D(): pass

    label("Function_28_5D6D")

    Sound(2192, 255, 80, 0)    #voice#Tio
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sound(812, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(357, 0, 70, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xFE, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    label("loc_5E0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E29")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("loc_5E0C")

    label("loc_5E29")

    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Fade(250)
    Sound(812, 0, 100, 0)
    StopSound(852, 500, 100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_28_5D6D end

    SaveToFile()

Try(main)
