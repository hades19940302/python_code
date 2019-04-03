Contract{
	function transfer(addressto,int amt) {
		address from = msg.sender;
		from.eth = from.eth - amt;
		to.eth = to.eth + amt;	
		// body...
	}
}