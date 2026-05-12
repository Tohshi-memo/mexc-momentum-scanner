# Decision Report

- generated_at: 2026-05-12T19:25:00.498840+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4155**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4155, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.23% | **-0.06%** |
| ASK | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.36% | **+2.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.78% | **+1.25%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.99** / 初期 $100.00 (+19.99%)
- 確定: 291件 (Win 83 / Loss 100 / Flat 108) / skip 425件
- 成長率目線: 平均log +0.000626 / 幾何平均 +0.063% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOLV/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $119.99

## 4. Latest Market Context

- 更新: 2026-05-12T19:24:57.040953+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=80721.6
- Funnel: target 758 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +23.10% | $4,980,584.16 |
| PEAQ/USDT:USDT | +13.32% | $1,846,592.70 |
| LAB/USDT:USDT | +11.17% | $155,666,710.10 |
| IRYS/USDT:USDT | +9.08% | $2,142,542.57 |
| EDU/USDT:USDT | +7.57% | $3,629,143.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.95% | +2.86% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.93% | +1.83% |
| TIA/USDT:USDT | below_1h_threshold | +1.72% | +1.62% |
| KITE/USDT:USDT | below_1h_threshold | +1.66% | +1.56% |
| SATO/USDT:USDT | below_1h_threshold | +1.65% | +1.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
