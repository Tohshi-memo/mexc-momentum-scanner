# Decision Report

- generated_at: 2026-11-06T10:01:33.917880+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18269**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18269, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +3.60% | **+1.44%** |
| LIMIT_BB3S | 5/16 | 31.2% | +4.05% | **+1.26%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.52% | **+0.83%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.86% | **+1.39%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.00% | **+1.00%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.97% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7795件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$376.73** / 初期 $100.00 (+276.73%)
- 確定: 4639件 (Win 1246 / Loss 1034 / Flat 2359) / skip 7041件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1410 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $376.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6430件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T10:01:18.658231+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=76152.6
- Funnel: target 1084 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +93.79% | $34,411,714.58 |
| UAI/USDT:USDT | +86.12% | $10,731,343.01 |
| CYBER/USDT:USDT | +53.25% | $4,172,959.76 |
| JCT/USDT:USDT | +29.01% | $6,958,295.47 |
| ICNT/USDT:USDT | +28.61% | $1,595,304.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +3.80% | +3.80% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +3.43% | +3.43% |
| SOXL/USDT:USDT | below_1h_threshold | +3.18% | +3.18% |
| SNXX/USDT:USDT | below_1h_threshold | +2.86% | +2.86% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.46% | +2.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
