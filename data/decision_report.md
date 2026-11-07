# Decision Report

- generated_at: 2026-11-07T04:56:37.079357+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18357**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18357, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.56% | **+0.89%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.36% | **+0.29%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.30% | **+1.32%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.39% | **+1.31%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.49% | **+1.12%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.97% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,472.97** / 初期 $100.00 (+1372.97%)
- 確定: 7053件 (Win 2027 / Loss 2251 / Flat 2775) / skip 7865件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,472.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.71** / 初期 $100.00 (+289.71%)
- 確定: 4723件 (Win 1271 / Loss 1041 / Flat 2411) / skip 7045件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0535 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $389.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6517件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T04:56:21.421691+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=75862.7
- Funnel: target 1089 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +54.33% | $6,475,273.78 |
| AKE/USDT:USDT | +28.63% | $63,816,589.34 |
| ONE/USDT:USDT | +24.04% | $15,149,490.46 |
| LYN/USDT:USDT | +21.59% | $1,840,454.56 |
| IDOL/USDT:USDT | +10.68% | $4,818,975.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +4.05% | +4.04% |
| AGT/USDT:USDT | below_1h_threshold | +2.27% | +2.26% |
| BLESS/USDT:USDT | below_1h_threshold | +1.99% | +1.98% |
| MUU/USDT:USDT | below_1h_threshold | +1.17% | +1.17% |
| MVLL/USDT:USDT | below_1h_threshold | +1.04% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
