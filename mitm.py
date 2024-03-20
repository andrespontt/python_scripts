from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster

class Addon(object):
    def __init__(self):
        pass

    def request(self, flow):
        # examine request here 
        pass

    def response(self, flow):
        # examine response here
        pass

if __name__ == "__main__":
    opts = options.Options(listen_host='0.0.0.0', listen_port=8080)
    pconf = proxy.config.ProxyConfig(opts)

    m = DumpMaster(None)
    m.server = proxy.server.ProxyServer(pconf)

    a = Addon()
    m.addons.add(a)

    try:
        print('starting mitmproxy')
        m.run()
    except KeyboardInterrupt:
        m.shutdown()
