from mininet.topo import Topo
class MyFirstTopo( Topo ):
	def __init__( self ):
		Topo.__init__( self )

		# Add hosts and switches
		h1 = self.addHost( 'h1' )
		h2 = self.addHost( 'h2' )
		h3 = self.addHost( 'h3' )
		h4 = self.addHost( 'h4' )
		h5 = self.addHost( 'h5' )
		h6 = self.addHost( 'h6' )
		h7 = self.addHost( 'h7' )
		h8 = self.addHost( 'h8' )
		h9 = self.addHost( 'h9' )
		h10 = self.addHost( 'h10' )
		h11 = self.addHost('h11')


		leftSwitch = self.addSwitch( 's1' )
		rightSwitch = self.addSwitch( 's2' )
		
		# Add links
		self.addLink( h1, leftSwitch )
		self.addLink( h2, leftSwitch )
		self.addLink( h3, leftSwitch )
		self.addLink( h4, leftSwitch )
		self.addLink( h5, leftSwitch )

		self.addLink( leftSwitch, rightSwitch )

		self.addLink( rightSwitch, h6 )
		self.addLink( rightSwitch, h7 )
		self.addLink( rightSwitch, h8 )
		self.addLink( rightSwitch, h9 )
		self.addLink( rightSwitch, h10 )
		self.addLink( rightSwitch, h11 )
topos = { 'myfirsttopo': ( lambda: MyFirstTopo() ) }
