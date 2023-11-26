/* This file was generated by upbc (the upb compiler) from the input
 * file:
 *
 *     google/protobuf/empty.proto
 *
 * Do not edit -- your changes will be discarded when the file is
 * regenerated. */

#ifndef GOOGLE_PROTOBUF_EMPTY_PROTO_UPB_H_
#define GOOGLE_PROTOBUF_EMPTY_PROTO_UPB_H_

#include "upb/collections/array_internal.h"
#include "upb/collections/map_gencode_util.h"
#include "upb/message/accessors.h"
#include "upb/message/internal.h"
#include "upb/mini_table/enum_internal.h"
#include "upb/wire/decode.h"
#include "upb/wire/decode_fast.h"
#include "upb/wire/encode.h"

// Must be last. 
#include "upb/port/def.inc"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct google_protobuf_Empty google_protobuf_Empty;
extern const upb_MiniTable google_protobuf_Empty_msg_init;



/* google.protobuf.Empty */

UPB_INLINE google_protobuf_Empty* google_protobuf_Empty_new(upb_Arena* arena) {
  return (google_protobuf_Empty*)_upb_Message_New(&google_protobuf_Empty_msg_init, arena);
}
UPB_INLINE google_protobuf_Empty* google_protobuf_Empty_parse(const char* buf, size_t size, upb_Arena* arena) {
  google_protobuf_Empty* ret = google_protobuf_Empty_new(arena);
  if (!ret) return NULL;
  if (upb_Decode(buf, size, ret, &google_protobuf_Empty_msg_init, NULL, 0, arena) != kUpb_DecodeStatus_Ok) {
    return NULL;
  }
  return ret;
}
UPB_INLINE google_protobuf_Empty* google_protobuf_Empty_parse_ex(const char* buf, size_t size,
                           const upb_ExtensionRegistry* extreg,
                           int options, upb_Arena* arena) {
  google_protobuf_Empty* ret = google_protobuf_Empty_new(arena);
  if (!ret) return NULL;
  if (upb_Decode(buf, size, ret, &google_protobuf_Empty_msg_init, extreg, options, arena) !=
      kUpb_DecodeStatus_Ok) {
    return NULL;
  }
  return ret;
}
UPB_INLINE char* google_protobuf_Empty_serialize(const google_protobuf_Empty* msg, upb_Arena* arena, size_t* len) {
  char* ptr;
  (void)upb_Encode(msg, &google_protobuf_Empty_msg_init, 0, arena, &ptr, len);
  return ptr;
}
UPB_INLINE char* google_protobuf_Empty_serialize_ex(const google_protobuf_Empty* msg, int options,
                                 upb_Arena* arena, size_t* len) {
  char* ptr;
  (void)upb_Encode(msg, &google_protobuf_Empty_msg_init, options, arena, &ptr, len);
  return ptr;
}


extern const upb_MiniTableFile google_protobuf_empty_proto_upb_file_layout;

#ifdef __cplusplus
}  /* extern "C" */
#endif

#include "upb/port/undef.inc"

#endif  /* GOOGLE_PROTOBUF_EMPTY_PROTO_UPB_H_ */