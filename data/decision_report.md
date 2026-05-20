# Decision Report

- generated_at: 2026-05-20T10:33:49.157951+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4539**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4539, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.82% | **+0.49%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.08% | **-0.06%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |
| ASK | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.63% | **+0.19%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.06% | **+0.03%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.01** / 初期 $100.00 (+25.01%)
- 確定: 501件 (Win 131 / Loss 172 / Flat 198) / skip 599件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $125.01

## 4. Latest Market Context

- 更新: 2026-05-20T10:33:47.113729+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=77575.9
- Funnel: target 763 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +98.84% | $1,711,961.46 |
| FIDA/USDT:USDT | +32.46% | $2,896,433.69 |
| PROMPT/USDT:USDT | +32.02% | $12,626,440.92 |
| EDEN/USDT:USDT | +25.28% | $22,271,275.63 |
| PLAY/USDT:USDT | +25.21% | $10,009,968.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +2.59% | +2.43% |
| DASH/USDT:USDT | below_1h_threshold | +2.30% | +2.14% |
| PLAY/USDT:USDT | below_1h_threshold | +2.24% | +2.08% |
| CHIP/USDT:USDT | below_1h_threshold | +1.86% | +1.69% |
| JUP/USDT:USDT | below_1h_threshold | +1.81% | +1.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
