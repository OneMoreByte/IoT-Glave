#ifndef COLORFLX
#define COLORFLX
#include <string>


std::class color
{
  public:
    color(std::string title);

      uint16_t getHue();
      uint16_t getSat();
      uint16_t getBright();
      uint16_t getKelvin();
      std::string getHexEquiv();

      void readConfig(std::string config);
      std::string writeConfig();

    private:
      uint16_t hue;
      uint16_t sat;
      uint16_t bright;
      uint16_t kelvin;

      std::string hexEquiv;

};

#endif
