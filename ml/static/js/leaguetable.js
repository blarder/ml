/**
 * Created by brett on 24/08/15.
 */

(function() {
    var width = 500;
    var height = 500;
    var numberTeams = 20;

    var barWidth = width / 2;
    var barBorderHeight = 3;
    var barHeight = height / numberTeams;

    var teamsData = [];
    for (var i = 0; i < numberTeams; ++i) {
        teamsData.push({
            name: 'team' + i.toString(),
            points: 0,
            arrayIndex: i,
            leaguePosition: i + 1,
            goalsFor: 0,
            goalsAgainst: 0
        })
    }

    var matchDatesProcessed = 0;
    var matches = [
        [
            {homeGoals: 1, awayGoals: 0, homeTeam: 'team1', awayTeam: 'team2'},
            {homeGoals: 1, awayGoals: 1, homeTeam: 'team3', awayTeam: 'team4'}
        ],
        [
            {homeGoals: 1, awayGoals: 2, homeTeam: 'team0', awayTeam: 'team5'},
            {homeGoals: 1, awayGoals: 1, homeTeam: 'team6', awayTeam: 'team7'}
        ]
    ];





    var createTotalModification = function(matchesArr) {
        var createModification = function(match) {
            var modification = {};
            var pointsAwarded;

            if (match.homeGoals > match.awayGoals) {
                pointsAwarded = [3, 0]
            } else if (match.homeGoals == match.awayGoals) {
                pointsAwarded = [1, 1]
            } else {
                pointsAwarded = [0, 3]
            }

            modification[match.homeTeam] = {};
            modification[match.homeTeam].goalsFor = match.homeGoals;
            modification[match.homeTeam].goalsAgainst = match.awayGoals;
            modification[match.homeTeam].points = pointsAwarded[0];

            modification[match.awayTeam] = {};
            modification[match.awayTeam].goalsFor = match.awayGoals;
            modification[match.awayTeam].goalsAgainst = match.homeGoals;
            modification[match.awayTeam].points = pointsAwarded[1];

            return modification;
        };

        var mergeModifications = function(first, second) {
            var mapped = _.mapObject(first, function(mod, teamName) {
                var addGoalsFor = 0;
                var addGoalsAgainst = 0;
                var addPoints = 0;

                if (teamName in second) {
                    addGoalsFor = second[teamName].goalsFor;
                    addGoalsAgainst = second[teamName].goalsAgainst;
                    addPoints = second[teamName].points;
                }

                return {
                    goalsFor: mod.goalsFor + addGoalsFor,
                    goalsAgainst: mod.goalsAgainst + addGoalsAgainst,
                    points: mod.points + addPoints
                }
            });

            return _.defaults(mapped, second);

        };
        var mapped = _.map(matchesArr, createModification);
        return _.reduce(mapped, mergeModifications, {})
    };

    var modifiedTeamsData = function(data, mod, reverse) {
        var multiplier = 1;
        if (reverse) {
            multiplier = -1
        }
        var mapped = _.map(data, function(team) {
            var extension = {};
            if (team.name in mod) {
                extension.goalsFor = team.goalsFor + multiplier * mod[team.name].goalsFor;
                extension.goalsAgainst = team.goalsAgainst + multiplier * mod[team.name].goalsAgainst;
                extension.points = team.points + multiplier * mod[team.name].points;
            }
            return _.extend(team, extension)
        });

        var sorted = _.chain(mapped)
            .sortBy('goalsFor')
            .sortBy(function(team) {return team.goalsFor - team.goalsAgainst})
            .sortBy('points')
            .reverse()
            .map(function(team, index) {return _.extend(team, {leaguePosition: index + 1})})
            .value();

        for (var i = 0; i < sorted.length; i++) {
            mapped[sorted[i].arrayIndex].leaguePosition = sorted[i].leaguePosition;
        }

        return mapped;
    };

    var svg = d3.select('body').append('svg')
        .attr('width', width)
        .attr('height', height)
        .attr('class', 'chart');

    var y = d3.scale.linear()
        .range([height - barHeight - barBorderHeight, barBorderHeight])
        .domain([numberTeams, 1]);

    var transformBar = function (d) {
        return 'translate(' + (width - barWidth) / 2 + ',' + y(d.leaguePosition) + ')';
    };

    var bar = svg.selectAll('g')
        .data(teamsData)
        .enter().append('g')
        .attr('class', 'bar')
        .attr('transform', transformBar);

    bar.append('rect')
        .attr('width', barWidth)
        .attr('height', barHeight - 2 * barBorderHeight)
        .attr('rx', 20)
        .attr('ry', 20);

    bar.append('text')
        .attr('x', 3 * barWidth / 4)
        .attr('y', barHeight / 3)
        .attr('dy', '.75em')
        .text(function (d) {
            return d.name + ': ' + d.points.toString();
        });

    var updateTable = function(newData) {
        bar.data(newData)
            .transition()
            .duration(1000)
            .attr('transform', transformBar)
            .select('text')
            .text(function(d) {
                return d.name + ': ' + d.points.toString();
            });
    };

    //TODO: consider caching modification objects
    var forwardDate = function() {
        if (matchDatesProcessed < matches.length) {
            var nextMatches = matches[matchDatesProcessed];
            teamsData = modifiedTeamsData(teamsData, createTotalModification(nextMatches));
            updateTable(teamsData);
            matchDatesProcessed++;
        }

    };

    var backDate = function() {
        if (matchDatesProcessed > 0) {
            var prevMatches = matches[matchDatesProcessed - 1];
            teamsData = modifiedTeamsData(teamsData, createTotalModification(prevMatches), true);
            updateTable(teamsData);
            matchDatesProcessed--;
        }
    };

    LeagueTable = {
        forwardDate: forwardDate,
        backDate: backDate
    }
}());
