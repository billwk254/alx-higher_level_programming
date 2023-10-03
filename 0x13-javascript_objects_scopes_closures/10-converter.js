#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (number === 0) {
      return '0';
    } else if (number < 0) {
      return '-' + exports.converter(base)(-number);
    } else if (number < base) {
      return number.toString(base);
    } else {
      return exports.converter(base)(Math.floor(number / base)) + (number % base).toString(base);
    }
  };
};
