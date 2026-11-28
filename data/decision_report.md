# Decision Report

- generated_at: 2026-11-28T01:51:22.378241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19811**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=19811, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.47% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +4.21% | **+2.81%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.30% | **+0.92%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.02% | **+0.46%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,955.30** / 初期 $100.00 (+1855.30%)
- 確定: 7650件 (Win 2201 / Loss 2462 / Flat 2987) / skip 8722件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account -0.30% 残高後 $1,955.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5297件 (Win 1410 / Loss 1141 / Flat 2746) / skip 7925件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0039 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7970件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000059 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-28T01:51:08.411534+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.49% price=60161.6
- Funnel: target 1101 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +43.65% | $13,158,686.84 |
| ACE/USDT:USDT | +14.09% | $3,207,849.54 |
| SKY/USDT:USDT | +13.58% | $3,506,401.06 |
| VELVET/USDT:USDT | +9.73% | $5,683,970.82 |
| BTW/USDT:USDT | +7.80% | $8,998,774.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +2.29% | +1.80% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.74% | +1.25% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.60% | +1.12% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.50% | +1.02% |
| NEAR/USDT:USDT | below_1h_threshold | +1.23% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
