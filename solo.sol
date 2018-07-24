pragma solidity ^0.4.20;

contract Mytoken{
    mapping(address => uint256) public balanceOf;
    
    constructor (uint256 initSupply) public{
        balanceOf[msg.sender] = initSupply;
        
    }
    function transfer(address _to,uint256 _value)public{
        require(balanceOf[msg.sender] >= _value);
        require(balanceOf[_to] + _value  >= balanceOf[_to]) ;
        balanceOf[msg.sender] = balanceOf[msg.sender] -= _value;
        balanceOf[_to] = balanceOf[_to] += _value;
        
    }
}