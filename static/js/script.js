var tradecode = document.getElementById('dropdown').value
var date = []
var close = []
var open = []
var high = []
var low = []
for (const elem of data) {
    if (elem['trade_code'] == tradecode) {
        // console.log(elem['close'])
        date.push(elem['date'])
        close.push(elem['close'])
        open.push(elem['open'])
        high.push(elem['high'])
        low.push(elem['low'])
    }
}
date.reverse()
close.reverse()
open.reverse()
high.reverse()
low.reverse()


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
        ]
    }
});

dropdown = document.getElementById('dropdown')
dropdown.addEventListener('change', UpdateChart)
function UpdateChart() {
    tradecode = dropdown.value
    // var date = masterdict[tradecode]['date']
    // var high = masterdict[tradecode]['high']
    // var low = masterdict[tradecode]['low']
    // var open = masterdict[tradecode]['open']
    // var close = masterdict[tradecode]['close']
    // var volume = masterdict[tradecode]['volume']

    // myChart.data.labels = date
    // myChart.data.datasets[0].data = close
    // myChart.data.datasets[1].data = high
    // myChart.data.datasets[2].data = low
    // myChart.data.datasets[3].data = open

    close = []
    open = []
    high = []
    low = []
    for (const elem of data) {
        if (elem['trade_code'] == tradecode) {
            // console.log(elem['close'])
            close.push(elem['close'])
            open.push(elem['open'])
            high.push(elem['high'])
            low.push(elem['low'])
        }

    }
    myChart.data.datasets[0].data = close.reverse()
    myChart.data.datasets[1].data = high.reverse()
    myChart.data.datasets[2].data = low.reverse()
    myChart.data.datasets[3].data = open.reverse()


    myChart.update()




}
clos = []
for (const elem of data) {
    if (elem['trade_code'] == '1JANATAMF') {
        // console.log(elem['close'])
        clos.push(elem['close'])

    }
}