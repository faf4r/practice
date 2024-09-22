#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define ll long long

ll c, m, n;
vector<ll> cup;
vector<ll> cup_index;
vector<pair<ll, ll>> tmp;

vector<ll> explode_once(ll i) {
    vector<ll> ret;
    cup.erase(cup.begin() + i);
    cup_index.erase(cup_index.begin() + i);

    ll left = i - 1;
    ll right = i;

    if (left >= 0) {
        cup[left] += 1;
        if (cup[left] >= 5) {
            ret.push_back(left);
        }
    }

    if (right < cup.size()) {
        cup[right] += 1;
        if (cup[right] >= 5) {
            ret.push_back(right);
        }
    }

    return ret;
};

ll index_of(ll p) {
    for (ll i = 0; i < cup_index.size(); i++) {
        if (cup_index[i] == p) {
            return i;
        }
    }
    return -1;
}

int main() {
    cin >> c >> m >> n;

    for (ll i = 0; i < m; i++) {
        ll x, w;
        cin >> x >> w;
        tmp.push_back(make_pair(x, w));
    }
    sort(tmp.begin(), tmp.end());
    for (auto item : tmp) {
        cup_index.push_back(item.first);
        cup.push_back(item.second);
    }

    for (ll i = 0; i < n; i++) {
        ll p;
        cin >> p;
        ll index = index_of(p);
        cup[index] += 1;

        if (cup[index] < 5) {
            cout << m << endl;
            continue;
        }

        vector<ll> explode_index_list = {index};
        while (!explode_index_list.empty()) {
            vector<ll> ret = explode_once(explode_index_list[0]);
            m -= 1;
            explode_index_list.clear();
            explode_index_list.insert(explode_index_list.begin(), ret.begin(), ret.end());
        }

        cout << m << endl;
    }

    return 0;
}