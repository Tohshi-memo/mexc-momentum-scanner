# Decision Report

- generated_at: 2026-05-10T05:32:44.760313+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3943**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3943, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.51% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.81% | **+1.54%** |
| ASK_LONG | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +2.39% | **+0.60%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.90% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 307件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T05:32:41.076343+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80728.4
- Funnel: target 769 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.2 >= 65=1, 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAYER/USDT:USDT | +48.26% | $1,993,918.09 |
| SATO/USDT:USDT | +22.52% | $6,276,893.52 |
| JASMY/USDT:USDT | +17.88% | $21,492,281.13 |
| BAS/USDT:USDT | +17.26% | $1,036,915.46 |
| AIGENSYN/USDT:USDT | +11.02% | $1,188,985.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +4.92% | +4.91% |
| JTO/USDT:USDT | below_1h_threshold | +4.32% | +4.31% |
| PLAY/USDT:USDT | below_1h_threshold | +3.53% | +3.52% |
| JASMY/USDT:USDT | below_1h_threshold | +2.78% | +2.77% |
| UNI/USDT:USDT | below_1h_threshold | +2.75% | +2.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
