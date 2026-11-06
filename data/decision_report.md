# Decision Report

- generated_at: 2026-11-06T10:51:13.433390+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18272**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18272, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.57% | **-1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +3.60% | **+1.44%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_BB3S | 6/17 | 35.3% | +2.94% | **+1.04%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.79% | **+3.19%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.33% | **+1.28%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.69% | **+1.10%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.28% | **+1.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7798件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$376.73** / 初期 $100.00 (+276.73%)
- 確定: 4642件 (Win 1246 / Loss 1034 / Flat 2362) / skip 7041件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1405 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $376.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6431件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000330 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T10:51:05.313587+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=76135.0
- Funnel: target 1089 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +87.59% | $35,658,270.83 |
| UAI/USDT:USDT | +82.04% | $11,174,074.39 |
| CYBER/USDT:USDT | +46.06% | $4,350,649.29 |
| ICNT/USDT:USDT | +28.24% | $1,749,078.51 |
| ONE/USDT:USDT | +25.48% | $1,128,892.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AAOISTOCK/USDT:USDT | below_1h_threshold | +4.17% | +4.19% |
| MUU/USDT:USDT | below_1h_threshold | +3.80% | +3.82% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +3.43% | +3.45% |
| BEAT/USDT:USDT | below_1h_threshold | +3.35% | +3.37% |
| SOXL/USDT:USDT | below_1h_threshold | +3.18% | +3.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
