# Decision Report

- generated_at: 2026-05-08T23:17:32.414480+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3827**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3827, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/16 | 43.8% | +1.54% | **+0.67%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.43% | **+0.30%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.44% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.71%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.14% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 196件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T23:17:29.612864+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=80149.1
- Funnel: target 767 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +20.17% | $4,974,195.46 |
| OP/USDT:USDT | +13.03% | $33,165,920.39 |
| CORE/USDT:USDT | +11.57% | $1,650,296.47 |
| BILL/USDT:USDT | +11.52% | $17,315,762.18 |
| JUP/USDT:USDT | +11.24% | $9,757,494.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +1.25% | +1.36% |
| AKT/USDT:USDT | below_1h_threshold | +1.12% | +1.24% |
| DOGS/USDT:USDT | below_1h_threshold | +0.94% | +1.05% |
| MOVR/USDT:USDT | below_1h_threshold | +0.77% | +0.89% |
| MEGA/USDT:USDT | below_1h_threshold | +0.73% | +0.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
