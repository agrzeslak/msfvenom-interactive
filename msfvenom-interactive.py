"""
-l, --list            <type>     List all modules for [type]. Types are: payloads, encoders, nops, platforms, archs, encrypt, formats, all
-p, --payload         <payload>  Payload to use (--list payloads to list, --list-options for arguments). Specify '-' or STDIN for custom
    --list-options               List --payload <value>'s standard, advanced and evasion options
-f, --format          <format>   Output format (use --list formats to list)
-e, --encoder         <encoder>  The encoder to use (use --list encoders to list)
    --sec-name        <value>    The new section name to use when generating large Windows binaries. Default: random 4-character alpha string
    --smallest                   Generate the smallest possible payload using all available encoders
    --encrypt         <value>    The type of encryption or encoding to apply to the shellcode (use --list encrypt to list)
    --encrypt-key     <value>    A key to be used for --encrypt
    --encrypt-iv      <value>    An initialization vector for --encrypt
-a, --arch            <arch>     The architecture to use for --payload and --encoders (use --list archs to list)
    --platform        <platform> The platform for --payload (use --list platforms to list)
-o, --out             <path>     Save the payload to a file
-b, --bad-chars       <list>     Characters to avoid example: '\x00\xff'
-n, --nopsled         <length>   Prepend a nopsled of [length] size on to the payload
    --pad-nops                   Use nopsled size specified by -n <length> as the total payload size, auto-prepending a nopsled of quantity (nops minus payload length)
-s, --space           <length>   The maximum size of the resulting payload
    --encoder-space   <length>   The maximum size of the encoded payload (defaults to the -s value)
-i, --iterations      <count>    The number of times to encode the payload
-c, --add-code        <path>     Specify an additional win32 shellcode file to include
-x, --template        <path>     Specify a custom executable file to use as a template
-k, --keep                       Preserve the --template behaviour and inject the payload as a new thread
-v, --var-name        <value>    Specify a custom variable name to use for certain output formats
-t, --timeout         <second>   The number of seconds to wait when reading the payload from STDIN (default 30, 0 to disable)
-h, --help                       Show this message
"""

class Config:

    def __main__(self):
        self.clear_params()

    def clear_params(self):
        self.params = {
            'payload':'',
            'payload args':'',
            'format':'',
            'encoder':'',
            'sec name':'',
            'smallest':'',
            'encrypt':'',
            'encrypt key':'',
            'encrypt iv':'',
            'arch':'',
            'platform':'',
            'bad chars':'',
            'nopsled':'',
            'pad nops':'',
            'space':'',
            'encoder space':'',
            'iterations':'',
            'add code':'',
            'template':'',
            'keep':'',
            'var name':'',
            'timeout':''
        }

    def get_params(self):
        return self.params

    def set_params(self, params):
        self.params = params

def print_banner():
    return

def print_payloads():
    return

def ready_to_execute(config):
    if config.get_params[payload] == '':
        return false
    return true

def execute(config):
    params = config.get_params()
    command = 'msfvenom -p {}'.format(params['payload'])
    if params['payload args'] != '':
        command += ' {}'.format(params['payload args'])
    return

"""
Print banner
[mandatory] which payload?
[mandatory] payload args (free text with examples)
screen with list of all optional options, generate to file, generate to stdout or generate to clipboard

- always able to go back
- always able to reset optional options
- ideally just have all mandatory/optional options on same screen, just force mandatory fields to be filled before running
"""