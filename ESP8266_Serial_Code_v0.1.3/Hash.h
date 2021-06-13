#ifndef HASH_H_
#define HASH_H_

//#define DEBUG_SHA1

void sha1(const uint8_t* data, uint32_t size, uint8_t hash[20]);
void sha1(const char* data, uint32_t size, uint8_t hash[20]);
void sha1(const String& data, uint8_t hash[20]);

String sha1(const uint8_t* data, uint32_t size);
String sha1(const char* data, uint32_t size);
String sha1(const String& data);

#endif /* HASH_H_ */