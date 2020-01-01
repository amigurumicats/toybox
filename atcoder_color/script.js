function color(n){
  if(n < 400){ return "#d9d9d9" }  // gray
  else if(n < 800){ return "#d9c5b2" }  // brown
  else if(n < 1200){ return "#b2d9b2" }  // green
  else if(n < 1600){ return "#b2ecec" }  // sky-blue
  else if(n < 2000){ return "#b2b2ff" }  // blue
  else if(n < 2400){ return "#ececb2" }  // yello
  else if(n < 2800){ return "#ffd9b2" }  // orange
  else if(n < 3200){ return "#ffd2d2" }  // red
  else if(n < 3600){ return "#ffd2d2" }  // silver
  else{ return "#ffd2d2" }  // gold
}

var tbody = document.getElementById("history").children[1];
for(row of tbody.rows){
  for(i of [3,4]){
    row.cells[i].style.backgroundColor = color(parseInt(row.cells[i].textContent))
  }
}
