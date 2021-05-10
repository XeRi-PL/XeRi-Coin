#ifndef BR_BEARSSL_HASH_H__
#define BR_BEARSSL_HASH_H__

#include <stddef.h>
#include <stdint.h>
#include <string.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef struct br_hash_class_ br_hash_class;
struct br_hash_class_ {

	size_t context_size;

	uint32_t desc;

	void (*init)(const br_hash_class **ctx);

	void (*update)(const br_hash_class **ctx, const void *data, size_t len);

	void (*out)(const br_hash_class *const *ctx, void *dst);


	uint64_t (*state)(const br_hash_class *const *ctx, void *dst);


	void (*set_state)(const br_hash_class **ctx,
		const void *stb, uint64_t count);
};

#ifndef BR_DOXYGEN_IGNORE
#define BR_HASHDESC_ID(id)           ((uint32_t)(id) << BR_HASHDESC_ID_OFF)
#define BR_HASHDESC_ID_OFF           0
#define BR_HASHDESC_ID_MASK          0xFF

#define BR_HASHDESC_OUT(size)        ((uint32_t)(size) << BR_HASHDESC_OUT_OFF)
#define BR_HASHDESC_OUT_OFF          8
#define BR_HASHDESC_OUT_MASK         0x7F

#define BR_HASHDESC_STATE(size)      ((uint32_t)(size) << BR_HASHDESC_STATE_OFF)
#define BR_HASHDESC_STATE_OFF        15
#define BR_HASHDESC_STATE_MASK       0xFF

#define BR_HASHDESC_LBLEN(ls)        ((uint32_t)(ls) << BR_HASHDESC_LBLEN_OFF)
#define BR_HASHDESC_LBLEN_OFF        23
#define BR_HASHDESC_LBLEN_MASK       0x0F

#define BR_HASHDESC_MD_PADDING       ((uint32_t)1 << 28)
#define BR_HASHDESC_MD_PADDING_128   ((uint32_t)1 << 29)
#define BR_HASHDESC_MD_PADDING_BE    ((uint32_t)1 << 30)
#endif

#define br_md5_ID     1

#define br_md5_SIZE   16

extern const br_hash_class br_md5_vtable;

typedef struct {

	const br_hash_class *vtable;
#ifndef BR_DOXYGEN_IGNORE
	unsigned char buf[64];
	uint64_t count;
	uint32_t val[4];
#endif
} br_md5_context;

void br_md5_init(br_md5_context *ctx);

void br_md5_update(br_md5_context *ctx, const void *data, size_t len);

void br_md5_out(const br_md5_context *ctx, void *out);

uint64_t br_md5_state(const br_md5_context *ctx, void *out);

void br_md5_set_state(br_md5_context *ctx, const void *stb, uint64_t count);

#define br_sha1_ID     2


#define br_sha1_SIZE   20


extern const br_hash_class br_sha1_vtable;


typedef struct {

	const br_hash_class *vtable;
#ifndef BR_DOXYGEN_IGNORE
	unsigned char buf[64];
	uint64_t count;
	uint32_t val[5];
#endif
} br_sha1_context;


void br_sha1_init(br_sha1_context *ctx);


void br_sha1_update(br_sha1_context *ctx, const void *data, size_t len);


void br_sha1_out(const br_sha1_context *ctx, void *out);


uint64_t br_sha1_state(const br_sha1_context *ctx, void *out);
 void br_sha1_set_state(br_sha1_context *ctx, const void *stb, uint64_t count);


#define br_sha224_ID     3

#define br_sha224_SIZE   28

extern const br_hash_class br_sha224_vtable;

typedef struct {

	const br_hash_class *vtable;
#ifndef BR_DOXYGEN_IGNORE
	unsigned char buf[64];
	uint64_t count;
	uint32_t val[8];
#endif
} br_sha224_context;

void br_sha224_init(br_sha224_context *ctx);

void br_sha224_update(br_sha224_context *ctx, const void *data, size_t len);

void br_sha224_out(const br_sha224_context *ctx, void *out);

uint64_t br_sha224_state(const br_sha224_context *ctx, void *out);

void br_sha224_set_state(br_sha224_context *ctx,
	const void *stb, uint64_t count);

#define br_sha256_ID     4

#define br_sha256_SIZE   32


extern const br_hash_class br_sha256_vtable;

#ifdef BR_DOXYGEN_IGNORE

typedef struct {

	const br_hash_class *vtable;
} br_sha256_context;
#else
typedef br_sha224_context br_sha256_context;
#endif

void br_sha256_init(br_sha256_context *ctx);

#ifdef BR_DOXYGEN_IGNORE

void br_sha256_update(br_sha256_context *ctx, const void *data, size_t len);
#else
#define br_sha256_update      br_sha224_update
#endif


void br_sha256_out(const br_sha256_context *ctx, void *out);

