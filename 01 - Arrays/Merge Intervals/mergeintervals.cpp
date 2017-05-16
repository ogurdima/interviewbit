/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
vector<Interval> Solution::insert(vector<Interval> &intervals, Interval newInterval) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    int newIntervalIdx = -1;
    vector<Interval> res;
    
    if (newInterval.start > newInterval.end) {
        auto tmp = newInterval.start;
        newInterval.start = newInterval.end;
        newInterval.end = tmp;
    }
    
    auto intervalToAdd = Interval(0, 0);
    bool carryInterval = false;
    for (auto i = 0; i < intervals.size(); i++) {
        auto intervalToCheck = newInterval;
        if (carryInterval) {
            intervalToCheck = intervalToAdd;
        }
        
        if (intervals[i].start > intervals[i].end) {
            auto tmp = intervals[i].start;
            intervals[i].start = intervals[i].end;
            intervals[i].end = tmp;
        }
        
        bool isOverlapping = (  
            intervalToCheck.start <= intervals[i].end && intervalToCheck.start >= intervals[i].start || 
            intervalToCheck.end <= intervals[i].end && intervalToCheck.end >= intervals[i].start || 
            intervals[i].start <= intervalToCheck.end && intervals[i].start >= intervalToCheck.start || 
            intervals[i].end <= intervalToCheck.end && intervals[i].end >= intervalToCheck.start 
        );
        
        if (isOverlapping) 
        {
            //cout << "isOverlapping" << endl;
            carryInterval = true;
            newIntervalIdx = i;
            auto maxEnd = (intervalToCheck.end > intervals[i].end) ? intervalToCheck.end : intervals[i].end;
            auto minStart = (intervalToCheck.start < intervals[i].start) ? intervalToCheck.start : intervals[i].start;
            intervalToAdd.start = minStart;
            intervalToAdd.end = maxEnd;
        }
        else
        {
            if (carryInterval)
            {
                res.push_back(intervalToAdd);
            }
            carryInterval = false;
        }
        
        if (newIntervalIdx == -1)
        {
            if (newInterval.start < intervals[i].start) 
            {
                newIntervalIdx = i;
                if (!carryInterval) {
                    res.push_back(newInterval);
                }
            }
        }
        
        if (!carryInterval) {
            res.push_back(intervals[i]);
        }
    }
    
    if (carryInterval)
    {
        res.push_back(intervalToAdd);
    }
    else if (newIntervalIdx == -1) {
        res.push_back(newInterval);
    }
    
    return res;
}
