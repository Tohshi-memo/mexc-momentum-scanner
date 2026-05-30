# Decision Report

- generated_at: 2026-05-30T00:15:13.552034+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5080**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=5080, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.55% | **+1.55%** |
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.83% | **+0.67%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.93% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.63% | **-0.28%** |
| MARKET_LONG | 20/20 | 100.0% | -0.47% | **-0.47%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | -1.02% | **-0.56%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 741件 (Win 175 / Loss 226 / Flat 340) / skip 900件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-30T00:15:10.803844+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=73448.0
- Funnel: target 773 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XLM/USDT:USDT | +22.60% | $400,486,062.43 |
| OL/USDT:USDT | +16.29% | $1,456,044.97 |
| BASED/USDT:USDT | +13.52% | $2,461,787.43 |
| LAB/USDT:USDT | +11.88% | $129,026,082.12 |
| HBAR/USDT:USDT | +10.64% | $31,263,009.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HBAR/USDT:USDT | below_1h_threshold | +3.14% | +3.11% |
| SEI/USDT:USDT | below_1h_threshold | +1.89% | +1.87% |
| XLM/USDT:USDT | below_1h_threshold | +1.39% | +1.36% |
| XMR/USDT:USDT | below_1h_threshold | +0.94% | +0.92% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +0.90% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
