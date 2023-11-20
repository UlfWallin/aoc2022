const ROUNDS = 10000;
const fs = require('fs');
const text = fs.readFileSync('input.txt', 'utf8');
const monkeys = deserializeMonkeyRules(text);
const allDivs = monkeys.reduce((acc, curr) => acc * curr.test, 1);

console.log(monkeys);

for (let round = 1; round <= ROUNDS; round++) {
    for (const monkey of monkeys) {
        turn(monkey);
    }
}

function turn(monkey) {
    while(monkey.items.length > 0) {
        let item = monkey.items.shift();
        
        const operation = monkey.operation.replaceAll('old', item);
        const tokens = operation.split(' ');
        let newValue = 0;
        if (tokens[3] === '+') {
            newValue = parseInt(tokens[2]) + parseInt(tokens[4]);
        } else {
            newValue = parseInt(tokens[2]) * parseInt(tokens[4]);
        }
        monkey.inspections++;
        

        newValue = newValue % allDivs;
        if (newValue % monkey.test === 0) {
            monkeys[monkey.nextMonkey.pass].items.push(newValue);
        } else {
            monkeys[monkey.nextMonkey.fail].items.push(newValue);
        }
    }
}

monkeys.forEach(m => console.log(m.inspections));
monkeys.sort((a, b) => b.inspections - a.inspections);
const result = monkeys[0].inspections * monkeys[1].inspections;

console.log(result);

function deserializeMonkeyRules(text) {
    const monkeys = [];
    let currentMonkeyId = 0;

    for (const line of text.split('\n')) {
        if (line.startsWith('Monkey ')) {
            const monkeyId = parseInt(line.split(' ')[1]);
            monkeys.push({
                items: [],
                operation: null,
                test: null,
                nextMonkey: {
                    pass: null,
                    fail: null
                },
                inspections: 0
            });
            currentMonkeyId = monkeyId;
        } else if (line.trim().startsWith('Starting items:')) {
            const startingItems = line.split(':')[1].split(', ')
            monkeys[currentMonkeyId].items = startingItems.map((n) => parseInt(n));;
        } else if (line.trim().startsWith('Operation:')) {
            const operationString = line.split(': ')[1];
            monkeys[currentMonkeyId].operation = operationString;
        } else if (line.trim().startsWith('Test:')) {
            const testString = line.split(': ')[1];
            monkeys[currentMonkeyId].test = parseInt(testString.split(' ').pop());
        } else if (line.trim().startsWith('If true:')) {
            const nextMonkeyId = parseInt(line.split(' ').splice(-1));
            monkeys[currentMonkeyId].nextMonkey.pass = nextMonkeyId;
        } else if (line.trim().startsWith('If false:')) {
            const nextMonkeyId = parseInt(line.split(' ').splice(-1));
            monkeys[currentMonkeyId].nextMonkey.fail = nextMonkeyId;
        }
    }
    return monkeys;
}