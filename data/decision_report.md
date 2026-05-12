# Decision Report

- generated_at: 2026-05-12T19:18:18.684174+00:00
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

- 更新: 2026-05-12T19:18:15.633320+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=80741.6
- Funnel: target 758 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +24.52% | $4,937,997.13 |
| PEAQ/USDT:USDT | +10.46% | $1,789,630.47 |
| LAB/USDT:USDT | +9.27% | $154,898,064.15 |
| IRYS/USDT:USDT | +8.98% | $2,138,303.29 |
| SAHARA/USDT:USDT | +7.50% | $5,192,122.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEAQ/USDT:USDT | below_1h_threshold | +4.22% | +4.09% |
| SAHARA/USDT:USDT | below_1h_threshold | +3.22% | +3.09% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.62% | +1.50% |
| TIA/USDT:USDT | below_1h_threshold | +1.58% | +1.46% |
| SATO/USDT:USDT | below_1h_threshold | +1.57% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
