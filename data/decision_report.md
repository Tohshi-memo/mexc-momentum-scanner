# Decision Report

- generated_at: 2026-11-06T04:41:39.015672+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18245**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18245, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 11/20 | 55.0% | +4.69% | **+2.58%** |
| LIMIT_7PCT | 7/20 | 35.0% | +6.29% | **+2.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.99% | **+1.20%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.48% | **+0.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.11% | **+1.44%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7771件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$374.47** / 初期 $100.00 (+274.47%)
- 確定: 4615件 (Win 1237 / Loss 1031 / Flat 2347) / skip 7041件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1223 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $374.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6405件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000105 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T04:41:23.002692+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=75777.0
- Funnel: target 1084 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +57.14% | $8,677,748.89 |
| AKE/USDT:USDT | +51.47% | $21,580,293.24 |
| CYBER/USDT:USDT | +48.41% | $2,585,436.51 |
| IRENSTOCK/USDT:USDT | +18.42% | $3,138,813.15 |
| BLESS/USDT:USDT | +15.98% | $5,449,519.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +2.67% | +2.80% |
| BLESS/USDT:USDT | below_1h_threshold | +2.06% | +2.19% |
| LYN/USDT:USDT | below_1h_threshold | +1.75% | +1.89% |
| LIT/USDT:USDT | below_1h_threshold | +1.21% | +1.34% |
| PYTH/USDT:USDT | below_1h_threshold | +1.08% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
