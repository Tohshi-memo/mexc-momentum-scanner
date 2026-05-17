# Decision Report

- generated_at: 2026-05-17T21:08:32.536814+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4420**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4420, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.91% | **-0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/14 | 28.6% | +1.50% | **+0.43%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.69% | **-0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.81% | **+1.82%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.19% | **+1.43%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.94% | **+1.16%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.79% | **+0.80%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.98** / 初期 $100.00 (+21.98%)
- 確定: 417件 (Win 109 / Loss 140 / Flat 168) / skip 564件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BUILDONBOB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $121.98

## 4. Latest Market Context

- 更新: 2026-05-17T21:08:30.563734+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78217.3
- Funnel: target 760 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +14.93% | $2,694,260.11 |
| BUILDONBOB/USDT:USDT | +13.55% | $1,202,160.78 |
| UB/USDT:USDT | +12.07% | $13,821,658.55 |
| BILL/USDT:USDT | +7.37% | $33,722,416.95 |
| HYPE/USDT:USDT | +7.19% | $267,786,599.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +2.84% | +2.86% |
| RIVER/USDT:USDT | below_1h_threshold | +1.90% | +1.92% |
| ZEC/USDT:USDT | below_1h_threshold | +0.78% | +0.80% |
| DASH/USDT:USDT | below_1h_threshold | +0.67% | +0.68% |
| HYPE/USDT:USDT | below_1h_threshold | +0.65% | +0.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
