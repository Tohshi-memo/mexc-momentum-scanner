# Decision Report

- generated_at: 2026-09-21T09:41:29.192066+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15244**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=15244, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.24% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.11% | **+0.06%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.09% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,172.15** / 初期 $100.00 (+1072.15%)
- 確定: 5735件 (Win 1708 / Loss 1846 / Flat 2181) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,172.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.16** / 初期 $100.00 (+147.16%)
- 確定: 3306件 (Win 913 / Loss 765 / Flat 1628) / skip 5349件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0175 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.65** / 初期 $100.00 (+22.65%)
- 確定: 3022件 (Win 891 / Loss 1186 / Flat 945) / pending 5件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000160 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.65

## 6. Latest Market Context

- 更新: 2026-09-21T09:41:17.566249+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.38% price=84880.2
- Funnel: target 1050 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.9 >= 65=1, 4h RSI 74.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +72.73% | $5,661,773.25 |
| PHA/USDT:USDT | +44.07% | $1,079,759.38 |
| NIL/USDT:USDT | +35.16% | $7,203,143.78 |
| PTB/USDT:USDT | +30.75% | $1,118,517.51 |
| UAI/USDT:USDT | +23.18% | $1,488,819.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_relative_strength | +5.23% | +3.85% |
| ZAMA/USDT:USDT | below_1h_threshold | +4.77% | +3.39% |
| PTB/USDT:USDT | below_1h_threshold | +4.60% | +3.22% |
| UAI/USDT:USDT | below_1h_threshold | +4.55% | +3.16% |
| USELESS/USDT:USDT | below_1h_threshold | +4.18% | +2.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
