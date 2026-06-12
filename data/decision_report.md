# Decision Report

- generated_at: 2026-06-12T08:30:08.333341+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6487**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6487, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.52% | **-0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/20 | 15.0% | +5.02% | **+0.75%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.05% | **+0.03%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.02% | **+0.02%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.78% | **+0.63%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.48% | **+0.52%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.23% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$162.31** / 初期 $100.00 (+62.31%)
- 確定: 1362件 (Win 368 / Loss 438 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HMSTR/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $162.31

## 4. Latest Market Context

- 更新: 2026-06-12T08:30:04.717133+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.68% price=63495.1
- Funnel: target 779 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +97.67% | $146,598,756.46 |
| XPL/USDT:USDT | +42.57% | $8,872,437.56 |
| NAORIS/USDT:USDT | +39.15% | $2,751,549.54 |
| ESPORTS/USDT:USDT | +32.70% | $36,703,306.73 |
| STG/USDT:USDT | +28.31% | $14,714,073.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +4.36% | +3.68% |
| XPL/USDT:USDT | below_1h_threshold | +3.96% | +3.28% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +3.11% | +2.43% |
| ZEC/USDT:USDT | below_1h_threshold | +2.23% | +1.55% |
| ORDI/USDT:USDT | below_1h_threshold | +1.90% | +1.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
