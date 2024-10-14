// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Flipper {
    bool state;

    constructor() {
        state = true;
    }

    function flip() external {
        state = !state;
    }

    function getState() external view returns (bool) {
        return state;
    }
}
