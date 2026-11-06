# Decision Report

- generated_at: 2026-11-06T14:06:39.336508+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18285**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18285, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_6PCT | 3/20 | 15.0% | +4.04% | **+0.61%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.33% | **+0.27%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.16% | **+0.23%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.31% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.66% | **+1.49%** |
| MARKET_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.83% | **+1.19%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.41% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7811件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$382.28** / 初期 $100.00 (+282.28%)
- 確定: 4655件 (Win 1250 / Loss 1034 / Flat 2371) / skip 7041件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1207 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $382.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000370 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T14:06:25.271663+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=75615.3
- Funnel: target 1089 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +93.10% | $41,506,381.11 |
| UAI/USDT:USDT | +80.71% | $18,036,828.48 |
| CYBER/USDT:USDT | +56.63% | $5,919,953.81 |
| ONE/USDT:USDT | +37.13% | $3,751,806.50 |
| JCT/USDT:USDT | +28.98% | $6,312,690.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +1.93% | +2.26% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.56% | +1.89% |
| MVLL/USDT:USDT | below_1h_threshold | +1.19% | +1.52% |
| ICNT/USDT:USDT | below_1h_threshold | +1.12% | +1.45% |
| SNXX/USDT:USDT | below_1h_threshold | +1.08% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
