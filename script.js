let ctx=document.getElementById("graph").getContext("2d")

let chart=new Chart(ctx,{
type:"line",
data:{
labels:[],
datasets:[{
label:"Traffic Density",
data:[]
}]
}
})

async function updateDashboard(){

let res=await fetch("traffic_state.json")

let data=await res.json()

document.getElementById("vehicles").innerText=data.vehicles
document.getElementById("pedestrians").innerText=data.pedestrians

if(data.ambulance.area){

document.getElementById("ambulance").innerText=
data.ambulance.area+" "+data.ambulance.lane

}

let html=""
let total=0

for(let area in data.traffic){

html+="<h3>"+area+"</h3>"

for(let signal in data.traffic[area]){

html+="<b>"+signal+"</b><br>"

let lanes=data.traffic[area][signal]

for(let lane in lanes){

html+=lane+" : "+lanes[lane]+" cars<br>"

total+=lanes[lane]

}

html+="Time : "+data.signal_timing[area][signal]+" sec<br><br>"

}

}

document.getElementById("signals").innerHTML=html

chart.data.labels.push("")
chart.data.datasets[0].data.push(total)

if(chart.data.labels.length>15){

chart.data.labels.shift()
chart.data.datasets[0].data.shift()

}

chart.update()

document.getElementById("camera").src="frame.jpg?"+Date.now()

}

setInterval(updateDashboard,2000)
