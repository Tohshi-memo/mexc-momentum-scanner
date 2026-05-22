# Decision Report

- generated_at: 2026-05-22T09:58:53.280907+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4682**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4682, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.57% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +3.63% | **+2.18%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.68% | **+1.43%** |
| ASK_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.08% | **+1.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.70** / 初期 $100.00 (+21.70%)
- 確定: 553件 (Win 140 / Loss 185 / Flat 228) / skip 690件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $121.70

## 4. Latest Market Context

- 更新: 2026-05-22T09:58:50.961482+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77276.1
- Funnel: target 768 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +41.38% | $3,434,963.43 |
| ALT/USDT:USDT | +30.51% | $1,514,902.09 |
| GENIUS/USDT:USDT | +29.05% | $1,319,817.02 |
| BEAT/USDT:USDT | +26.12% | $11,049,798.96 |
| NEAR/USDT:USDT | +24.64% | $105,120,495.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.94% | +4.89% |
| PEAQ/USDT:USDT | below_1h_threshold | +4.92% | +4.88% |
| BEAT/USDT:USDT | below_1h_threshold | +3.38% | +3.33% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.94% | +2.90% |
| FET/USDT:USDT | below_1h_threshold | +1.99% | +1.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
