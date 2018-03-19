#ifndef CONFIGG
#define CONFIGG
#include <string>


class config
{
  public:
    config(std::string title, int request);

    private:
      std::string buttonTitle;
      int requestType;
};

#endif
