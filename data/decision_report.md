# Decision Report

- generated_at: 2026-05-20T10:29:05.495363+00:00
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

- 更新: 2026-05-20T10:29:03.292093+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77526.9
- Funnel: target 763 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +102.19% | $1,701,388.23 |
| PROMPT/USDT:USDT | +30.89% | $12,622,659.87 |
| FIDA/USDT:USDT | +29.70% | $2,864,206.65 |
| PLAY/USDT:USDT | +25.10% | $9,947,130.26 |
| EDEN/USDT:USDT | +24.77% | $22,244,262.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +4.59% | +4.49% |
| PLAY/USDT:USDT | below_1h_threshold | +2.37% | +2.27% |
| DASH/USDT:USDT | below_1h_threshold | +1.84% | +1.75% |
| CHIP/USDT:USDT | below_1h_threshold | +1.76% | +1.66% |
| JUP/USDT:USDT | below_1h_threshold | +1.23% | +1.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
