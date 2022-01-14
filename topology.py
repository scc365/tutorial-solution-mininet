from mininet.topo import Topo
from mininet.link import TCLink

class TutorialTopology( Topo ):

  def build( self ):

    # add switches
    for s in range(0, 2):
      self.addSwitch( "s{}".format(s+1) )

    # add hosts to s1
    for h in range(0, 5):
      host = self.addHost( "h{}".format(h+1) )
      self.addLink( host, 's1' )

    # add hosts to s2
    for h in range(0, 5):
      host = self.addHost( "h{}".format(h+6) )
      self.addLink( host, 's2' )

    # link the switches
    self.addLink( 's1', 's2', cls=TCLink, bw=50, delay='30ms', loss=10 )

# the topologies accessible to the mn tool's `--topo` flag
# note: if using the Dockerfile, this must be the same as in the Dockerfile
topos = { 'tutorialTopology': ( lambda: TutorialTopology() ) }
