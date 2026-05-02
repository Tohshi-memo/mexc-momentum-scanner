# Decision Report

- generated_at: 2026-05-02T07:57:01.571642+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2879**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=2879, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.96% | **+0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.97% | **+0.40%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.83% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T07:56:59.350325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=78180.1
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1, 4h RSI 92.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +157.85% | $81,583,685.86 |
| KNC/USDT:USDT | +23.61% | $1,035,626.07 |
| BIO/USDT:USDT | +16.82% | $1,295,737.29 |
| IRYS/USDT:USDT | +15.44% | $1,346,367.26 |
| B/USDT:USDT | +11.76% | $80,452,109.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNC/USDT:USDT | below_1h_threshold | +4.59% | +4.71% |
| UB/USDT:USDT | below_1h_threshold | +2.48% | +2.60% |
| USTC/USDT:USDT | below_1h_threshold | +2.44% | +2.57% |
| ORCA/USDT:USDT | below_1h_threshold | +1.75% | +1.88% |
| PLAY/USDT:USDT | below_1h_threshold | +1.69% | +1.81% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
