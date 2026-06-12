# Decision Report

- generated_at: 2026-06-12T13:21:31.128485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6510**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6510, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.54% | **+0.69%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.66% | **+0.50%** |
| LIMIT_BB3S | 6/16 | 37.5% | +1.15% | **+0.43%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.91% | **+1.43%** |
| ASK_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.98% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.19** / 初期 $100.00 (+67.19%)
- 確定: 1383件 (Win 380 / Loss 447 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000372 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $167.19

## 4. Latest Market Context

- 更新: 2026-06-12T13:21:27.850703+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63437.5
- Funnel: target 774 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +93.95% | $49,310,995.20 |
| VELVET/USDT:USDT | +92.83% | $159,479,132.60 |
| NAORIS/USDT:USDT | +53.18% | $5,746,360.41 |
| AIN/USDT:USDT | +40.34% | $1,274,655.75 |
| SKYAI/USDT:USDT | +39.48% | $17,636,778.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.90% | +3.90% |
| BILL/USDT:USDT | below_1h_threshold | +1.13% | +1.13% |
| STG/USDT:USDT | below_1h_threshold | +1.13% | +1.12% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.96% | +0.95% |
| VVV/USDT:USDT | below_1h_threshold | +0.91% | +0.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
