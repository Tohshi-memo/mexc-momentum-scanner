# Decision Report

- generated_at: 2026-05-11T11:12:44.294795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4026**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4026, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.77% | **+0.66%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.65% | **+0.42%** |
| LIMIT_FIB1272 | 14/20 | 70.0% | +0.19% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.32% | **+0.59%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.06% | **+0.47%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.71% | **+0.37%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.71% | **+0.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.27% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 369件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T11:12:41.077520+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80885.1
- Funnel: target 761 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +39.20% | $13,182,827.69 |
| B/USDT:USDT | +28.45% | $10,804,609.80 |
| SAGA/USDT:USDT | +28.18% | $2,904,064.74 |
| TROLLSOL/USDT:USDT | +18.59% | $4,519,885.30 |
| VVV/USDT:USDT | +18.33% | $18,933,380.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XNY/USDT:USDT | below_1h_threshold | +2.50% | +2.52% |
| GIGA/USDT:USDT | below_1h_threshold | +1.99% | +2.01% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.80% | +1.82% |
| CHIP/USDT:USDT | below_1h_threshold | +1.63% | +1.65% |
| US/USDT:USDT | below_1h_threshold | +1.25% | +1.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
