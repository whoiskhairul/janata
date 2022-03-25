let high, low, open, close, trade_code, volume, date

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

function ShowChart(){
    const trade_code = document.getElementById('dropdown').value
    $.ajax({
        method: 'GET',
        url: `getjson/${trade_code}`,
        success: function (response){
            high = response.high
            low = response.low
            open = response.open
            close = response.close
            volume = response.volume
            date = response.date
            tc = response.trade_code
            console.log(tc)
            document.getElementById('com_code').innerHTML = tc

            myChart.data.datasets[0].data = close
            myChart.data.datasets[1].data = high
            myChart.data.datasets[2].data = low
            myChart.data.datasets[3].data = open
            myChart.data.labels = date

            myChart.update()
        }
    })
}

ShowChart()
dropdown = document.getElementById('dropdown')
dropdown.addEventListener('change', ShowChart)