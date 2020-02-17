let arr = [];
let n = 50;
let maxHeight = 560;

let fillColor = document.querySelector("#color11");
let borderColor = document.querySelector("#color12");
let backgroundC = document.querySelector("#color13");

let rectColor = fillColor.value;
let rectBorderColor = borderColor.value;
let backgroundColor = backgroundC.value;

var audio = new Audio("n.mp3");

function isSorted(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      return false;
    }
  }
  return true;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function swap(arr, i, j) {
  let temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
  // audio.play();
  await sleep(50);
}

const generateArray = n => {
  let arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(Math.round(Math.random() * maxHeight));
  }
  return arr;
};

// randomArr = [200, 100, 200, 100, 200, 100, 200, 100, 200];
// console.log("Unsorted array..");
// console.log(randomArr);
// console.log("Sorting process started\n\n");

async function aSort(arr) {
  const len = arr.length;
  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      if (arr[i] > arr[j]) {
        // console.log(arr[i] + " is greater than " + arr[j] + " time to swap it");
        await swap(arr, i, j);
        // console.log("SWAPPING => " + arr[i] + " with " + arr[j]);
        // console.log(arr);

        // audio.pause();
      } else {
        // console.log(arr[i] + " is smaller than " + arr[j] + " so it's fine.");
      }
    }
  }
}
let randomArr;
function setup() {
  createCanvas(windowWidth, windowHeight);
  maxHeight = height;
  background(0);
  randomArr = generateArray(n);
}

function update1() {
  rectColor = fillColor.value;
}
function update2() {
  rectBorderColor = borderColor.value;
}

function update3() {
  backgroundColor = backgroundC.value;
  randomArr = generateArray(n);
  aSort(randomArr);
}
function draw() {
  background(backgroundColor);
  for (let i = 0; i < randomArr.length; i++) {
    fill(rectColor);
    stroke(rectBorderColor);
    rect(i * (width / n), height, width / n, -randomArr[i]);
  }
}

fillColor.addEventListener("change", update1, false);
borderColor.addEventListener("change", update2, false);
backgroundC.addEventListener("change", update3, false);
