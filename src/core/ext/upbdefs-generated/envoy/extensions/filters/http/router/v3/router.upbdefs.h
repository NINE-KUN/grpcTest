/* This file was generated by upbc (the upb compiler) from the input
 * file:
 *
 *     envoy/extensions/filters/http/router/v3/router.proto
 *
 * Do not edit -- your changes will be discarded when the file is
 * regenerated. */

#ifndef ENVOY_EXTENSIONS_FILTERS_HTTP_ROUTER_V3_ROUTER_PROTO_UPBDEFS_H_
#define ENVOY_EXTENSIONS_FILTERS_HTTP_ROUTER_V3_ROUTER_PROTO_UPBDEFS_H_

#include "upb/reflection/def.h"
#include "upb/reflection/def_pool_internal.h"
#include "upb/port/def.inc"
#ifdef __cplusplus
extern "C" {
#endif

#include "upb/reflection/def.h"

#include "upb/port/def.inc"

extern _upb_DefPool_Init envoy_extensions_filters_http_router_v3_router_proto_upbdefinit;

UPB_INLINE const upb_MessageDef *envoy_extensions_filters_http_router_v3_Router_getmsgdef(upb_DefPool *s) {
  _upb_DefPool_LoadDefInit(s, &envoy_extensions_filters_http_router_v3_router_proto_upbdefinit);
  return upb_DefPool_FindMessageByName(s, "envoy.extensions.filters.http.router.v3.Router");
}

UPB_INLINE const upb_MessageDef *envoy_extensions_filters_http_router_v3_Router_UpstreamAccessLogOptions_getmsgdef(upb_DefPool *s) {
  _upb_DefPool_LoadDefInit(s, &envoy_extensions_filters_http_router_v3_router_proto_upbdefinit);
  return upb_DefPool_FindMessageByName(s, "envoy.extensions.filters.http.router.v3.Router.UpstreamAccessLogOptions");
}

#ifdef __cplusplus
}  /* extern "C" */
#endif

#include "upb/port/undef.inc"

#endif  /* ENVOY_EXTENSIONS_FILTERS_HTTP_ROUTER_V3_ROUTER_PROTO_UPBDEFS_H_ */
