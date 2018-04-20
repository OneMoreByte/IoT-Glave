#ifndef CONFIGG
#define CONFIGG
#include <string>


std::class config
{
  public:
    config(std::string title, int request);

    private:
      std::string buttonTitle;
      int requestType;
};

#endif
