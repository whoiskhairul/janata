var tradecode = document.getElementById('dropdown').value
var date = masterdict[tradecode]['date']
var high = masterdict[tradecode]['high']
var low = masterdict[tradecode]['low']
var open = masterdict[tradecode]['open']
var close = masterdict[tradecode]['close']
var volume = masterdict[tradecode]['volume']

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
type: 'line',
data: {
    labels: date,
    datasets: [
    {
        data: close,
        label: 'Close',
        borderColor: "#66c938",

    },
    {
        data: high,
        label: "High",
        borderColor: "#1eb8e3",
    },
    {
        data: low,
        label: "Low",
        borderColor: "#cf5246",
    },
    {
        data: open,
        label: "Open",
        borderColor: "#c9b22e",
    },
    // {
    //     data: volume,
    //     label: "Volume",
    //     borderColor: "#66c938",
    // },
    ]
}
});

dropdown = document.getElementById('dropdown')
dropdown.addEventListener('change', UpdateChart)
function UpdateChart(){
    tradecode = dropdown.value
    var date = masterdict[tradecode]['date']
    var high = masterdict[tradecode]['high']
    var low = masterdict[tradecode]['low']
    var open = masterdict[tradecode]['open']
    var close = masterdict[tradecode]['close']
    var volume = masterdict[tradecode]['volume']

    myChart.data.labels = date
    myChart.data.datasets[0].data = close
    myChart.data.datasets[1].data = high
    myChart.data.datasets[2].data = low
    myChart.data.datasets[3].data = open

    myChart.update()




}