#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
#include "/usr/local/cs/cs251/react.h"
#include "State.h"

void _receive_and_send()
{
    // initialization
    _read_event_info_file("event_info");
    if (_just_starting())
        _read_global_mem_from_file("startup_mem");
    else
        _read_global_mem_from_file("begin_mem");

    istringstream iss(_global_mem + State::offset);
    State state(iss);

    // event handling and display
    state.update();
    display(state);

    // write out the end state
    ostringstream oss;
    state.write_to(oss);
    string s = oss.str();
    s.copy(_global_mem + state.offset, s.length());

    _write_global_mem_to_file("end_mem");
    _write_global_yaml_to_file("react.yaml");
    delete[] _global_mem;
}

int main()
{
    _receive_and_send();
}
