# Decision Report

- generated_at: 2026-09-05T16:21:35.650615+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13750**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13750, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.98% | **-1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.13% | **+0.06%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| MARKET_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.39% | **+1.52%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.50% | **+1.37%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.74% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$848.84** / 初期 $100.00 (+748.84%)
- 確定: 5056件 (Win 1519 / Loss 1651 / Flat 1886) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $848.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.03** / 初期 $100.00 (+89.03%)
- 確定: 2495件 (Win 697 / Loss 588 / Flat 1210) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0459 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $189.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.12** / 初期 $100.00 (+19.12%)
- 確定: 2374件 (Win 704 / Loss 902 / Flat 768) / pending 6件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.12

## 6. Latest Market Context

- 更新: 2026-09-05T16:21:22.044772+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79800.0
- Funnel: target 1050 → liquid 131 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1, 4h RSI 76.8 >= 65=1, 4h RSI 73.2 >= 65=1, 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +13.07% | $20,313,588.07 |
| MARSCOIN/USDT:USDT | +8.41% | $8,705,914.33 |
| BULLA/USDT:USDT | +5.57% | $20,007,873.48 |
| BASECAT/USDT:USDT | +5.48% | $1,940,657.25 |
| 4/USDT:USDT | +4.19% | $22,905,185.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.27% | +4.22% |
| CATI/USDT:USDT | below_1h_threshold | +3.29% | +3.24% |
| PONS/USDT:USDT | below_1h_threshold | +2.30% | +2.25% |
| EDGE/USDT:USDT | below_1h_threshold | +2.23% | +2.18% |
| CHIP/USDT:USDT | below_1h_threshold | +2.23% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
