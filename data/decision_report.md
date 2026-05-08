# Decision Report

- generated_at: 2026-05-08T22:02:44.608055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3824**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3824, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/17 | 41.2% | +1.54% | **+0.63%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.52% | **+0.41%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.98% | **+0.39%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.83% | **+0.37%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.45% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 193件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T22:02:41.485677+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=80285.0
- Funnel: target 767 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +28.17% | $3,700,642.39 |
| OP/USDT:USDT | +16.72% | $25,443,225.53 |
| JUP/USDT:USDT | +12.10% | $8,949,928.67 |
| CORE/USDT:USDT | +11.57% | $1,545,698.59 |
| ICP/USDT:USDT | +10.82% | $206,811,848.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VET/USDT:USDT | below_1h_threshold | +1.64% | +1.57% |
| OP/USDT:USDT | below_1h_threshold | +1.37% | +1.29% |
| XPL/USDT:USDT | below_1h_threshold | +1.19% | +1.11% |
| ONDO/USDT:USDT | below_1h_threshold | +1.01% | +0.93% |
| DYDX/USDT:USDT | below_1h_threshold | +1.00% | +0.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
