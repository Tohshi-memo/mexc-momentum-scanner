# Decision Report

- generated_at: 2026-09-25T12:21:30.003162+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15526**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15526, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +2.19% | **+1.86%** |
| LIMIT_ATR | 18/20 | 90.0% | +1.61% | **+1.45%** |
| LIMIT_5PCT | 7/20 | 35.0% | +3.97% | **+1.39%** |
| LIMIT_4PCT | 14/20 | 70.0% | +1.71% | **+1.20%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.35% | **+0.94%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.97% | **+0.53%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.72% | **+0.47%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.31% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 220件 (TP 80 / SL 135 / EXP 5)
- 最新: MYX/USDT:USDT TP_HIT PnL +7.62% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,206.94** / 初期 $100.00 (+1106.94%)
- 確定: 5901件 (Win 1740 / Loss 1890 / Flat 2271) / skip 6186件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.76% 残高後 $1,206.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3459件 (Win 952 / Loss 793 / Flat 1714) / skip 5478件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0567 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3829件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T12:21:16.585384+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=84067.5
- Funnel: target 1069 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +47.65% | $3,094,586.00 |
| BP/USDT:USDT | +29.74% | $1,020,811.75 |
| ARK/USDT:USDT | +28.57% | $2,008,467.51 |
| B3/USDT:USDT | +19.74% | $1,025,724.10 |
| QNT/USDT:USDT | +17.95% | $15,862,365.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +1.24% | +1.79% |
| XPL/USDT:USDT | below_1h_threshold | +0.92% | +1.47% |
| SOXL/USDT:USDT | below_1h_threshold | +0.81% | +1.36% |
| KORU/USDT:USDT | below_1h_threshold | +0.72% | +1.27% |
| MVLL/USDT:USDT | below_1h_threshold | +0.64% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
