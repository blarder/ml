/**
 * Created by brett on 24/08/15.
 */

(function() {
    var width = 500;
    var height = 500;
    var numberTeams = 20;

    var barWidth = width;
    var barBorderHeight = 3;
    var barHeight = height / numberTeams;

    var teamsData;

    var matchDatesProcessed = 0;
    var matches;
    var bar;

    var extractTeams = function(data) {
        return _.chain(data)
            .pluck('home_team')
            .uniq()
            .map(function(teamName, index) {
                return {
                    name: teamName,
                    points: 0,
                    arrayIndex: index,
                    leaguePosition: index + 1,
                    goals_for: 0,
                    goals_against: 0
                }
            })
            .value();
    };

    var extractMatches = function(data) {
        return _.chain(data)
            .groupBy('match_date')
            .values()
            .sortBy(function(matchList) {
                return matchList[0].match_date;
            })
            .value()
    };

    var createTotalModification = function(matchesArr) {
        var createModification = function(match) {
            var modification = {};
            var pointsAwarded;

            if (match.home_goals > match.away_goals) {
                pointsAwarded = [3, 0]
            } else if (match.home_goals == match.away_goals) {
                pointsAwarded = [1, 1]
            } else {
                pointsAwarded = [0, 3]
            }

            modification[match.home_team] = {};
            modification[match.home_team].goals_for = match.home_goals;
            modification[match.home_team].goals_against = match.away_goals;
            modification[match.home_team].points = pointsAwarded[0];

            modification[match.away_team] = {};
            modification[match.away_team].goals_for = match.away_goals;
            modification[match.away_team].goals_against = match.home_goals;
            modification[match.away_team].points = pointsAwarded[1];

            return modification;
        };

        var mergeModifications = function(first, second) {
            var mapped = _.mapObject(first, function(mod, teamName) {
                return _.mapObject(mod, function(val, key) {
                    return (teamName in second)? val + second[teamName][key] : val;
                });
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
                extension.goals_for = team.goals_for + multiplier * mod[team.name].goals_for;
                extension.goals_against = team.goals_against + multiplier * mod[team.name].goals_against;
                extension.points = team.points + multiplier * mod[team.name].points;
            }
            return _.extend(team, extension)
        });

        var sorted = _.chain(mapped)
            .sortBy('goals_for')
            .sortBy(function(team) {return team.goals_for - team.goals_against})
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

    d3.json('/football/api/matches/?season=2015', function(error, json) {
        teamsData = extractTeams(json);
        matches = extractMatches(json);

        console.log(matches);

        bar = svg.selectAll('g')
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
