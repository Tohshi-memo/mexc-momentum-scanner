# Decision Report

- generated_at: 2026-07-21T02:56:26.565019+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9144**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=9144, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.34% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.70% | **+1.53%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.78% | **+1.51%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.48% | **+1.40%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.07% | **+0.85%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.22% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$108.59** / 初期 $100.00 (+8.59%)
- 確定トレード: 124件 (TP 44 / SL 75 / EXP 5)
- 最新: ZHIPUSTOCK/USDT:USDT SL_HIT PnL -3.93% 残高後 $108.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$415.11** / 初期 $100.00 (+315.11%)
- 確定: 3206件 (Win 1005 / Loss 1020 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $415.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.02** / 初期 $100.00 (+30.02%)
- 確定: 1105件 (Win 291 / Loss 228 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1139 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $130.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.26** / 初期 $100.00 (+1.26%)
- 確定: 339件 (Win 120 / Loss 150 / Flat 69) / pending 2件 / skip 277件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000228 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.26

## 6. Latest Market Context

- 更新: 2026-07-21T02:56:18.831519+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=65454.4
- Funnel: target 885 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +60.97% | $1,897,147.13 |
| JIMOTHY/USDT:USDT | +25.88% | $2,825,461.39 |
| BLESS/USDT:USDT | +15.67% | $2,024,879.49 |
| ZHIPUSTOCK/USDT:USDT | +15.23% | $1,173,122.34 |
| AKE/USDT:USDT | +13.25% | $20,113,536.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +4.99% | +4.61% |
| AKE/USDT:USDT | below_1h_threshold | +4.98% | +4.60% |
| BLESS/USDT:USDT | below_1h_threshold | +4.18% | +3.80% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.03% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.01% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
