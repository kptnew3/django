var Status = 0;

while (Status < 11) {


  if (Status === 4)
  {
    console.log("Status is " + Status + ". Hence Breaking.")
    break;
  }

  console.log(typeof(Status));
  Status = Status+1;
}

console.log(typeof(Status));
console.log(Status);


for (var i = 0; i < 10; i++) {
  if (i === 7 ){
    console.log("i is 7 so would continue")
    continue;
  }
  console.log("Printing i " + i)
  if (i === 9 )
  {
    console.log("i is 9 so breaking.")
    console.log( i );
    break;
  }
}

var word = "ABCDEFGHIJK";

for (var i = 0; i < word.length; i++) {
 console.log(word[i]);
}

//Test Arrays

var roster =[];

function addStudent(roster,name)
{
  roster.push(name);
}

addStudent(roster,"Gagan");

addStudent(roster,"Anhad");
console.log(roster);

function removeStudent(roster)
{
  var roster = ['pooja','dhun'];
  roster.pop();
  this.roster.pop();
  console.log("roster of inside function " +roster);
  console.log("roster outside function " + this.roster);
}


removeStudent(roster);

console.log("Array after popping up the student" + roster);



while (prompt("Do you want to work on roster") === 'y')
{
  var optionStudent = prompt("Enter 1 for Adding the Student, 2 for Removing the student, 3 for Printing the roster");
  if (optionStudent === "1")
  {
    console.log("User wants to add the new student");
    this.roster.push(prompt("Enter the Student Name"));
    console.log("student added");
  }
  else if (optionStudent === "2")
  {
    console.log("User wants to pop the new student");
    this.roster.pop();
    console.log("student popped");
    console.log(this.roster);
  }
  else if (optionStudent === "3") {
    console.log("User wants to quit");
    break;
  }
}
console.log("loop broken");
console.log("roster is " + roster);
printRoster();

function printRoster()
{
  for (student of this.roster)
  {
    console.log(student);
  }
}

for (var arrvariable in this.roster) {
  console.log(this.roster[arrvariable]);
  }
