const fs = require('fs')
const faceapi = require('face-api.js')
const path = require('path');
const fetch = require('node-fetch-polyfill');
const canvas = require('canvas')
const { Canvas, Image, ImageData } = canvas
faceapi.env.monkeyPatch({ Canvas, Image, ImageData })

const baseDir = path.resolve(__dirname, '../out')
// faceapi.env.monkeyPatch({ fetch: fetch });

function convetion_function(file, url_href){
    file_name = './public/images/'+(file)+'.jpg'
    fs.readFile(file_name, (err, data)=>{
        if(!err){
            convert(file_name, url_href)
        } else {
            console.log(err)
        }
    })
}

async function convert(file, url_href){
    try{
        console.log(file, url_href)
        // img_file = await faceapi.fetchImage(url_href)
        await faceapi.nets.ssdMobilenetv1.loadFromDisk('./public/models')

        const img_file = await canvas.loadImage(file)
        const face = await faceapi.detectSingleFace(img_file)
    
        const out = await faceapi.createCanvasFromMedia(file)
        await faceapi.draw.drawDetections(out, face)
    
        saveFile('faceDetection.jpg', out.toBuffer('./public/images'))

    } catch (err) {
        console.log(err)
    }

}

function saveFile(fileName , buf) {
  if (!fs.existsSync(baseDir)) {
    fs.mkdirSync(baseDir)
  }

  fs.writeFileSync(path.resolve(baseDir, fileName), buf)
}

module.exports = convetion_function
