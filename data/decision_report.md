# Decision Report

- generated_at: 2026-07-26T17:41:13.881061+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9580**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.20% / filled 20/20。**
- 全期間 MARKET基準: n=9580, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.80% | **+2.66%** |
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.65% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.23% | **+0.18%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.03% | **-0.02%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.10% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$105.87** / 初期 $100.00 (+5.87%)
- 確定トレード: 141件 (TP 48 / SL 88 / EXP 5)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $105.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$452.56** / 初期 $100.00 (+352.56%)
- 確定: 3399件 (Win 1078 / Loss 1106 / Flat 1215) / skip 2742件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $452.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.72** / 初期 $100.00 (+37.72%)
- 確定: 1222件 (Win 338 / Loss 274 / Flat 610) / skip 1769件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0548 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.21** / 初期 $100.00 (+8.21%)
- 確定: 616件 (Win 207 / Loss 238 / Flat 171) / pending 0件 / skip 435件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000130 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.11% 残高後 $108.21

## 6. Latest Market Context

- 更新: 2026-07-26T17:41:06.920801+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=64647.2
- Funnel: target 898 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +11.23% | $17,978,716.50 |
| CROSS/USDT:USDT | +4.77% | $1,147,402.96 |
| BANK/USDT:USDT | +3.95% | $70,806,343.94 |
| EPIC/USDT:USDT | +3.82% | $1,056,368.51 |
| ON/USDT:USDT | +3.32% | $4,765,564.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CROSS/USDT:USDT | below_1h_threshold | +3.54% | +3.62% |
| DIA/USDT:USDT | below_1h_threshold | +3.34% | +3.42% |
| LAB/USDT:USDT | below_1h_threshold | +3.26% | +3.34% |
| EPIC/USDT:USDT | below_1h_threshold | +2.91% | +2.99% |
| PROM/USDT:USDT | below_1h_threshold | +2.08% | +2.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
