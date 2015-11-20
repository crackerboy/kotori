typedef struct struct_position         // added 06.03.2014 C.L.
{
    struct_position()
    : length(9), ID(1)
    {}
    uint8_t  length             ;//1
    uint8_t  ID                 ;//2
    uint16_t flag_1             ;//4
    int16_t  hdg                ;//6
    int16_t  pitch              ;//8
    char     ck                 ;//9
} Tstruct_prog;