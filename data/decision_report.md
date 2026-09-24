# Decision Report

- generated_at: 2026-09-24T19:56:33.496595+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15488**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=15488, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.99% | **+0.75%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.36% | **+0.32%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.02% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/12 | 66.7% | +2.92% | **+1.95%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.31% | **+0.23%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.24% | **+0.10%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.05% | **+0.03%** |
| MARKET_LONG | 20/20 | 100.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5899件 (Win 1739 / Loss 1890 / Flat 2270) / skip 6150件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$254.44** / 初期 $100.00 (+154.44%)
- 確定: 3435件 (Win 949 / Loss 791 / Flat 1695) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0298 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $254.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.27** / 初期 $100.00 (+21.27%)
- 確定: 3159件 (Win 932 / Loss 1246 / Flat 981) / pending 0件 / skip 3803件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.27

## 6. Latest Market Context

- 更新: 2026-09-24T19:56:20.336789+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=84477.5
- Funnel: target 1069 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAI/USDT:USDT | +19.72% | $7,464,752.42 |
| LSK/USDT:USDT | +10.97% | $16,919,712.15 |
| CHIP/USDT:USDT | +8.67% | $1,169,994.13 |
| RAY/USDT:USDT | +5.38% | $10,244,036.95 |
| PLUME/USDT:USDT | +4.55% | $1,016,842.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +4.93% | +4.89% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.11% | +3.07% |
| ENA/USDT:USDT | below_1h_threshold | +2.91% | +2.87% |
| NEAR/USDT:USDT | below_1h_threshold | +2.83% | +2.78% |
| MVLL/USDT:USDT | below_1h_threshold | +2.79% | +2.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
