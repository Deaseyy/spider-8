function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
}
// Person.prototype = {'xxxx': 1}
Person.prototype.x = 'xxoo';
Person.prototype.name = function() {
  return this.firstName + " " + this.lastName;
};

p = new Person('z', 's', 18, 'xx')
console.log(p.age);
console.log(p.x);
console.log(p.name());
console.log(p.prototype); // undefined
console.log(Person.prototype);