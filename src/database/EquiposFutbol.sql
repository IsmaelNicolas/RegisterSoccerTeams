/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     10/26/2022 11:05:06 PM                       */
/*==============================================================*/


drop index CATEGORY_PK;

drop table CATEGORY;

drop index PLAYERTEAM_FK;

drop index PLAYER_PK;

drop table PLAYER;

drop index TEAMCATEGORY_FK;

drop index TEAM_PK;

drop table TEAM;

/*==============================================================*/
/* Table: CATEGORY                                              */
/*==============================================================*/
create table CATEGORY (
   CATEGORYCODE         UUID             	DEFAULT gen_random_uuid() UNIQUE,  
   CATEGORYNAME         VARCHAR(16)         not null UNIQUE,
   CATEGORYMINAGE       INT2                not null,
   CATEGORYMAXAGE       INT2                null,
   constraint PK_CATEGORY primary key (CATEGORYCODE)
);

/*==============================================================*/
/* Index: CATEGORY_PK                                           */
/*==============================================================*/
create unique index CATEGORY_PK on CATEGORY (
CATEGORYCODE
);

/*==============================================================*/
/* Table: PLAYER                                                */
/*==============================================================*/
create table PLAYER (
   PLAYERCODE           UUID             DEFAULT gen_random_uuid(),
   CATEGORYCODE         UUID             DEFAULT gen_random_uuid(),
   TEAMCODE             UUID             DEFAULT gen_random_uuid(),
   PLAYERNAME           VARCHAR(32)          not null UNIQUE,
   PLAYERNUMBER         INT2                 not null UNIQUE,
   PLAYERAGE            INT2                 not null,
   PLAYERPOSSITION      CHAR(2)              null
      constraint CKC_PLAYERPOSSITION_PLAYER check (PLAYERPOSSITION is null or (PLAYERPOSSITION in ('A','DF','DC','LB','LD','LI','MF','CD') and PLAYERPOSSITION = upper(PLAYERPOSSITION))),
   constraint PK_PLAYER primary key (PLAYERCODE)
);

/*==============================================================*/
/* Index: PLAYER_PK                                             */
/*==============================================================*/
create unique index PLAYER_PK on PLAYER (
PLAYERCODE
);

/*==============================================================*/
/* Index: PLAYERTEAM_FK                                         */
/*==============================================================*/
create  index PLAYERTEAM_FK on PLAYER (
CATEGORYCODE,
TEAMCODE
);

/*==============================================================*/
/* Table: TEAM                                                  */
/*==============================================================*/
create table TEAM (
   CATEGORYCODE         UUID             DEFAULT gen_random_uuid(),
   TEAMCODE             UUID             DEFAULT gen_random_uuid(),
   TEAMNAME             VARCHAR(16)          not null UNIQUE,
   TEAMCOACH            VARCHAR(16)          not null UNIQUE,
   constraint PK_TEAM primary key (CATEGORYCODE, TEAMCODE)
);

/*==============================================================*/
/* Index: TEAM_PK                                               */
/*==============================================================*/
create unique index TEAM_PK on TEAM (
CATEGORYCODE,
TEAMCODE
);

/*==============================================================*/
/* Index: TEAMCATEGORY_FK                                       */
/*==============================================================*/
create  index TEAMCATEGORY_FK on TEAM (
CATEGORYCODE
);

alter table PLAYER
   add constraint FK_PLAYER_PLAYERTEA_TEAM foreign key (CATEGORYCODE, TEAMCODE)
      references TEAM (CATEGORYCODE, TEAMCODE)
      on delete restrict on update restrict;

alter table TEAM
   add constraint FK_TEAM_TEAMCATEG_CATEGORY foreign key (CATEGORYCODE)
      references CATEGORY (CATEGORYCODE)
      on delete restrict on update restrict;

