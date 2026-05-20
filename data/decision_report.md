# Decision Report

- generated_at: 2026-05-20T09:39:17.279511+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4536**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4536, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.58% | **+0.35%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.48% | **+0.14%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.10% | **-0.08%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.06% | **-0.21%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| ASK_LONG | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.59%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.72% | **+0.51%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.24% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.27** / 初期 $100.00 (+26.27%)
- 確定: 498件 (Win 131 / Loss 170 / Flat 197) / skip 599件
- 成長率目線: 平均log +0.000468 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $126.27

## 4. Latest Market Context

- 更新: 2026-05-20T09:39:12.002038+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77506.7
- Funnel: target 762 → liquid 133 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1, 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +112.71% | $1,462,573.65 |
| PROMPT/USDT:USDT | +36.63% | $12,502,317.41 |
| FIDA/USDT:USDT | +33.76% | $2,724,615.78 |
| EDEN/USDT:USDT | +29.30% | $21,785,576.61 |
| LIT/USDT:USDT | +25.34% | $8,621,202.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +4.82% | +4.72% |
| DASH/USDT:USDT | below_1h_threshold | +3.20% | +3.10% |
| CHIP/USDT:USDT | below_1h_threshold | +2.31% | +2.21% |
| ZEN/USDT:USDT | below_1h_threshold | +1.94% | +1.84% |
| HOME/USDT:USDT | below_1h_threshold | +1.83% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
