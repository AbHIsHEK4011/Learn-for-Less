// var nameValue = document.getElementById("uniqueID").value;
  const url="http://127.0.0.1:3000/search_course/?title=ibm machine learning";
let datas="";

async function find(){

  await fetch(url).then((response) => response.text()).then((data)=>datas=data);
  // console.log(datas);
  let output = JSON.parse(datas);
  output = JSON.parse(output["newans"])
  console.log(output[""]);
//   console.log("done")
  document.getElementById("slink1").href=output["4"];
}
find();
