from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c103c.bin",                # FileName
        "c103c",                    # MapName
        "c103c",                    # Location
        0x0012,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 18, 0, 3, 0, 4],
    )

    BuildStringList((
        "c103c",                  # 0
        "チャンホイ",             # 1
        "フェン",                 # 2
        "サンサン",               # 3
        "グリッド",               # 4
        "パック",                 # 5
        "ルース",                 # 6
        "見物客",                 # 7
        "遊撃士スコット",         # 8
        "遊撃士ヴェンツェル",     # 9
        "遊撃士リン",             # 10
        "キリカ",                 # 11
    ))

    AddCharChip((
        "chr/ch31600.itc",                   # 00
        "chr/ch25100.itc",                   # 01
        "chr/ch32500.itc",                   # 02
        "chr/ch26302.itc",                   # 03
        "chr/ch20402.itc",                   # 04
        "chr/ch21202.itc",                   # 05
        "chr/ch24202.itc",                   # 06
        "chr/ch27202.itc",                   # 07
        "chr/ch27302.itc",                   # 08
        "chr/ch32002.itc",                   # 09
        "chr/ch07302.itc",                   # 0A
    ))

    DeclNpc(16000,   0,       15989,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(16030,   0,       6050,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(12310,   0,       -1990,   225,  261,  0x0, 0,   2,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(7130,    150,     -1480,   180,  261,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(10689,   150,     3170,    270,  261,  0x0, 0,   4,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(7300,    150,     3230,    90,   261,  0x0, 0,   5,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(13949,   150,     2900,    90,   261,  0x0, 0,   6,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(3220,    150,     5539,    0,    389,  0x0, 0,   7,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(3130,    150,     8930,    180,  389,  0x0, 0,   8,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(1440,    150,     7170,    90,   389,  0x0, 0,   9,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(4989,    150,     7179,    270,  389,  0x0, 0,   10,  0,   255, 255, 0,   18,  255,  0)

    DeclActor(14590,   0,       4630,    1000,    16030,   1500,    6050,    0x007E, 0,  5,  0x0000)

    ScpFunction((
        "Function_0_264",          # 00, 0
        "Function_1_31C",          # 01, 1
        "Function_2_470",          # 02, 2
        "Function_3_49B",          # 03, 3
        "Function_4_57B",          # 04, 4
        "Function_5_5CC",          # 05, 5
        "Function_6_61D",          # 06, 6
        "Function_7_727",          # 07, 7
        "Function_8_B6B",          # 08, 8
        "Function_9_C75",          # 09, 9
        "Function_10_1141",        # 0A, 10
        "Function_11_14F5",        # 0B, 11
        "Function_12_1A14",        # 0C, 12
        "Function_13_1DAF",        # 0D, 13
        "Function_14_2164",        # 0E, 14
        "Function_15_24D9",        # 0F, 15
        "Function_16_270D",        # 10, 16
        "Function_17_2893",        # 11, 17
        "Function_18_2C33",        # 12, 18
    ))


    def Function_0_264(): pass

    label("Function_0_264")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2A4"),
        (1, "loc_2B0"),
        (2, "loc_2BC"),
        (3, "loc_2C8"),
        (4, "loc_2D4"),
        (5, "loc_2E0"),
        (6, "loc_2EC"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_2A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_31B")

    Return()

    # Function_0_264 end

    def Function_1_31C(): pass

    label("Function_1_31C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46F")
    OP_95(0xFE, 7200, 0, 370, 1000, 0x0)
    OP_95(0xFE, 7280, 30, 1390, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_95(0xFE, 5850, 0, 1930, 1000, 0x0)
    OP_95(0xFE, 4730, 0, 3700, 1000, 0x0)
    OP_95(0xFE, 4840, 0, 5570, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 5660, 0, 5540, 1000, 0x0)
    OP_95(0xFE, 10470, 0, 10350, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1200)
    OP_95(0xFE, 12980, 0, 7230, 1000, 0x0)
    OP_95(0xFE, 12730, 0, 2100, 1000, 0x0)
    OP_95(0xFE, 13200, 0, 1420, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1600)
    OP_95(0xFE, 12280, 0, 680, 1000, 0x0)
    OP_95(0xFE, 11230, 0, 110, 1000, 0x0)
    OP_95(0xFE, 8930, 30, -1570, 1000, 0x0)
    Sleep(1400)
    OP_95(0xFE, 8720, 0, -510, 1000, 0x0)
    Jump("Function_1_31C")

    label("loc_46F")

    Return()

    # Function_1_31C end

    def Function_2_470(): pass

    label("Function_2_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49A")
    OP_94(0xFE, 0xFFFF408E, 0xFFFF30F8, 0xFFFF3724, 0xFFFF236A, 0x3E8)
    Sleep(300)
    Jump("Function_2_470")

    label("loc_49A")

    Return()

    # Function_2_470 end

    def Function_3_49B(): pass

    label("Function_3_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4B3")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_57A")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_50A")
    SetChrPos(0x8, 16030, 0, 6050, 270)
    SetChrPos(0x9, 12310, 0, -1990, 225)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, -49600, 30, -55300, 135)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_57A")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_557")
    SetChrPos(0x8, 16030, 0, 6050, 270)
    SetChrPos(0x9, 12310, 0, -1990, 225)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, -53960, 0, -55210, 180)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_57A")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_571")
    OP_93(0x8, 0xB4, 0x0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_57A")

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_57A")

    label("loc_57A")

    Return()

    # Function_3_49B end

    def Function_4_57B(): pass

    label("Function_4_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_58C")
    SetScenarioFlags(0x1, 0)
    Jump("loc_5CB")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_59D")
    SetScenarioFlags(0x0, 7)
    Jump("loc_5CB")

    label("loc_59D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5AE")
    SetScenarioFlags(0x0, 7)
    Jump("loc_5CB")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5BF")
    SetScenarioFlags(0x1, 0)
    Jump("loc_5CB")

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5CB")
    SetScenarioFlags(0x1, 0)

    label("loc_5CB")

    Return()

    # Function_4_57B end

    def Function_5_5CC(): pass

    label("Function_5_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5DD")
    Call(0, 8)
    Jump("loc_61C")

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5EE")
    Call(0, 6)
    Jump("loc_61C")

    label("loc_5EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5FF")
    Call(0, 6)
    Jump("loc_61C")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_610")
    Call(0, 8)
    Jump("loc_61C")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_61C")
    Call(0, 8)

    label("loc_61C")

    Return()

    # Function_5_5CC end

    def Function_6_61D(): pass

    label("Function_6_61D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_720")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_716")

    label("loc_6C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E6")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_716")

    label("loc_6E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FA")
    Jump("loc_716")

    label("loc_6FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_716")

    Jump("loc_633")

    label("loc_71B")

    Jump("loc_723")

    label("loc_720")

    Call(0, 7)

    label("loc_723")

    TalkEnd(0x8)
    Return()

    # Function_6_61D end

    def Function_7_727(): pass

    label("Function_7_727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_80C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A8")

    #C0001
    ChrTalk(
        0x8,
        "特製チャーハン２、お待ち！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "……今日の客入りはそれほどでもない。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "何とか乗り切れそうね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_807")

    label("loc_7A8")


    #C0004
    ChrTalk(
        0x8,
        (
            "この人出も今日限り。\x01",
            "また明日からは常連客ばかりの営業ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "……何とか乗り切れそうね。\x02",
    )

    CloseMessageWindow()

    label("loc_807")

    Jump("loc_B6A")

    label("loc_80C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_876")

    #C0006
    ChrTalk(
        0x8,
        "ハイお客さん！　ご注文は何ね！\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "ん？　んん？\x01",
            "何を食べるかね……ッ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8D7")

    label("loc_876")


    #C0008
    ChrTalk(
        0x8,
        (
            "宿のチェックインは\x01",
            "夕方５時からよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "それまでは\x01",
            "宿部屋に入ってはいけない。\x01",
            "……いいね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D7")

    Jump("loc_B6A")

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_989")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_933")

    #C0010
    ChrTalk(
        0x8,
        "……何か食べるか？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "ん？　何か食べるかね……ッ！？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_984")

    label("loc_933")


    #C0012
    ChrTalk(
        0x8,
        "サンサンは奥に下がらせたよ。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "大勢の男どもに\x01",
            "さらすのは、やはり心配ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_984")

    Jump("loc_B6A")

    label("loc_989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A36")
    TurnDirection(0x8, 0xE, 300)

    #C0014
    ChrTalk(
        0x8,
        (
            "……あそこの席の男、\x01",
            "ちらちらサンサンに色目使っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "………ギンッ…………………\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xE,
        (
            "お、おかしいな……\x01",
            "何だか寒気が……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_A7B")

    label("loc_A36")


    #C0017
    ChrTalk(
        0x8,
        (
            "サンサンに手を\x01",
            "出したら許さないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "よく覚えておくよろし。\x02",
    )

    CloseMessageWindow()

    label("loc_A7B")

    Jump("loc_B6A")

    label("loc_A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B13")
    OP_63(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0019
    ChrTalk(
        0x8,
        "さすが記念祭は騒がしいね……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "ワタシは静かな店が好き。\x01",
            "……客なんて来なくていいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B6A")

    label("loc_B13")


    #C0021
    ChrTalk(
        0x8,
        (
            "……あまり騒がしいと\x01",
            "東方人街を思い出すよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "あの街はいつもこんな空気だった。\x02",
    )

    CloseMessageWindow()

    label("loc_B6A")

    Return()

    # Function_7_727 end

    def Function_8_B6B(): pass

    label("Function_8_B6B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_C6E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C69")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BF4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_BF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C14")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C64")

    label("loc_C14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C34")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C64")

    label("loc_C34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C48")
    Jump("loc_C64")

    label("loc_C48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C64")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_C64")

    Jump("loc_B81")

    label("loc_C69")

    Jump("loc_C71")

    label("loc_C6E")

    Call(0, 9)

    label("loc_C71")

    TalkEnd(0x9)
    Return()

    # Function_8_B6B end

    def Function_9_C75(): pass

    label("Function_9_C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D38")

    #C0023
    ChrTalk(
        0x9,
        "いやあ、今年は色々あった。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "サンサンが店を手伝い始めて\x01",
            "初めての記念祭だったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        "お陰で客入りは倍増した㈱\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x9,
        (
            "店長は気が気じゃ\x01",
            "なかったみたいだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D96")

    label("loc_D38")


    #C0027
    ChrTalk(
        0x9,
        (
            "今年はサンサンが\x01",
            "店を手伝い始めたんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "店長があたふたして\x01",
            "色々と面白かったぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D96")

    Jump("loc_1140")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF2")

    #C0029
    ChrTalk(
        0x9,
        "はいそこ、座れ座れ～。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        "立ってると邪魔になんだろ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E5C")

    label("loc_DF2")


    #C0031
    ChrTalk(
        0x9,
        (
            "俺っちはいま手一杯だ。\x01",
            "注文ならマスターに言いな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "すっげー怖ぇ顔してるけどな。\x01",
            "はははは……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5C")

    Jump("loc_1140")

    label("loc_E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED4")

    #C0033
    ChrTalk(
        0x9,
        (
            "うっす！　警察の人か。\x01",
            "お仕事ご苦労さん！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            "何か食べてくか？\x01",
            "今日は大変だろ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F44")

    label("loc_ED4")


    #C0035
    ChrTalk(
        0x9,
        (
            "マスターは昨日から\x01",
            "ちょーっと気が立ってんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "ま、無理もねえ。\x01",
            "サンサンは可愛くて目立つからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F44")

    Jump("loc_1140")

    label("loc_F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_103F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCA")

    #C0037
    ChrTalk(
        0x9,
        (
            "昨日は旧市街の方で\x01",
            "ドタバタがあったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "客が興奮して話してたぜ。\x01",
            "一体何があったんだ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_103A")

    label("loc_FCA")


    #C0039
    ChrTalk(
        0x9,
        (
            "昨日は旧市街の方で\x01",
            "ドタバタがあったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "客は面白かったとか言ってたが\x01",
            "一体何があったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103A")

    Jump("loc_1140")

    label("loc_103F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D0")

    #C0041
    ChrTalk(
        0x9,
        (
            "４００００、５００００、\x01",
            "６００００ミラ……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "うひゃひゃ、\x01",
            "いい儲かりっぷりだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "記念祭さまさまだな～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1140")

    label("loc_10D0")


    #C0044
    ChrTalk(
        0x9,
        "いよう、場末の宿酒場へようこそっ！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "『東口に一番近い店』ってのは\x01",
            "うちのことだぜ。\x01",
            "今後もよろしくぅ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1140")

    Return()

    # Function_9_C75 end

    def Function_10_1141(): pass

    label("Function_10_1141")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11CA")

    #C0046
    ChrTalk(
        0xFE,
        (
            "せっせっ……\x01",
            "今日は創立記念祭の最終日よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "お客さんも張り切って食べていくの。\x01",
            "最後に思いっきり楽しむんだって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F1")

    label("loc_11CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_12C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124D")

    #C0048
    ChrTalk(
        0xFE,
        (
            "パパが今日は\x01",
            "宿の掃除をしろというの。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "パパ、どうしたんだろ。\x01",
            "そんなに掃除する所もないよ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12BD")

    label("loc_124D")


    #C0050
    ChrTalk(
        0xFE,
        (
            "宿の掃除なんて\x01",
            "すぐに済んでしまうのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "ふう、パレード見たかったなぁ……\x01",
            "もう終わっちゃったのかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BD")

    Jump("loc_14F1")

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_13DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1382")

    #C0052
    ChrTalk(
        0xFE,
        (
            "リーシャ、今ごろ\x01",
            "公演ガンバッてるかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "ふふっ、きっと大勢のお客さんに\x01",
            "拍手されているに違いないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "私も負けてられないよ。\x01",
            "お仕事頑張らなくっちゃ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_13D9")

    label("loc_1382")


    #C0055
    ChrTalk(
        0xFE,
        "今日はお泊りの部屋も満室だったの。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "せっせっ……\x01",
            "はりきって綺麗にしないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D9")

    Jump("loc_14F1")

    label("loc_13DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_144C")

    #C0057
    ChrTalk(
        0xFE,
        (
            "パパったら\x01",
            "またお客さんをおどかして……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ダメよ、お客さんには\x01",
            "いつもスマイルでないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F1")

    label("loc_144C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_14F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BC")

    #C0059
    ChrTalk(
        0xFE,
        "あ、いらっしゃい～！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "ふう、お客さん多くてびっくり。\x01",
            "注文をとるのも大変ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_14F1")

    label("loc_14BC")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1200)

    #C0061
    ChrTalk(
        0xFE,
        "うう……手が足りないよ～。\x02",
    )

    CloseMessageWindow()

    label("loc_14F1")

    TalkEnd(0xFE)
    Return()

    # Function_10_1141 end

    def Function_11_14F5(): pass

    label("Function_11_14F5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1589")
    Jump("loc_15D3")

    label("loc_1589")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15A9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15D3")

    label("loc_15A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15C9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15D3")

    label("loc_15C9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15D3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1695")

    #C0062
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "みんな盛り上がってるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "俺は今日も変わらず\x01",
            "共和国までドライブだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "運送業には休みがないんだよな～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_16C6")

    label("loc_1695")


    #C0065
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "盛り上がってる奴が羨ましいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C6")

    Jump("loc_1A0C")

    label("loc_16CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1792")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1756")

    #C0066
    ChrTalk(
        0xFE,
        (
            "やれやれ、この人出じゃ\x01",
            "表通りを走るのは難しそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "事故っても困るし\x01",
            "裏通りから街道に出るとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_178D")

    label("loc_1756")


    #C0068
    ChrTalk(
        0xFE,
        (
            "やれやれ、今日の運送は\x01",
            "だいぶ遅れちまいそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178D")

    Jump("loc_1A0C")

    label("loc_1792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1896")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182D")

    #C0069
    ChrTalk(
        0xFE,
        "今日はパレードがあるんだってな。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "ウチの会社も\x01",
            "運転手を１人貸し出してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "なにせ俺たちは\x01",
            "運転のプロだからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1891")

    label("loc_182D")


    #C0072
    ChrTalk(
        0xFE,
        (
            "ウチの会社も\x01",
            "運転手を１人貸し出してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "……その分こっちは\x01",
            "忙しくなっちまったけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1891")

    Jump("loc_1A0C")

    label("loc_1896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1906")

    #C0074
    ChrTalk(
        0xFE,
        (
            "観光バスがぞくぞく\x01",
            "来てるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "タングラム門の方には\x01",
            "まだ何台も入国待ちしてたぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0C")

    label("loc_1906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A0")

    #C0076
    ChrTalk(
        0xFE,
        (
            "記念祭の影響で\x01",
            "共和国方面の道が渋滞していたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "驚いたぜ……\x01",
            "導力車で道が埋まっちまうなんて\x01",
            "世界初なんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A0C")

    label("loc_19A0")


    #C0078
    ChrTalk(
        0xFE,
        (
            "クロスベルは導力車が多いし\x01",
            "共和国も導力バスが普及してるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "共和国方面は\x01",
            "だいぶ混雑してたぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_14F5 end

    def Function_12_1A14(): pass

    label("Function_12_1A14")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AA8")
    Jump("loc_1AF2")

    label("loc_1AA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1AC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AF2")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AE8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AF2")

    label("loc_1AE8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AF2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1B8F")

    #C0080
    ChrTalk(
        0xFE,
        "相棒とやり直すことにしたんだ。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "へへっ、ルースの奴……\x01",
            "やっぱりオレと\x01",
            "店を出したいんじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA7")

    label("loc_1B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1C02")

    #C0082
    ChrTalk(
        0xFE,
        "すごい観光客だったよなぁ……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "確かにルースの言うとおり、\x01",
            "観光客相手の商売なら売れそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA7")

    label("loc_1C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5D")

    #C0084
    ChrTalk(
        0xFE,
        "確かに……人が多いよな。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "うん、オレも素直に認めるぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1CB2")

    label("loc_1C5D")


    #C0086
    ChrTalk(
        0xFE,
        "相棒とは喧嘩してたんだけど……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "確かに人が多いよな。\x01",
            "オレも素直に認めるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB2")

    Jump("loc_1DA7")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D25")

    #C0088
    ChrTalk(
        0xFE,
        (
            "相棒の奴、ぼそぼそと\x01",
            "独り言を言いやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "……もう商売は\x01",
            "やめるって言ったのにな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA7")

    label("loc_1D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DA7")
    SetChrSubChip(0xC, 0x0)

    #C0090
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "ふん、オレがどこで\x01",
            "楽しもうが勝手じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "ルースこそオレの\x01",
            "楽しい記念祭を邪魔するなよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_1A14 end

    def Function_13_1DAF(): pass

    label("Function_13_1DAF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E43")
    Jump("loc_1E8D")

    label("loc_1E43")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E63")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E8D")

    label("loc_1E63")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E83")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E8D")

    label("loc_1E83")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E8D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F6D")

    #C0092
    ChrTalk(
        0xFE,
        (
            "……パックと\x01",
            "店を出す事にしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "記念祭には間に合わないが……\x01",
            "クロスベルは観光客が多いもんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "うん、今度はきっと大丈夫だ。\x01",
            "いい店が出せそうな気がするぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215C")

    label("loc_1F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_200A")

    #C0095
    ChrTalk(
        0xFE,
        (
            "ついつい観光客の\x01",
            "チェックをしちまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "どんな商品なら\x01",
            "売れそうか……とかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "うーん、俺も正直言うと\x01",
            "商売をしたいんだよな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215C")

    label("loc_200A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_206E")

    #C0098
    ChrTalk(
        0xFE,
        (
            "こんなに\x01",
            "観光客が来るなんてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "観光客相手の商売をしたら\x01",
            "儲かりそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215C")

    label("loc_206E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20EA")
    SetChrSubChip(0xD, 0x0)

    #C0100
    ChrTalk(
        0xFE,
        (
            "おいパック……\x01",
            "外は凄い人出だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "商売したら\x01",
            "儲かりそうだよな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215C")

    label("loc_20EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_215C")
    SetChrSubChip(0xD, 0x0)

    #C0103
    ChrTalk(
        0xFE,
        (
            "むしゃむしゃ……\x01",
            "おいパック、\x01",
            "なんでここに来てるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "もう顔を\x01",
            "合わせねえって約束だろ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_1DAF end

    def Function_14_2164(): pass

    label("Function_14_2164")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21F8")
    Jump("loc_2242")

    label("loc_21F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2218")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2242")

    label("loc_2218")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2238")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2242")

    label("loc_2238")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2242")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_22DB")

    #C0105
    ChrTalk(
        0xFE,
        "ここのマスター、怖い人だね。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "ウェイトレスさんに\x01",
            "声を掛けたら、お玉で殴られたよ。\x01",
            "とほほ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D1")

    label("loc_22DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_234F")

    #C0107
    ChrTalk(
        0xFE,
        (
            "あれ、ウェイトレスさんが\x01",
            "居なくなっちゃったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "残念だよ……\x01",
            "スゴク可愛い子だったのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D1")

    label("loc_234F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_23DC")

    #C0109
    ChrTalk(
        0xFE,
        (
            "今日はパレードがあるらしいねえ。\x01",
            "私も見に行ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "ところで……ここのマスター\x01",
            "何だか威圧的だね。\x01",
            "気のせいかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D1")

    label("loc_23DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2462")

    #C0111
    ChrTalk(
        0xFE,
        (
            "ずずー……いやあしかし\x01",
            "ここのメシは美味いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "ウェイトレスさんも可愛いし……\x01",
            "むふふ、長居したくなっちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D1")

    label("loc_2462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_24D1")

    #C0113
    ChrTalk(
        0xFE,
        (
            "いやあ、参った参った。\x01",
            "外は大した賑わいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "やっぱり地図も持たずに\x01",
            "回るものじゃないねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_2164 end

    def Function_15_24D9(): pass

    label("Function_15_24D9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_256D")
    Jump("loc_25B7")

    label("loc_256D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_258D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25B7")

    label("loc_258D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25B7")

    label("loc_25AD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25B7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B2")

    #C0115
    ChrTalk(
        0xFE,
        "やあ君たち、今戻ったのか？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "俺は今さっき、\x01",
            "依頼結果の報告を済ませたところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "また力を合わせるような\x01",
            "機会があるといいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0000Fええ、そのときは\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2705")

    label("loc_26B2")


    #C0119
    ChrTalk(
        0xFE,
        (
            "あの時、アリオスさんが来てくれて\x01",
            "本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "俺もまだまだだなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_2705")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_24D9 end

    def Function_16_270D(): pass

    label("Function_16_270D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27A1")
    Jump("loc_27EB")

    label("loc_27A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_27C1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27EB")

    label("loc_27C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27EB")

    label("loc_27E1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27EB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_288B")

    #C0121
    ChrTalk(
        0xFE,
        (
            "スコットと協力して\x01",
            "依頼を達成したそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "……それは我々にとって、\x01",
            "本来あるべき姿なのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_288B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_270D end

    def Function_17_2893(): pass

    label("Function_17_2893")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2927")
    Jump("loc_2971")

    label("loc_2927")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2947")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2971")

    label("loc_2947")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2967")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2971")

    label("loc_2967")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2971")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B30")

    #C0123
    ChrTalk(
        0x12,
        (
            "#3400F久し振りね、リン。\x01",
            "大きくなったものだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x11,
        "ふふ、そりゃあ８年ぶりですから……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x11,
        (
            "お手合わせしてもらった\x01",
            "あの日のことは\x01",
            "今でも鮮明に覚えていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x12,
        (
            "#3404Fふふ……\x01",
            "そんなこともあったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#0005F（リンさん、キリカさんと\x01",
            "  知り合いだったのか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#0300F（つーか、キリカさんも\x01",
            "  武術ができる人みたいだな。\x01",
            "  只者じゃねぇとは思っていたが……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2C2B")

    label("loc_2B30")


    #C0129
    ChrTalk(
        0x11,
        (
            "えっ……あの２人には\x01",
            "会っていかないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x11,
        (
            "せっかく、クロスベルに\x01",
            "来ているのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x12,
        (
            "#3403F今回は遠慮しておくわ。\x01",
            "私は一抜けした身だし……\x02\x03",

            "#3400Fあなたの方から\x01",
            "よろしく言っておいて頂戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x11,
        (
            "そうですか……\x01",
            "絶対喜ぶと思うんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_2893 end

    def Function_18_2C33(): pass

    label("Function_18_2C33")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CC7")
    Jump("loc_2D11")

    label("loc_2CC7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CE7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D11")

    label("loc_2CE7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D07")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D11")

    label("loc_2D07")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D11")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D59")
    Call(0, 17)
    Jump("loc_2E63")

    label("loc_2D59")


    #C0133
    ChrTalk(
        0x12,
        (
            "#3404F話には聞いていたけど、\x01",
            "立派に遊撃士をしているみたいね。\x02\x03",

            "#3400F男勝りな喋り方は\x01",
            "子供の頃から変わってないけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x11,
        "はは……お恥ずかしい限りです。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x11,
        (
            "……キリカ先輩は……\x01",
            "この８年、何をしていたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x12,
        (
            "#3404Fふふ……\x01",
            "色々、とだけ言っておくわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E63")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_2C33 end

    SaveToFile()

Try(main)
