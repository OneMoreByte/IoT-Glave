#ifndef CONFIGG
#define CONFIGG
#include <String>


class Game
{
  public:
    void config(String title, int request);

    private:
      String buttonTitle;
      int requestType;
};

#endif
