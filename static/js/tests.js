let divTests = document.querySelector('div.tests');

let fetch_tests = await fetch("/get_tests")

console.log(fetch_tests);
for (const item of fetch_tests) {
    console.log(item);
}

