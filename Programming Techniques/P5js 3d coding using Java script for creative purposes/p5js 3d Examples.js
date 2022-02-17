// P5.js Sample code for 3d. 

// video source: https://vimeo.com/90312869
let img;
let vid;
let theta = 0;

function setup() {
  createCanvas(710, 400, WEBGL);

  img = loadImage('assets/cat.jpg');
  vid = createVideo(['assets/360video_256crop_v2.mp4']);
  vid.elt.muted = true;
  vid.loop();
  vid.hide();
}

function draw() {
  background(250);
  translate(-220, 0, 0);
  push();
  rotateZ(theta * mouseX * 0.001);
  rotateX(theta * mouseX * 0.001);
  rotateY(theta * mouseX * 0.001);
  //pass image as texture
  texture(vid);
  sphere(150);
  pop();
  translate(440, 0, 0);
  push();
  rotateZ(theta * 0.1);
  rotateX(theta * 0.1);
  rotateY(theta * 0.1);
  texture(img);
  box(100, 100, 100);
  pop();
  theta += 0.05;
}

// 3d Shape Primitives available via P5.js

function setup() {
  createCanvas(710, 400, WEBGL);
}

function draw() {
  background(250);

  translate(-240, -100, 0);
  normalMaterial();
  push();
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  plane(70);
  pop();

  translate(240, 0, 0);
  push();
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  box(70, 70, 70);
  pop();

  translate(240, 0, 0);
  push();
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  cylinder(70, 70);
  pop();

  translate(-240 * 2, 200, 0);
  push();
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  cone(70, 70);
  pop();

  translate(240, 0, 0);
  push();
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  torus(70, 20);
  pop();

  translate(240, 0, 0);
  push();
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  sphere(70);
  pop();
}


// Sine and Cosine in 3D 

function setup() {
    createCanvas(710, 400, WEBGL);
  }
  
  function draw() {
    background(250);
    rotateY(frameCount * 0.01);
  
    for (let j = 0; j < 5; j++) {
      push();
      for (let i = 0; i < 80; i++) {
        translate(
          sin(frameCount * 0.001 + j) * 100,
          sin(frameCount * 0.001 + j) * 100,
          i * 0.1
        );
        rotateZ(frameCount * 0.002);
        push();
        sphere(8, 6, 4);
        pop();
      }
      pop();
    }
  }

// Multiple Lights on 3D objects

function setup() {
    createCanvas(710, 400, WEBGL);
  }
  
  function draw() {
    background(0);
  
    let locX = mouseX - height / 2;
    let locY = mouseY - width / 2;
  
    ambientLight(50);
    directionalLight(255, 0, 0, 0.25, 0.25, 0);
    pointLight(0, 0, 255, locX, locY, 250);
  
    push();
    translate(-width / 4, 0, 0);
    rotateZ(frameCount * 0.02);
    rotateX(frameCount * 0.02);
    specularMaterial(250);
    box(100, 100, 100);
    pop();
  
    translate(width / 4, 0, 0);
    ambientMaterial(250);
    sphere(120, 64);
  }
  
// 3D textures to be imposed on shapes

let img;
function setup() {
  createCanvas(710, 400, WEBGL);
  img = loadImage('assets/cat.jpg');
}

