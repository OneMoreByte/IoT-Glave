
BINARY = iotgl

BUILDDIR = build
SOURCEDIR = src
HEADERDIR = include

RM = rm -rf
MKDIR = mkdir

CXX = g++

CXXFLAGS = -Wall -g -std=c++17

SOURCES := $(shell find $(SOURCEDIR) -name '*.cpp')

OBJECTS := $(addprefix $(BUILDDIR)/,$(SOURCES:%.cpp=%.o))

all: $(BINARY)


$(BINARY): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(BINARY)

$(BUILDDIR)/%.o: %.cpp
	$(CXX) $(CXXFLAGS) -I$(HEADERDIR) -I$(dir $<) -c $< -o $@


setup:
	$(MKDIR) -p $(BUILDDIR)

clean:
	$(RM) $(BINARY) $(OBJECTS)
