# Decision Report

- generated_at: 2026-10-02T12:31:28.552099+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15997**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15997, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.52% | **+0.46%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_BB3S | 2/11 | 18.2% | -0.34% | **-0.06%** |
| LIMIT_4PCT | 10/20 | 50.0% | -0.30% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.36% | **+0.75%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.59% | **+0.56%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.54% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,326.06** / 初期 $100.00 (+1226.06%)
- 確定: 6102件 (Win 1805 / Loss 1960 / Flat 2337) / skip 6456件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,326.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5803件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0094 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4159件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000062 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T12:31:16.833496+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.57% price=86872.0
- Funnel: target 1098 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +69.13% | $4,129,991.71 |
| SAND/USDT:USDT | +57.03% | $35,249,853.63 |
| ENJ/USDT:USDT | +28.51% | $1,088,707.04 |
| SI/USDT:USDT | +28.26% | $3,594,279.81 |
| MAGMA/USDT:USDT | +19.43% | $2,499,347.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.34% | +3.77% |
| APE/USDT:USDT | below_1h_threshold | +3.85% | +3.27% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.01% | +2.44% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +2.76% | +2.18% |
| SKY/USDT:USDT | below_1h_threshold | +2.01% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
