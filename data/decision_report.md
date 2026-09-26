# Decision Report

- generated_at: 2026-09-26T16:17:12.013109+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15607**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=15607, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.05% | **+0.42%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.32% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.59% | **+1.03%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.25% | **+1.01%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.58% | **+0.71%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.63% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,274.13** / 初期 $100.00 (+1174.13%)
- 確定: 5968件 (Win 1765 / Loss 1916 / Flat 2287) / skip 6200件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PAID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,274.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5485件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1120 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.95** / 初期 $100.00 (+19.95%)
- 確定: 3192件 (Win 940 / Loss 1264 / Flat 988) / pending 5件 / skip 3883件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000342 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PAID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.95

## 6. Latest Market Context

- 更新: 2026-09-26T16:16:55.981753+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=84084.6
- Funnel: target 1070 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +8.40% | $3,192,650.88 |
| ORDI/USDT:USDT | +5.81% | $2,651,399.63 |
| BTW/USDT:USDT | +1.98% | $11,085,074.32 |
| MUBARAK/USDT:USDT | +1.84% | $3,375,418.60 |
| CC/USDT:USDT | +1.76% | $1,852,967.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +2.00% | +2.03% |
| BTW/USDT:USDT | below_1h_threshold | +1.94% | +1.97% |
| CC/USDT:USDT | below_1h_threshold | +1.75% | +1.79% |
| GALA/USDT:USDT | below_1h_threshold | +1.68% | +1.71% |
| WLD/USDT:USDT | below_1h_threshold | +1.53% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
