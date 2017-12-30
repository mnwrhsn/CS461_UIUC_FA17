#!/usr/bin/python2.7
import dpkt
import sys
import socket


def main():
    if (len(sys.argv) < 2):
        print "error: need argument"
        sys.exit(1)

    filename = sys.argv[1]
    #filename = "lbl-internal.20041004-1305.port002.dump.anon.pcap"
    print "input filename: " + filename

    f = open(filename)
    pcap = dpkt.pcap.Reader(f)

    #count = 0

    save_syn = {}
    save_syn_ack ={}



    for ts, buf in pcap:

        try:
            eth = dpkt.ethernet.Ethernet(buf)

        except dpkt.UnpackError or AttributeError:
            continue


        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
            ip = eth.data

            if ip.p == dpkt.ip.IP_PROTO_TCP:
                tcp = ip.data

                src = socket.inet_ntoa(ip.src)
                dst = socket.inet_ntoa(ip.dst)

                # print "src: " + src + "dst: " + dst

                if tcp.flags & dpkt.tcp.TH_SYN != 0:

                    if tcp.flags & dpkt.tcp.TH_ACK != 0:

                        # print "in if!"

                        if dst not in save_syn_ack:
                            save_syn_ack[dst] = 0
                        save_syn_ack[dst] += 1

                    else:
                        if src not in save_syn:
                            save_syn[src] = 0
                        save_syn[src] += 1

    for address in save_syn:

        if address not in save_syn_ack:
            # print "not here"
            save_syn_ack[address] = 0

        if save_syn[address] > save_syn_ack[address]*3:
            print address

    # print "script finished!"
    sys.exit(0)


if __name__ == '__main__':
    main()
