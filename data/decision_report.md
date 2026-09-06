# Decision Report

- generated_at: 2026-09-06T11:06:20.395402+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13809**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.96% / filled 20/20。**
- 全期間 MARKET基準: n=13809, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.72% | **+0.43%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.20% | **+0.14%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.21% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.82% | **+0.65%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.59% | **+0.44%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$839.29** / 初期 $100.00 (+739.29%)
- 確定: 5115件 (Win 1535 / Loss 1674 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $839.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$192.56** / 初期 $100.00 (+92.56%)
- 確定: 2554件 (Win 715 / Loss 608 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0087 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $192.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.49** / 初期 $100.00 (+19.49%)
- 確定: 2421件 (Win 721 / Loss 922 / Flat 778) / pending 5件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.49

## 6. Latest Market Context

- 更新: 2026-09-06T11:06:10.651897+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79938.0
- Funnel: target 1054 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +47.80% | $164,755,990.07 |
| RAY/USDT:USDT | +39.03% | $4,037,894.17 |
| FLOCK/USDT:USDT | +37.37% | $1,747,012.00 |
| COTI/USDT:USDT | +27.00% | $1,102,674.09 |
| JUP/USDT:USDT | +20.17% | $5,374,808.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +1.86% | +1.89% |
| JUP/USDT:USDT | below_1h_threshold | +1.43% | +1.47% |
| SUSHI/USDT:USDT | below_1h_threshold | +1.20% | +1.23% |
| FLOCK/USDT:USDT | below_1h_threshold | +0.90% | +0.93% |
| DOT/USDT:USDT | below_1h_threshold | +0.72% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