#ifdef BR_DOXYGEN_IGNORE

uint64_t br_sha256_state(const br_sha256_context *ctx, void *out);
#else
#define br_sha256_state       br_sha224_state
#endif

#ifdef BR_DOXYGEN_IGNORE

void br_sha256_set_state(br_sha256_context *ctx,
	const void *stb, uint64_t count);
#else
#define br_sha256_set_state   br_sha224_set_state
#endif

#define br_sha384_ID     5

#define br_sha384_SIZE   48


extern const br_hash_class br_sha384_vtable;


typedef struct {

	const br_hash_class *vtable;
#ifndef BR_DOXYGEN_IGNORE
	unsigned char buf[128];
	uint64_t count;
	uint64_t val[8];
#endif
} br_sha384_context;

void br_sha384_init(br_sha384_context *ctx);

void br_sha384_update(br_sha384_context *ctx, const void *data, size_t len);


void br_sha384_out(const br_sha384_context *ctx, void *out);


uint64_t br_sha384_state(const br_sha384_context *ctx, void *out);


void br_sha384_set_state(br_sha384_context *ctx,
	const void *stb, uint64_t count);

#define br_sha512_ID     6

#define br_sha512_SIZE   64


extern const br_hash_class br_sha512_vtable;

#ifdef BR_DOXYGEN_IGNORE

typedef struct {

	const br_hash_class *vtable;
} br_sha512_context;
#else
typedef br_sha384_context br_sha512_context;
#endif


void br_sha512_init(br_sha512_context *ctx);

#ifdef BR_DOXYGEN_IGNORE

void br_sha512_update(br_sha512_context *ctx, const void *data, size_t len);
#else
#define br_sha512_update   br_sha384_update
#endif


void br_sha512_out(const br_sha512_context *ctx, void *out);

#ifdef BR_DOXYGEN_IGNORE

uint64_t br_sha512_state(const br_sha512_context *ctx, void *out);
#else
#define br_sha512_state   br_sha384_state
#endif

#ifdef BR_DOXYGEN_IGNORE

void br_sha512_set_state(br_sha512_context *ctx,
	const void *stb, uint64_t count);
#else
#define br_sha512_set_state   br_sha384_set_state
#endif


#define br_md5sha1_ID     0


#define br_md5sha1_SIZE   36


extern const br_hash_class br_md5sha1_vtable;


typedef struct {

	const br_hash_class *vtable;
#ifndef BR_DOXYGEN_IGNORE
	unsigned char buf[64];
	uint64_t count;
	uint32_t val_md5[4];
	uint32_t val_sha1[5];
#endif
} br_md5sha1_context;


void br_md5sha1_init(br_md5sha1_context *ctx);

void br_md5sha1_update(br_md5sha1_context *ctx, const void *data, size_t len);


void br_md5sha1_out(const br_md5sha1_context *ctx, void *out);


uint64_t br_md5sha1_state(const br_md5sha1_context *ctx, void *out);


void br_md5sha1_set_state(br_md5sha1_context *ctx,
	const void *stb, uint64_t count);

typedef union {
	const br_hash_class *vtable;
	br_md5_context md5;
	br_sha1_context sha1;
	br_sha224_context sha224;
	br_sha256_context sha256;
	br_sha384_context sha384;
	br_sha512_context sha512;
	br_md5sha1_context md5sha1;
} br_hash_compat_context;


typedef struct {
#ifndef BR_DOXYGEN_IGNORE
	unsigned char buf[128];
	uint64_t count;
	uint32_t val_32[25];
	uint64_t val_64[16];
	const br_hash_class *impl[6];
#endif
} br_multihash_context;


void br_multihash_zero(br_multihash_context *ctx);


static inline void
br_multihash_setimpl(br_multihash_context *ctx,
	int id, const br_hash_class *impl)
{

	ctx->impl[id - 1] = impl;
}


static inline const br_hash_class *
br_multihash_getimpl(const br_multihash_context *ctx, int id)
{
	return ctx->impl[id - 1];
}


void br_multihash_init(br_multihash_context *ctx);


void br_multihash_update(br_multihash_context *ctx,
	const void *data, size_t len);


size_t br_multihash_out(const br_multihash_context *ctx, int id, void *dst);


typedef void (*br_ghash)(void *y, const void *h, const void *data, size_t len);

void br_ghash_ctmul(void *y, const void *h, const void *data, size_t len);


void br_ghash_ctmul32(void *y, const void *h, const void *data, size_t len);


void br_ghash_ctmul64(void *y, const void *h, const void *data, size_t len);

void br_ghash_pclmul(void *y, const void *h, const void *data, size_t len);


br_ghash br_ghash_pclmul_get(void);


void br_ghash_pwr8(void *y, const void *h, const void *data, size_t len);


br_ghash br_ghash_pwr8_get(void);

#ifdef __cplusplus
}
#endif

#endif
