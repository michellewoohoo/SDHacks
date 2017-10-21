const request = require("request");

const token = "GENOMELINKTEST";
const options = { headers: { authorization: `Bearer ${token}` }, json: true };

const name = 'eye-color';
const population = 'european';
const reportUrl = `https://genomicexplorer.io/v1/reports/${name}/?population=${population}`;
request.get(reportUrl, options, function (error, response, body) { console.log(body.summary.text); });

const chrom = 'chr1';
const startPos = '100000';
const endPos = '100500';
const sequenceUrl = `https://genomicexplorer.io/v1/genomes/sequence/?region=${chrom}:${startPos}-${endPos}`
request.get(sequenceUrl, options, function (error, response, body) { console.log(body); });