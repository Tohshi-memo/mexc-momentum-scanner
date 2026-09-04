# Decision Report

- generated_at: 2026-09-04T00:56:34.770245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13562**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.33% / filled 20/20。**
- 全期間 MARKET基準: n=13562, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.25% | **+2.13%** |
| LIMIT_BB3S | 4/18 | 22.2% | +6.06% | **+1.35%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.77% | **+1.06%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.46% | **+1.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.39% | **-0.37%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.91% | **-0.50%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5115件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.99** / 初期 $100.00 (+84.99%)
- 確定: 2380件 (Win 674 / Loss 576 / Flat 1130) / skip 4593件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0148 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $184.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.96** / 初期 $100.00 (+16.96%)
- 確定: 2222件 (Win 662 / Loss 871 / Flat 689) / pending 4件 / skip 2811件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000232 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.96

## 6. Latest Market Context

- 更新: 2026-09-04T00:56:21.194258+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=80994.7
- Funnel: target 1046 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +29.18% | $9,313,435.31 |
| BASECAT/USDT:USDT | +13.85% | $1,823,909.97 |
| PONS/USDT:USDT | +12.25% | $9,393,863.27 |
| AKE/USDT:USDT | +11.28% | $26,546,980.28 |
| BR/USDT:USDT | +9.79% | $8,775,340.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +3.20% | +3.49% |
| ARB/USDT:USDT | below_1h_threshold | +3.02% | +3.31% |
| LDO/USDT:USDT | below_1h_threshold | +2.20% | +2.49% |
| CRV/USDT:USDT | below_1h_threshold | +2.08% | +2.38% |
| BICO/USDT:USDT | below_1h_threshold | +1.18% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
