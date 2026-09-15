# Decision Report

- generated_at: 2026-09-15T06:31:34.072388+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14571**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14571, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.18% | **+0.05%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.06% | **+1.68%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.22% | **+1.29%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,078.22** / 初期 $100.00 (+978.22%)
- 確定: 5473件 (Win 1642 / Loss 1773 / Flat 2058) / skip 5659件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.00% 残高後 $1,078.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.20** / 初期 $100.00 (+130.20%)
- 確定: 3012件 (Win 835 / Loss 718 / Flat 1459) / skip 4970件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0713 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $230.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.98** / 初期 $100.00 (+23.98%)
- 確定: 2908件 (Win 862 / Loss 1133 / Flat 913) / pending 1件 / skip 3136件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.98

## 6. Latest Market Context

- 更新: 2026-09-15T06:31:18.792124+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=77397.0
- Funnel: target 1075 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +53.59% | $1,564,683.54 |
| POWER/USDT:USDT | +52.40% | $9,510,748.05 |
| AIN/USDT:USDT | +51.96% | $9,310,684.57 |
| FF/USDT:USDT | +28.93% | $1,178,986.27 |
| STORJ/USDT:USDT | +18.58% | $1,059,462.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +3.48% | +3.73% |
| AIN/USDT:USDT | below_1h_threshold | +2.03% | +2.27% |
| RIVER/USDT:USDT | below_1h_threshold | +0.82% | +1.07% |
| MUU/USDT:USDT | below_1h_threshold | +0.60% | +0.85% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +0.41% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
