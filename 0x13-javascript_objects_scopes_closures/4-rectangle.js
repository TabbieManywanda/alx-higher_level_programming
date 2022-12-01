#!/usr/bin/node

class Rectangle {
  console (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const exes = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(exes);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
}

module.exports = Rectangle;
