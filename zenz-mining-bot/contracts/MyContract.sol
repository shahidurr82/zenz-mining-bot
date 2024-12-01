// SPDX-License-Identifier: MIT  
pragma solidity ^0.8.0;  

contract MyContract {  
    string public name;  
    uint public value;  

    constructor(string memory _name, uint _value) {  
        name = _name;  
        value = _value;  
    }  

    function setValue(uint newValue) public {  
        value = newValue;  
    }  

    function getValue() public view returns (uint) {  
        return value;  
    }  
}