function draw() {
  background(0);

  let locX = mouseX - height / 2;
  let locY = mouseY - width / 2;

  ambientLight(60, 60, 60);
  pointLight(255, 255, 255, locX, locY, 100);

  push();
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  texture(img);
  box(80);
  pop();

  push();
  translate(-width / 4, -height / 4, 0);
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  fill(250, 0, 0);
  torus(80, 20, 64, 64);
  pop();

  push();
  translate(width / 4, -height / 4, 0);
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  normalMaterial();
  torus(80, 20, 64, 64);
  pop();

  push();
  translate(-width / 4, height / 4, 0);
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  ambientMaterial(250);
  torus(80, 20, 64, 64);
  pop();

  push();
  translate(width / 4, height / 4, 0);
  rotateZ(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  specularMaterial(250);
  torus(80, 20, 64, 64);
  pop();
}

// 3D Ray casting in p5.js

const objects = [];
let eyeZ;

function setup() {
  createCanvas(710, 400, WEBGL);

  eyeZ = height / 2 / tan((30 * PI) / 180); // The default distance the camera is away from the origin.

  objects.push(new IntersectPlane(1, 0, 0, -100, 0, 0)); // Left wall
  objects.push(new IntersectPlane(1, 0, 0, 100, 0, 0)); // Right wall
  objects.push(new IntersectPlane(0, 1, 0, 0, -100, 0)); // Bottom wall
  objects.push(new IntersectPlane(0, 1, 0, 0, 100, 0)); // Top wall
  objects.push(new IntersectPlane(0, 0, 1, 0, 0, 0)); // Back wall

  noStroke();
  ambientMaterial(250);
}

function draw() {
  background(0);

  // Lights
  pointLight(255, 255, 255, 0, 0, 400);
  ambientLight(244, 122, 158);

  // Left wall
  push();
  translate(-100, 0, 200);
  rotateY((90 * PI) / 180);
  plane(400, 200);
  pop();

  // Right wall
  push();
  translate(100, 0, 200);
  rotateY((90 * PI) / 180);
  plane(400, 200);
  pop();

  // Bottom wall
  push();
  translate(0, 100, 200);
  rotateX((90 * PI) / 180);
  plane(200, 400);
  pop();

  // Top wall
  push();
  translate(0, -100, 200);
  rotateX((90 * PI) / 180);
  plane(200, 400);
  pop();

  plane(200, 200); // Back wall

  const x = mouseX - width / 2;
  const y = mouseY - height / 2;

  const Q = createVector(0, 0, eyeZ); // A point on the ray and the default position of the camera.
  const v = createVector(x, y, -eyeZ); // The direction vector of the ray.

  let intersect; // The point of intersection between the ray and a plane.
  let closestLambda = eyeZ * 10; // The draw distance.

  for (let x = 0; x < objects.length; x += 1) {
    let object = objects[x];
    let lambda = object.getLambda(Q, v); // The value of lambda where the ray intersects the object

    if (lambda < closestLambda && lambda > 0) {
      // Find the position of the intersection of the ray and the object.
      intersect = p5.Vector.add(Q, p5.Vector.mult(v, lambda));
      closestLambda = lambda;
    }
  }

  // Cursor
  push();
  translate(intersect);
  fill(237, 34, 93);
  sphere(10);
  pop();
}

// Class for a plane that extends to infinity.
class IntersectPlane {
  constructor(n1, n2, n3, p1, p2, p3) {
    this.normal = createVector(n1, n2, n3); // The normal vector of the plane
    this.point = createVector(p1, p2, p3); // A point on the plane
    this.d = this.point.dot(this.normal);
  }

  getLambda(Q, v) {
    return (-this.d - this.normal.dot(Q)) / this.normal.dot(v);
  }
}

// 3D Orbit Control - Useful for doing interfaces and several other interface based projects. 

function setup() {
    createCanvas(710, 400, WEBGL);
  }
  
  function draw() {
    background(250);
    let radius = width * 1.5;
  
    //drag to move the world.
    orbitControl();
  
    normalMaterial();
    translate(0, 0, -600);
    for (let i = 0; i <= 12; i++) {
      for (let j = 0; j <= 12; j++) {
        push();
        let a = (j / 12) * PI;
        let b = (i / 12) * PI;
        translate(
          sin(2 * a) * radius * sin(b),
          (cos(b) * radius) / 2,
          cos(2 * a) * radius * sin(b)
        );
        if (j % 2 === 0) {
          cone(30, 30);
        } else {
          box(30, 30, 30);
        }
        pop();
      }
    }
  }


// Basic Shader, used to create gradient effects, particularly useful 


// this variable will hold our shader object
let theShader;

function preload(){
  // load the shader
  theShader = loadShader('assets/basic.vert', 'assets/basic.frag');
}

function setup() {
  // shaders require WEBGL mode to work
  createCanvas(710, 400, WEBGL);
  noStroke();
}

function draw() {
  // shader() sets the active shader with our shader
  shader(theShader);

  // rect gives us some geometry on the screen
  rect(0,0,width, height);
}


// Shader as a Texture for 3D texture mapping in P5.js


// this variable will hold our shader object
let theShader;

function preload(){
  // load the shader
  theShader = loadShader('assets/basic.vert', 'assets/basic.frag');
}

function setup() {
  // shaders require WEBGL mode to work
  createCanvas(710, 400, WEBGL);
  noStroke();
}

function draw() {
  // shader() sets the active shader with our shader
  shader(theShader);

  // rect gives us some geometry on the screen
  rect(0,0,width, height);
}

// Passing Shader Uniforms
// Uniforms are the way in which information is passed from p5 to the shader.
// To learn more about using shaders in p5.js: p5.js Shaders

 // this variable will hold our shader object
 let theShader;

 function preload(){
   // load the shader
   theShader = loadShader('assets/uniforms.vert', 'assets/uniforms.frag');
 }

 function setup() {
   // shaders require WEBGL mode to work
   createCanvas(710, 400, WEBGL);
   noStroke();
 }

 function draw() {
   // shader() sets the active shader with our shader
   shader(theShader);

   // lets send the resolution, mouse, and time to our shader
   // before sending mouse + time we modify the data so it's more easily usable by the shader
   theShader.setUniform('resolution', [width, height]);
   theShader.setUniform('mouse', map(mouseX, 0, width, 0, 7));
   theShader.setUniform('time', frameCount * 0.01);

   // rect gives us some geometry on the screen
   rect(0,0,width, height);
 }

// Shader that works to put video ontop of texture


 // this variable will hold our shader object
 let theShader;
 // this variable will hold our webcam video
 let cam;

 function preload(){
   // load the shader
   theShader = loadShader('assets/webcam.vert', 'assets/webcam.frag');
 }

 function setup() {
   // shaders require WEBGL mode to work
   createCanvas(710, 400, WEBGL);
   noStroke();

   cam = createCapture(VIDEO);
   cam.size(710, 400);

   cam.hide();
 }

 function draw() {
   // shader() sets the active shader with our shader
   shader(theShader);

   // passing cam as a texture
   theShader.setUniform('tex0', cam);

   // rect gives us some geometry on the screen
   rect(0,0,width,height);
 }