# Decision Report

- generated_at: 2026-05-09T17:07:28.335319+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3904**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3904, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_BB3S | 7/13 | 53.8% | +0.62% | **+0.33%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.65% | **+0.19%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +3.59% | **+3.08%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.63% | **+1.97%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.01% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 270件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T17:07:25.461591+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80700.0
- Funnel: target 769 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BILL/USDT:USDT | +20.89% | $27,100,013.97 |
| SATO/USDT:USDT | +11.20% | $4,032,234.83 |
| RAVE/USDT:USDT | +10.04% | $16,150,015.23 |
| INX/USDT:USDT | +7.00% | $2,730,546.39 |
| OFC/USDT:USDT | +5.56% | $1,060,955.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.47% | +3.31% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.43% | +2.27% |
| JUP/USDT:USDT | below_1h_threshold | +2.04% | +1.89% |
| VVV/USDT:USDT | below_1h_threshold | +1.77% | +1.62% |
| NIL/USDT:USDT | below_1h_threshold | +1.31% | +1.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
