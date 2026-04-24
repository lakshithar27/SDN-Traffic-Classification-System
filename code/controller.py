from pox.core import core
import pox.openflow.libopenflow_01 as of

from classifier import classify_packet

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed
    print("DEBUG PACKET:", repr(packet))
    result = classify_packet(packet)

    print("\n--- Packet Received ---")
    print("Packet:", packet)
    print("Classification:", result)

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.in_port = event.port
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    log.info("Starting POX Traffic Classification Controller...")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)