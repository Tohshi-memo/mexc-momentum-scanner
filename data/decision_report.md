# Decision Report

- generated_at: 2026-11-27T13:16:17.169845+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19775**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19775, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.37% | **+0.20%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.45% | **-0.31%** |
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +6.72% | **+6.72%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.56% | **+1.92%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,928.72** / 初期 $100.00 (+1828.72%)
- 確定: 7645件 (Win 2199 / Loss 2461 / Flat 2985) / skip 8691件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,928.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$466.64** / 初期 $100.00 (+366.64%)
- 確定: 5281件 (Win 1409 / Loss 1135 / Flat 2737) / skip 7905件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0134 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.54% 残高後 $466.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7935件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-27T13:16:06.411251+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=61442.0
- Funnel: target 1101 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +81.74% | $3,044,817.09 |
| BULLA/USDT:USDT | +53.14% | $13,615,933.79 |
| HAEDAL/USDT:USDT | +34.40% | $2,069,223.71 |
| PONS/USDT:USDT | +23.88% | $2,577,836.47 |
| LISTA/USDT:USDT | +20.64% | $3,857,546.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.84% | +4.11% |
| SNXX/USDT:USDT | below_1h_threshold | +1.89% | +2.16% |
| SOXL/USDT:USDT | below_1h_threshold | +1.78% | +2.05% |
| KORU/USDT:USDT | below_1h_threshold | +1.43% | +1.70% |
| BULLA/USDT:USDT | below_1h_threshold | +1.28% | +1.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
