# Decision Report

- generated_at: 2026-05-08T21:40:25.017614+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3823**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3823, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/17 | 41.2% | +1.54% | **+0.63%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.39% | **+0.29%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.22% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.25% | **+0.21%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.43% | **+0.19%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.17%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.40% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 192件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T21:40:22.049825+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80177.1
- Funnel: target 767 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +20.12% | $3,209,823.26 |
| OP/USDT:USDT | +13.36% | $23,942,862.41 |
| JUP/USDT:USDT | +12.10% | $8,626,400.44 |
| SATO/USDT:USDT | +11.67% | $6,126,745.53 |
| ICP/USDT:USDT | +10.47% | $208,886,894.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +3.49% | +3.40% |
| BILL/USDT:USDT | below_1h_threshold | +3.43% | +3.34% |
| JUP/USDT:USDT | below_1h_threshold | +2.62% | +2.53% |
| OP/USDT:USDT | below_1h_threshold | +2.26% | +2.16% |
| AKT/USDT:USDT | below_1h_threshold | +2.23% | +2.14% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
