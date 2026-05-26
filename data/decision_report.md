# Decision Report

- generated_at: 2026-05-26T13:14:16.819022+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4900**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=4900, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 12/20 | 60.0% | +1.51% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +8.00% | **+8.00%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.29% | **+0.77%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.87% | **+0.66%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.25% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.87** / 初期 $100.00 (+29.87%)
- 確定: 675件 (Win 171 / Loss 214 / Flat 290) / skip 786件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DRIFT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $129.87

## 4. Latest Market Context

- 更新: 2026-05-26T13:14:14.711287+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77039.9
- Funnel: target 769 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +75.71% | $2,825,534.03 |
| WLD/USDT:USDT | +29.98% | $148,821,301.02 |
| DRIFT/USDT:USDT | +29.54% | $3,676,340.89 |
| OKB/USDT:USDT | +17.83% | $1,402,837.00 |
| IO/USDT:USDT | +16.52% | $1,206,274.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRIFT/USDT:USDT | below_1h_threshold | +3.93% | +4.00% |
| OKB/USDT:USDT | below_1h_threshold | +1.67% | +1.75% |
| GRT/USDT:USDT | below_1h_threshold | +1.11% | +1.19% |
| WLD/USDT:USDT | below_1h_threshold | +1.00% | +1.08% |
| DYDX/USDT:USDT | below_1h_threshold | +0.96% | +1.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
