# Decision Report

- generated_at: 2026-09-26T17:56:17.642328+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15612**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=15612, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.87% | **+0.35%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.74% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.26% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.40% | **+0.98%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.53% | **+0.61%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.64% | **+0.38%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.56% | **+0.25%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.25% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,271.07** / 初期 $100.00 (+1171.07%)
- 確定: 5973件 (Win 1766 / Loss 1918 / Flat 2289) / skip 6200件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PAID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,271.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5490件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0842 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.84** / 初期 $100.00 (+19.84%)
- 確定: 3196件 (Win 941 / Loss 1266 / Flat 989) / pending 6件 / skip 3884件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000324 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PAID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.84

## 6. Latest Market Context

- 更新: 2026-09-26T17:56:08.328278+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=84071.3
- Funnel: target 1070 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1, 4h RSI 77.9 >= 65=1, 4h RSI 82.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +9.75% | $1,111,112.46 |
| PAID/USDT:USDT | +5.94% | $3,370,515.06 |
| QNT/USDT:USDT | +5.93% | $15,497,670.02 |
| GRASS/USDT:USDT | +3.33% | $3,165,988.48 |
| LSK/USDT:USDT | +3.30% | $2,609,001.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.30% | +3.30% |
| KAS/USDT:USDT | below_1h_threshold | +2.15% | +2.15% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.68% | +1.67% |
| NEAR/USDT:USDT | below_1h_threshold | +1.12% | +1.12% |
| BTW/USDT:USDT | below_1h_threshold | +0.85% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
