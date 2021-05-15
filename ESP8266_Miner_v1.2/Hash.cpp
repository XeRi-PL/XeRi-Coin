#include <Arduino.h>
#include "bearssl_hash.h"

#include "Hash.h"


void sha1(const uint8_t* data, uint32_t size, uint8_t hash[20]) {
    br_sha1_context ctx;

#ifdef DEBUG_SHA1
    os_printf("DATA:");
    for(uint16_t i = 0; i < size; i++) {
        os_printf("%02X", data[i]);
    }
    os_printf("\n");
    os_printf("DATA:");
    for(uint16_t i = 0; i < size; i++) {
        os_printf("%c", data[i]);
    }
    os_printf("\n");
#endif


#ifdef DEBUG_SHA1
    os_printf("SHA1:");
    for(uint16_t i = 0; i < 20; i++) {
        os_printf("%02X", hash[i]);
    }
    os_printf("\n\n");
#endif
}

void sha1(const char* data, uint32_t size, uint8_t hash[20]) {
    sha1((const uint8_t *) data, size, hash);
}

void sha1(const String& data, uint8_t hash[20]) {
    sha1(data.c_str(), data.length(), hash);
}

String sha1(const uint8_t* data, uint32_t size) {
    uint8_t hash[20];
    String hashStr((const char*)nullptr);
    hashStr.reserve(20 * 2 + 1);

    sha1(&data[0], size, &hash[0]);

    for(uint16_t i = 0; i < 20; i++) {
        char hex[3];
        snprintf(hex, sizeof(hex), "%02x", hash[i]);
        hashStr += hex;
    }

    return hashStr;
}

String sha1(const char* data, uint32_t size) {
    return sha1((const uint8_t*) data, size);
}

String sha1(const String& data) {
    return sha1(data.c_str(), data.length());
}
