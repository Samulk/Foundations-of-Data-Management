use inf551;

drop table if exists Elections;
/*
I have created just one table for the whole database. This way there is not redundant value stored as foreign key
Year is the primary key for the table

I have columns for storing election results for each state. The name of the states are included in column names and it would help in searching in Q3b

We should create index for the year so as to speed up the searching in Q3(a)
But I am not creating this index because year is Primary Key and primary key is already indexed

After the creation of the table, I have created an index using 3 columns year, candidate_d and candidate_r
*/
create table Elections(

year char(4) PRIMARY KEY,
candidate_d varchar(100),
candidate_r varchar(100),

AK_electoral_d int DEFAULT 0,
AK_electoral_r int DEFAULT 0,
AK_popular_d int DEFAULT 0,
AK_popular_r int DEFAULT 0,

AL_electoral_d int DEFAULT 0,
AL_electoral_r int DEFAULT 0,
AL_popular_d int DEFAULT 0,
AL_popular_r int DEFAULT 0,

AR_electoral_d int DEFAULT 0,
AR_electoral_r int DEFAULT 0,
AR_popular_d int DEFAULT 0,
AR_popular_r int DEFAULT 0,

AZ_electoral_d int DEFAULT 0,
AZ_electoral_r int DEFAULT 0,
AZ_popular_d int DEFAULT 0,
AZ_popular_r int DEFAULT 0,

CA_electoral_d int DEFAULT 0,
CA_electoral_r int DEFAULT 0,
CA_popular_d int DEFAULT 0,
CA_popular_r int DEFAULT 0,

CO_electoral_d int DEFAULT 0,
CO_electoral_r int DEFAULT 0,
CO_popular_d int DEFAULT 0,
CO_popular_r int DEFAULT 0,

CT_electoral_d int DEFAULT 0,
CT_electoral_r int DEFAULT 0,
CT_popular_d int DEFAULT 0,
CT_popular_r int DEFAULT 0,

DC_electoral_d int DEFAULT 0,
DC_electoral_r int DEFAULT 0,
DC_popular_d int DEFAULT 0,
DC_popular_r int DEFAULT 0,

DE_electoral_d int DEFAULT 0,
DE_electoral_r int DEFAULT 0,
DE_popular_d int DEFAULT 0,
DE_popular_r int DEFAULT 0,


FL_electoral_d int DEFAULT 0,
FL_electoral_r int DEFAULT 0,
FL_popular_d int DEFAULT 0,
FL_popular_r int DEFAULT 0,

GA_electoral_d int DEFAULT 0,
GA_electoral_r int DEFAULT 0,
GA_popular_d int DEFAULT 0,
GA_popular_r int DEFAULT 0,

HI_electoral_d int DEFAULT 0,
HI_electoral_r int DEFAULT 0,
HI_popular_d int DEFAULT 0,
HI_popular_r int DEFAULT 0,

IA_electoral_d int DEFAULT 0,
IA_electoral_r int DEFAULT 0,
IA_popular_d int DEFAULT 0,
IA_popular_r int DEFAULT 0,

ID_electoral_d int DEFAULT 0,
ID_electoral_r int DEFAULT 0,
ID_popular_d int DEFAULT 0,
ID_popular_r int DEFAULT 0,

IL_electoral_d int DEFAULT 0,
IL_electoral_r int DEFAULT 0,
IL_popular_d int DEFAULT 0,
IL_popular_r int DEFAULT 0,

IN_electoral_d int DEFAULT 0,
IN_electoral_r int DEFAULT 0,
IN_popular_d int DEFAULT 0,
IN_popular_r int DEFAULT 0,

KS_electoral_d int DEFAULT 0,
KS_electoral_r int DEFAULT 0,
KS_popular_d int DEFAULT 0,
KS_popular_r int DEFAULT 0,

KY_electoral_d int DEFAULT 0,
KY_electoral_r int DEFAULT 0,
KY_popular_d int DEFAULT 0,
KY_popular_r int DEFAULT 0,

LA_electoral_d int DEFAULT 0,
LA_electoral_r int DEFAULT 0,
LA_popular_d int DEFAULT 0,
LA_popular_r int DEFAULT 0,


MA_electoral_d int DEFAULT 0,
MA_electoral_r int DEFAULT 0,
MA_popular_d int DEFAULT 0,
MA_popular_r int DEFAULT 0,

MD_electoral_d int DEFAULT 0,
MD_electoral_r int DEFAULT 0,
MD_popular_d int DEFAULT 0,
MD_popular_r int DEFAULT 0,

ME_electoral_d int DEFAULT 0,
ME_electoral_r int DEFAULT 0,
ME_popular_d int DEFAULT 0,
ME_popular_r int DEFAULT 0,

MI_electoral_d int DEFAULT 0,
MI_electoral_r int DEFAULT 0,
MI_popular_d int DEFAULT 0,
MI_popular_r int DEFAULT 0,

MN_electoral_d int DEFAULT 0,
MN_electoral_r int DEFAULT 0,
MN_popular_d int DEFAULT 0,
MN_popular_r int DEFAULT 0,

MO_electoral_d int DEFAULT 0,
MO_electoral_r int DEFAULT 0,
MO_popular_d int DEFAULT 0,
MO_popular_r int DEFAULT 0,

MS_electoral_d int DEFAULT 0,
MS_electoral_r int DEFAULT 0,
MS_popular_d int DEFAULT 0,
MS_popular_r int DEFAULT 0,

MT_electoral_d int DEFAULT 0,
MT_electoral_r int DEFAULT 0,
MT_popular_d int DEFAULT 0,
MT_popular_r int DEFAULT 0,

NC_electoral_d int DEFAULT 0,
NC_electoral_r int DEFAULT 0,
NC_popular_d int DEFAULT 0,
NC_popular_r int DEFAULT 0,

ND_electoral_d int DEFAULT 0,
ND_electoral_r int DEFAULT 0,
ND_popular_d int DEFAULT 0,
ND_popular_r int DEFAULT 0,

NE_electoral_d int DEFAULT 0,
NE_electoral_r int DEFAULT 0,
NE_popular_d int DEFAULT 0,
NE_popular_r int DEFAULT 0,

NH_electoral_d int DEFAULT 0,
NH_electoral_r int DEFAULT 0,
NH_popular_d int DEFAULT 0,
NH_popular_r int DEFAULT 0,

NJ_electoral_d int DEFAULT 0,
NJ_electoral_r int DEFAULT 0,
NJ_popular_d int DEFAULT 0,
NJ_popular_r int DEFAULT 0,

NM_electoral_d int DEFAULT 0,
NM_electoral_r int DEFAULT 0,
NM_popular_d int DEFAULT 0,
NM_popular_r int DEFAULT 0,

NV_electoral_d int DEFAULT 0,
NV_electoral_r int DEFAULT 0,
NV_popular_d int DEFAULT 0,
NV_popular_r int DEFAULT 0,


NY_electoral_d int DEFAULT 0,
NY_electoral_r int DEFAULT 0,
NY_popular_d int DEFAULT 0,
NY_popular_r int DEFAULT 0,

OH_electoral_d int DEFAULT 0,
OH_electoral_r int DEFAULT 0,
OH_popular_d int DEFAULT 0,
OH_popular_r int DEFAULT 0,

OK_electoral_d int DEFAULT 0,
OK_electoral_r int DEFAULT 0,
OK_popular_d int DEFAULT 0,
OK_popular_r int DEFAULT 0,

OR_electoral_d int DEFAULT 0,
OR_electoral_r int DEFAULT 0,
OR_popular_d int DEFAULT 0,
OR_popular_r int DEFAULT 0,

PA_electoral_d int DEFAULT 0,
PA_electoral_r int DEFAULT 0,
PA_popular_d int DEFAULT 0,
PA_popular_r int DEFAULT 0,

RI_electoral_d int DEFAULT 0,
RI_electoral_r int DEFAULT 0,
RI_popular_d int DEFAULT 0,
RI_popular_r int DEFAULT 0,

SC_electoral_d int DEFAULT 0,
SC_electoral_r int DEFAULT 0,
SC_popular_d int DEFAULT 0,
SC_popular_r int DEFAULT 0,

SD_electoral_d int DEFAULT 0,
SD_electoral_r int DEFAULT 0,
SD_popular_d int DEFAULT 0,
SD_popular_r int DEFAULT 0,

TN_electoral_d int DEFAULT 0,
TN_electoral_r int DEFAULT 0,
TN_popular_d int DEFAULT 0,
TN_popular_r int DEFAULT 0,

TX_electoral_d int DEFAULT 0,
TX_electoral_r int DEFAULT 0,
TX_popular_d int DEFAULT 0,
TX_popular_r int DEFAULT 0,

UT_electoral_d int DEFAULT 0,
UT_electoral_r int DEFAULT 0,
UT_popular_d int DEFAULT 0,
UT_popular_r int DEFAULT 0,

VA_electoral_d int DEFAULT 0,
VA_electoral_r int DEFAULT 0,
VA_popular_d int DEFAULT 0,
VA_popular_r int DEFAULT 0,

VT_electoral_d int DEFAULT 0,
VT_electoral_r int DEFAULT 0,
VT_popular_d int DEFAULT 0,
VT_popular_r int DEFAULT 0,

WA_electoral_d int DEFAULT 0,
WA_electoral_r int DEFAULT 0,
WA_popular_d int DEFAULT 0,
WA_popular_r int DEFAULT 0,

WI_electoral_d int DEFAULT 0,
WI_electoral_r int DEFAULT 0,
WI_popular_d int DEFAULT 0,
WI_popular_r int DEFAULT 0,

WV_electoral_d int DEFAULT 0,
WV_electoral_r int DEFAULT 0,
WV_popular_d int DEFAULT 0,
WV_popular_r int DEFAULT 0,

WY_electoral_d int DEFAULT 0,
WY_electoral_r int DEFAULT 0,
WY_popular_d int DEFAULT 0,
WY_popular_r int DEFAULT 0

);

ALTER TABLE Elections ADD INDEX search(year,candidate_d, candidate_r);
