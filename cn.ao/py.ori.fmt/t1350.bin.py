from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1350.bin",                # FileName
        "t1350",                    # MapName
        "t1350",                    # Location
        0x00B8,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 184, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1350",                  # 0
        "艾莉",                   # 1
        "缇欧",                   # 2
        "兰迪",                   # 3
        "琪雅",                   # 4
        "芙兰",                   # 5
        "伊莉娅",                 # 6
        "莉夏",                   # 7
        "修利",                   # 8
        "梅尔斯",                 # 9
        "柯洛娜",                 # 10
        "利玛",                   # 11
        "奇幻乐园工作人员",       # 12
        "游客",                   # 13
        "游客",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "假",                     # 17
        "咪雪",                   # 18
        "奇幻乐园入口广场方向",   # 19
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00300.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch08500.itc",                   # 04
        "chr/ch05100.itc",                   # 05
        "chr/ch05200.itc",                   # 06
        "chr/ch10100.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch22700.itc",                   # 09
        "chr/ch20700.itc",                   # 0A
        "chr/ch25900.itc",                   # 0B
        "chr/ch20400.itc",                   # 0C
        "chr/ch23700.itc",                   # 0D
        "chr/ch21000.itc",                   # 0E
        "chr/ch24600.itc",                   # 0F
        "chr/ch45400.itc",                   # 10
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

    DeclNpc(-1500,   0,       -2299,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-2599,   0,       -9300,   350,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-2500,   0,       -2299,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-2910,   0,       -4469,   45,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-1669,   0,       -9319,   350,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-2930,   0,       -4030,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-2049,   0,       -4869,   315,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1759,   0,       -4469,   315,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-2910,   0,       -3269,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-1759,   0,       -3269,   225,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-2309,   0,       -4469,   0,    389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       800,     2250,    180,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-1549,   -4000,   -24340,  90,   389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-550,    -4000,   -24340,  270,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3019,    0,       -4440,   125,  389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(3670,    0,       -5219,   305,  389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-6000,   0,       -3170,   270,  389,  0x0, 0,   16,  0,   0,   0,   0,   25,  255,  0)

    DeclActor(-5620,   0,       2730,    1200,    -5620,   2000,    2730,    0x007C, 0,  26, 0x0000)

    PlaceName(-0.17000000178813934, 0.0, -65.44999694824219, 0x0000, 0x0000, "奇幻乐园入口广场方向")

    ChipFrameInfo(936, 0)                                        # 0

    ScpFunction((
        "Function_0_3A8",          # 00, 0
        "Function_1_460",          # 01, 1
        "Function_2_4F1",          # 02, 2
        "Function_3_531",          # 03, 3
        "Function_4_60C",          # 04, 4
        "Function_5_6E0",          # 05, 5
        "Function_6_7B7",          # 06, 6
        "Function_7_889",          # 07, 7
        "Function_8_96C",          # 08, 8
        "Function_9_AF7",          # 09, 9
        "Function_10_C15",         # 0A, 10
        "Function_11_CA8",         # 0B, 11
        "Function_12_D68",         # 0C, 12
        "Function_13_DF5",         # 0D, 13
        "Function_14_E92",         # 0E, 14
        "Function_15_F9B",         # 0F, 15
        "Function_16_1058",        # 10, 16
        "Function_17_1100",        # 11, 17
        "Function_18_1159",        # 12, 18
        "Function_19_11CD",        # 13, 19
        "Function_20_1249",        # 14, 20
        "Function_21_13A8",        # 15, 21
        "Function_22_26F4",        # 16, 22
        "Function_23_271D",        # 17, 23
        "Function_24_2746",        # 18, 24
        "Function_25_3434",        # 19, 25
        "Function_26_3A2A",        # 1A, 26
    ))


    def Function_0_3A8(): pass

    label("Function_0_3A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3E8"),
        (1, "loc_3F4"),
        (2, "loc_400"),
        (3, "loc_40C"),
        (4, "loc_418"),
        (5, "loc_424"),
        (6, "loc_430"),
        (SWITCH_DEFAULT, "loc_43C"),
    )


    label("loc_3E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_3F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_400")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_40C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_418")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_424")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_430")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_43C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_45F")

    Return()

    # Function_0_3A8 end

    def Function_1_460(): pass

    label("Function_1_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_46F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_47D")
    Jump("loc_4F0")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_48B")
    Jump("loc_4F0")

    label("loc_48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_499")
    Jump("loc_4F0")

    label("loc_499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4AA")
    Call(0, 20)
    Jump("loc_4F0")

    label("loc_4AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4BD")
    ClearChrFlags(0x13, 0x80)
    Jump("loc_4F0")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_4F0")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_4F0")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_4F0")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4F0")

    label("loc_4F0")

    Return()

    # Function_1_460 end

    def Function_2_4F1(): pass

    label("Function_2_4F1")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)

    label("loc_52A")

    Sound(944, 0, 100, 0)
    Return()

    # Function_2_4F1 end

    def Function_3_531(): pass

    label("Function_3_531")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A")
    Jump("loc_608")

    label("loc_54A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D")
    Call(0, 19)
    Jump("loc_5C6")

    label("loc_56D")


    #C0001
    ChrTalk(
        0x8,
        (
            "#00106F呼……\x01",
            "我很怕这种东西呢。\x02\x03",

            "#00111F说不定贝尔\x01",
            "建造这种东西\x01",
            "就是为了吓唬我……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C6")

    Jump("loc_608")

    label("loc_5CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E1")
    Jump("loc_608")

    label("loc_5E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7")
    Jump("loc_608")

    label("loc_5F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_608")

    label("loc_608")

    TalkEnd(0xFE)
    Return()

    # Function_3_531 end

    def Function_4_60C(): pass

    label("Function_4_60C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_625")
    Jump("loc_6DC")

    label("loc_625")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63B")
    Jump("loc_6DC")

    label("loc_63B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_651")
    Jump("loc_6DC")

    label("loc_651")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CB")

    #C0002
    ChrTalk(
        0x9,
        (
            "#00203F站在这里，也能清楚地\x01",
            "听到惊呼和惨叫声呢。\x02\x03",

            "#00204F听到那些声音之后，\x01",
            "既害怕又有些兴奋。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC")

    label("loc_6CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DC")

    label("loc_6DC")

    TalkEnd(0xFE)
    Return()

    # Function_4_60C end

    def Function_5_6E0(): pass

    label("Function_5_6E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9")
    Jump("loc_7B3")

    label("loc_6F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71C")
    Call(0, 19)
    Jump("loc_771")

    label("loc_71C")


    #C0003
    ChrTalk(
        0xA,
        (
            "#00309F哈哈，大小姐的胆子真小啊。\x02\x03",

            "#00304F嗯，越是这种性格，\x01",
            "就越想让她试试呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_771")

    Jump("loc_7B3")

    label("loc_776")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78C")
    Jump("loc_7B3")

    label("loc_78C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A2")
    Jump("loc_7B3")

    label("loc_7A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B3")

    label("loc_7B3")

    TalkEnd(0xFE)
    Return()

    # Function_5_6E0 end

    def Function_6_7B7(): pass

    label("Function_6_7B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D0")
    Jump("loc_885")

    label("loc_7D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E6")
    Jump("loc_885")

    label("loc_7E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC")
    Jump("loc_885")

    label("loc_7FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_812")
    Jump("loc_885")

    label("loc_812")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885")

    #C0004
    ChrTalk(
        0xB,
        (
            "#01106F我还没想好最后\x01",
            "要玩什么……\x02\x03",

            "#01109F不过，要是和伊莉娅一起去坐这个，\x01",
            "应该会很有趣呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_885")

    TalkEnd(0xFE)
    Return()

    # Function_6_7B7 end

    def Function_7_889(): pass

    label("Function_7_889")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A2")
    Jump("loc_968")

    label("loc_8A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8")
    Jump("loc_968")

    label("loc_8B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CE")
    Jump("loc_968")

    label("loc_8CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_957")

    #C0005
    ChrTalk(
        0xC,
        (
            "#06402F据说这个游乐设施是\x01",
            "ＩＢＣ将米修拉姆的一座\x01",
            "老旧房屋改建而成的。\x02\x03",

            "#06409F做得相当用心呢～\x01",
            "真是令人赞叹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_968")

    label("loc_957")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968")

    label("loc_968")

    TalkEnd(0xFE)
    Return()

    # Function_7_889 end

    def Function_8_96C(): pass

    label("Function_8_96C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E2")

    #C0006
    ChrTalk(
        0xD,
        (
            "#01702F呵¤\x01",
            "很有气氛啊～！\x02\x03",

            "#01709F嗯，我开始兴奋了，\x01",
            "真想赶快去玩玩看～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A16")

    label("loc_9E2")


    #C0007
    ChrTalk(
        0xD,
        (
            "#01709F嗯，我开始兴奋了，\x01",
            "真想赶快去玩玩看～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A16")

    Jump("loc_AF3")

    label("loc_A1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A31")
    Jump("loc_AF3")

    label("loc_A31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A47")
    Jump("loc_AF3")

    label("loc_A47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5D")
    Jump("loc_AF3")

    label("loc_A5D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF3")

    #C0008
    ChrTalk(
        0xD,
        (
            "#01702F我们差不多也该走了，\x01",
            "最后就玩个刺激些的东西如何？\x02\x03",

            "#01700F如果只有你们两个去玩，\x01",
            "也许会遭到限乘，\x01",
            "不过有我在就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF3")

    TalkEnd(0xFE)
    Return()

    # Function_8_96C end

    def Function_9_AF7(): pass

    label("Function_9_AF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B82")

    #C0009
    ChrTalk(
        0xE,
        (
            "#01805F那边那个东西……\x01",
            "莫非是游乐设施\x01",
            "的轨道吗？\x02\x03",

            "#01806F竟然那样子通向室外，\x01",
            "看来相当刺激呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BB9")

    label("loc_B82")


    #C0010
    ChrTalk(
        0xE,
        (
            "#01802F轨道竟然\x01",
            "那样子通向室外，\x01",
            "看来相当刺激呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB9")

    Jump("loc_C11")

    label("loc_BBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD4")
    Jump("loc_C11")

    label("loc_BD4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEA")
    Jump("loc_C11")

    label("loc_BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C00")
    Jump("loc_C11")

    label("loc_C00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C11")

    label("loc_C11")

    TalkEnd(0xFE)
    Return()

    # Function_9_AF7 end

    def Function_10_C15(): pass

    label("Function_10_C15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2E")
    Jump("loc_CA4")

    label("loc_C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C44")
    Jump("loc_CA4")

    label("loc_C44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5A")
    Jump("loc_CA4")

    label("loc_C5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C70")
    Jump("loc_CA4")

    label("loc_C70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA4")

    #C0011
    ChrTalk(
        0xF,
        "#14006F唔……我倒是无所谓……\x02",
    )

    CloseMessageWindow()

    label("loc_CA4")

    TalkEnd(0xFE)
    Return()

    # Function_10_C15 end

    def Function_11_CA8(): pass

    label("Function_11_CA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC1")
    Jump("loc_D64")

    label("loc_CC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD7")
    Jump("loc_D64")

    label("loc_CD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3D")

    #C0012
    ChrTalk(
        0x10,
        (
            "呼……\x01",
            "真是有点太刺激了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x10,
        (
            "不过，让利玛看到了\x01",
            "我英勇的一面，真是不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D64")

    label("loc_D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D53")
    Jump("loc_D64")

    label("loc_D53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D64")

    label("loc_D64")

    TalkEnd(0xFE)
    Return()

    # Function_11_CA8 end

    def Function_12_D68(): pass

    label("Function_12_D68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D81")
    Jump("loc_DF1")

    label("loc_D81")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D97")
    Jump("loc_DF1")

    label("loc_D97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCA")

    #C0014
    ChrTalk(
        0x11,
        (
            "呵呵……\x01",
            "辛苦啦，老公。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1")

    label("loc_DCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE0")
    Jump("loc_DF1")

    label("loc_DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF1")

    label("loc_DF1")

    TalkEnd(0xFE)
    Return()

    # Function_12_D68 end

    def Function_13_DF5(): pass

    label("Function_13_DF5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0E")
    Jump("loc_E8E")

    label("loc_E0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E24")
    Jump("loc_E8E")

    label("loc_E24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E67")

    #C0015
    ChrTalk(
        0x12,
        "爸爸好帅啊！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x12,
        (
            "消灭了好多\x01",
            "妖怪呢～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8E")

    label("loc_E67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7D")
    Jump("loc_E8E")

    label("loc_E7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8E")

    label("loc_E8E")

    TalkEnd(0xFE)
    Return()

    # Function_13_DF5 end

    def Function_14_E92(): pass

    label("Function_14_E92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F97")
    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        (
            "欢迎体验人称『疯狂飞车』\x01",
            "的恐怖过山车……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "这是一座恐怖的冒险型游乐设施。\x01",
            "挑战者进入之后，要单凭一把导力枪\x01",
            "来穿越栖息着众多妖怪的洋馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00003F（我们正在和咪雪捉迷藏……\x01",
            "　现在还是不要去\x01",
            "　游乐设施游玩了。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F9A")

    label("loc_F97")

    Call(0, 21)

    label("loc_F9A")

    Return()

    # Function_14_E92 end

    def Function_15_F9B(): pass

    label("Function_15_F9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1006")
    OP_4B(0x15, 0xFF)

    #C0020
    ChrTalk(
        0x14,
        (
            "哈、哈哈哈、哈哈……\x01",
            "怎么可能\x01",
            "会害怕嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x15,
        "（明明怕得要死……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    Jump("loc_1054")

    label("loc_1006")


    #C0022
    ChrTalk(
        0x14,
        (
            "多玩几次就\x01",
            "不再害怕了，\x01",
            "反而越来越开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x14,
        "哈哈哈，好，再去坐一次吧！\x02",
    )

    CloseMessageWindow()

    label("loc_1054")

    TalkEnd(0xFE)
    Return()

    # Function_15_F9B end

    def Function_16_1058(): pass

    label("Function_16_1058")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A0")

    #C0024
    ChrTalk(
        0x15,
        (
            "没问题吗？如果你不想坐，\x01",
            "不必勉强陪我哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FC")

    label("loc_10A0")


    #C0025
    ChrTalk(
        0x15,
        (
            "我男朋友得意忘形，\x01",
            "坐了好多次\x01",
            "恐怖过山车。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x15,
        (
            "唉，我还想\x01",
            "多玩一些\x01",
            "其它的游乐设施呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FC")

    TalkEnd(0xFE)
    Return()

    # Function_16_1058 end

    def Function_17_1100(): pass

    label("Function_17_1100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1155")

    #C0027
    ChrTalk(
        0x16,
        (
            "呀！我一直在大声叫喊！\x01",
            "惊险型的游乐设施\x01",
            "果然很有趣啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1155")

    label("loc_1155")

    TalkEnd(0xFE)
    Return()

    # Function_17_1100 end

    def Function_18_1159(): pass

    label("Function_18_1159")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C9")

    #C0028
    ChrTalk(
        0x17,
        (
            "爸爸真是的，\x01",
            "一直在大声喊叫，\x01",
            "连开枪都忘了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x17,
        (
            "下次再坐时，\x01",
            "还是由我来射击吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C9")

    label("loc_11C9")

    TalkEnd(0xFE)
    Return()

    # Function_18_1159 end

    def Function_19_11CD(): pass

    label("Function_19_11CD")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0030
    ChrTalk(
        0xA,
        (
            "#00309F好，大小姐，\x01",
            "我们赶快进去吧～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#00106F等、等一下，\x01",
            "我还要再做下心理准备……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_19_11CD end

    def Function_20_1249(): pass

    label("Function_20_1249")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1291")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_13A7")

    label("loc_1291")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BB")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    Jump("loc_13A7")

    label("loc_12BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E5")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_13A7")

    label("loc_12E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_132F")
    SetChrFlags(0x9, 0x80)
    Jump("loc_133D")

    label("loc_132F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_133D")
    SetChrFlags(0xC, 0x80)

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1358")
    ClearChrFlags(0x19, 0x80)

    label("loc_1358")

    Jump("loc_13A7")

    label("loc_135D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A7")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2310, 0, -3270, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_13A7")

    Return()

    # Function_20_1249 end

    def Function_21_13A8(): pass

    label("Function_21_13A8")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1800, 1650, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(10500, 0)
    OP_4B(0x13, 0xFF)
    SetChrPos(0x101, 0, 800, 1000, 0)
    Call(0, 22)
    OP_0D()

    #C0032
    ChrTalk(
        0x13,
        (
            "欢迎体验人称『疯狂飞车』\x01",
            "的恐怖过山车……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x13,
        (
            "这是一座恐怖的冒险型游乐设施。\x01",
            "挑战者进入之后，要仅凭一把导力枪\x01",
            "来穿越栖息着众多妖怪的洋馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x13,
        (
            "如果条件允许，建议您与\x01",
            "同伴一起入场体验……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#00004F#6P（……要邀请谁呢？）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要邀请谁？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "艾莉")
    MenuCmd(1, 0, "缇欧")
    MenuCmd(1, 0, "兰迪")
    MenuCmd(1, 0, "诺艾尔")
    MenuCmd(1, 0, "瓦吉")
    MenuCmd(1, 0, "琪雅")
    MenuCmd(1, 0, "芙兰")
    MenuCmd(1, 0, "塞茜尔")
    MenuCmd(1, 0, "伊莉娅")
    MenuCmd(1, 0, "莉夏")
    MenuCmd(1, 0, "修利")
    MenuCmd(1, 0, "放弃")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_158F")
    MenuCmd(3, 0, 0x0)

    label("loc_158F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_15A1")
    MenuCmd(3, 0, 0x1)

    label("loc_15A1")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_15B3")
    MenuCmd(3, 0, 0x2)

    label("loc_15B3")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_15C5")
    MenuCmd(3, 0, 0x3)

    label("loc_15C5")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_15D7")
    MenuCmd(3, 0, 0x4)

    label("loc_15D7")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_15E9")
    MenuCmd(3, 0, 0x5)

    label("loc_15E9")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_15FB")
    MenuCmd(3, 0, 0x6)

    label("loc_15FB")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_160D")
    MenuCmd(3, 0, 0x7)

    label("loc_160D")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_161F")
    MenuCmd(3, 0, 0x8)

    label("loc_161F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1631")
    MenuCmd(3, 0, 0x9)

    label("loc_1631")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1643")
    MenuCmd(3, 0, 0xA)

    label("loc_1643")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26A7")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16C9"),
        (1, "loc_1817"),
        (2, "loc_1949"),
        (3, "loc_1AC3"),
        (4, "loc_1BEE"),
        (5, "loc_1D3F"),
        (6, "loc_1E8F"),
        (7, "loc_1FDB"),
        (8, "loc_213D"),
        (9, "loc_228B"),
        (10, "loc_23A8"),
        (SWITCH_DEFAULT, "loc_250D"),
    )


    label("loc_16C9")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0037
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请艾莉吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0038
    NpcTalk(
        0x18,
        "艾莉",
        (
            "#00106F#6P恐怖过山车……\x01",
            "唔唔，真的要去吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00004F#5P哈哈，有我在一起呢，\x01",
            "没关系的。\x02\x03",

            "#00002F我一定会\x01",
            "保护好你的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0040
    NpcTalk(
        0x18,
        "艾莉",
        "#00100F#12P嗯，那就拜托你啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_1817")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0041
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请缇欧吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0042
    NpcTalk(
        0x18,
        "缇欧",
        (
            "#00204F#6P传闻中的最新游乐设施……\x01",
            "真有点期待呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0043
    ChrTalk(
        0x101,
        (
            "#00004F#5P虽然稍微有些恐怖，\x01",
            "但你好像并不在乎呢。\x02\x03",

            "#00000F我们这就进去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0044
    NpcTalk(
        0x18,
        "缇欧",
        "#00200F#12P嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_1949")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请兰迪吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x2)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19C2")
    SetChrFlags(0xA, 0x8)

    label("loc_19C2")

    FadeToBright(1000, 0)
    OP_0D()

    #N0046
    NpcTalk(
        0x18,
        "兰迪",
        (
            "#00303F#6P唔……按照常理，\x01",
            "应该邀请心仪的女孩子一起\x01",
            "玩这种刺激型的游乐设施啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00002F#5P哈哈，两个男人一起玩，\x01",
            "说不定也很有趣呢。\x02\x03",

            "#00000F我们赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0048
    NpcTalk(
        0x18,
        "兰迪",
        (
            "#00300F#12P算啦，难得来一次，\x01",
            "就陪你玩玩好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_1AC3")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0049
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请诺艾尔吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0050
    NpcTalk(
        0x18,
        "诺艾尔",
        (
            "#10100F#6P消灭妖怪……\x01",
            "真让人热血沸腾呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0051
    ChrTalk(
        0x101,
        (
            "#00009F#5P哈哈，你好像很有兴趣嘛。\x02\x03",

            "#00000F那我们就赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0052
    NpcTalk(
        0x18,
        "诺艾尔",
        "#10100F#12P嗯，走吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_1BEE")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0053
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请瓦吉吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch03000.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0054
    NpcTalk(
        0x18,
        "瓦吉",
        (
            "#10304F#6P恐怖过山车吗……\x01",
            "呵呵，想让我一边尖叫\x01",
            "一边抱住你吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x101,
        (
            "#00006F#5P我才没期待那种事。\x02\x03",

            "#00000F好啦，这就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0056
    NpcTalk(
        0x18,
        "瓦吉",
        "#10300F#12P呵呵，知道啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_1D3F")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0057
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请琪雅吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x3)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0058
    NpcTalk(
        0x18,
        "琪雅",
        (
            "#01109F#6P这里面有怪物吗？\x01",
            "好兴奋！好期待！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0059
    ChrTalk(
        0x101,
        (
            "#00012F#5P哈哈，肯定不会\x01",
            "出现真正的怪物啦……\x01",
            "不过气氛应该很不错。\x02\x03",

            "#00000F那我们这就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0060
    NpcTalk(
        0x18,
        "琪雅",
        "#01109F#12P出发！\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_1E8F")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0061
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请芙兰吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x4)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0062
    NpcTalk(
        0x18,
        "芙兰",
        (
            "#06409F#6P传闻中的最新游乐设施……\x01",
            "我紧张得心跳加速呢～！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0063
    ChrTalk(
        0x101,
        (
            "#00004F#5P哈哈，虽然是恐怖类型，\x01",
            "但你好像很有兴趣呢。\x02\x03",

            "#00000F好，那我们这就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0064
    NpcTalk(
        0x18,
        "芙兰",
        "#06400F#12P呵呵，请多关照了～\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_1FDB")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0065
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请塞茜尔姐姐吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch07500.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0066
    NpcTalk(
        0x18,
        "塞茜尔",
        (
            "#05902F#6P这就是那个传闻中的最新游乐设施吧？\x01",
            "呵呵，真期待呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0067
    ChrTalk(
        0x101,
        (
            "#00002F#5P哈哈，面对恐怖类的项目也如此轻松自若啊。\x02\x03",

            "#00000F我一定会保护好\x01",
            "塞茜尔姐姐的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0068
    NpcTalk(
        0x18,
        "塞茜尔",
        "#05900F#12P嗯，那就靠你啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_213D")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0069
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请伊莉娅小姐吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21BC")
    SetChrFlags(0xD, 0x8)

    label("loc_21BC")

    FadeToBright(1000, 0)
    OP_0D()

    #N0070
    NpcTalk(
        0x18,
        "伊莉娅",
        (
            "#01709F#6P我对这种刺激型的东西\x01",
            "很有兴趣呢～！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0071
    ChrTalk(
        0x101,
        (
            "#00009F#5P哈哈，果然是伊莉娅小姐\x01",
            "喜欢的类型啊。\x02\x03",

            "#00000F那我们这就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0072
    NpcTalk(
        0x18,
        "伊莉娅",
        "#01700F#12P嗯，赶快进去吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_228B")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0073
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请莉夏吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x6)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0074
    NpcTalk(
        0x18,
        "莉夏",
        (
            "#01802F#6P呵呵，这个游乐设施\x01",
            "好像很有气氛呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0075
    ChrTalk(
        0x101,
        (
            "#00002F#5P哈哈，你真是镇定自若啊。\x02\x03",

            "#00000F那我们这就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    #N0076
    NpcTalk(
        0x18,
        "莉夏",
        "#01809F#12P好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_23A8")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0077
    ChrTalk(
        0x101,
        "#00000F#6P（好……邀请修利吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x7)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0078
    NpcTalk(
        0x18,
        "修利",
        (
            "#14004F#6P哼、哼……\x01",
            "这东西也恐怖不到哪去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00004F#5P哈哈，谁知道～\x01",
            "说不定其实很恐怖呢……\x02\x03",

            "#00000F好，那我们这就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x18)
    OP_93(0x18, 0x10E, 0x1F4)

    #N0080
    NpcTalk(
        0x18,
        "修利",
        (
            "#14011F#12P稍、稍等一下，\x01",
            "我还没做好心理准备……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250D")

    label("loc_250D")


    #C0081
    ChrTalk(
        0x13,
        "好，请把票交给我。\x02",
    )

    CloseMessageWindow()

    def lambda_252A():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_252A)
    Sleep(50)

    def lambda_253A():
        OP_93(0x18, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_253A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把一张票交给了检票人员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0083
    ChrTalk(
        0x13,
        (
            "用来消灭妖怪的导力枪\x01",
            "就放置在二位所乘坐的车内。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x13,
        (
            "呵呵……\x01",
            "希望你们能平安归来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x13, 0x0, 0x1F4)
    OP_9B(0x0, 0x13, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(200)
    Sound(121, 0, 100, 0)
    OP_71(0x0, 0x1, 0xA, 0x1, 0x0)
    OP_79(0x0)

    def lambda_2633():
        OP_98(0xFE, 0xFFFFFA88, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2633)
    OP_93(0x13, 0x5A, 0x1F4)
    WaitChrThread(0x13, 1)
    Sleep(300)
    FadeToDark(1000, 0, -1)

    def lambda_2665():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2665)
    Sleep(50)

    def lambda_267D():
        OP_9B(0x0, 0x18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_267D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    OP_0D()
    NewScene("t1360", 0, 0, 0)
    IdleLoop()
    Jump("loc_26D9")

    label("loc_26A7")


    #C0085
    ChrTalk(
        0x13,
        "哦，不进去了吗？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x13,
        (
            "期待您\x01",
            "再次前来……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_26D9")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 400, -350, 180)
    EventEnd(0x5)
    Return()

    # Function_21_13A8 end

    def Function_22_26F4(): pass

    label("Function_22_26F4")

    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xF, 0x8)
    Return()

    # Function_22_26F4 end

    def Function_23_271D(): pass

    label("Function_23_271D")

    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xF, 0x8)
    Return()

    # Function_23_271D end

    def Function_24_2746(): pass

    label("Function_24_2746")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("chr/ch03000.itc", 0x1F)
    LoadChrToIndex("chr/ch07500.itc", 0x20)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x18, 0x80)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_27B8"),
        (1, "loc_27C1"),
        (2, "loc_27CA"),
        (3, "loc_27D3"),
        (4, "loc_27DC"),
        (5, "loc_27E5"),
        (6, "loc_27EE"),
        (7, "loc_27F7"),
        (8, "loc_2800"),
        (9, "loc_2809"),
        (10, "loc_2812"),
        (SWITCH_DEFAULT, "loc_281B"),
    )


    label("loc_27B8")

    SetChrChipByIndex(0x18, 0x0)
    Jump("loc_281B")

    label("loc_27C1")

    SetChrChipByIndex(0x18, 0x1)
    Jump("loc_281B")

    label("loc_27CA")

    SetChrChipByIndex(0x18, 0x2)
    Jump("loc_281B")

    label("loc_27D3")

    SetChrChipByIndex(0x18, 0x1E)
    Jump("loc_281B")

    label("loc_27DC")

    SetChrChipByIndex(0x18, 0x1F)
    Jump("loc_281B")

    label("loc_27E5")

    SetChrChipByIndex(0x18, 0x3)
    Jump("loc_281B")

    label("loc_27EE")

    SetChrChipByIndex(0x18, 0x4)
    Jump("loc_281B")

    label("loc_27F7")

    SetChrChipByIndex(0x18, 0x20)
    Jump("loc_281B")

    label("loc_2800")

    SetChrChipByIndex(0x18, 0x5)
    Jump("loc_281B")

    label("loc_2809")

    SetChrChipByIndex(0x18, 0x6)
    Jump("loc_281B")

    label("loc_2812")

    SetChrChipByIndex(0x18, 0x7)
    Jump("loc_281B")

    label("loc_281B")

    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x4)
    SetChrPos(0x101, -600, 800, 1000, 90)
    SetChrPos(0x18, 600, 800, 1000, 270)
    Call(0, 22)
    OP_68(0, 1800, 1650, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(11500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(10500, 2500)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_28D7"),
        (1, "loc_29C8"),
        (2, "loc_2AA3"),
        (3, "loc_2BA4"),
        (4, "loc_2C8D"),
        (5, "loc_2D56"),
        (6, "loc_2E25"),
        (7, "loc_2EFD"),
        (8, "loc_2FE8"),
        (9, "loc_30DC"),
        (10, "loc_31C1"),
        (SWITCH_DEFAULT, "loc_32BE"),
    )


    label("loc_28D7")


    #N0087
    NpcTalk(
        0x18,
        "艾莉",
        (
            "#00106F#12P呼……妖怪居然\x01",
            "凑得那么近，\x01",
            "真是吓了我一跳。\x02\x03",

            "#00100F呵呵，不过也没有\x01",
            "想象中那么可怕，\x01",
            "玩得很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，开心就好，\x01",
            "邀请你真是正确的决定啊。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0089
    NpcTalk(
        0x18,
        "艾莉",
        "#00100F#12P嗯，一会见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_29C8")


    #N0090
    NpcTalk(
        0x18,
        "缇欧",
        (
            "#00204F#12P一群妖怪不断袭来……\x01",
            "真是很刺激呢。\x02\x03",

            "#00200F不愧是最新的游乐设施，\x01",
            "难怪这么受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，你好像玩得很开心，\x01",
            "真是太好了。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0092
    NpcTalk(
        0x18,
        "缇欧",
        "#00200F#12P嗯，一会见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_2AA3")


    #N0093
    NpcTalk(
        0x18,
        "兰迪",
        (
            "#00300F#12P哈哈，作为恐怖类型的游乐设施，\x01",
            "气氛营造得相当不错。\x02\x03",

            "#00306F但一起玩的人居然是你而不是\x01",
            "漂亮的大姐姐，真是有点遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00009F算啦，反正也玩得很开心，\x01",
            "这不是很好嘛。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0095
    NpcTalk(
        0x18,
        "兰迪",
        "#00300F#12P嗯，一会见啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_2BA4")


    #N0096
    NpcTalk(
        0x18,
        "诺艾尔",
        (
            "#10100F#12P呼，真是很有意思。\x02\x03",

            "#10109F要是警备队能把这样的游戏\x01",
            "投入到射击训练中，\x01",
            "队员们肯定会进步神速。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，确实……\x01",
            "早晚有一天会实现的。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0098
    NpcTalk(
        0x18,
        "诺艾尔",
        "#10100F#12P好的，一会见！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_2C8D")


    #N0099
    NpcTalk(
        0x18,
        "瓦吉",
        (
            "#10304F#12P呵呵，这游乐设施\x01",
            "倒也有些意思呢。\x02\x03",

            "#10302F连我都有点\x01",
            "沉迷了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00009F我好像也有些上瘾……\x01",
            "总之，玩得开心就好。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0101
    NpcTalk(
        0x18,
        "瓦吉",
        "#10300F#12P呵呵，再见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_2D56")


    #N0102
    NpcTalk(
        0x18,
        "琪雅",
        (
            "#01109F#12P哈哈，好有趣！\x02\x03",

            "在一片黑暗中前进，\x01",
            "风呼呼地吹过来，\x01",
            "感觉真不错！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，能让你\x01",
            "玩得这么开心，\x01",
            "真是叫对了人。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0104
    NpcTalk(
        0x18,
        "琪雅",
        "#01100F#12P嗯，一会见哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_2E25")


    #N0105
    NpcTalk(
        0x18,
        "芙兰",
        (
            "#06400F#12P呼，真是刺激性十足啊～！\x02\x03",

            "#06409F多亏有\x01",
            "罗伊德警官\x01",
            "努力射击。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00009F应付那么多妖怪\x01",
            "真是相当吃力……\x01",
            "不过，你玩得开心就好。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0107
    NpcTalk(
        0x18,
        "芙兰",
        "#06400F#12P好的，稍后见～\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_2EFD")


    #N0108
    NpcTalk(
        0x18,
        "塞茜尔",
        (
            "#05900F#12P呵呵，真是相当有趣啊。\x02\x03",

            "#05909F罗伊德射击时的样子\x01",
            "显得相当可靠。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，其实和真枪\x01",
            "的手感完全不同……\x01",
            "不过，塞茜尔姐姐玩得开心就好。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0110
    NpcTalk(
        0x18,
        "塞茜尔",
        "#05900F#12P嗯，一会见啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_2FE8")


    #N0111
    NpcTalk(
        0x18,
        "伊莉娅",
        (
            "#01704F#12P嗯，这个游乐设施\x01",
            "果然没有辜负我的期待啊！\x02\x03",

            "#01702F呵呵，不过妖怪要是\x01",
            "再多一些就更好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00012F那、那可就真是\x01",
            "应付不过来了……\x01",
            "总之，玩得开心就好。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0113
    NpcTalk(
        0x18,
        "伊莉娅",
        "#01700F#12P嗯，我先走啦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_30DC")


    #N0114
    NpcTalk(
        0x18,
        "莉夏",
        (
            "#01802F#12P呼，真是很有趣。\x02\x03",

            "#01806F妖怪的行动让人眼花缭乱，\x01",
            "负责射击的罗伊德警官\x01",
            "肯定很辛苦吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，虽然稍微有点累，\x01",
            "但我也玩得很开心。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0116
    NpcTalk(
        0x18,
        "莉夏",
        "#01802F#12P好的，一会见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_31C1")


    #N0117
    NpcTalk(
        0x18,
        "修利",
        (
            "#14006F#12P呼……车速实在太快了，\x01",
            "我完全睁不开眼。\x01",
            "不过还算比较刺激。\x02\x03",

            "#14002F话说回来，\x01",
            "你好像玩得很开心啊，\x01",
            "我也想试试射击呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……其实射击\x01",
            "也是相当累人的。\x02\x03",

            "#00000F那就稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0119
    NpcTalk(
        0x18,
        "修利",
        "#14000F#12P嗯，那我先走啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_32BE")


    def lambda_32C3():

        label("loc_32C3")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_32C3")

    QueueWorkItem2(0x101, 2, lambda_32C3)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_32DC():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_32DC)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x18, 1)
    EndChrThread(0x101, 0x2)
    SetChrFlags(0x18, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3359"),
        (1, "loc_3367"),
        (2, "loc_3375"),
        (3, "loc_3383"),
        (4, "loc_3391"),
        (5, "loc_339F"),
        (6, "loc_33AD"),
        (7, "loc_33BB"),
        (8, "loc_33C9"),
        (9, "loc_33D7"),
        (10, "loc_33E5"),
        (SWITCH_DEFAULT, "loc_33F3"),
    )


    label("loc_3359")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_3367")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_3375")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_3383")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_3391")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_339F")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_33AD")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_33BB")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_33C9")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_33D7")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_33E5")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33F3")

    label("loc_33F3")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3419")
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_3419")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 0, -2000, 180)
    EventEnd(0x5)
    Return()

    # Function_24_2746 end

    def Function_25_3434(): pass

    label("Function_25_3434")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3070, 2300, -4040, 0)
    MoveCamera(310, 39, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x101, -2970, 0, -3760, 270)
    SetChrPos(0xEF, -2050, 0, -2510, 270)
    OP_4B(0x19, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0120
    ChrTalk(
        0x101,
        "#00002F找到了！\x02",
    )

    CloseMessageWindow()
    OP_9C(0x19, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    OP_93(0x19, 0x5A, 0x1F4)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "呀！被发现啦☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-630, 2300, -4310, 0)
    MoveCamera(330, 32, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x19, -2930, 0, -3100, 90)
    SetChrPos(0x101, -1440, 0, -4040, 270)
    SetChrPos(0xEF, -940, 0, -2450, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0122
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "真是的，竟然这么快\x01",
            "就找到了我四次，\x01",
            "简直不敢相信呢～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，和我那个\x01",
            "笨哥哥真是\x01",
            "完全不同呢～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_362E")
    OP_63(0x153, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3646")

    label("loc_362E")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3646")

    Sleep(1000)

    #C0124
    ChrTalk(
        0x101,
        (
            "#00006F（咪雪对咪西\x01",
            "  还真是不留情面呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "……嗯嗯，接下来就是最后一次啦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "好～最后这一次，我会藏到\x01",
            "更加难找的地方，你们就加油找吧～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36EF():

        label("loc_36EF")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_36EF")

    QueueWorkItem2(0x101, 1, lambda_36EF)

    def lambda_3701():

        label("loc_3701")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_3701")

    QueueWorkItem2(0xEF, 1, lambda_3701)
    SetChrFlags(0x19, 0x1000)
    OP_95(0x19, -1430, 0, -8620, 4000, 0x0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(2740, 4000, -15010, 0)
    MoveCamera(322, 28, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8039, 0)
    SetChrPos(0x101, -430, 0, -11830, 180)
    SetChrPos(0xEF, 960, 0, -11900, 180)
    SetChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0127
    ChrTalk(
        0x101,
        (
            "#00006F终于到了最后一次……\x02\x03",

            "#00000F既然它还藏在主题公园内，\x01",
            "就应该不会太难找。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_3825")

    #C0128
    ChrTalk(
        0x102,
        (
            "#00100F好，那我们\x01",
            "这就开始找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_3825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_3855")

    #C0129
    ChrTalk(
        0x103,
        (
            "#00200F那我们这就\x01",
            "开始找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_3855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_3885")

    #C0130
    ChrTalk(
        0x104,
        (
            "#00300F那我们这就\x01",
            "去找它吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_3885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_38B5")

    #C0131
    ChrTalk(
        0x109,
        (
            "#10100F那我们这就\x01",
            "去找它吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_38B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_38E5")

    #C0132
    ChrTalk(
        0x105,
        (
            "#10300F那我们这就\x01",
            "开始找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_38E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_3910")

    #C0133
    ChrTalk(
        0x153,
        "#01100F那就赶快去找吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_3910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_3942")

    #C0134
    ChrTalk(
        0x156,
        (
            "#06400F那我们这就\x01",
            "去找它吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_3942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_3978")

    #C0135
    ChrTalk(
        0x14C,
        (
            "#05900F呵呵，那我们这就\x01",
            "开始找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_3978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_39AE")

    #C0136
    ChrTalk(
        0x134,
        (
            "#01700F呵呵，那我们这就\x01",
            "去找它吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_39AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_39DE")

    #C0137
    ChrTalk(
        0x135,
        (
            "#01802F那我们这就\x01",
            "开始找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FE")

    label("loc_39DE")


    #C0138
    ChrTalk(
        0x166,
        (
            "#14000F那就赶快\x01",
            "开始找吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xE)
    SetScenarioFlags(0x1C9, 6)
    SetChrPos(0x0, 160, 0, -12030, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_3434 end

    def Function_26_3A2A(): pass

    label("Function_26_3A2A")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "张贴着主题公园的\x01",
            "导览地图。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_26_3A2A end

    SaveToFile()

Try(main)
