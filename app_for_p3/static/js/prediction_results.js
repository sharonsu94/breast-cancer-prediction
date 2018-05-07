// Fetch data from model prediction and populate table
d3.json('/model_predict', function(error, predictionData){
    if (error) return console.warn(error);

    console.log(predictionData);
    
    // Setup data mapping
    var IDs = predictionData.sample_id;
    var results = predictionData.prediction;

    // Populate table
    var resultsTable = document.getElementById('resultsTable');

    // Header first
    var firstRow = resultsTable.insertRow(0);
    var idCell = firstRow.insertCell(0);
    var resultCell = firstRow.insertCell(1);
    idCell.innerHTML = '<b>ID</b>';
    resultCell.innerHTML = '<b>Result</b>';

    // Loop through the data to populate results rows
    for (var i = 0; i < IDs.length; i++){
        var row = resultsTable.insertRow(1);
        var current_id = row.insertCell(0);
        var current_result = row.insertCell(1);
        current_id.innerHTML = IDs[i];
        current_result.innerHTML = results[i];
    };
});