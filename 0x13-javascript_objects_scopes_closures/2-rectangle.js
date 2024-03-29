#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || isNaN(w) || isNaN(h) || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
