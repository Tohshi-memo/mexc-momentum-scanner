# Decision Report

- generated_at: 2026-05-22T18:39:30.955989+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4734**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4734, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +4.29% | **+1.29%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.69% | **+0.84%** |
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.12% | **+0.74%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.85% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.33% | **+1.83%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.97% | **+1.79%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.44% | **+1.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 580件 (Win 149 / Loss 187 / Flat 244) / skip 715件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-22T18:39:28.938578+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=76630.1
- Funnel: target 765 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +63.24% | $34,455,984.48 |
| BEAT/USDT:USDT | +8.99% | $34,042,043.81 |
| BILL/USDT:USDT | +7.81% | $14,044,224.68 |
| PEAQ/USDT:USDT | +3.91% | $1,312,923.24 |
| SKHYNIXSTOCK/USDT:USDT | +1.50% | $3,056,165.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.93% | +2.04% |
| BILL/USDT:USDT | below_1h_threshold | +1.30% | +1.41% |
| VVV/USDT:USDT | below_1h_threshold | +0.73% | +0.84% |
| PEAQ/USDT:USDT | below_1h_threshold | +0.69% | +0.80% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.66% | +0.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
