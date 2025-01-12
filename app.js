// Initial setup of Three.js
let scene, camera, renderer, cube;

function initThreeJS() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('threejs-container').appendChild(renderer.domElement);

    let geometry = new THREE.BoxGeometry(1, 1, 1);
    let material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    animate();
}

function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
}

function generateProblem() {
    // Fetch a new math problem from the Flask backend
    fetch('/api/math_problem')
        .then(response => response.json())
        .then(data => {
            // Display the problem in the page
            document.getElementById('math-problem').innerText = `Solve: ${data.problem}`;
        });
}

// Initialize the 3D visualization
initThreeJS();
