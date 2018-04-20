#ifndef LIFX
#define LIFX

#include "device.h"
#include "color.h"

std::class lifx : public device
{
  public:

    lifx(std::string config);

    /// Sets color to given color. Returns true if successful
    bool setColor(Color c);

    /// Toggles power setting. Returns true if successful
    bool setPower();

  private:

    bool getPower();
    bool getColor();

    #pragma pack(push, 1)
    typedef struct {
      /* frame */
      uint16_t size;
      uint16_t protocol:12;
      uint8_t  addressable:1;
      uint8_t  tagged:1;
      uint8_t  origin:2;
      uint32_t source;
      /* frame address */
      uint8_t  target[8];
      uint8_t  reserved[6];
      uint8_t  res_required:1;
      uint8_t  ack_required:1;
      uint8_t  :6;
      uint8_t  sequence;
      /* protocol header */
      uint64_t :64;
      uint16_t type;
      uint16_t :16;
      /* variable length payload follows */
    } lx_protocol_header_t;
    #pragma pack(pop)
};

#endif
