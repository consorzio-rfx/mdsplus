#ifndef __SERVERSHR
#define __SERVERSHR

#define ServerNOT_DISPATCHED  0xfe18008
#define ServerINVALID_DEPENDENCY  0xfe18012
#define ServerCANT_HAPPEN  0xfe1801a
#define ServerINVSHOT  0xfe18022
#define ServerNOREPLY  0xfe1802b
#define ServerABORT    0xfe18032
#define ServerPATH_DOWN 0xfe18042

#ifdef CREATE_STS_TEXT
#include        "facility_list.h"

static struct stsText  servershr_stsText[] = {
    STS_TEXT(ServerNOT_DISPATCHED,"action not dispatched, depended on failed action")
   ,STS_TEXT(ServerINVALID_DEPENDENCY,"action dependency cannot be evaluated")
   ,STS_TEXT(ServerCANT_HAPPEN,"action contains circular dependency or depends on action which was not dispatched")
   ,STS_TEXT(ServerINVSHOT,"invalid shot number, cannot dispatch actions in model")
   ,STS_TEXT(ServerNOREPLY,"operation in progress, do not reply to request yet")
   ,STS_TEXT(ServerABORT,"operation was aborted")
   ,STS_TEXT(ServerPATH_DOWN,"connection to server broken or remote server is down")
   };

#endif

extern int ServerAbortServer( char *server, int *flush );
extern int ServerBuildDispatchTable( char *wildcard, char *monitor_name, void **table);
extern int ServerCloseTrees( char *server );
extern int ServerCreatePulse(int efn, char *server, char *tree, int shot,
                        void (*ast)(), void *astprm, int *retstatus, int *netid, void (*link_down_handler)(),void (*before_ast)());
extern int ServerDispatchAction(int efn, char *server, char *tree, int shot, int nid,
                        void (*ast)(), void *astprm, int *retstatus, int *netid, void (*link_down_handler)(),
                        void (*before_ast)());
extern int ServerDispatchClose(void *vtable);
extern int ServerDispatchCommand(int efn, char *server, char *cli, char *command,
                        void (*ast)(), void *astprm, int *retstatus, int *netid, void (*link_down)(), void (*before_ast)());
extern int ServerSendMessage( int efn, int sendast, char *server, MsgType type, int length, char *msg, int *retstatus, 
                         void (*ast)(), void *astparam, void (*before_ast)(), int *netid_return);
extern int ServerSendReply(void *lid,int length,char *reply);
extern int ServerSetLinkDownHandler(void (*handler)());
extern void ServerSetDetailProc(char *(*detail_proc)(int));
extern char *(*ServerGetDetailProc())();
extern int ServerDispatchPhase(int efn, void *vtable, char *phasenam, char *noact_in,
                          int *sync, void (*output_rtn)(), char *monitor);
extern int ServerFailedEssential(void *vtable,int reset);
extern char *ServerFindServers(void **ctx, char *wild_match);
extern int ServerMonitorCheckin(char *server, void (*ast)(), void *astparam, void (*link_down)());
extern int ServerSetLogging( char *server, char *logging_mode );
extern int ServerStartServer( char *server );
extern int ServerStopServer( char *server );

#endif