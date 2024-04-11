// Justifull comments

let questions = await (await fetch("/test/questions")).json()

console.log(questions);