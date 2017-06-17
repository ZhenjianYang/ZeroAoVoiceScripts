from ScenarioHelper import *

def main():
    CreateScenaFile(
        "a0004.bin",                # FileName
        "a0002",                    # MapName
        "a0002",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 25000, 500, 20, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0004",                  # 0
        "CH40000 4パタ",          # 1
        "CH40001 5パタ",          # 2
        "CH40002 6パタ",          # 3
        "CH40003 7パタ",          # 4
    ))

    AddCharChip((
        "chr/ch40000.itc",                   # 00
        "chr/ch40001.itc",                   # 01
        "chr/ch40002.itc",                   # 02
        "chr/ch40003.itc",                   # 03
    ))

    DeclNpc(4000,    0,       4000,    180,  257,  0x0, 0,   0,   0,   255, 255, 0,   2,   599,  0)
    DeclNpc(8000,    0,       4000,    180,  257,  0x0, 0,   1,   0,   255, 255, 0,   2,   623,  0)
    DeclNpc(12000,   0,       4000,    180,  257,  0x0, 0,   2,   0,   255, 255, 0,   2,   647,  0)
    DeclNpc(16000,   0,       4000,    180,  257,  0x0, 0,   3,   0,   255, 255, 0,   2,   671,  0)

    ChipFrameInfo(1000, 0, [0, 1, 2, 1])                         # 0

    ScpFunction((
        "Function_0_154",          # 00, 0
        "Function_1_166",          # 01, 1
        "Function_2_217",          # 02, 2
        "Function_3_23E",          # 03, 3
        "Function_4_23F",          # 04, 4
        "Function_5_257",          # 05, 5
        "Function_6_26F",          # 06, 6
        "Function_7_287",          # 07, 7
        "Function_8_29F",          # 08, 8
        "Function_9_2B7",          # 09, 9
    ))


    def Function_0_154(): pass

    label("Function_0_154")

    SetChrPos(0x0, 0, 0, 0, 0)
    Return()

    # Function_0_154 end

    def Function_1_166(): pass

    label("Function_1_166")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_166 end

    def Function_2_217(): pass

    label("Function_2_217")

    TalkBegin(0xFF)

    #C0001
    ChrTalk(
        0xFE,
        "私は???テストキャラ???です\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_2_217 end

    def Function_3_23E(): pass

    label("Function_3_23E")

    Return()

    # Function_3_23E end

    def Function_4_23F(): pass

    label("Function_4_23F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_256")
    OP_A0(0xFE, 1200, 0x0, 0x2)
    Jump("Function_4_23F")

    label("loc_256")

    Return()

    # Function_4_23F end

    def Function_5_257(): pass

    label("Function_5_257")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26E")
    OP_A0(0xFE, 1200, 0x0, 0x3)
    Jump("Function_5_257")

    label("loc_26E")

    Return()

    # Function_5_257 end

    def Function_6_26F(): pass

    label("Function_6_26F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_286")
    OP_A0(0xFE, 1200, 0x0, 0x4)
    Jump("Function_6_26F")

    label("loc_286")

    Return()

    # Function_6_26F end

    def Function_7_287(): pass

    label("Function_7_287")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29E")
    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("Function_7_287")

    label("loc_29E")

    Return()

    # Function_7_287 end

    def Function_8_29F(): pass

    label("Function_8_29F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B6")
    OP_A0(0xFE, 1200, 0x0, 0x6)
    Jump("Function_8_29F")

    label("loc_2B6")

    Return()

    # Function_8_29F end

    def Function_9_2B7(): pass

    label("Function_9_2B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CE")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("Function_9_2B7")

    label("loc_2CE")

    Return()

    # Function_9_2B7 end

    SaveToFile()

Try(main)
